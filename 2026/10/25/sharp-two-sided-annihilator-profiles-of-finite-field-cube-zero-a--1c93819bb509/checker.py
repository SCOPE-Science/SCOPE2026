#!/usr/bin/env python3
"""Exhaustive prime-field verification of paired square-image/annihilator profile counts."""
from collections import Counter
from itertools import product
from math import prod

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    z=1
    for i in range(k):
        z=z*(q**(n-i)-1)//1  # postpone division below
    denom=prod(q**(k-i)-1 for i in range(k))
    return z//denom

def surj(m,t,q):
    if t>m:return 0
    return prod(q**m-q**i for i in range(t))

def dimension(v,symmetric):return v*(v+1)//2 if symmetric else v*v

def formula(q,r,s,symmetric):
    res={}
    for d in range(r+1):
      for t in range(s+1):
        z=0
        for j in range(r-d+1):
          z+=(-1)**j*q**(j*(j-1)//2)*gaussian(r-d,j,q)*surj(dimension(r-d-j,symmetric),t,q)
        count=gaussian(r,d,q)*gaussian(s,t,q)*z
        assert count>=0,(q,r,s,symmetric,d,t,count)
        res[(d,t)]=count
    assert sum(res.values())==q**(s*dimension(r,symmetric))
    return res

def rank_mod(a,q):
    a=[row[:] for row in a]
    if not a:return 0
    m=len(a);n=len(a[0]);i=0
    for j in range(n):
        h=next((h for h in range(i,m) if a[h][j]%q),None)
        if h is None:continue
        a[i],a[h]=a[h],a[i]
        inv=pow(a[i][j],-1,q)
        a[i]=[(v*inv)%q for v in a[i]]
        for k in range(i+1,m):
            c=a[k][j]%q
            if c:a[k]=[(u-c*v)%q for u,v in zip(a[k],a[i])]
        i+=1
        if i==m:break
    return i

def enumerate_case(q,r,s,symmetric):
    positions=[(i,j) for i in range(r) for j in range(i if symmetric else 0,r)]
    N=len(positions)
    out=Counter(); examined=0
    for flat in product(range(q),repeat=s*N):
        components=[]
        for k in range(s):
            m=[[0]*r for _ in range(r)]
            for h,(i,j) in enumerate(positions):
                v=flat[k*N+h]
                m[i][j]=v
                if symmetric:m[j][i]=v
            components.append(m)
        rad_constraints=[]
        for m in components:
            rad_constraints+=m
            if not symmetric:
                rad_constraints+=list(map(list,zip(*m)))
        d=r-rank_mod(rad_constraints,q)
        t=rank_mod([list(flat[k*N:(k+1)*N]) for k in range(s)],q)
        out[(d,t)]+=1
        examined+=1
    prediction=formula(q,r,s,symmetric)
    assert all(out[k]==v for k,v in prediction.items()),(q,r,s,symmetric,out,prediction)
    return examined,out

def main():
    cases=[(2,1,1,False),(2,2,2,True),(2,3,2,True),(2,3,1,False),
           (2,4,1,False),(2,3,1,True),(3,2,2,True),(3,2,1,False),
           (3,3,1,True),(3,2,1,True)]
    n=0
    for q,r,s,symmetric in cases:
        examined,counts=enumerate_case(q,r,s,symmetric)
        n+=examined
        tag='commutative' if symmetric else 'general'
        print(f'q={q} r={r} s={s} type={tag} maps={examined} profiles={sorted(counts.items())}')
    print(f'ALL_NILPOTENT_ANNIHILATOR_PROFILE_CHECKS_PASSED cases={len(cases)} maps={n}')
if __name__=='__main__':main()
