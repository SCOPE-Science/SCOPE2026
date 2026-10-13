#!/usr/bin/env python3
"""Independent finite-field and identity checks for the three-dimensional polynomial transposed-Leibniz moduli. Standard library only."""
import itertools


def field(q):
    if q in (3, 5, 7):
        return (lambda a,b: (a+b)%q), (lambda a,b: (a*b)%q), (lambda a: (-a)%q)
    polys={2:3,4:7,8:11,16:19}
    if q not in polys: raise ValueError(q)
    bits=q.bit_length()-1; poly=polys[q]
    mult=[[0]*q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            v=0
            for i in range(bits):
                if (a>>i)&1: v^=b<<i
            for k in range(2*bits-2,bits-1,-1):
                if (v>>k)&1: v^=poly<<(k-bits)
            mult[a][b]=v
    return (lambda a,b:a^b), (lambda a,b:mult[a][b]), (lambda a:a)


def table_odd(b,c,e,i,s):
    return {(0,0):(e,b,c),(0,1):(0,e,0),(0,2):(0,0,i),
            (1,1):(0,0,0),(1,2):(0,0,0),(2,2):(0,0,s)}


def table_even(b,c,e,f,i,j,k,l,o,s):
    return {(0,0):(e,b,c),(0,1):(k,e,f),(0,2):(0,0,i),
            (1,1):(j,k,l),(1,2):(0,0,o),(2,2):(0,0,s)}


def basis(i):
    return tuple(int(i==j) for j in range(3))


def multiply(A,u,v,add,mul):
    ans=[0,0,0]
    for i in range(3):
        for j in range(3):
            d=mul(u[i],v[j])
            w=A[min(i,j),max(i,j)]
            for k in range(3): ans[k]=add(ans[k],mul(d,w[k]))
    return tuple(ans)


def bracket(u,v,add,mul,neg):
    return (0, add(mul(u[0],v[1]),neg(mul(u[1],v[0]))),0)


def valid_basis(A,q,associativity=True,compatibility=True):
    add,mul,neg=field(q); E=[basis(i) for i in range(3)]
    if compatibility:
        for i,j,k in itertools.product(range(3),repeat=3):
            x,y,z=E[i],E[j],E[k]
            lhs=multiply(A,z,bracket(x,y,add,mul,neg),add,mul)
            lhs=tuple(add(t,t) for t in lhs)
            rhs1=bracket(multiply(A,z,x,add,mul),y,add,mul,neg)
            rhs2=bracket(x,multiply(A,z,y,add,mul),add,mul,neg)
            if lhs!=tuple(add(a,b) for a,b in zip(rhs1,rhs2)):
                return False
    if associativity:
        for i,j,k in itertools.product(range(3),repeat=3):
            x,y,z=E[i],E[j],E[k]
            if multiply(A,multiply(A,x,y,add,mul),z,add,mul)!=multiply(A,x,multiply(A,y,z,add,mul),add,mul):
                return False
    return True


def rank_modp(M,p):
    A=[list(row) for row in M]; r=0
    for c in range(len(A[0])):
        pivot=next((j for j in range(r,len(A)) if A[j][c]%p),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        t=pow(A[r][c],-1,p)
        A[r]=[(v*t)%p for v in A[r]]
        for j in range(len(A)):
            if j!=r:
                t=A[j][c]%p
                A[j]=[(u-t*v)%p for u,v in zip(A[j],A[r])]
        r+=1
        if r==len(A):break
    return r


def compatibility_rank(p):
    coords=list(itertools.combinations_with_replacement(range(3),2))
    zero=(0,0,0)
    rows=[]
    for pos in range(18):
        t={ij:list(zero) for ij in coords}
        t[coords[pos//3]][pos%3]=1
        A={ij:tuple(v) for ij,v in t.items()}
        add,mul,neg=field(p); E=[basis(j) for j in range(3)]
        values=[]
        for i,j,k in itertools.product(range(3),repeat=3):
            x,y,z=E[i],E[j],E[k]
            L=multiply(A,z,bracket(x,y,add,mul,neg),add,mul)
            L=tuple(add(a,a) for a in L)
            Q=bracket(multiply(A,z,x,add,mul),y,add,mul,neg)
            R=bracket(x,multiply(A,z,y,add,mul),add,mul,neg)
            values.extend(tuple(add(L[u],neg(add(Q[u],R[u]))) for u in range(3)))
        rows.append(values)
    return rank_modp(list(map(list,zip(*rows))),p)


def brute_counts():
    assert compatibility_rank(2)==8
    assert compatibility_rank(3)==13
    for q in (3,5,7):
        add,mul,_=field(q)
        total=0
        for b,c,e,i,s in itertools.product(range(q),repeat=5):
            okay=add(mul(i,add(e,(-i)%q)),mul(c,s))==0
            if q==3:
                A=table_odd(b,c,e,i,s)
                assert valid_basis(A,q)==okay
            if okay: total+=1
        assert total==q**4+q**3-q**2,(q,total)
    for q in (2,4):
        add,mul,_=field(q)
        total=0
        for b,c,e,f,i,j,k,l,o,s in itertools.product(range(q),repeat=10):
            cond=(add(mul(e,k),mul(b,j))==0 and
                  add(add(mul(b,l),mul(c,add(k,o))),mul(f,i))==0 and
                  add(add(mul(b,o),mul(c,s)),add(mul(e,i),mul(i,i)))==0 and
                  add(add(mul(j,c),mul(add(e,i),l)),mul(f,o))==0 and
                  add(add(mul(k,i),mul(e,o)),add(mul(f,s),mul(o,i)))==0 and
                  add(add(mul(j,i),mul(k,o)),add(mul(l,s),mul(o,o)))==0)
            if q==2:
                A=table_even(b,c,e,f,i,j,k,l,o,s)
                assert valid_basis(A,q)==cond
            total+=cond
        assert total==q**6+2*q**5-q**4-q**2,(q,total)
    return True


def extension_count(q):
    add,mul,_=field(q)
    Bcount=0; good_pairs=0; rr=[0,0,0]
    for e,b,j,k in itertools.product(range(q),repeat=4):
        if mul(e,k)!=mul(b,j):continue
        Bcount+=1
        for i,o in itertools.product(range(q),repeat=2):
            if mul(i,i)!=add(mul(e,i),mul(b,o)):continue
            if mul(i,o)!=add(mul(k,i),mul(e,o)):continue
            if mul(o,o)!=add(mul(j,i),mul(k,o)):continue
            good_pairs+=1
            a=(add(k,o),i,b);d=(j,o,add(e,i))
            if not any(a) and not any(d):r=0
            elif not any(a) or not any(d):r=1
            else:
                pivot=next(m for m in range(3) if a[m]!=0)
                r=1 if all(mul(a[pivot],d[t])==mul(d[pivot],a[t]) for t in range(3)) else 2
            rr[r]+=1
    assert Bcount==q**3+q**2-q
    assert good_pairs==2*q**3+q**2-2*q
    assert rr==[1,good_pairs-1,0]
    N0=rr[0]*q**3+rr[1]*q**2+rr[2]*q
    N1=(q-1)*q**2*Bcount
    assert N0==2*q**5+q**4-q**3-q**2
    assert N0+N1==q**6+2*q**5-q**4-q**2
    return (q,Bcount,good_pairs,N0,N1,N0+N1)


if __name__=='__main__':
    brute_counts()
    for q in (2,4,8,16):print('CHAR2',extension_count(q))
    print('ODD',[(q,q**4+q**3-q**2) for q in (3,5,7)])
    print('VERIFY_OK')
