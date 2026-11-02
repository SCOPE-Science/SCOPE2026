#!/usr/bin/env python3
"""Independent exact finite-field checks for square-zero derivations of free class-two Lie algebras."""
from itertools import product, combinations
from math import prod


def add(x,y,q):
    return x ^ y if q == 4 else (x+y) % q


def neg(x,q):
    return x if q == 4 else (-x)%q


def mul(x,y,q):
    if q!=4: return (x*y)%q
    p=0
    for _ in range(2):
        if y&1:p^=x
        y>>=1
        x<<=1
        if x&4:x^=7
    return p


def inv(x,q):
    assert x
    for y in range(1,q):
        if mul(x,y,q)==1:return y
    raise ValueError('not a field')


def zero(n,m):return [[0]*m for _ in range(n)]


def mm(A,B,q):
    out=zero(len(A),len(B[0]))
    for i,row in enumerate(A):
        for k,x in enumerate(row):
            if x:
                for j,y in enumerate(B[k]):
                    if y:out[i][j]=add(out[i][j],mul(x,y,q),q)
    return out


def rank(A,q):
    if not A:return 0
    a=[row[:] for row in A]
    h=len(a);w=len(a[0]);p=0
    for j in range(w):
        t=next((i for i in range(p,h) if a[i][j]),None)
        if t is None:continue
        a[p],a[t]=a[t],a[p]
        u=inv(a[p][j],q)
        a[p]=[mul(x,u,q) for x in a[p]]
        for i in range(h):
            if i!=p and a[i][j]:
                v=a[i][j]
                a[i]=[add(a[i][k],neg(mul(v,a[p][k],q),q),q) for k in range(w)]
        p+=1
        if p==h:break
    return p


def pairs(n):return list(combinations(range(n),2))


def induced(A,q):
    n=len(A);ps=pairs(n);N=len(ps);C=zero(N,N)
    for col,(i,j) in enumerate(ps):
        for row,(h,k) in enumerate(ps):
            v=add(mul(A[h][i],int(k==j),q),mul(A[k][j],int(h==i),q),q)
            v=add(v,neg(mul(A[k][i],int(h==j),q),q),q)
            v=add(v,neg(mul(A[h][j],int(k==i),q),q),q)
            C[row][col]=v
    return C


def fiber_rank(A,C,q):
    n=len(A);N=len(C);mat=zero(n*N,n*N)
    # Relation (BA+CB)_{i,j}, variables B_{u,v}
    for i in range(N):
        for j in range(n):
            ri=i*n+j
            for u in range(N):
                for v in range(n):
                    coeff=0
                    if i==u:coeff=add(coeff,A[v][j],q)
                    if j==v:coeff=add(coeff,C[i][u],q)
                    mat[ri][u*n+v]=coeff
    return rank(mat,q)


def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den


def predicted(n,q):
    N=n*(n-1)//2
    s=q**(n*N)
    pieces=[(0,1,n*N)]
    for r in range(1,n//2+1):
        if q!=2 and q!=4 and r>=2:break
        rho=r*(n-r-1)
        exponent=(n-r)*N-(n-2*r)*rho
        gl=prod((q**r-q**i) for i in range(r))
        count=gaussian(n,r,q)*gaussian(n-r,r,q)*gl
        pieces.append((r,count,exponent))
        s+=count*q**exponent
    return s,pieces


def check_A(n,q,limit=None):
    N=n*(n-1)//2
    found={};bad=0;examined=0
    for tup in product(range(q), repeat=n*n):
        A=[list(tup[i*n:(i+1)*n]) for i in range(n)]
        if any(v for row in mm(A,A,q) for v in row):continue
        r=rank(A,q);C=induced(A,q)
        if any(v for row in mm(C,C,q) for v in row):
            assert q%2==1 and r>=2
            bad+=1
            continue
        rho=rank(C,q)
        assert rho==r*(n-r-1),(n,q,r,rho)
        fiber_exp=n*N-fiber_rank(A,C,q)
        want=(n-r)*N-(n-2*r)*rho
        assert fiber_exp==want,(n,q,r,fiber_exp,want)
        count,exp=found.get(r,(0,fiber_exp))
        assert exp==fiber_exp
        found[r]=(count+1,exp)
        examined+=1
        if limit and examined>=limit:break
    if not limit:
        _,pieces=predicted(n,q)
        assert [(r,c,e) for r,(c,e) in sorted(found.items())]==pieces,(found,pieces)
    return examined,bad,found


def full_brute(n,q):
    N=n*(n-1)//2
    total=0
    for atup in product(range(q),repeat=n*n):
        A=[list(atup[i*n:(i+1)*n]) for i in range(n)]
        if any(x for row in mm(A,A,q) for x in row):continue
        C=induced(A,q)
        if any(x for row in mm(C,C,q) for x in row):continue
        for btup in product(range(q),repeat=n*N):
            B=[list(btup[i*n:(i+1)*n]) for i in range(N)]
            BA=mm(B,A,q);CB=mm(C,B,q)
            if all(add(BA[i][j],CB[i][j],q)==0 for i in range(N) for j in range(n)):
                total+=1
    assert total==predicted(n,q)[0],(n,q,total,predicted(n,q))
    return total


if __name__=='__main__':
    for n,q in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)]:
        a=check_A(n,q)
        print('A_FIBER_OK',n,q,a,'TOTAL',predicted(n,q)[0],flush=True)
    for n,q in [(2,2),(2,3),(3,2)]:
        print('FULL_DERIVATION_BRUTE_OK',n,q,full_brute(n,q),flush=True)
    # Independent arithmetic on a representative rank-two square-zero matrix in characteristic two.
    n=4;q=2
    A=zero(n,n);A[0][2]=1;A[1][3]=1
    C=induced(A,q)
    assert rank(A,q)==2 and rank(C,q)==2
    assert all(v==0 for row in mm(C,C,q) for v in row)
    assert n*6-fiber_rank(A,C,q)==12
    print('RANK_TWO_MODULAR_BRANCH_OK',n,q,'fiber_size',2**12,flush=True)
    C3=induced(A,3)
    assert any(v for row in mm(C3,C3,3) for v in row)
    print('ODD_CHARACTERISTIC_RANK_TWO_OBSTRUCTION_OK',flush=True)
    print('SQUARE_ZERO_FREE_TWO_STEP_DERIVATIONS_OK',flush=True)
