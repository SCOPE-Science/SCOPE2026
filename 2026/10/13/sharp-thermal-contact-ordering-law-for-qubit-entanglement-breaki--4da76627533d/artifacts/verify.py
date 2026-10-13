"""Direct exact-rational and matrix checks of definite-order thermal relaxation.

Run: python artifacts/verify.py   (requires numpy>=1.24).
The finite tests corroborate; they do not prove the all-length theorem.
"""
from fractions import Fraction as F
from itertools import permutations
from math import sqrt
from random import Random
import numpy as np


def offset(channels):
    # First element acts first; (damping strength, stationary excited population).
    s = F(0)
    r = F(1)
    for gamma, nu in channels:
        s = (1 - gamma)*s + gamma*nu
        r *= 1-gamma
    return s, r


def eb(channels):
    s,r = offset(channels)
    G = 1-r
    return s*(G-s) >= r


def kraus(gamma, nu):
    g = float(gamma); v = float(nu)
    return [
       sqrt(1-v)*np.array([[1.,0.],[0.,sqrt(1-g)]]),
       sqrt((1-v)*g)*np.array([[0.,1.],[0.,0.]]),
       sqrt(v)*np.array([[sqrt(1-g),0.],[0.,1.]]),
       sqrt(v*g)*np.array([[0.,0.],[1.,0.]]),
    ]


def direct_choi(channels):
    # System is the second qubit, reference is untouched; normalized Bell input.
    ket = np.array([1.,0.,0.,1.]) / sqrt(2)
    rho = np.outer(ket,ket)
    for gamma,nu in channels:
        nxt = np.zeros((4,4))
        for K in kraus(gamma,nu):
            op = np.kron(np.eye(2),K)
            nxt += op @ rho @ op.T
        rho = nxt
    return rho


def direct_negativity(channels):
    rho = direct_choi(channels)
    assert np.linalg.norm(rho - rho.T) < 1e-12
    assert abs(np.trace(rho) - 1) < 1e-12
    eigs = np.linalg.eigvalsh(rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4))
    return sum(max(0.,-v) for v in eigs)


def predicted_negativity(channels):
    s,r = offset(channels)
    G = 1-r
    return max(0., (sqrt(float((G-2*s)**2+4*r)) - float(G))/4)


def main():
    cold=(F(2,3),F(0)); hot=(F(2,3),F(1,2))
    assert eb((cold,hot)) and not eb((hot,cold))
    assert offset((cold,hot)) == (F(1,3),F(1,9))
    assert offset((hot,cold)) == (F(1,9),F(1,9))
    # EB for a single GAD requires gamma^2 nu(1-nu)>=1-gamma.
    assert not eb((cold,)) and not eb((hot,))
    assert direct_negativity((cold,hot)) < 1e-12
    assert direct_negativity((hot,cold)) > 1e-5

    def bisect(f):
        low,high=0.,1.
        for _ in range(75):
            mid=(low+high)/2
            if f(mid)>=0: high=mid
            else: low=mid
        return (low+high)/2
    lower=bisect(lambda g: g*g*(3-2*g)-4*(1-g)**2)
    upper=bisect(lambda g: g*g*(3-g)-4*(1-g))
    assert abs(lower-0.598278796872131)<2e-12
    assert abs(upper-0.710831453551690)<2e-12
    assert 0 < lower < F(2,3) < upper < F(3,4)
    rng=Random(140271)
    strengths=[F(1,5), F(1,3), F(1,2), F(2,3), F(4,5)]
    temperatures=[F(0),F(1,8),F(1,4),F(3,8),F(1,2)]
    count=0
    for n in range(2,6):
        for t in range(35):
            cs=tuple((rng.choice(strengths),rng.choice(temperatures)) for _ in range(n))
            forward=sorted(cs,key=lambda c:c[1])
            reverse=list(reversed(forward))
            low=offset(reverse)[0]; high=offset(forward)[0]
            ref_r=offset(forward)[1]
            for p in permutations(cs):
                s,r=offset(p)
                assert r==ref_r and low<=s<=high
                assert eb(reverse) <= eb(p) <= eb(forward)
                assert abs(direct_negativity(p)-predicted_negativity(p))<1e-11
                count+=1
            # Check explicit neighboring-swap exact relation.
            for j in range(n-1):
                p=list(cs)
                a,b=p[j],p[j+1]
                v1=offset(p)[0]
                p[j],p[j+1]=p[j+1],p[j]
                v2=offset(p)[0]
                suffix=F(1)
                for g,_ in p[j+2:]:
                    suffix*=1-g
                assert v1-v2==a[0]*b[0]*(b[1]-a[1])*suffix
    print('VERIFY_OK',count,'permutation matrices; exact rational composition/EB checks; example verified')


if __name__=='__main__':
    main()
