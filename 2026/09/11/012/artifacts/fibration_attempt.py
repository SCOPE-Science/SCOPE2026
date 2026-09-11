"""Bounded recovery test: try quadric-ruling genus-1 fibration through P0."""
from fractions import Fraction
# Q: 2X^2+7Y^2+8Z^2-17W^2=0, P=(1,1,1,1). Tangent plane: 2a+7b+8c-17d=0 (directions).
# Parametrize plane: set b = s, c = t, d = 1 (affine), then a = (17 - 7s - 8t)/2.
# Plug into cone: 2a^2+7s^2+8t^2-17 = 0. Get conic in (s,t) with known point (1,1).
# Expand to find second intersection / ruling slopes.
import sympy as sp
s,t = sp.symbols('s t')
a = (17-7*s-8*t)/2
F = 2*a**2+7*s**2+8*t**2-17
sp.expand(F)
print("F(s,t) =", sp.expand(F))
# Translate u=s-1, v=t-1 to analyze singularity/splitting at (1,1)
u,v = sp.symbols('u v')
G = sp.expand(F.subs({s:u+1, t:v+1}))
print("G(u,v) =", G)
# Collect homogeneous parts
G2 = sp.expand(2*(( -7*u-8*v)/2)**2 + 7*u**2 + 8*v**2)
print("quadratic part:", sp.expand(G2))
G1 = G - G2
print("linear+const part:", sp.expand(G1))
# Quadratic part matrix
# G2 = 2*(7u+8v)^2/4 +7u^2+8v^2 = (49u^2+112uv+64v^2)/2 +7u^2+8v^2
# = (49/2+7)u^2 + 56 uv + (32+8)v^2 = (63/2)u^2+56uv+40v^2
# discriminant: 56^2 - 4*(63/2)*40 = 3136 - 5040 = -1904 <0. So over Q, quadratic part
# -1904 = -16*119 = -16*7*17. Not a square in Q. So the two rulings are conjugate over Q(sqrt(-119))?
print("disc =", 56**2 - 4*sp.Rational(63,2)*40)
import math
print("disc factored: -1904 = -16*119; squarefree part -119; is square in Q? NO")
print("=> the two lines on Q through P are NOT defined over Q (conjugate pair over Q(sqrt(-119)) or Q(sqrt(-1904))).")
print("=> ruling fibration is not defined over Q with fibre through P0; need different base point or biquadratic descent.")
print("RECOVERY_TEST_RESULT: FAIL - no Q-ruling line through P; fibration-density route blocked without deeper search")
