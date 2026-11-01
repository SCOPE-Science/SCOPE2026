"""Independent finite checks for the sharp cycle heat/edge-variation theorem.

All combinatorial tests use exact integers. NumPy/SciPy checks are numerical diagnostics
only and are never used in proving the theorem.
"""
from itertools import product
from random import Random
from fractions import Fraction
import numpy as np
from scipy.linalg import expm


def gain(w, i, j):
    """Exact right-derivative of weighted variation at edge dipole e_i-e_j."""
    n = len(w)
    adj = int((i - j) % n in (1, n - 1))
    return -(2 + adj) * (w[i] + w[j]) + sum(
        w[k] * abs(int((i-k) % n in (1, n-1)) -
                   int((j-k) % n in (1, n-1)))
        for k in range(n) if k != i and k != j)


def dipole_criterion(w):
    n = len(w)
    return all(gain(w, i, j) <= 0 for i in range(n) for j in range(i+1, n))


def theorem_criterion(w):
    n = len(w)
    if n == 3:
        return True
    if n == 4:
        return all(3 * (w[i] + w[(i+1) % n]) >=
                   w[(i-1) % n] + w[(i+2) % n] for i in range(n))
    if n == 5:
        return all(3 * (w[i] + w[(i+1) % n]) >=
                   w[(i-1) % n] + w[(i+2) % n] and
                   2 * (w[i] + w[(i+2) % n]) >=
                   w[(i-1) % n] + w[(i+3) % n] for i in range(n))
    if n == 6:
        S = w[0] + w[3]
        return (all(w[i] + w[(i+3) % n] == S for i in range(n)) and
                all(3*(w[i] + w[(i+2) % n]) >= 2*S for i in range(n)))
    return all(x == w[0] for x in w)


def run():
    checks = 0
    # Exhaustive integer weights for small cycles; exact inequalities.
    for n, maximum in [(3, 5), (4, 5), (5, 4), (6, 3), (7, 3), (8, 2), (9, 2)]:
        for w in product(range(1, maximum+1), repeat=n):
            checks += 1
            assert dipole_criterion(w) == theorem_criterion(w), (n,w)
    print('exact finite weight-profile tests:', checks)

    rng = Random(20261025)
    sampled = 0
    for n in range(3, 21):
        for _ in range(300):
            w = tuple(rng.randint(1, 100) for _ in range(n))
            assert dipole_criterion(w) == theorem_criterion(w), (n,w)
            sampled += 1
    print('random integer-weight profile tests:', sampled)

    # Construct an explicit nonconstant admissible hexagon.
    w6 = (2, 3, 2, 3, 2, 3)
    assert theorem_criterion(w6) and len(set(w6))>1
    assert not theorem_criterion((2, 3, 2, 3, 2, 4))

    # Exact right-derivative vs finite difference with the actual heat matrix.
    heat_tests = 0
    violation_tests = 0
    for n in range(3, 11):
        L=np.diag([2.]*n)
        for i in range(n):
            L[i,(i+1)%n] -= 1
            L[i,(i-1)%n] -= 1
        for _ in range(20):
            w=tuple(rng.randint(1,8) for _ in range(n))
            g=np.zeros(n)
            i,j=rng.sample(range(n),2)
            g[i]=1;g[j]=-1
            eps=1e-7
            U=expm(-eps*L)
            derivative=(np.sum(np.array(w)*np.abs(U@g))-(w[i]+w[j]))/eps
            exact=gain(w,i,j)
            assert abs(derivative-exact)<1e-3*(1+abs(exact)),(n,w,i,j,derivative,exact)
            heat_tests+=1
            if exact>0:
                assert np.sum(np.array(w)*np.abs(U@g))>w[i]+w[j]
                violation_tests+=1
    print('numerical matrix-exponential directional checks:',heat_tests)
    print('strict amplification witnesses:',violation_tests)

    # All-time heat contraction on tested admissible profiles.
    contraction_tests=0
    for n,w in [(3,(1,9,4)),(4,(2,1,1,1)),(5,(2,1,1,1,1)),
                (6,w6),(7,(1,)*7),(8,(1,)*8),(13,(1,)*13)]:
        assert theorem_criterion(w)
        L=np.diag([2.]*n)
        for i in range(n):
            L[i,(i+1)%n]-=1;L[i,(i-1)%n]-=1
        for t in [0.001,0.01,0.1,0.5,2.0]:
            U=expm(-t*L)
            for i in range(n):
                for j in range(i+1,n):
                    g=np.zeros(n);g[i]=1;g[j]=-1
                    assert np.sum(np.array(w)*np.abs(U@g)) <= w[i]+w[j]+1e-9
                    contraction_tests+=1
    print('finite-time semigroup-dipole tests:',contraction_tests)
    print('PASS: exact combinatorics and supporting independent numerical diagnostics')

if __name__ == '__main__':
    run()
