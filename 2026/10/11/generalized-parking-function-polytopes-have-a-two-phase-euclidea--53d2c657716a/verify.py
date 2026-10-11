#!/usr/bin/env python3
import math
from itertools import combinations
from scipy.optimize import linprog

def threshold(n,a,b,k):
    U=k*(a+b*(n-(k+1)/2))
    return (U-k)/(k+math.sqrt(k))

def formula(n,a,b):
    A=a-1
    r1=(A+b*(n-1))/2
    rn=math.sqrt(n)/(math.sqrt(n)+1)*(A+b*(n-1)/2)
    return min(r1,rn),r1,rn

def lp(n,a,b):
    # Variables x_1,...,x_n,r; minimize -r.
    c=[0.0]*n+[-1.0]
    A=[]; B=[]
    for i in range(n):
        row=[0.0]*(n+1)
        row[i]=-1.0; row[-1]=1.0
        A.append(row); B.append(-1.0)
    for k in range(1,n+1):
        if a==1 and k==n-1:
            continue
        U=k*(a+b*(n-(k+1)/2))
        for I in combinations(range(n),k):
            row=[0.0]*(n+1)
            for i in I: row[i]=1.0
            row[-1]=math.sqrt(k)
            A.append(row); B.append(U)
    res=linprog(c,A_ub=A,b_ub=B,bounds=[(None,None)]*n+[(0,None)],method='highs')
    assert res.success
    return res.x[-1],res.x[:-1]

cases=0
for n in range(2,31):
    for a in (1,2,3,5,9,17,33):
        for b in (1,2,4,7):
            r,r1,rn=formula(n,a,b)
            ks=[k for k in range(1,n+1) if not (a==1 and k==n-1)]
            vals={k:threshold(n,a,b,k) for k in ks}
            assert abs(min(vals.values())-r) < 2e-11*max(1.0,r)
            t=1+r
            for k,v in vals.items():
                U=k*(a+b*(n-(k+1)/2))
                clearance=(U-k*t)/math.sqrt(k)
                assert clearance >= r-2e-10
            if r1 < rn-1e-10:
                assert abs(vals[1]-r)<1e-10
                assert all(vals[k]>r+1e-10 for k in ks if k!=1)
            elif rn < r1-1e-10:
                assert abs(vals[n]-r)<1e-10
                assert all(vals[k]>r+1e-10 for k in ks if k!=n)
            cases+=1

lp_cases=0
for n in range(2,6):
    for a in (1,2,4,8,15):
        for b in (1,2,3):
            r,_,_=formula(n,a,b)
            rlp,x=lp(n,a,b)
            assert abs(rlp-r) < 2e-8*max(1.0,r),(n,a,b,r,rlp)
            assert max(abs(z-(1+r)) for z in x) < 2e-7,(n,a,b,x,1+r)
            lp_cases+=1

print(f"VERIFY_OK parking-inradius threshold_cases={cases} lp_cases={lp_cases} n=2..30")
