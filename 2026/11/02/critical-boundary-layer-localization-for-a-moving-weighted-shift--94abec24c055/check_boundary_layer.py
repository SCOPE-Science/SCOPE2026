#!/usr/bin/env python3
"""Finite checks of a moving single-bond perturbation of a unilateral weighted shift.
The complete infinite-dimensional conclusions use the proof, not these finite tests.
Requires Python 3 and scipy for finite-matrix comparisons.
"""
import math
from scipy.linalg import eigh_tridiagonal


def beta_at_y(L, y):
    return L * math.expm1(2*y/L) / (-math.expm1(-2*y))


def y_for_beta(L, beta):
    assert beta > 1 and L >= 1
    lo, hi = 0., max(1., beta)
    while beta_at_y(L, hi) <= beta:
        hi *= 2
    for _ in range(90):
        mid = (lo+hi)/2
        if beta_at_y(L, mid) < beta:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def y_continuum(beta):
    lo,hi = 0., max(1.,beta)
    def f(y):
        return 2*y/(-math.expm1(-2*y))
    while f(hi)<beta:
        hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)<beta:lo=mid
        else:hi=mid
    return (lo+hi)/2


def eigenvector(L,t,kappa,n_tail):
    left=[math.sinh((j+1)*kappa)/math.sinh(L*kappa) for j in range(L)]
    c=math.sinh((L+1)*kappa)/(t*math.sinh(L*kappa))
    return left+[c*math.exp(-k*kappa) for k in range(n_tail)]


def upper_edge(L,t,n_total):
    weights=[1.0]*(n_total-1)
    weights[L-1]=t
    return float(eigh_tridiagonal([0.0]*n_total,weights,select='i',select_range=(n_total-1,n_total-1),eigvals_only=True)[0])


def continuum_left_mass(y):
    return (math.sinh(2*y)-2*y)/(math.exp(2*y)-1-2*y)


def discrete_left_mass(L,t,y):
    kappa=y/L
    v=eigenvector(L,t,kappa,0)
    c=math.sinh((L+1)*kappa)/(t*math.sinh(L*kappa))
    a=sum(z*z for z in v)
    tail=c*c/(-math.expm1(-2*kappa))
    return a/(a+tail)


def run():
    checked=0
    # Both sides of the sharp finite-depth transition, and a Perron-eigenvector residual.
    for L in [1,2,3,5,8,15,25]:
        for beta in [1.1,1.3,2.,3.,5.]:
            t=math.sqrt(1+beta/L)
            y=y_for_beta(L,beta)
            kappa=y/L
            target=2*math.cosh(kappa)
            assert abs(beta_at_y(L,y)-beta)<5e-12*(1+beta)
            N=max(L+450,650)
            finite=upper_edge(L,t,N)
            assert finite<=target+5e-12 and target-finite<1e-6
            v=eigenvector(L,t,kappa, min(70, N-L))
            for j in range(1,len(v)-1):
                wleft=t if j==L else 1.
                wright=t if j==L-1 else 1.
                residual=wleft*v[j-1]+wright*v[j+1]-target*v[j]
                assert abs(residual)<3e-10*max(1., abs(v[j]))
                checked+=1
            # The finite truncation never exceeds the essential edge in subcritical cases.
        for beta in [0.,0.5,0.95,1.]:
            t=math.sqrt(1+beta/L)
            edge=upper_edge(L,t,max(250,L+250))
            assert edge<2+1e-10
            checked+=1
    for beta in [1.2,1.5,2.,3.,5.]:
        y0=y_continuum(beta)
        assert abs(2*y0/(-math.expm1(-2*y0))-beta)<1e-11
        for L in [100,300,1000,3000]:
            y=y_for_beta(L,beta)
            scaled=L*L*(math.cosh(y/L)-1)
            expected=y0*y0/2
            assert abs(scaled-expected)<20/L
            m=discrete_left_mass(L,math.sqrt(1+beta/L),y)
            m0=continuum_left_mass(y0)
            assert abs(m-m0)<10/L
            checked+=1
    print('PASS',checked,'recurrence/finite-spectral/scaling/mass checks; 7 depths, 5 supercritical and 4 subcritical parameters, 5 scaling regimes.')

if __name__=='__main__':
    run()
