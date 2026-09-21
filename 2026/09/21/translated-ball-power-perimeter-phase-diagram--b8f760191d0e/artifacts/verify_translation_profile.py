#!/usr/bin/env python3
"""Numerical checks for the translated-ball power-perimeter phase diagram."""

import mpmath as mp

mp.mp.dps = 50

def phi(n, p, t):
    """Normalized spherical mean of |t e1 + theta|^p on S^{n-1}."""
    c = mp.gamma(n / 2) / (mp.sqrt(mp.pi) * mp.gamma((n - 1) / 2))
    def integrand(u):
        return (1 + t*t + 2*t*u)**(p/2) * (1-u*u)**((n-3)/2)
    cuts = [-1, -mp.mpf("0.99"), -mp.mpf("0.9"), 0, 1] if t == 1 else [-1, 0, 1]
    return c * mp.quad(integrand, cuts)

def boundary_formula(n, p):
    return (2**(p+n-2) * mp.gamma(n/2)
            * mp.gamma((p+n-1)/2)
            / (mp.sqrt(mp.pi) * mp.gamma(n-1+p/2)))

def check():
    # Critical Newton-shell profile in dimensions 3,4,5.
    for n in (3, 4, 5):
        p = 2 - n
        for t in (mp.mpf("0.2"), mp.mpf("0.8"), mp.mpf("1.2"), mp.mpf("2.0")):
            expected = mp.mpf(1) if t < 1 else t**(2-n)
            assert abs(phi(n, p, t) - expected) < mp.mpf("1e-35")

    # Representative monotonicity regimes in n=4:
    # p=-1 lies in (2-n,0), while p=-5/2 lies in (1-n,2-n).
    vals_decreasing = [phi(4, -1, t) for t in (0, mp.mpf(".3"), mp.mpf(".7"), mp.mpf("1.3"), 2)]
    assert all(vals_decreasing[i] > vals_decreasing[i+1] for i in range(len(vals_decreasing)-1))

    vals_hill_left = [phi(4, mp.mpf("-2.5"), t) for t in (0, mp.mpf(".3"), mp.mpf(".7"))]
    vals_hill_right = [phi(4, mp.mpf("-2.5"), t) for t in (mp.mpf("1.3"), 2)]
    assert vals_hill_left[0] < vals_hill_left[1] < vals_hill_left[2]
    assert vals_hill_right[0] > vals_hill_right[1]

    # Boundary beta integral for an integrable touching sphere.
    n, p = 5, mp.mpf("-3.5")  # 1-n < p < 2-n
    direct = phi(n, p, mp.mpf(1))
    exact = boundary_formula(n, p)
    assert abs(direct - exact) < mp.mpf("1e-12")

    print("all translated-ball checks passed")

if __name__ == "__main__":
    check()
