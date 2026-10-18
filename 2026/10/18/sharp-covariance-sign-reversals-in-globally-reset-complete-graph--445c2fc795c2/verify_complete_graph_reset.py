"""Finite-state checks for complete-graph exclusion with fixed-state Poisson resets.
All edge clocks have unit rate; a reset has rate r.
This script checks the algebra against the explicitly constructed Markov generator.
"""
from itertools import combinations
from fractions import Fraction
import numpy as np
from scipy.linalg import solve


def formulas(N, K, rate, pair_type):
    L = N - K
    den = (N + rate)**2 * (2*N + rate - 2)
    if pair_type == (0,0):
        return K*((K-2)*rate-2*L)/den
    if pair_type == (1,1):
        return L*((L-2)*rate-2*K)/den
    return -(rate**2 + (N+K*L)*rate + 2*K*L)/den


def stationary(N, K, r):
    states = [sum(1 << i for i in cc) for cc in combinations(range(N),K)]
    ix = {x:i for i,x in enumerate(states)}
    B = np.zeros((len(states), len(states)), dtype=float)
    reset_mask = (1 << K)-1
    reset_ix=ix[reset_mask]
    for a,x in enumerate(states):
        for i in range(N):
            if not (x >> i & 1):
                continue
            for j in range(N):
                if x >> j & 1:
                    continue
                y = x ^ (1<<i) ^ (1<<j)
                B[a,ix[y]] += 1.0
                B[a,a] -= 1.0
        if a != reset_ix:
            B[a,reset_ix] += r
            B[a,a] -= r
    A = B.T.copy()
    b = np.zeros(len(states))
    A[-1,:] = 1
    b[-1]=1
    pi=solve(A,b,assume_a='gen')
    assert np.max(np.abs(B.sum(axis=1))) < 1e-10
    assert min(pi) >= -1e-12
    assert abs(pi.sum()-1)<1e-10
    return states,pi


def run():
    checks=0
    for N in range(3,9):
      for K in range(1,N):
       for r in (0.05,0.4,1.,2.3,10.,40.):
        states, pi=stationary(N,K,r)
        reset=[int(i<K) for i in range(N)]
        means=np.array([sum(p*(x>>i&1) for x,p in zip(states,pi)) for i in range(N)])
        for i in range(N):
          m=(K+r*reset[i])/(N+r)
          assert abs(means[i]-m)<1e-10,(N,K,r,i,means[i],m)
        for i in range(N):
         for j in range(i+1,N):
          u=sum(p*(x>>i&1)*(x>>j&1) for x,p in zip(states,pi))
          cov=u-means[i]*means[j]
          target=formulas(N,K,r,tuple(sorted([reset[i],reset[j]])))
          assert abs(cov-target)<1e-10,(N,K,r,i,j,cov,target)
          checks+=1
    # exact polynomial identities obtained from independently defined first/second-moment equations
    import sympy as s
    N,K,r,x,y=s.symbols('N K r x y', positive=True)
    mm=lambda a:(K+r*a)/(N+r)
    pair=((K-1)*(mm(x)+mm(y))+r*x*y)/(2*N+r-2)-mm(x)*mm(y)
    for vals,expect in [((0,0),K*((K-2)*r-2*(N-K))/((N+r)**2*(2*N+r-2))),
                        ((1,1),(N-K)*((N-K-2)*r-2*K)/((N+r)**2*(2*N+r-2))),
                        ((0,1),-(r**2+(N+K*(N-K))*r+2*K*(N-K))/((N+r)**2*(2*N+r-2)))]:
        assert s.simplify(pair.subs({x:vals[0], y:vals[1]})-expect)==0
    print(f'PASS: {checks} independent finite-generator covariance comparisons plus all one-point means; 3 symbolic polynomial identities.')

if __name__=='__main__': run()
