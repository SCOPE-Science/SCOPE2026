"""Exact covariance/orbit and facet audit for a four-coordinate Gaussian maximum.

Requires SymPy and NumPy. This is finite verification, not a substitute for
proof of the Gaussian integration-by-parts identity used in the accompanying note.
"""
import itertools
import math
import numpy as np
import sympy as S

ROOT = S.sqrt
PI = S.pi


def covariance(signs):
    return S.Matrix(4, 4, lambda i, j: S.Integer(1) if i == j else -S.Rational(signs[i] * signs[j], 3))


def dot_difference(C, i, j, k, l):
    return C[i, k] - C[i, l] - C[j, k] + C[j, l]


def facet_data(C, i, j):
    l, m = [h for h in range(4) if h != i and h != j]
    dd = dot_difference(C, i, j, i, j)
    ad = dot_difference(C, i, l, i, j)
    bd = dot_difference(C, i, m, i, j)
    aa = dot_difference(C, i, l, i, l) - ad**2 / dd
    bb = dot_difference(C, i, m, i, m) - bd**2 / dd
    ab = dot_difference(C, i, l, i, m) - ad * bd / dd
    return S.simplify(ROOT(dd)), S.simplify(ab / ROOT(aa * bb))


def orbit_mean(signs):
    C = covariance(signs)
    return S.simplify(sum(d * (S.Rational(1, 4) + S.asin(rho) / (2 * PI))
                  for i, j in itertools.combinations(range(4), 2)
                  for d, rho in [facet_data(C, i, j)]) / ROOT(2 * PI))


expected = {
    0: ROOT(3) * (PI + 2*S.asin(S.Rational(1, 3))) / PI**S.Rational(3, 2),
    1: ((ROOT(6) + ROOT(3)) / 2 + ROOT(6) * S.asin(1/ROOT(3)) / PI) / ROOT(2*PI),
    2: 2 * ROOT(6) / (3 * ROOT(PI)),
}
checks = 0
orbits = {0: 0, 1: 0, 2: 0}
for signs in itertools.product([-1, 1], repeat=4):
    C = covariance(signs)
    v = S.Matrix(signs) / 2
    assert C == S.Rational(4,3) * (S.eye(4) - v*v.T)
    checks += 1
    assert C.diagonalize()[1] is not None  # exact real symmetric structure also checked by projector identity
    checks += 1
    assert C.trace() == 4 and C.rank() == 3 and all(C[i,i] == 1 for i in range(4))
    checks += 1
    n_minus = min(signs.count(-1), signs.count(1))
    orbits[n_minus] += 1
    for i, j in itertools.combinations(range(4), 2):
        d, rho = facet_data(C, i, j)
        same = signs[i] == signs[j]
        assert S.simplify(d - (2*ROOT(6)/3 if same else 2*ROOT(3)/3)) == 0
        checks += 1
        target = ((S.Rational(1,3) if n_minus == 0 else 1/ROOT(3)) if same else S.Integer(0)) if n_minus != 2 else (-S.Integer(1) if same else S.Integer(1))
        assert S.simplify(rho - target) == 0, (signs, i, j, rho, target)
        checks += 1
    actual = orbit_mean(signs)
    assert S.simplify(actual - expected[n_minus]) == 0, (signs, actual, expected[n_minus])
    checks += 1
assert orbits == {0: 2, 1: 8, 2: 6}
checks += 1
assert all(float(expected[j].evalf(30)) > float(expected[j+1].evalf(30)) for j in (0, 1))
checks += 1

# Independent quasi-Monte-Carlo integration: four equal-norm Gaussian rows obtained
# from the covariance eigenvectors and eigenvalues (no facet formula involved).
from scipy.stats import qmc
from scipy.special import ndtri
sample = ndtri(qmc.Sobol(d=3, scramble=True, seed=271828).random_base2(18))
for k, signs in [(0,(1,1,1,1)),(1,(1,1,1,-1)),(2,(1,1,-1,-1))]:
    C = np.asarray(covariance(signs), dtype=float)
    eig, evec = np.linalg.eigh(C)
    L = evec[:,1:] @ np.diag(np.sqrt(eig[1:]))
    numerical = np.max(sample @ L.T, axis=1).mean()
    exact = float(expected[k].evalf(30))
    assert abs(numerical-exact)<0.006,(k, numerical, exact)
    checks += 1
    print('class',k,'expectation',f'{exact:.12f}', 'independent_approximation',f'{numerical:.12f}')

print('covariance sign patterns verified',sum(orbits.values()))
print('orbit sizes',orbits)
print('deterministic checks passed',checks)
