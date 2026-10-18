"""Finite diagnostic checks for an analytic nine-node Gaussian tomography theorem.

Run: python verify_design.py
Only finite sanity tests are performed; uniqueness and global optimization use the proof.
"""
from itertools import combinations
import numpy as np
from scipy.optimize import root

ROOT3 = np.sqrt(3.0)
COEFFICIENT = 81 * ROOT3 / 8


def design(radii, offsets):
    """Nine real Hermitian-HS measurement rows, diagonal first."""
    rows = []
    for r, delta in zip(radii, offsets):
        for j in range(3):
            z = r * np.exp(1j * (delta + 2 * np.pi * j / 3))
            v = np.array([1, z, z * z / np.sqrt(2)], complex)
            row = list(np.abs(v) ** 2)
            for k, l in combinations(range(3), 2):
                c = np.conj(v[k]) * v[l]
                row.extend((np.sqrt(2) * c.real,
                            np.sqrt(2) * c.imag))
            rows.append(np.exp(-r * r) * np.asarray(row))
    return np.asarray(rows, float)


def analytic_absdet(radii, offsets):
    x, y, z = radii
    t = np.exp(-3 * np.dot(radii, radii))
    v = (x * y * z) ** 2 * (y*y-x*x) * (z*z-x*x) * (z*z-y*y)
    A = x * (z*z-y*y)
    B = y * (z*z-x*x)
    C = z * (y*y-x*x)
    u = np.exp(-3j * np.asarray(offsets))
    return COEFFICIENT * t * v * abs(-A*u[0] + B*u[1] - C*u[2]) ** 2


def gradient(r):
    x, y, z = r
    return np.asarray((
        -6*x+2/x-1/(y-x)-3/(z-x)+3/(x+y)+1/(x+z),
        -6*y+2/y+1/(y-x)-1/(z-y)+3/(x+y)+3/(y+z),
        -6*z+2/z+1/(z-y)+3/(z-x)+1/(x+z)+3/(y+z),
    ))


def run():
    rng = np.random.default_rng(20261014)
    cases = 0
    for radii in ([.3,.8,1.4], [.45,.9,1.45], [.17,.33,2.1], [.7,1.,1.7], [1.1,1.3,2.0]):
        radii = np.asarray(radii, float)
        for _ in range(8):
            offsets = rng.uniform(-4, 4, 3)
            mat = design(radii, offsets)
            numeric = abs(np.linalg.det(mat))
            exact = analytic_absdet(radii, offsets)
            assert abs(numeric-exact) <= 2e-9 * max(exact, 1e-14), (numeric, exact)
            cases += 1
    sol = root(gradient, [.42,.93,1.40], tol=1e-13)
    assert np.linalg.norm(gradient(sol.x), np.inf) < 5e-14
    x, y, z = sol.x
    assert 0 < x < y < z
    assert abs(sum(sol.x**2)-3) < 5e-13
    for rad in ([.42,.93,1.4], [.32,.8,1.55], [.6,1.0,1.3]):
        rad = np.asarray(rad)
        aligned = analytic_absdet(rad, [0,0,0])
        staggered = analytic_absdet(rad, [0,np.pi/3,0])
        for _ in range(40):
            val = analytic_absdet(rad, rng.uniform(-4,4,3))
            assert aligned*(1-2e-12) <= val <= staggered*(1+2e-12)
    mat = design(sol.x, [0,np.pi/3,0])
    assert np.linalg.matrix_rank(mat) == 9
    for _ in range(100):
        param = rng.normal(size=9)
        data = mat @ param
        recovered = np.linalg.solve(mat, data)
        assert np.linalg.norm(recovered-param) < 1e-10
    nopt = abs(np.linalg.det(mat))
    assert abs(nopt-0.008239970366854745) < 1e-14
    for _ in range(80):
        proposal = np.sort(rng.uniform(.1,2.4,3))
        val = analytic_absdet(proposal, [0,np.pi/3,0])
        assert val < nopt*(1+1e-9)
    print('PASS: 40 determinant identities, 120 angle inequalities, 100 reconstructions, 80 competitor checks')
    print('Unique analytic optimum radii (numerical solution):', sol.x)
    print('Squared-radius sum:', np.dot(sol.x,sol.x))
    print('Optimal absolute determinant:', nopt)
    print('NOTE: Global uniqueness and injectivity require the analytic arguments, not these tests.')

if __name__ == '__main__':
    run()
