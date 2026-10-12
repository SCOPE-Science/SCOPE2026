#!/usr/bin/env python3
import sympy as s
L4,M4,L2,M2,a=s.symbols('L4 M4 L2 M2 a', nonzero=False)
Delta=L4*M2**3+M4*L2**3  # in characteristic 2, plus = minus
expr=L4*a**4+M4*a
sub=s.factor(expr.subs(a,M2/L2)*L2**4)
assert s.expand(sub-M2*Delta)==0
# Structural cases proved in RESULT: with L4,M4 nonzero over alg. closed char 2,
# L2=M2=0 leaves a*(L4*a^3+M4)=0: 4 distinct roots -> m=2 -> sigma=1.
# If (L2,M2)!=(0,0), any nonzero common root forces L2,M2 nonzero and a=M2/L2.
# The displayed identity then shows existence iff Delta=0, uniquely -> m=1 -> sigma=2.
# Otherwise only a=0 -> m=0 -> sigma=3.
print('VERIFY_OK identity=M2*Delta cases=sigma1_origin,sigma2_Delta0_punctured,sigma3_Delta_nonzero')
