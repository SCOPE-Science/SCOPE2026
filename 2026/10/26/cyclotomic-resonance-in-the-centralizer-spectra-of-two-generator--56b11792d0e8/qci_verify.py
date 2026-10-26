#!/usr/bin/env python3
"""Independent finite-field checks of centralizer ranks for two-generator skew truncated algebras."""
from itertools import product
from collections import Counter

def direct_rank(a, p, lam, m):
    """Compute inner-commutator rank directly using the 2m x 2m multiplication table.

    Coordinates are y^0,...,y^(m-1),x y^0,...,x y^(m-1),
    using y x = lam^{-1} x y.
    """
    inv = pow(lam,-1,p)
    def mul(u,v):
        z=[0]*(2*m)
        # y^i * y^j
        for i in range(m):
            for j in range(m-i):
                z[i+j]=(z[i+j]+u[i]*v[j])%p
                # y^i * x y^j = inv^i * x y^(i+j)
                z[m+i+j]=(z[m+i+j]+u[i]*v[m+j]*pow(inv,i,p)+u[m+i]*v[j])%p
        return z
    cols=[]
    for j in range(2*m):
        e=[0]*(2*m); e[j]=1
        z1=mul(a,e);z2=mul(e,a)
        cols.append([(z1[i]-z2[i])%p for i in range(2*m)])
    mat=[[cols[j][i] for j in range(2*m)] for i in range(2*m)]
    rank=0
    for col in range(2*m):
        pivot=next((i for i in range(rank,2*m) if mat[i][col]),None)
        if pivot is None:continue
        mat[rank],mat[pivot]=mat[pivot],mat[rank]
        d=pow(mat[rank][col],-1,p)
        for j in range(col,2*m):mat[rank][j]=mat[rank][j]*d%p
        for i in range(rank+1,2*m):
            fac=mat[i][col]
            if fac:
                for j in range(col,2*m):mat[i][j]=(mat[i][j]-fac*mat[rank][j])%p
        rank+=1
    return rank

def expected_rank(a,p,lam,m):
    d=next(j for j in range(1,p) if pow(lam,j,p)==1)
    f=a[:m];g=a[m:]
    t=next((j for j in range(1,m) if j%d and f[j]),m)
    s=next((j for j in range(m) if g[j]),m)
    return m-t+sum(1 for j in range(1,max(1,t-s)) if j%d)

def expected_hist(p,lam,m,d_override=None):
    d=d_override or next(j for j in range(1,p) if pow(lam,j,p)==1)
    nf={}
    for t in range(1,m):
        if t%d:
            nf[t]=(p-1)*p**(m-sum(j%d!=0 for j in range(1,t))-1)
    nf[m]=p**(m-sum(j%d!=0 for j in range(1,m)))
    ng={s:(p-1)*p**(m-s-1) for s in range(m)}
    ng[m]=1
    hist=Counter()
    for t,ft in nf.items():
        for s,gs in ng.items():
            rank=m-t+sum(j%d!=0 for j in range(1,max(1,t-s)))
            hist[rank]+=ft*gs
    assert sum(hist.values())==p**(2*m)
    return hist

def full(p,lam,m):
    hist=Counter()
    for a in product(range(p),repeat=2*m):
        r=direct_rank(a,p,lam,m)
        assert r==expected_rank(a,p,lam,m),(p,lam,m,a,r,expected_rank(a,p,lam,m))
        hist[r]+=1
    assert hist==expected_hist(p,lam,m),(p,lam,m,hist,expected_hist(p,lam,m))
    prob_num=sum(N*p**(2*m-r) for r,N in hist.items())
    print(f'PASS full p={p} lambda={lam} m={m} elements={p**(2*m)} ranks={dict(sorted(hist.items()))} commuting_pairs={prob_num}')
    return p**(2*m)

def spot(p,lam,m,limit=2000):
    from random import Random
    rng=Random(704183)
    hist=expected_hist(p,lam,m)
    assert sum(hist.values())==p**(2*m)
    for _ in range(limit):
        a=[rng.randrange(p) for _ in range(2*m)]
        r=direct_rank(a,p,lam,m)
        assert r==expected_rank(a,p,lam,m),(p,lam,m,a,r,expected_rank(a,p,lam,m))
    print(f'PASS spot p={p} lambda={lam} m={m} samples={limit} ranks={dict(sorted(hist.items()))}')

