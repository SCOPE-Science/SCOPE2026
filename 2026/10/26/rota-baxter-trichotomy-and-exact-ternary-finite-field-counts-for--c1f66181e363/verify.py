#!/usr/bin/env python3
"""Independent coefficient tests for the rank-one evolution-algebra Rota--Baxter trichotomy.

No external packages are required. Matrices act on column vectors.
"""
from itertools import product


def maps(n, q):
    for a in product(range(q), repeat=n*n):
        yield tuple(tuple(a[i*n:(i+1)*n]) for i in range(n))


def mv(P, v, q):
    n=len(v)
    return tuple(sum(P[i][j]*v[j] for j in range(n)) % q for i in range(n))


def pair(x,y,B,q):
    n=len(x)
    return sum(x[i]*B[i][j]*y[j] for i in range(n) for j in range(n))%q


def rb_direct(P,B,u,lam,q):
    n=len(u)
    pu=mv(P,u,q)
    for i in range(n):
        x=tuple(int(i==j) for j in range(n)); px=mv(P,x,q)
        for j in range(i,n):
            y=tuple(int(k==j) for k in range(n)); py=mv(P,y,q)
            lhs=pair(px,py,B,q)
            rhs=(pair(px,y,B,q)+pair(x,py,B,q)+lam*pair(x,y,B,q))%q
            if any((lhs*u[k]-rhs*pu[k])%q for k in range(n)):
                return False
    return True


def trichotomy(P,B,u,lam,q):
    n=len(u); pu=mv(P,u,q)
    z=tuple(0 for _ in range(n))
    def image_isotropic(Q):
        cols=[tuple(Q[k][j] for k in range(n)) for j in range(n)]
        return all(pair(cols[i],cols[j],B,q)==0 for i in range(n) for j in range(i,n))
    if pu==z and image_isotropic(P):
        return 'A'
    if pu==tuple((-lam*u[i])%q for i in range(n)):
        Q=tuple(tuple((P[i][j]+(lam if i==j else 0))%q for j in range(n)) for i in range(n))
        if image_isotropic(Q):return 'B'
    columns=[tuple(P[k][j] for k in range(n)) for j in range(n)]
    basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    adjoint_condition=all((pair(columns[i],basis[j],B,q)+pair(basis[i],columns[j],B,q)+lam*pair(basis[i],basis[j],B,q))%q==0 for i in range(n) for j in range(n))
    sqzero_condition=all((sum(P[i][k]*P[k][j] for k in range(n))+lam*P[i][j])%q==0 for i in range(n) for j in range(n))
    if adjoint_condition and sqzero_condition:return 'C'
    return None


def square_zero(P,q):
    n=len(P)
    return all(sum(P[i][k]*P[k][j] for k in range(n))%q==0 for i in range(n) for j in range(n))


def diagonal(ds):
    n=len(ds)
    return tuple(tuple(ds[i] if i==j else 0 for j in range(n)) for i in range(n))


def exhaustive(n,q,ds,u):
    B=diagonal(ds)
    for lam in (0,1):
        count=0; zero=0; seen=0
        for P in maps(n,q):
            direct=rb_direct(P,B,u,lam,q)
            cls=trichotomy(P,B,u,lam,q)
            assert direct == (cls is not None), (n,q,ds,u,lam,P,direct,cls)
            seen+=1
            if direct:
                count+=1
                if square_zero(P,q):zero+=1
        if n==3:
            total=q**3+q*q-q
            assert count==(total if lam==0 else 2*total), (count,total)
            if lam==0:
                norm=pair(u,u,B,q)
                assert zero==(q*q if norm else 2*q*q-q), (zero,norm)
        print('EXHAUSTIVE',n,q,ds,u,'weight',lam,'maps',seen,'operators',count,'square_zero',zero)


def canonical(v,q):
    pivot=next(x for x in v if x%q)
    inv=pow(pivot,-1,q)
    return tuple((x*inv)%q for x in v)


def constructed_count(q,ds,u):
    B=diagonal(ds); n=3
    lines=set()
    for v in product(range(q),repeat=n):
        if any(v) and pair(v,v,B,q)==0:lines.add(canonical(v,q))
    assert len(lines)==q+1,len(lines)
    count=1; zeros=1
    for v in lines:
        for f in product(range(q),repeat=n):
            if not any(f) or sum(u[i]*f[i] for i in range(n))%q!=0:continue
            P=tuple(tuple(v[i]*f[j]%q for j in range(n)) for i in range(n))
            assert rb_direct(P,B,u,0,q)
            assert trichotomy(P,B,u,0,q)=='A'
            count+=1;zeros+=square_zero(P,q)
    norm=pair(u,u,B,q)
    assert count==q**3+q*q-q
    assert zeros==(q*q if norm else 2*q*q-q)
    print('CONSTRUCTED',3,q,ds,u,'lines',len(lines),'weight0',count,'square_zero',zeros)


def branch_c_witnesses():
    q=5
    B=((0,1),(1,0));u=(1,1)
    P=((q-1,0),(0,0))
    assert trichotomy(P,B,u,1,q)=='C' and rb_direct(P,B,u,1,q)
    B=((0,0,1,0),(0,0,0,1),(1,0,0,0),(0,1,0,0))
    u=(0,0,1,0)
    P=((0,0,0,q-1),(0,0,1,0),(0,0,0,0),(0,0,0,0))
    assert trichotomy(P,B,u,0,q)=='C' and rb_direct(P,B,u,0,q)
    assert not square_zero(((1,),),q)
    print('WITNESSES branch_C_weight0_dim4 branch_C_weight1_dim2 PASS')

if __name__=='__main__':
    cases=[(2,3,(1,1),(1,0)),(2,3,(1,2),(1,1)),
           (2,5,(1,1),(1,2)),(3,3,(1,1,1),(1,0,0)),
           (3,3,(1,1,1),(1,1,1)),(3,3,(1,1,2),(1,0,1)),
           (3,3,(1,1,2),(1,0,0))]
    for case in cases:exhaustive(*case)
    constructed_count(5,(1,1,1),(1,1,1))
    constructed_count(5,(1,1,1),(1,0,0))
    constructed_count(7,(1,1,1),(1,0,0))
    constructed_count(7,(1,1,1),(1,2,3))
    branch_c_witnesses()
    print('VERIFY_OK')
