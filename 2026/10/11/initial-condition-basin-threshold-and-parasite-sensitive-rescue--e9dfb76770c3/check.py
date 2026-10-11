"""Reproduce one algebraic example for a three-species harvested commensal model."""
from math import sqrt, isclose

r1 = r2 = r3 = k2 = k3 = a = c = E = m1 = 1.0
k1, m2, b, q = 4.0, 2.0, 2.0, 2.0
qstar = r1 * (m1*E + k1*m2)**2 / (4 * E * k1 * m2)
um = (7 - sqrt(17)) / 4
up = (7 + sqrt(17)) / 4
P = lambda u: r1*(1-u/k1)*(m1*E+m2*u)-q*E
lminus = r1*m2*um*(up-um)/(k1*(m1*E+m2*um))
I_at_k3 = 1/(lminus+r2*(b*k3/k2-1))
slope = -r1*a*um/k1*I_at_k3
assert r1*m1 < q < qstar
assert b*k3 > k2 and k1*m2 > m1*E
assert 0 < um < up
assert abs(P(um)) < 1e-12 and abs(P(up)) < 1e-12
assert isclose(qstar, 81/32)
assert isclose(lminus, 0.3040290210515867, rel_tol=1e-12)
assert isclose(slope, -0.1378848902104175, rel_tol=1e-12)
print('CHECK_OK')
