#!/usr/bin/env python3
"""Independent one-dimensional quadrature and symbolic identities for the documented harmonic-midpoint claim."""
import math
import mpmath as mp
import sympy as sp
mp.mp.dps = 75

x = sp.symbols('x', real=True)
angle = 2 * sp.atan(x / 2)
assert sp.simplify(sp.diff(angle, x) - 1 / (1 + x * x / 4)) == 0
assert sp.simplify(sp.diff(angle, x, 2) + x / (2 * (1 + x * x / 4)**2)) == 0
assert sp.simplify(sp.diff(angle,x,4).subs(x,0)) == 0
u = mp.mpf('1')
assert mp.quad(lambda v: v*v / 2, [-u,u]) == mp.mpf(1)/3
assert mp.quad(lambda v: v**4 / 2, [-u,u]) == mp.mpf(1)/5

T=mp.mpf('2'); kappa=mp.mpf('1'); alpha=mp.mpf('2.5')
passed=5
for m in [2,4,8,16,32,64]:
    h=T/(2*m); delta=kappa*h**alpha
    if delta >= h:
        continue
    theta=lambda s: 2*mp.atan(s/2)
    X=lambda v: theta(h+delta*v)
    Z=lambda v: X(v)+X(-v)
    E=lambda fn: mp.quad(lambda v: fn(v)/2, [-1,0,1])
    meanX=E(X); meanZ=E(Z)
    varX=E(lambda v:(X(v)-meanX)**2)
    varZ=E(lambda v:(Z(v)-meanZ)**2)
    vi=2*m*varX
    va=m*varZ
    chiX=E(lambda v:mp.exp(1j*X(v)))
    chiZ=E(lambda v:mp.exp(1j*Z(v)))
    di=-mp.expm1(4*m*mp.log(abs(chiX)))
    da=-mp.expm1(2*m*mp.log(abs(chiZ)))
    assert abs(meanZ-2*meanX)<mp.mpf('1e-65')
    assert va<vi and va>0 and di>0 and da>0
    assert abs(di/vi-1)<mp.mpf('.08')
    assert abs(da/va-1)<mp.mpf('.08')
    norm_i=vi/(T*kappa**2/3*h**(2*alpha-1))
    norm_a=va/(T*kappa**4/90*h**(4*alpha+1))
    if m>=16:
        assert abs(norm_i-1)<mp.mpf('.015')
        assert abs(norm_a-1)<mp.mpf('.018')
    phase_aligned = varX*2
    assert varZ<phase_aligned
    # A comonotone pair has variance four times the single-step variance.
    assert varZ<4*varX
    # A midpoint step is a plane rotation and has squared-column norms one.
    c=(1-(h/2)**2)/(1+(h/2)**2)
    s=h/(1+(h/2)**2)
    assert abs(c*c+s*s-1)<mp.mpf('1e-65')
    passed+=12
    print('m=',m,'normalized_iid=',mp.nstr(norm_i,12),'normalized_antithetic=',mp.nstr(norm_a,12), 'circular_dispersion_ratio=',mp.nstr(da/di,12))
print('VERIFY_OK',passed,'symbolic, exact uniform-moment, high-precision finite-grid checks')
