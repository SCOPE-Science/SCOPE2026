"""Finite-diffusivity checks of a rare uphill-passage transform.

Run: python verify.py (requires numpy). The analytic asymptotic proof is in RESULT.md.
"""
import math
import numpy as np


def exact_transform(D, b, r, a, xi, z, u):
    eps = math.sqrt(r * D)
    delta = xi * eps
    s = u * eps
    p = np.polymul([D, delta, -r - s], [D, delta - 2 * b, -r - s])
    p[-1] -= r * r * z * z
    roots = np.roots(p)
    positive = sorted(float(t.real) for t in roots
                      if abs(t.imag) < 1e-6 and t.real > 1e-9)
    assert len(positive) == 2, (D, xi, z, u, roots)
    slow, fast = positive
    if z == 0:
        return math.exp(-slow * a)
    slow_minus = -(D * slow**2 + delta * slow - r - s) / (r * z)
    fast_plus = -(D * fast**2 + (delta - 2 * b) * fast - r - s) / (r * z)
    amp_slow = (1 - fast_plus) / (1 - slow_minus * fast_plus)
    amp_fast = (1 - slow_minus) / (1 - slow_minus * fast_plus)
    return amp_slow * math.exp(-slow * a) + fast_plus * amp_fast * math.exp(-fast * a)


def predicted(xi, b, r, a, z, u):
    k = (math.sqrt(xi * xi + 4) - xi) / 2
    h = math.sqrt(xi * xi + 4)
    mu = a * r / (2 * b * k * h)
    return math.exp(-a * u / h + mu * (z*z - 1))


def main():
    b, r, a = 1.0, 1.0, 1.0
    for xi in (-1.5, 0.0, 1.5):
        for z, u in ((0.0, 0.0), (0.3, 0.4), (0.7, 0.2)):
            errs = []
            for D in (1e-2, 1e-3, 1e-4):
                observed = exact_transform(D,b,r,a,xi,z,u) / exact_transform(D,b,r,a,xi,1.0,0.0)
                expected = predicted(xi,b,r,a,z,u)
                assert 0.0 < observed <= 1.0 + 1e-8, (D,xi,z,u,observed)
                errs.append(abs(observed - expected))
            print(f"xi={xi:4.1f}, z={z:3.1f}, u={u:3.1f}, errors={errs}")
            assert errs[-1] < errs[0], (xi,z,u,errs)
            assert errs[-1] < 0.005, (xi,z,u,errs)
    print('All finite-diffusivity transform checks passed.')


if __name__ == '__main__':
    main()
