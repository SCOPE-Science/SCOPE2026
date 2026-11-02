#!/usr/bin/env python3
"""Exact coefficient checks for the odd missing-part survival identity."""
from math import exp, pi

def multiply_all(dp,j,nmax,forced=False):
    # local factor 1+2q^j+... or forced-positive factor 2q^j+...
    nxt=[0]*(nmax+1)
    for n,v in enumerate(dp):
        if not v: continue
        if not forced:nxt[n]+=v
        for k in range(n+j,nmax+1,j):nxt[k]+=2*v
    return nxt

def coefficients(nmax,forced_m):
    dp=[1]+[0]*nmax
    for j in range(1,nmax+1):
        dp=multiply_all(dp,j,nmax,forced=(j%2==1 and j<=2*forced_m-1))
    return dp

def algebraic_constraint(pbar,nmax,m):
    dp=pbar[:]
    for j in range(1,2*m,2):
        for k in range(j,nmax+1):
            dp[k]-=dp[k-j]   # divide by (1+q^j): f_k=d_k-f_(k-j)
    out=[0]*(nmax+1)
    for n in range(m*m,nmax+1):out[n]=2**m*dp[n-m*m]
    return out

def main():
    N=170
    base=coefficients(N,0)
    assert base[:10]==[1,2,4,8,14,24,40,64,100,154],base[:10]
    examined=0
    for m in range(0,14):
        direct=coefficients(N,m)
        alt=algebraic_constraint(base,N,m)
        for n in range(N+1):
            assert direct[n]==alt[n],(m,n,direct[n],alt[n])
            assert 0<=direct[n]<=base[n]
            examined+=1
    # independent base normalization and tail monotonicity
    for n in range(N+1):
        seq=[algebraic_constraint(base,N,m)[n] for m in range(14)]
        assert all(seq[i]>=seq[i+1] for i in range(13))
    print(f'VERIFY_OK exact_coefficients={examined} n_max={N} m_max=13 base_overpartitions=verified identity=verified monotone=verified')
    for n in (50,100,150):
        y=2.0
        m=int((y*n**0.25)/2)
        c=algebraic_constraint(base,N,m)[n]/base[n]
        print('finite_sample n=',n,'m=',m,'observed_survival=',round(c,6),'Rayleigh_target=',round(exp(-pi*(2*m-1)**2/(16*n**0.5)),6))
if __name__=='__main__':main()
