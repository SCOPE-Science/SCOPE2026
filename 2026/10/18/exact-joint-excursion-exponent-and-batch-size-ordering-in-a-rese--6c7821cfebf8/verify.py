"""Independent numerical and finite combinatorial checks for batch-reset joint tails.

Requires Python 3, NumPy and SciPy. Run: python verify.py
Finite checks complement, rather than replace, the theorem's analytical proof.
"""
from itertools import combinations, product
from math import comb, exp, log, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import erfc, erfcx


def hit(N, m, k):
    return 1.0 - (comb(N-k, m) / comb(N, m) if m <= N-k else 0.0)


def decay(N, m, k, r=1.0, D=1.0):
    return sqrt(r * k * hit(N,m,k) / D)


def pair_probability(z, N, m, r=1.0, D=1.0):
    """One-dimensional quadrature using independent Poisson shock types.

    For two tagged particles, the individual-only and shared shock rates
    are b and a respectively. Last ages are min(U1,C), min(U2,C).
    """
    a = r*m*(m-1)/(N*(N-1))
    b = r*m*(N-m)/(N*(N-1))
    if a == 0:
        return exp(-2*z*sqrt(b/D))

    def conditional(c):
        if c <= 0:
            return 0.0
        u=z/(2*sqrt(D*c))
        v=sqrt(b*c)
        w=z*sqrt(b/D)
        # The erfcx form prevents overflow of exp(w)erfc(u+v).
        return 0.5*(exp(-u*u-v*v)*erfcx(u+v)+exp(-w)*erfc(u-v))

    val, error = quad(lambda c: a*exp(-a*c)*conditional(c)**2,
                      0, np.inf, epsrel=2e-10, epsabs=1e-140,
                      limit=300)
    assert val > 0 and error < max(1e-7*val, 1e-120), (val,error)
    return val


def exact_pair_mgf(theta,N,m,r=1.0):
    one=r*hit(N,m,1)
    two=r*hit(N,m,2)
    if theta >= two/2:
        return float('inf')
    return (one*two+theta*(two-2*one))/((one-theta)*(two-2*theta))


def run():
    total=0
    # Cross-check two equivalent formulas for all admissible parameters.
    for N in range(2,15):
        for m in range(1,N+1):
            for k in range(1,N+1):
                lhs=hit(N,m,k)/hit(N,m,1)
                rhs=sum(np.prod([(N-m-t)/(N-1-t) for t in range(j)])
                        if j<=N-m else 0.0 for j in range(k))
                assert abs(lhs-rhs) <= 1e-10, (N,m,k,lhs,rhs)
                total+=1
            for k in range(2,N+1):
                if m<N:
                    assert decay(N,m,k)/decay(N,m,1) > decay(N,m+1,k)/decay(N,m+1,1)-1e-12
            one=r_one=hit(N,m,1)
            two=hit(N,m,2)
            c=two/2
            for theta in (0.1*c,0.5*c,0.9*c):
                exact=exact_pair_mgf(theta,N,m)
                assert np.isfinite(exact) and exact>1
            assert exact_pair_mgf(c,N,m)==float('inf')
    print('combinatorial identities, monotonicity and pair-mgf thresholds:',total,'cases PASS')
    # Directly integrate the joint stationary two-particle distribution,
    # independently of the age-sum moment argument in the proof.
    for N,m in ((3,1),(3,2),(3,3),(8,2),(8,5),(8,8)):
        target=decay(N,m,2)
        rates=[]
        for z in (8.,16.,32.):
            p=pair_probability(z,N,m)
            rates.append(-log(p)/z)
        assert abs(rates[-1]-target)<0.06,(N,m,rates,target)
        print('N,m:',N,m,'predicted rate:',f'{target:.8f}',
              'observed -log(P)/z:',*[f'{x:.8f}' for x in rates])
    print('pair exceedance quadrature: PASS (finite-z asymptotic checks)')

if __name__=='__main__': run()
