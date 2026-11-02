"""Supplementary Gram-matrix checks for half-ball polynomial concentration.

Uses monomial integration, not the derived singular-value formulas, to
assemble the full concentration matrix and compare its spectrum.
"""
import itertools
import math
import numpy as np


def exponents(d, L):
    return [alpha for alpha in itertools.product(range(L + 1), repeat=d) if sum(alpha) <= L]


def integral_monomial(alpha, sign=False):
    """Uniform-ball moment, optionally multiplied by sign of first coordinate."""
    d = len(alpha)
    if sign:
        if alpha[0] % 2 != 1 or any(a % 2 for a in alpha[1:]):
            return 0.0
    elif any(a % 2 for a in alpha):
        return 0.0
    D = (d + 2) / 2
    return math.exp(math.lgamma(D) - math.lgamma(D + sum(alpha) / 2) +
                    sum(math.lgamma((a + 1) / 2) - math.lgamma(.5) for a in alpha))


def spectrum(d, L, details=False):
    exp = exponents(d, L)
    n = len(exp)
    G = np.empty((n, n), dtype=float)
    H = np.empty((n, n), dtype=float)
    for i, a in enumerate(exp):
        for j, b in enumerate(exp):
            monomial = tuple(x+y for x, y in zip(a,b))
            G[i,j] = integral_monomial(monomial)
            H[i,j] = integral_monomial(monomial, sign=True)
    evals,U = np.linalg.eigh(G)
    if min(evals)<1.e-10:
        raise AssertionError(('Gram near-singular',d,L,min(evals)))
    Ginvsqrt = (U/np.sqrt(evals)) @ U.T
    C = (np.eye(n) + Ginvsqrt @ H @ Ginvsqrt) / 2
    vals = np.linalg.eigvalsh(C)
    return (vals, exp, G, H) if details else vals


def mu1(d):
    D=(d+2)/2
    return math.exp(math.lgamma(D)-math.lgamma(D+.5)-.5*math.log(math.pi))


def predicted(d):
    m=mu1(d)
    s0=m*(d+2)/(d+3)*math.sqrt((3*d+11)/2)
    s1=m*(d+2)/(d+3)*math.sqrt(d+4)
    M=(d+1)*(d+2)//2
    return sorted([(1-s0)/2, (1+s0)/2]+[(1-s1)/2]*(d-1)+
                  [(1+s1)/2]*(d-1)+[.5]*(M-2*d)),s0,s1


def half_count(d,L):
    m=d-1
    return sum(math.comb(m+r-1,r) for r in range(L,-1,-2))


def main():
    tested=0
    for d in range(2,10):
        observed, exp, G, H = spectrum(d,2,details=True)
        target,s0,s1=predicted(d)
        assert 0 < s1 < s0 < 1
        assert np.allclose(observed,target,atol=2.e-8,rtol=0), (d,observed,target)
        assert sum(abs(x-.5)<1.e-8 for x in observed) == half_count(d,2)
        # Verify the explicit maximizing eigenfunction against the independently
        # integrated generalized eigenproblem (G+H)/2 q = lambda G q.
        def vec(poly):
            z=np.zeros(len(exp))
            for powers,value in poly.items():
                z[exp.index(powers)]=value
            return z
        a=math.sqrt((d+2)/(2*(3*d+11)))
        b=math.sqrt(d+2)
        e0=(0,)*d
        e1=(1,)+(0,)*(d-1)
        e2=(2,)+(0,)*(d-1)
        for sg in (-1,1):
            z=vec({e0:a,e1:sg*b,e2:a*(d+4)})
            rhs=((1+sg*s0)/2)*G@z
            lhs=(G+H)@z/2
            assert np.allclose(lhs,rhs,atol=1.e-9,rtol=0),(d,sg)
        tested+=1
    for d in range(2,6):
        for L in range(0,4):
            obs=spectrum(d,L)
            assert sum(abs(x-.5)<1.e-7 for x in obs) == half_count(d,L),(d,L,obs)
            assert np.allclose(obs,1-obs[::-1],atol=2.e-8,rtol=0),(d,L,obs)
            assert min(obs)>0 and max(obs)<1,(d,L,obs)
            tested+=1
    print('PASS: independent monomial Gram assembly, exact half-energy counts and symmetry;',tested,'dimension-band tests')

if __name__ == '__main__':
    main()
