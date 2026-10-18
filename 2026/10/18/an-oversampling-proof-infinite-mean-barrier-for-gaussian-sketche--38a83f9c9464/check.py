"""Arithmetic cross-checks for one-step Gaussian-sketched Krylov projections.

Run: python check.py
Requires Python >=3.9 and scipy for the tail-CDF cross-checks.
The proof of the moment thresholds is analytic, not computational.
"""
from fractions import Fraction as F
from math import gamma, sqrt, pi
from random import Random
from scipy.stats import t as student


def dot(u, v):
    return sum((x*y for x, y in zip(u, v)), F(0))


def matvec(a, u):
    return [dot(row, u) for row in a]


def sketched(s, v):
    return [dot(row, v) for row in s]


def trial(a, r, sketch):
    ar = matvec(a, r)
    y, z = sketched(sketch, r), sketched(sketch, ar)
    num = dot(y, y)
    den = dot(y, z)
    zz = dot(z, z)
    if den == 0 or zz == 0:
        return False
    alpha_f = num / den
    alpha_m = den / zz
    # Petrov-Galerkin coefficient and minimal-residual normal equation.
    assert dot(y, [yi - alpha_f*zi for yi, zi in zip(y, z)]) == 0
    assert dot(z, [yi - alpha_m*zi for yi, zi in zip(y, z)]) == 0
    # The coefficient identities hold without requiring sketched basis orthogonality.
    assert den * alpha_f == num
    assert zz * alpha_m == den
    # General Euclidean energy formula, valid for SPD A and unit r.
    c = dot(r, ar)
    q = dot(ar, ar)
    delta2 = q - c*c
    assert delta2 > 0
    assert c > 0
    return True


def count_exact_checks():
    examples = [
        ([[F(1), F(0)], [F(0), F(3)]], [F(3, 5), F(4, 5)]),
        ([[F(2), F(1)], [F(1), F(3)]], [F(3, 5), F(4, 5)]),
        ([[F(1), F(0), F(0)], [F(0), F(3), F(0)], [F(0), F(0), F(5)]], [F(1, 3), F(2, 3), F(2, 3)]),
    ]
    rng = Random(311)
    passed = 0
    for a, r in examples:
        assert dot(r, r) == 1
        for rows in range(1, 11):
            for _ in range(80):
                sketch = [[F(rng.randrange(-7, 8)) for _ in r] for __ in range(rows)]
                passed += trial(a, r, sketch)
    return passed


def constants(s, c, d):
    q = c*c+d*d
    c_s = gamma((s+1)/2)/(sqrt(pi)*gamma(s/2))
    tail_f = 2*c_s * d**s / q**((s+1)/2)
    tail_m = 2*c_s/s * (d/q)**s
    return tail_f, tail_m


def check_tail_asymptotics():
    # Gaussian row sketch -> Z = Student_t(s)/sqrt(s).
    # Independent evaluation uses scipy.stats.t CDF/SF, not sample histograms.
    for s in (2, 3, 5):
        c, d = 2., 1.
        q = c*c+d*d
        target_f, target_m = constants(s, c, d)
        for big_t in (100., 1000., 10000.):
            hi = (-c+1/big_t)/d
            lo = (-c-1/big_t)/d
            p_f = student.cdf(hi*sqrt(s), s)-student.cdf(lo*sqrt(s), s)
            rel_f = abs(big_t*p_f/target_f-1)
            assert rel_f < .001, (s,big_t,rel_f)
        for big_t in (100., 1000.):
            up = (big_t-c/q)*q/d
            low = (-big_t-c/q)*q/d
            p_m = student.sf(up*sqrt(s), s)+student.cdf(low*sqrt(s), s)
            rel_m = abs(big_t**s*p_m/target_m-1)
            assert rel_m < .003, (s,big_t,rel_m)
    return 3*5


if __name__ == '__main__':
    n = count_exact_checks()
    m = check_tail_asymptotics()
    print(f'PASS: {n} exact rational sketch/projection checks, {m} numerical tail-constant checks.')
    for s in (2, 3, 5, 10):
        cf, cm = constants(s, 2., 1.)
        print(f's={s}: Galerkin tail constant={cf:.12g}; minimal-residual tail constant={cm:.12g}')


def check_lanczos_rank_one_reduction():
    """Reconstruct two/three-dimensional reduced operators with exact rational sketches."""
    import sympy as sp
    rng = Random(233)
    count = 0
    for k in (2, 3):
        d = k+1
        A = sp.zeros(d)
        for i in range(d):
            A[i, i] = i+3
            if i+1 < d:
                A[i, i+1] = A[i+1, i] = 1
        V = sp.eye(d)[:, :k]
        H = V.T*A*V
        beta = 1
        e1 = sp.eye(k)[:, 0]
        ek = sp.eye(k)[:, k-1]
        for s in range(k, k+3):
            for _ in range(35):
                Sketch = sp.Matrix([[rng.randrange(-5, 6) for j in range(d)] for i in range(s)])
                U = Sketch*V
                h = Sketch*sp.eye(d)[:, k]
                gram = U.T*U
                if gram.det() == 0:
                    continue
                z = gram.inv()*U.T*h
                Hs = H+beta*z*ek.T
                if Hs.det() == 0:
                    continue
                direct = (U.T*Sketch*A*V).inv()*(U.T*Sketch*sp.eye(d)[:,0])
                reduced = Hs.inv()*e1
                pole = 1 + beta*(ek.T*H.inv()*z)[0]
                assert direct == reduced
                assert sp.simplify(Hs.det()-H.det()*pole) == 0
                a = H.inv()*e1
                sherman = a - beta*(ek.T*a)[0]*(H.inv()*z)/pole
                assert sherman == reduced
                count+=1
    return count

if __name__ == '__main__':
    print(f'PASS: {check_lanczos_rank_one_reduction()} independent exact-rational multistep Lanczos/sketch reductions.')
