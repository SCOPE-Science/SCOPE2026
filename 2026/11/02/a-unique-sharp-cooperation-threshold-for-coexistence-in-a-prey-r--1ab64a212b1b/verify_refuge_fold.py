"""Numerical checks for the explicit prey-refuge equilibrium-fold theorem.

Python >=3.9; standard library only. Finite checks complement, not replace,
the analytic all-parameter convexity proof.
"""
from math import exp, expm1, isclose


def ingredients(lam, beta, gamma):
    assert lam > 1 and beta > 0 and 0 < gamma <= (lam - 1) / (2 * lam)
    A = lam * (1 - gamma) - 1
    B = lam * gamma
    k = beta * gamma
    R = k * (lam - 1)
    assert R < 1 and A + 1e-14 >= B > 0

    def F(t):
        z = exp(-t)
        return k * (-expm1(-t)) * (A + B * z)

    def fp(t):
        z = exp(-t)
        return k * ((A - B) * z + 2 * B * z * z)

    def K(t):
        return F(t) / fp(t) + F(t) - 2 * t

    def C(t):
        f = F(t)
        return (t - f) / (f * f)

    return A, B, k, R, F, fp, K, C


def bisect(f, low, high, target=0, steps=120):
    vl = f(low) - target
    vh = f(high) - target
    assert vl * vh < 0, (low, high, vl, vh)
    for _ in range(steps):
        mid = (low + high) / 2
        vm = f(mid) - target
        if vm == 0:
            return mid
        if (vm > 0) == (vl > 0):
            low, vl = mid, vm
        else:
            high = mid
    return (low + high) / 2


def check(lam, beta, gamma, verbose=False):
    A, B, k, R, F, fp, K, C = ingredients(lam, beta, gamma)
    small = 1e-7
    large = 1.0
    assert K(small) < 0
    while K(large) <= 0:
        large *= 2
    tstar = bisect(K, small, large)
    cstar = C(tstar)
    assert cstar > 0
    # Verify strict decrease then strict increase of the one-dimensional
    # equilibrium parameterization at a finite sampling mesh.
    left = [tstar * v / 120 for v in range(1, 120)]
    right = [tstar + (8 * tstar + 8 - tstar) * v / 120 for v in range(1, 121)]
    assert all(C(left[i]) > C(left[i + 1]) for i in range(len(left) - 1))
    assert all(C(right[i]) < C(right[i + 1]) for i in range(len(right) - 1))
    for mult in (1.001, 1.02, 1.5, 3., 8.):
        c = cstar * mult
        lo = bisect(C, 1e-9, tstar, target=c)
        high = max(2.0 * tstar, 2.0)
        while C(high) <= c:
            high *= 2
        hi = bisect(C, tstar, high, target=c)
        assert 0 < lo < tstar < hi
        for t in (lo, hi):
            y = F(t)
            x = A + B * exp(-t)
            assert x > 0 and y > 0
            assert isclose(t, y * (1 + c * y), rel_tol=2e-10, abs_tol=2e-10)
            xp = lam * x * (1 - gamma + gamma * exp(-y * (1 + c * y))) / (1 + x)
            yp = beta * gamma * x * (-expm1(-y * (1 + c * y)))
            assert isclose(x, xp, rel_tol=2e-10, abs_tol=2e-10)
            assert isclose(y, yp, rel_tol=2e-10, abs_tol=2e-10)
    if verbose:
        print('source parameters: threshold c* = %.12f; t* = %.12f;' % (cstar, tstar))
        print('fold prey x* = %.12f; predator y* = %.12f' % (A+B*exp(-tstar), F(tstar)))
        print('C(.4) = %.12f, C(.7) = %.12f' % (C(.4), C(.7)))
    return cstar


if __name__ == '__main__':
    cstar = check(3., 4., .1, verbose=True)
    assert 2.31932345 < cstar < 2.31932346
    for lam, beta, gamma in [(2., 1., .1), (2., 2., .25),
                             (3., 1., 1/3), (4., .5, .2),
                             (5., 1., .08), (3., .45, 1/3)]:
        check(lam, beta, gamma)
    print('PASS: original-model residuals, fold, branch ordering and six further parameter examples')
