#!/usr/bin/env python3
"""Exact rational checks for the regular-polygon Filippov contraction formulas.

The general-integer theorem is proved analytically in RESULT.md. This script
checks nontrivial algebra and explicit sliding flow at rational polygon data.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from math import exp, log, isclose

CASES = {3: (F(3,2), F(3,4)), 4: (F(1), F(1)), 6: (F(1,2), F(3,4))}
checks = 0
for N, (a,b2) in CASES.items():
    lam, om = F(3,2), F(2,3)
    assert a*a + b2 == 2*a; checks+=1
    assert b2 > 0 and 2*a >= b2; checks+=1
    threshold = om/(lam*a)
    for factor in [F(2),F(7),F(101)]:
        z=threshold*factor
        left_y_sign=om+lam*a*z
        right_y_sign=om-lam*a*z
        assert left_y_sign>0>right_y_sign; checks+=1
        alpha=(1-om/(lam*a*z))/2
        assert F(0)<alpha<F(1); checks+=1
        radial_slide=(2*alpha-1)*om*a-lam*b2*z
        explicit=-om*om/(lam*z)-lam*b2*z
        assert radial_slide==explicit; checks+=1
        assert -radial_slide/z >= lam*b2; checks+=1
        assert 2*a*lam>=lam*b2; checks+=1
    # Above the sliding edge, the exact square-radius equation is
    # S' = -2*lam*b2*S - 2*om*om/lam.
    s0=float((threshold*10)**2)
    c=float(om*om/(lam*lam*b2))
    exit_s=float(threshold**2)
    T=log((s0+c)/(exit_s+c))/(2*float(lam*b2))
    s_exit=(s0+c)*exp(-2*float(lam*b2)*T)-c
    assert T>0 and isclose(s_exit,exit_s,rel_tol=1e-12,abs_tol=1e-12); checks+=1
    # The sharp bound is approached by very remote sliding initial data.
    eps=F(1,100)
    z=threshold*10000
    rate=lam*b2+om*om/(lam*z*z)
    assert lam*b2<rate<lam*b2+eps; checks+=1
    print(f"N={N}: exact interior/sliding identities and exit-time formula pass")
print(f"{checks} checks passed")
