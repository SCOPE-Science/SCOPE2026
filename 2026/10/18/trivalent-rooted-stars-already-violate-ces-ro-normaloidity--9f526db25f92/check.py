"""Exact finite-rational witness for a Cesaro operator on a rooted star.
Run with Python 3; no third-party dependencies. No numerical approximation is used.
"""
from fractions import Fraction as F

n = 20
w = [F(1)] + [F(1, 2 * (j + 1)) for j in range(1, n)]
h = [F(0)]
for j in range(1, n):
    h.append(h[-1] + F(1, j*j))
S = sum(w)
Z = sum(w[i]*w[j]*h[max(i,j)] for i in range(n) for j in range(n))
T = sum(v*v for v in w[1:])
lower_zeta = sum((F(1, j*j) for j in range(1, 204)), F(0))
lower_surplus = F(41,25)*S*S - Z - 2 - 4*T
assert lower_zeta > F(41,25)
assert lower_surplus > F(1,400)
assert S == F(71354639,31039008)
assert lower_surplus == F(189621663106457667280588609,63582532975129101742448640000)
# For a three-arm star, the squared-input norm of the symmetric witness
# is 1/3 + T, and the exact squared-output norm is zeta(2)*S^2-Z-2/3.
# Consequently the squared norm exceeds 4 by at least the displayed ratio.
assert F(4) + lower_surplus/(F(1,3)+T) > 4
print('PASS: exact trivalent-star strict norm witness')
print('lower gap in squared norm:', float(lower_surplus/(F(1,3)+T)))
