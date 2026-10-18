#!/usr/bin/env python3
"""Exact rational independent random-walk/pinning checks for a biclique theorem."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, ceil


def solution(A, rhs):
    n = len(rhs)
    m = [[F(v) for v in A[i]] + [F(rhs[i])] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c,n) if m[i][c])
        m[c],m[piv] = m[piv],m[c]
        scale = m[c][c]
        m[c] = [v/scale for v in m[c]]
        for r in range(n):
            if r != c:
                v = m[r][c]
                if v: m[r] = [a-v*b for a,b in zip(m[r],m[c])]
    return [r[-1] for r in m]


def direct_potential(a,b, lam, source):
    n=a+b; free=[v for v in range(n) if v not in source]
    M=[];c=[]
    for v in free:
        neighbors=range(a,a+b) if v<a else range(a)
        deg=b if v<a else a
        M.append([F(int(v==w)) - lam/deg*int(w in neighbors) for w in free])
        c.append(lam*sum(w in source for w in neighbors)/deg)
    h={v:F(1) for v in source}
    for v,value in zip(free,solution(M,c)):
        h[v]=value
    return tuple(h[i] for i in range(n))


def profile_feasible(a,b,lam,tau,q,r):
    if q==a and r==b: return True
    if q==a or r==b: return tau<=lam
    s=F(q,a);t=F(r,b);den=1-lam*lam*(1-s)*(1-t)
    u=(lam*t+lam*lam*s*(1-t))/den
    v=(lam*s+lam*lam*t*(1-s))/den
    return u>=tau and v>=tau


def distribution(a,b,lam,tau):
    p=[0]*(a+b+1)
    for q in range(a+1):
        for r in range(b+1):
            if profile_feasible(a,b,lam,tau,q,r):
                p[q+r]+=comb(a,q)*comb(b,r)
    return p


def bounds(a,b,lam,tau):
    if tau>lam: return a+b, a+b, 'high'
    beta=tau*(1-lam)/(lam*(1-tau))
    rho=tau*(1-lam*lam)/(lam*lam*(1-tau))
    low=min(a*min(F(1),rho),(a+b)*beta)
    lower=ceil(low)
    if a*min(F(1),rho)<=(a+b)*beta:return lower,lower,'one-sided'
    return lower,lower+1,'balanced'


def check():
    potential_cases=0; subset_count=0; threshold_tests=0; bound_tests=0;gap_examples=[]
    Ls=[F(1,4),F(1,2),F(3,4)]
    thresholds=[F(1,20),F(1,8),F(1,4),F(1,2),F(3,4),F(1)]
    for a in range(1,5):
        for b in range(a,5):
            n=a+b
            for lam in Ls:
                direct_coeff={tau:[0]*(n+1) for tau in thresholds}
                for bits in range(1<<n):
                    S={i for i in range(n) if (bits>>i)&1}
                    q=len(S.intersection(range(a)));r=len(S.intersection(range(a,n)))
                    H=direct_potential(a,b,lam,S)
                    potential_cases+=1
                    for tau in thresholds:
                        pred=profile_feasible(a,b,lam,tau,q,r)
                        obs=all(h>=tau for h in H)
                        assert pred == obs,(a,b,lam,tau,S,H,pred)
                        threshold_tests+=1
                        if obs:direct_coeff[tau][len(S)]+=1
                    subset_count+=1
                for tau in thresholds:
                    calc=distribution(a,b,lam,tau)
                    assert calc==direct_coeff[tau]
                    actual=next(k for k,x in enumerate(calc) if x)
                    lo,hi,which=bounds(a,b,lam,tau)
                    assert lo<=actual<=hi,(a,b,lam,tau,lo,actual,hi,which)
                    bound_tests+=1
    # Widen parameters independently of the direct matrix checks.
    for a in range(1,13):
        for b in range(a,15):
            for lam in [F(1,5),F(1,3),F(2,3),F(4,5),F(9,10)]:
                for tau in [F(1,100),F(1,20),F(1,10),F(1,4),F(1,3),F(1,2),F(3,4),F(9,10),F(1)]:
                    p=distribution(a,b,lam,tau)
                    actual=next(k for k,x in enumerate(p) if x)
                    lo,hi,which=bounds(a,b,lam,tau)
                    assert lo<=actual<=hi,(a,b,lam,tau,lo,actual,hi,which)
                    bound_tests+=1
    a,b,lam,tau=3,4,F(1,3),F(1,8)
    P=distribution(a,b,lam,tau)
    lo,hi,which=bounds(a,b,lam,tau)
    assert (lo,hi,which)==(2,3,'balanced')
    assert P[2]==0 and P[3]>0
    print('VERIFY_OK')
    print('exact_symmetric_matrix_solutions:',potential_cases)
    print('vertex_subsets:',subset_count)
    print('direct_threshold_checks:',threshold_tests)
    print('polynomial_vs_independent_matrix_profiles:',10*len(Ls)*len(thresholds))
    print('exact_relaxation_and_integrality_tests:',bound_tests)
    print('sharp_gap_example: K_3_4 lambda=1/3 tau=1/8 lower=2 exact=3')
    print('sharp_gap_example_optimum_count:',P[3])
    print('all_arithmetic: Python fractions.Fraction')
if __name__=='__main__':check()
