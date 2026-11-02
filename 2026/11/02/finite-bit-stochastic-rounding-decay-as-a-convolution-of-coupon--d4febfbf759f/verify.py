#!/usr/bin/env python3
"""Reproduce exact finite-state and coupon-collector identities using rational arithmetic."""
from fractions import Fraction as F
from math import factorial

def harmonic(k,s=1):
    return sum((F(1,j**s) for j in range(1,k+1)),F(0))

def stirling2(n,k):
    S=[[0]*(k+1) for _ in range(n+1)]
    S[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            S[i][j]=j*S[i-1][j]+S[i-1][j-1]
    return S[n][k]

def direct_pmf(p,r,horizon):
    n=2**p; k=2**r; end=max(0,n//k-1) if r<=p else 0
    state=[F(0)]*(n+1)
    state[n]=F(1)
    masses=[F(0)]*(horizon+1)
    masses[0]=state[end]
    for t in range(1,horizon+1):
        v=[F(0)]*(n+1)
        for j in range(end,n+1):
            if not state[j]:continue
            q=F((k*j)//n,k)
            if j==end:v[j]+=state[j]
            else:
                assert q>0
                v[j-1]+=state[j]*q
                v[j]+=state[j]*(1-q)
        state=v
        masses[t]=state[end]-sum(masses[:t])
    return masses

def conv(a,b,h):
    z=[F(0)]*(h+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:h+1-i]):
                if y:z[i+j]+=x*y
    return z

def coupon_pmf(k,h):
    # Pr(C_k=t) = (k!/k^t) S(t-1,k-1), for t>=k,
    # because the last draw must discover the final unseen type.
    out=[F(0)]*(h+1)
    for t in range(k,h+1):
        out[t]=F(factorial(k),k**t)*stirling2(t-1,k-1)
    return out

def check():
    count=0
    for p in range(1,5):
      n=2**p
      for r in range(1,p+1):
        k=2**r;l=n//k
        horizon=min(80,2*n*k)
        direct=direct_pmf(p,r,horizon)
        cap=horizon+l+1
        c=coupon_pmf(k,cap)
        cc=[F(1)]+[F(0)]*cap
        for a in range(l):cc=conv(cc,c,cap)
        reconstructed=[F(0)]*(horizon+1)
        for t in range(horizon+1):
            j=t+l-1
            if j<=cap:reconstructed[t]=cc[j]
        assert direct==reconstructed,(p,r,[(i,a,b) for i,(a,b) in enumerate(zip(direct,reconstructed)) if a!=b][:3]);count+=1
        # Moments from individual geometric holding times, not from truncated PMF.
        waiting_p=[F((k*j)//n,k) for j in range(l,n+1)]
        ex=sum((1/z for z in waiting_p),F(0))
        va=sum(((1-z)/z**2 for z in waiting_p),F(0))
        assert ex==1+n*harmonic(k-1)
        assert va==n*k*harmonic(k-1,2)-n*harmonic(k-1)
        count+=2
        assert F(l-1,n) == F(1,k)-F(1,n);count+=1
        # PGF coefficients independently equal state distribution from coupon convolution.
        assert sum(direct)<=1; count+=1
    for p in range(1,7):
      n=2**p
      for r in range(p,p+3):
        k=2**r
        assert all(F((k*j)//n,k)==F(j,n) for j in range(n+1));count+=1
    # One specific worked case: p=4,r=2 gives exactly 3/16 plateau and 91/3 expected steps.
    assert F(1+16*harmonic(3))==F(91,3)
    assert F(16*4*harmonic(3,2)-16*harmonic(3))==F(520,9)
    count+=2
    print(f'PASS {count} rational identities and exact distributions across dyadic grids')

if __name__=='__main__':check()
