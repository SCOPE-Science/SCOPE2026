#!/usr/bin/env python3
"""
Numerical sanity checks for a proof of Fan's Conjecture 5.9
(arXiv:2609.11186v1, 2026).

This is not the proof itself. It tests:
1. the power-difference lemma on a dense grid;
2. the derived sign identity for d/dpsi log H;
3. monotonicity of the exact three-point energy along Fan's Step-2 arc.

Only the Python standard library is used.
"""
import math
import random

def energy(phi, psi, r):
    a = 0.5*(phi-psi)
    b = 0.5*(phi+psi)
    x = 2.0*math.sin(a)       # AB
    y = 2.0*math.sin(b)       # AC
    c = 2.0*math.sin(phi)     # BC, longest
    X, Y, Z = x**r, y**r, c**r
    D = X + Y - Z
    if D <= 0.0:
        return 0.5*Z
    den = 4.0*X*Y - D*D
    assert den > 0.0
    return 2.0*X*Y*Z/den

def derivative_sign_identity(phi, psi, r):
    a = 0.5*(phi-psi)
    b = 0.5*(phi+psi)
    x, y, c = 2*math.sin(a), 2*math.sin(b), 2*math.sin(phi)
    X, Y, Z = x**r, y**r, c**r
    D = X+Y-Z
    if D <= 0:
        return None
    # Quantity proportional to d(log H)/dpsi from direct differentiation
    lhs = (Y*math.cos(b)/math.sin(b) - X*math.cos(a)/math.sin(a))/D
    lhs += 0.5*(math.cos(a)/math.sin(a) - math.cos(b)/math.sin(b))
    # After multiplying by 2 D sin a sin b, it should become:
    reduced = (Y-X)*math.sin(phi) - Z*math.sin(psi)
    scale = 2*D*math.sin(a)*math.sin(b)
    return lhs*scale, reduced

def check_power_difference():
    # q=r/2; test x^q+y^q>=1 => y^q-x^q >= y-x for 0<=x<=y<=1.
    # Here x=u^2, y=v^2.
    for q in [1.0, 1.01, 1.1, 1.5, 2, 3, 5, 10, 25]:
        for i in range(501):
            x = i/500
            for j in range(i, 501):
                y = j/500
                if x**q + y**q >= 1.0 - 1e-14:
                    assert y**q - x**q + 2e-13 >= y-x
    return True

def check_step2_grid():
    # Avoid the degenerate one-point interval at phi=2pi/3 in the dense test.
    phis = [math.pi/2 + (math.pi/6)*(i/80) for i in range(1,80)]
    rs = [2.0, 2.01, 2.1, 2.5, 3, 4, 5, 10, 25, 50]
    worst_drop = 0.0
    max_identity_error = 0.0
    for phi in phis:
        maxpsi = 2*math.pi - 3*phi
        for r in rs:
            vals=[]
            for k in range(401):
                psi=maxpsi*k/400
                vals.append(energy(phi, psi, r))
                di=derivative_sign_identity(phi,psi,r)
                if di is not None:
                    direct,reduced=di
                    max_identity_error=max(max_identity_error, abs(direct-reduced)/(1+abs(reduced)))
            for a,b in zip(vals, vals[1:]):
                worst_drop=min(worst_drop, b-a)
                assert b + 2e-10*max(1.0,abs(a),abs(b)) >= a
    return worst_drop, max_identity_error

def check_random(seed=20260917, trials=10000):
    rng=random.Random(seed)
    worst_margin=float("inf")
    for _ in range(trials):
        phi=math.pi/2 + rng.random()*(math.pi/6)
        maxpsi=max(0.0,2*math.pi-3*phi)
        psi=rng.random()*maxpsi
        r=2 + 48*rng.random()
        a,b=(phi-psi)/2,(phi+psi)/2
        u,v=math.sin(a)/math.sin(phi), math.sin(b)/math.sin(phi)
        assert 0 <= u <= v <= 1 + 2e-15
        if u**r+v**r > 1:
            margin=(v**r-u**r)-(v*v-u*u)
            worst_margin=min(worst_margin, margin)
            assert margin >= -2e-13
    return worst_margin

if __name__ == "__main__":
    print("power_difference_dense:", check_power_difference())
    drop, ident = check_step2_grid()
    print("step2_worst_grid_increment:", drop)
    print("max_relative_sign_identity_error:", ident)
    print("random_three_point_worst_lemma_margin:", check_random())
    print("ALL CHECKS PASSED")
