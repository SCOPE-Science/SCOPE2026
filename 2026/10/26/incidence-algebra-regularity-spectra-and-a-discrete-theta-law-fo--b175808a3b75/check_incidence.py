#!/usr/bin/env python3
"""Exhaustive independent checks of incidence-algebra regularity and count stratification."""
from itertools import product
from collections import Counter


def inverse_mod(x,q):return pow(x,-1,q)

def rank_augmented(vectors,target,q):
    d=len(target)
    a=[[vectors[j][i] for j in range(d)]+[target[i]] for i in range(d)]
    piv=0
    for col in range(d):
        k=next((h for h in range(piv,d) if a[h][col]%q),None)
        if k is None: continue
        a[piv],a[k]=a[k],a[piv]
        fac=inverse_mod(a[piv][col],q)
        a[piv]=[(x*fac)%q for x in a[piv]]
        for h in range(d):
            if h==piv:continue
            coeff=a[h][col]
            if coeff:a[h]=[(a[h][t]-coeff*a[piv][t])%q for t in range(d+1)]
        piv+=1
    return not any(all(x%q==0 for x in row[:-1]) and row[-1]%q for row in a)

def case(name,n,strict,q):
    edges=sorted(strict); pairs=[(i,i) for i in range(n)]+edges
    assert all(i<j for i,j in edges)
    assert all((i,k) in strict for i,j in edges for h,k in edges if j==h)
    d=len(pairs); ind={p:k for k,p in enumerate(pairs)}
    def mul(a,b):
        return tuple(sum(a[ind[i,h]]*b[ind[h,j]] for h in range(i,j+1) if (i,h) in ind and (h,j) in ind)%q for i,j in pairs)
    seen=Counter(); found=0
    for a in product(range(q),repeat=d):
        zeros={i for i in range(n) if a[i]==0}
        P=[i for i in range(n) if i not in zeros]
        # Schur residual matrix via triangular inversion on the pivot support.
        B={(u,v):a[ind[u,v]] if (u,v) in ind else 0 for u in P for v in P}
        inv={}
        for i in P:
            inv[i,i]=inverse_mod(B[i,i],q)
        for gap in range(1,n):
            for u in P:
                v=u+gap
                if v in P and (u,v) in ind:
                    inv[u,v]=(-inv[u,u]*sum(B.get((u,h),0)*inv.get((h,v),0) for h in P if u<h<=v))%q
        S={}
        for i in zeros:
            for j in zeros:
                if (i,j) not in ind or i==j:continue
                correction=sum(a[ind[i,u]]*inv.get((u,v),0)*a[ind[v,j]] for u in P for v in P if (i,u) in ind and (v,j) in ind)%q
                S[i,j]=(a[ind[i,j]]-correction)%q
        schur_reg=all(v==0 for v in S.values())
        # Independently solve a*x*a=a as linear equations over the field.
        basis=[tuple(1 if h==j else 0 for h in range(d)) for j in range(d)]
        vectors=[mul(mul(a,e),a) for e in basis]
        brute=rank_augmented(vectors,a,q)
        assert brute==schur_reg,(name,n,q,a,S)
        if brute:seen[len(zeros)]+=1;found+=1
    expected=Counter()
    for mask in range(1<<n):
        z={i for i in range(n) if mask&(1<<i)}
        eZ=sum(i in z and j in z for i,j in edges)
        expected[len(z)]+=(q-1)**(n-len(z))*q**(len(edges)-eZ)
    assert seen==expected,(name,q,seen,expected)
    print('INCIDENCE',name,'n',n,'q',q,'elements',q**d,'regular',found,'strata',dict(seen))
    return q**d

if __name__=='__main__':
    cases=[
      ('chain3',3,{(0,1),(0,2),(1,2)},2),
      ('chain3',3,{(0,1),(0,2),(1,2)},3),
      ('chain4',4,{(i,j) for i in range(4) for j in range(i+1,4)},2),
      ('diamond4',4,{(0,1),(0,2),(1,3),(2,3),(0,3)},2),
      ('diamond4',4,{(0,1),(0,2),(1,3),(2,3),(0,3)},3),
      ('V4',4,{(0,2),(1,2),(1,3)},2),
      ('antichain4',4,set(),2),
    ]
    count=sum(case(*row) for row in cases)
    print('ALL_INCIDENCE_ALGEBRA_REGULAR_CHECKS_PASSED cases=%d elements=%d'%(len(cases),count))
