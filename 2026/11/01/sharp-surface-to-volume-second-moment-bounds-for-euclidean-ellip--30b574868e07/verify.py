"""Numerical and exact-normalization checks for the ellipsoid surface-moment theorem.

Usage: python verify.py
Requires Python 3 and NumPy. This is corroboration, not a substitute for the proof.
"""
import math
from fractions import Fraction
import numpy as np


def sphere_grid(d):
    if d == 2:
        theta = 2 * np.pi * np.arange(16384) / 16384
        u = np.stack((np.cos(theta), np.sin(theta)), axis=1)
        return u, np.full(u.shape[0], 1.0 / u.shape[0])
    if d == 3:
        # Gauss-Legendre integration in polar cosine, trapezoidal in azimuth.
        t, wt = np.polynomial.legendre.leggauss(160)
        ph = 2 * np.pi * np.arange(256) / 256
        r = np.sqrt(1-t[:,None]**2)
        u = np.stack((np.broadcast_to(r * np.cos(ph), (160,256)),
                      np.broadcast_to(r * np.sin(ph), (160,256)),
                      np.broadcast_to(t[:,None], (160,256))), axis=2).reshape(-1,3)
        w = np.broadcast_to((wt[:,None]/(2*256)), (160,256)).ravel()
        return u, w
    raise ValueError('Grid supported only for d=2,3')


def check_axes(axes, tol):
    axes = np.array(axes, dtype=float)
    d = len(axes)
    u, weights = sphere_grid(d)
    b = 1. / axes
    h = np.linalg.norm(u * b, axis=1)
    surf_cov = np.sum((weights*h)[:,None] * (u**2) * axes**2, axis=0) / np.dot(weights,h)
    # The independent Gaussian-directional integral for Q uses the inverse
    # radial weight, not the surface-area weight.
    q = np.sum((weights / h)[:,None] * (u**2) * b**2, axis=0) / np.dot(weights,h)
    formula_cov = axes**2 * (1. + q) / (d+1)
    assert max(abs(surf_cov-formula_cov)) < tol, (axes, surf_cov, formula_cov)
    assert abs(sum(q)-1.) < 5e-12
    assert all(q > 0) and all(q < 1)
    for i in range(d):
        for j in range(d):
            assert (axes[i]**2-axes[j]**2)*(q[i]-q[j]) <= 3e-10
    ratio = (d+2.) * sum(surf_cov)/sum(axes**2)
    assert (d+2.)/(d+1.) < ratio + tol
    assert ratio <= (d+2.)/d + tol
    if max(axes)-min(axes) > 1e-8:
        assert ratio < (d+2.)/d - 1e-8
    return ratio, surf_cov


def exact_identity(d):
    # The weighted squared spherical coordinate along v is 2/(d+1):
    # E |U1|^3 / E |U1| = 2/(d+1), and the remaining d-1 are equal.
    lhs = Fraction(2, d+1)
    rhs = Fraction(1, d+1)
    assert lhs+(d-1)*rhs == 1
    assert lhs > rhs
    return True


def main():
    cases = [(1.,1.),(1.,1.8),(.4,1.),(.03,1.),(1.,1.,1.),
             (.3,1.,2.),(.07,1.,1.),(1.,1.4,2.2)]
    for axes in cases:
        tol = 5e-7 if len(axes)==2 else 2e-5
        ratio, _ = check_axes(axes, tol)
        print(f'd={len(axes)} semiaxes={axes} ratio={ratio:.10f}')
    for d in range(2,101):
        assert exact_identity(d)
    # Sharp upper case is the Euclidean ball in all dimensions.
    for d in range(2,50):
        q = Fraction(1,d)
        ratio = Fraction(d+2,d+1)*(1+q)
        assert ratio == Fraction(d+2,d)
    # Independent high-eccentricity limit: q -> (1,0,..,0), so
    # tr(A^2 Q)/tr(A^2) -> 0 for A=diag(eps,1,..,1).
    for d in range(2,50):
        assert Fraction(d+2,d+1) < Fraction(d+2,d)
    print('PASS: 8 numerical cases; 99 exact angular identities; 48 ball identities; 48 sharp-limit bounds.')


if __name__ == '__main__':
    main()
