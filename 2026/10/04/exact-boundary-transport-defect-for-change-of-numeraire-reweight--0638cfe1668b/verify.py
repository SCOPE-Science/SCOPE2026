#!/usr/bin/env python3
from fractions import Fraction

# Primitive laws: masses 7/10 at (1,0), 1/5 at (eps,2), 1/10 at (eps,-3).
# The weak limit puts the last two atoms on a=0.
p0 = Fraction(7,10)
pp = Fraction(1,5)
pm = Fraction(1,10)
cplus = pp*2
cminus = pm*3
m = p0
pred_w1 = (cplus+cminus)/m
pred_call = cplus/m
pred_put = cminus/m


def pos(x):
    return x if x > 0 else Fraction(0)


def check_eps(eps):
    mn = p0 + (pp+pm)*eps
    # weighted Gamma_n atoms (z, mass)
    atoms = [
        (Fraction(0), p0/mn),
        (Fraction(2,1)/eps, pp*eps/mn),
        (Fraction(-3,1)/eps, pm*eps/mn),
    ]
    assert sum(w for _,w in atoms) == 1
    # Gamma = delta_0, so W1 is the absolute first moment exactly.
    w1 = sum(abs(z)*w for z,w in atoms)
    # bounded strike grid
    grid = [Fraction(k,2) for k in range(-10,11)]
    call_err = Fraction(0)
    put_err = Fraction(0)
    for K in grid:
        Cn = sum(pos(z-K)*w for z,w in atoms)
        C = pos(-K)
        Pn = sum(pos(K-z)*w for z,w in atoms)
        P = pos(K)
        call_err = max(call_err, abs((Cn-C)-pred_call))
        put_err = max(put_err, abs((Pn-P)-pred_put))
    return w1, call_err, put_err

assert pred_w1 == 1
assert pred_call == Fraction(4,7)
assert pred_put == Fraction(3,7)
prev = None
for k in range(2,8):
    eps = Fraction(1,10**k)
    w1, ce, pe = check_eps(eps)
    assert abs(float(w1-pred_w1)) < 2.0*float(eps)
    if prev is not None:
        assert ce <= prev[0]
        assert pe <= prev[1]
    prev = (ce,pe)
assert float(prev[0]) < 1e-5
assert float(prev[1]) < 1e-5
print('VERIFY_OK')
