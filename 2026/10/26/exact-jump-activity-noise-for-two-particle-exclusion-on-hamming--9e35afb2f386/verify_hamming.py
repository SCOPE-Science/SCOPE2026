"""Independent stationary full-generator comparisons and exact radial arithmetic.

Run: python verify_hamming.py
Requires Python 3, numpy, scipy. Uses unlabelled two-particle configurations.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def closed_form(q, d):
    assert q >= 2 and d >= 2
    N = q**d - 1
    degree = d * (q-1)
    w = [comb(d, j)*(q-1)**j for j in range(d+1)]
    S = [sum(w[j+1:]) for j in range(1, d)]
    T = sum((Fraction(S[j-1]**2, (d-j)*w[j]) for j in range(1, d)), Fraction())
    excess = Fraction(2*d, N*N*(N-1)) * T
    mean = Fraction(2*degree*(N-1), N)
    return mean, 1+excess


def independent_full_generator(q, d):
    n=q**d
    pairs=list(combinations(range(n),2))
    indices={pair:i for i,pair in enumerate(pairs)}
    Q=lil_matrix((len(pairs),len(pairs)),dtype=float)
    for i,(a,b) in enumerate(pairs):
        for x,y in ((a,b),(b,a)):
            for k in range(d):
                digit=(x//q**k)%q
                for z_digit in range(q):
                    if z_digit==digit:
                        continue
                    z=x+(z_digit-digit)*q**k
                    if z==y:
                        continue
                    j=indices[tuple(sorted((z,y)))]
                    Q[i,j]+=1.
                    Q[i,i]-=1.
    Q=Q.tocsc()
    intensities=-Q.diagonal()
    mean=float(intensities.mean())
    # Poisson equation on the full two-particle configuration space.
    B=Q.tolil()
    B[0,:]=1.0
    rhs=mean-intensities
    rhs[0]=0.0
    solution=spsolve(B.tocsc(),rhs)
    variance_rate=mean+2*np.dot(intensities-mean,solution)/len(pairs)
    return mean,variance_rate/mean


def scaling_ratio(q, d):
    N=q**d-1
    w=[comb(d,j)*(q-1)**j for j in range(d+1)]
    accum=0.0
    tail=0
    for j in range(d-1,0,-1):
        tail+=w[j+1]
        accum+=(tail/N)**2 / ((d-j)*w[j])
    return (d*d*(q-1)*q**d/(N-1))*accum


def run():
    cases=[(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(4,3),(5,2)]
    for q,d in cases:
        mu, f=closed_form(q,d)
        mu2,f2=independent_full_generator(q,d)
        assert abs(float(mu)-mu2)<2e-11,(q,d,mu,mu2)
        assert abs(float(f)-f2)<2e-11,(q,d,f,f2)
        assert f>1
        print(f'full generator q={q} d={d}: mean={mu}; F={f}; PASS')
    for q in (2,3,4):
        ratios=[scaling_ratio(q,d) for d in (20,50,100)]
        assert abs(ratios[-1]-1)<.07
        assert ratios[0]>ratios[1]>ratios[2]>1
        print(f'asymptotic normalized ratios q={q}: {ratios}')
    print('ALL PASSED: 9 independent full-generator checks, 9 large-d ratios, exact positivity')

if __name__=='__main__':
    run()