if __name__=='__main__':
    total=0
    for p,lam,m in [(3,1,2),(3,2,2),(3,2,3),(3,2,4),(5,1,2),(5,4,2),(5,4,3),(5,2,2),(5,2,3),(7,2,3)]:
        total+=full(p,lam,m)
    for p,lam,m in [(5,2,4),(5,2,5),(5,4,5),(7,2,5),(7,3,6),(11,3,7)]:spot(p,lam,m,1000)
    # full generic-spectrum simplification: d>=m, rank zero and all nonzero counts
    for p,lam,m in [(5,2,4),(7,3,5),(11,2,5),(13,2,9)]:
        d=next(j for j in range(1,p) if pow(lam,j,p)==1)
        if d>=m:
            hist=expected_hist(p,lam,m)
            assert hist[0]==p*p
            assert all(hist[r]==(p*p-1)*p**(2*r) for r in range(1,m))
            total_pairs=sum(N*p**(2*m-r) for r,N in hist.items())
            assert total_pairs==(p+1)*p**(3*m)-p**(2*m+1)
            print(f'PASS nonresonant closed form p={p} lambda={lam} m={m}')
    print('ALL_QUANTUM_COMPLETE_INTERSECTION_CENTRALIZER_CHECKS_PASSED',total)

# A separate extension-field arithmetic implementation tests that the
# characteristic-independent derivation also works in a non-prime field.
def gf4_mul(a,b):
    a0,a1=a&1,(a>>1)&1
    b0,b1=b&1,(b>>1)&1
    return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1)

def gf4_pow(a,k):
    z=1
    for _ in range(k):z=gf4_mul(z,a)
    return z

def gf4_rank(a,lam,m):
    inv=gf4_pow(lam,2)
    def mul(u,v):
        out=[0]*(2*m)
        for i in range(m):
            for j in range(m-i):
                out[i+j]^=gf4_mul(u[i],v[j])
                out[m+i+j]^=gf4_mul(gf4_mul(u[i],v[m+j]),gf4_pow(inv,i))^gf4_mul(u[m+i],v[j])
        return out
    cols=[]
    for j in range(2*m):
        e=[0]*(2*m);e[j]=1
        x=mul(a,e);y=mul(e,a)
        cols.append([x[i]^y[i] for i in range(2*m)])
    mat=[[cols[j][i] for j in range(2*m)] for i in range(2*m)]
    rank=0
    for col in range(2*m):
        pivot=next((i for i in range(rank,2*m) if mat[i][col]),None)
        if pivot is None:continue
        mat[rank],mat[pivot]=mat[pivot],mat[rank]
        d=gf4_pow(mat[rank][col],2)
        for j in range(col,2*m):mat[rank][j]=gf4_mul(mat[rank][j],d)
        for i in range(rank+1,2*m):
            f=mat[i][col]
            if f:
                for j in range(col,2*m):mat[i][j]^=gf4_mul(f,mat[rank][j])
        rank+=1
    return rank

def gf4_check(lam,m):
    d=next(j for j in range(1,4) if gf4_pow(lam,j)==1)
    hist=Counter()
    for a in product(range(4),repeat=2*m):
        f=a[:m];g=a[m:]
        t=next((j for j in range(1,m) if j%d and f[j]),m)
        s=next((j for j in range(m) if g[j]),m)
        pred=m-t+sum(1 for j in range(1,max(1,t-s)) if j%d)
        actual=gf4_rank(a,lam,m)
        assert pred==actual,(a,pred,actual)
        hist[actual]+=1
    assert hist==expected_hist(4,2,m,d)
    print('PASS extension field F4',lam,m,dict(sorted(hist.items())))

if __name__=='__main__':
    for lm, mm in [(1,2),(2,2),(2,3),(3,3)]:gf4_check(lm,mm)
    print('ALL_EXTENSION_FIELD_CHECKS_PASSED')
