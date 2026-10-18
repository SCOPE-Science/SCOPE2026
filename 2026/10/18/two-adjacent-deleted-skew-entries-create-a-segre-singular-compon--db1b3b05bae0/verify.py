#!/usr/bin/env python3
"""Finite-field singular-support census and integral Pfaffian Hessian tests.

This is a finite reproducibility aid; the arbitrary-size statements require
(and are established by) the separately written geometric proof.
"""
from itertools import combinations


def terms(indices):
    if not indices:
        yield (1, ())
        return
    a = indices[0]
    for k in range(1, len(indices)):
        b = indices[k]
        for s, rest in terms(indices[1:k] + indices[k+1:]):
            yield ((-1) ** (k-1) * s, ((a,b),) + rest)


def allowed(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)
            if (i,j) not in ((0,1),(0,2))]


def rank_mod2(n, coords):
    rows=[0]*n
    for (i,j),v in coords.items():
        if v&1:
            rows[i] ^= 1<<j
            rows[j] ^= 1<<i
    rank=0
    for col in range(n):
        sel=next((i for i in range(rank,n) if rows[i]>>col&1), None)
        if sel is None: continue
        rows[rank],rows[sel]=rows[sel],rows[rank]
        for i in range(n):
            if i!=rank and rows[i]>>col&1:rows[i]^=rows[rank]
        rank+=1
    return rank


def census_six():
    n=6; E=allowed(n); T=[]
    for sign,ps in terms(tuple(range(n))):
        if all(e in E for e in ps):T.append(tuple(E.index(e) for e in ps))
    counts={'total_projective':0,'singular':0,'rank_two':0,
            'Y1':0,'Y2':0,'Z':0,'other':0}
    for mask in range(1,1<<len(E)):
        vec=[(mask>>i)&1 for i in range(len(E))]
        coords=dict(zip(E,vec))
        p=0;grad=[0]*len(E)
        for t in T:
            q=vec[t[0]]&vec[t[1]]&vec[t[2]]
            p ^= q
            for k in range(3):
                grad[t[k]]^=vec[t[(k+1)%3]]&vec[t[(k+2)%3]]
        counts['total_projective']+=1
        singular=p==0 and not any(grad)
        rk=rank_mod2(n,coords)
        Y1=(rk<=2 and all(coords[0,j]==0 for j in range(3,n)))
        Y2=(rk<=2 and coords[1,2]==0)
        xzero=all(coords[0,j]==0 for j in range(3,n))
        rone=all(coords[1,j]*coords[2,k] == coords[1,k]*coords[2,j]
                 for j,k in combinations(range(3,n),2))
        Z=xzero and coords[1,2]==0 and rone
        if singular != (Y1 or Y2 or Z):
            raise AssertionError(('wrong singular description',mask,rk,p,grad,Y1,Y2,Z))
        if singular:counts['singular']+=1
        if rk==2:counts['rank_two']+=1
        if Y1:counts['Y1']+=1
        if Y2:counts['Y2']+=1
        if Z:counts['Z']+=1
        if singular and not (Y1 or Y2 or Z):counts['other']+=1
    return counts


def mat_vec(n, vals):
    return {(i,j):vals.get((i,j),0) for i,j in allowed(n)}


def rank_rational(M):
    from fractions import Fraction
    a=[[Fraction(z) for z in row] for row in M]
    n=len(a);r=0
    for j in range(n):
        idx=next((i for i in range(r,n) if a[i][j]),None)
        if idx is None:continue
        a[r],a[idx]=a[idx],a[r]
        x=a[r][j]
        a[r]=[v/x for v in a[r]]
        for i in range(n):
            if i!=r and a[i][j]:
                x=a[i][j]
                a[i]=[a[i][h]-x*a[r][h] for h in range(n)]
        r+=1
    return r


def hessian_rank(n, vals):
    E=allowed(n);idx={e:i for i,e in enumerate(E)}
    H=[[0]*len(E) for _ in E]
    grad=[0]*len(E);P=0
    for sign, matching in terms(tuple(range(n))):
        if not all(e in idx for e in matching):continue
        product=sign
        for e in matching:product*=vals.get(e,0)
        P+=product
        for i,e in enumerate(matching):
            q=sign
            for j,f in enumerate(matching):
                if i!=j:q*=vals.get(f,0)
            grad[idx[e]]+=q
        for i,e in enumerate(matching):
            for j,f in enumerate(matching):
                if i>=j:continue
                q=sign
                for k,g in enumerate(matching):
                    if k not in (i,j):q*=vals.get(g,0)
                H[idx[e]][idx[f]]+=q
                H[idx[f]][idx[e]]+=q
    assert P==0 and all(q==0 for q in grad), (n,P,grad)
    return rank_rational(H)


def witnesses():
    for n in (6,8,10):
        # Corank-two point on the exceptional rank-one locus.
        v={(1,3):1,(2,3):2}
        v.update((i,i+1) for i in [])
        for k in range(4,n,2):v[(k,k+1)]=1
        h=hessian_rank(n,mat_vec(n,v))
        assert h==2*n-6,(n,h)
    n=6
    u=[0,1,0,1,0,0];v=[0,0,1,0,1,0]
    for U,V in [(u,v),([1,1,1,0,0,0],[0,0,0,1,1,0])]:
        vals={(i,j):U[i]*V[j]-U[j]*V[i] for i,j in allowed(n)}
        assert hessian_rank(n,vals)==6
    C=[[1,0,0,0],[1,0,1,0],[0,0,0,1],[0,1,0,0],
       [0,0,1,0],[1,1,0,1],[2,1,1,0],[1,2,2,2]]
    J=[[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]]
    vals={(i,j):sum(C[i][a]*J[a][b]*C[j][b]
            for a in range(4) for b in range(4))
          for i,j in allowed(8)}
    A=[[0]*8 for _ in range(8)]
    for (i,j),q in vals.items():A[i][j]=q;A[j][i]=-q
    assert rank_rational(A)==4 and hessian_rank(8,vals)==6
    return 'HESSIAN_RANKS_OK' 

if __name__=='__main__':
    print('GF2_PROJECTIVE_CENSUS_n6',census_six())
    print(witnesses())
    print('VERIFY_OK')
