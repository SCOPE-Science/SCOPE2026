#!/usr/bin/env python3
"""Standalone finite-field verification for weight-zero Rota--Baxter operators on k+V, V^2=0."""
from itertools import product
from math import prod

def add(a,b,q):
    if q==4: return a^b
    return (a+b)%q

def mul(a,b,q):
    if q==4:
        z=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:
                    z ^= 1<<(i+j)
        if z&8: z^=0b1100 # t^3=t+1 so t^3+t+1=0
        if z&4: z^=0b111 # t^2=t+1
        return z
    return (a*b)%q

def mat_apply(M,v,q):
    return tuple(sum_mod([mul(a,b,q) for a,b in zip(row,v)],q) for row in M)

def sum_mod(items,q):
    z=0
    for x in items:z=add(z,x,q)
    return z

def squarezero(T,q):
    n=len(T)
    return all(x==0 for col in zip(*T) for x in mat_apply(T,col,q)) # each column of T -> zero

def rb_condition(P,q):
    # basis (1,e1,...,en); product (a,v)*(b,w)=(ab,aw+bv).
    N=len(P)
    def app(v):return mat_apply(P,v,q)
    def times(a,b):
        return (mul(a[0],b[0],q),)+tuple(add(mul(a[0],b[i],q),mul(b[0],a[i],q),q) for i in range(1,N))
    basis=[tuple(int(i==j) for i in range(N)) for j in range(N)]
    for a in basis:
        for b in basis:
            pa,pb=app(a),app(b)
            lhs=times(pa,pb)
            x,y=times(pa,b),times(a,pb)
            rhs=app(tuple(add(xx,yy,q) for xx,yy in zip(x,y)))
            if lhs!=rhs:return False
    return True

def expected(T,u,q):
    if not squarezero(T,q):return False
    if q%2==0:return True
    return all(x==0 for x in mat_apply(T,u,q))

def build(T,u):
    n=len(T)
    return ((0,)* (n+1),)+tuple((u[i],)+T[i] for i in range(n))

def all_matrices(n,q):
    return (tuple(tuple(a[i*n:(i+1)*n]) for i in range(n)) for a in product(range(q), repeat=n*n))

def rank(M,q):
    a=[list(row) for row in M]
    m=len(a);n=len(a[0]);r=0
    for c in range(n):
        ix=next((i for i in range(r,m) if a[i][c]),None)
        if ix is None:continue
        a[r],a[ix]=a[ix],a[r]
        inv=next(v for v in range(1,q) if mul(v,a[r][c],q)==1)
        a[r]=[mul(v,inv,q) for v in a[r]]
        for i in range(m):
            if i==r:continue
            t=a[i][c]
            a[i]=[add(a[i][j], (-t*a[r][j])%q,q) if q!=4 else add(a[i][j],mul(t,a[r][j],q),q) for j in range(n)]
        r+=1
        if r==m:break
    return r

def invert(M,q):
    n=len(M)
    a=[list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(M)]
    for c in range(n):
        ix=next((i for i in range(c,n) if a[i][c]),None)
        if ix is None:return None
        a[c],a[ix]=a[ix],a[c]
        inv=next(v for v in range(1,q) if mul(v,a[c][c],q)==1)
        a[c]=[mul(v,inv,q) for v in a[c]]
        for i in range(n):
            if i==c:continue
            k=a[i][c]
            a[i]=[add(a[i][j],mul(k,a[c][j],q) if q==4 else (-k*a[c][j])%q,q) for j in range(2*n)]
    return tuple(tuple(row[n:]) for row in a)

def matrix_prod(A,B,q):
    return tuple(tuple(sum_mod([mul(A[i][k],B[k][j],q) for k in range(len(B))],q) for j in range(len(B[0]))) for i in range(len(A)))

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def gl(r,q):return prod(q**r-q**i for i in range(r))

def counts(n,q):
    result={}
    for T in all_matrices(n,q):
        r=rank(T,q)
        if not squarezero(T,q):continue
        for u in product(range(q),repeat=n):
            P=build(T,u)
            expected_result=expected(T,u,q)
            assert expected_result==rb_condition(P,q),(n,q,T,u)
            if expected_result:
                kind='index3' if any(mat_apply(T,u,q)) else 'index2_or_zero'
                row=(r,kind)
                result[row]=result.get(row,0)+1
    for r in range(n//2+1):
        t=gaussian(n,r,q)*gaussian(n-r,r,q)*gl(r,q)
        e=(t*(q**n if q%2==0 else q**(n-r)))
        got=sum(v for (rankT,_),v in result.items() if rankT==r)
        assert got==e,(n,q,r,e,got)
    print('COUNTS_OK',n,q,sum(result.values()),result)
    return result

def check_orbits(n,q):
    Ts=[T for T in all_matrices(n,q) if squarezero(T,q)]
    points={(T,u) for T in Ts for u in product(range(q),repeat=n) if expected(T,u,q)}
    mats=[(G,invert(G,q)) for G in all_matrices(n,q)]
    mats=[(G,Ginv) for G,Ginv in mats if Ginv is not None]
    orbits=[]
    while points:
        T,u=next(iter(points))
        orbit=set()
        for G,Ginv in mats:
            tt=matrix_prod(matrix_prod(G,T,q),Ginv,q)
            uu=mat_apply(G,u,q)
            orbit.add((tt,uu))
        assert orbit<=points
        points-=orbit
        orbits.append((rank(T,q), 'zero' if not any(u) else 'image' if any(u==mat_apply(T,z,q) for z in product(range(q),repeat=n)) else 'kernel_nonimage' if not any(mat_apply(T,u,q)) else 'outside_kernel',len(orbit)))
    expected_num=2+sum((4 if q%2==0 else 3) if n-2*r>0 else (3 if q%2==0 else 2) for r in range(1,n//2+1))
    assert len(orbits)==expected_num,(orbits,expected_num)
    print('ORBIT_OK',n,q,len(orbits),sorted(orbits))

if __name__=='__main__':
    counts(2,2)
    counts(2,3)
    counts(2,4)
    counts(3,2)
    check_orbits(2,2)
    check_orbits(2,3)
    check_orbits(3,2)
    print('VERIFY_OK')
