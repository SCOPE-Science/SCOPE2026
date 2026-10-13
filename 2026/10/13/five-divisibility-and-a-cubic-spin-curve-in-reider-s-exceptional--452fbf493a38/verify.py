from fractions import Fraction

# Symbolic coefficient checks: each invariant is affine-linear in a formal positive integer m.
chi = 5
K2 = 24
c2 = 36
E2 = 6
pg_const, pg_m = 1, 5
g_const, g_m = 1, 9
h11_const, h11_m = 4, 26
b2p_const, b2p_m = 3, 10
b2m_const, b2m_m = 3, 26

assert K2 + c2 == 12 * chi
assert 3 * K2 == 2 * c2
assert K2 == 4 * E2
assert 2 * g_m == 3 * E2
assert 2 * g_const - 2 == 0
assert pg_m == chi and pg_const == 1
assert (2 * pg_m + h11_m) == c2
assert (2 * pg_const + h11_const) == 6
assert b2p_m + b2m_m == c2
assert b2p_const + b2m_const == 6
assert b2p_m - b2m_m == -16
assert b2p_const - b2m_const == 0
assert Fraction(K2, c2) == Fraction(2, 3)
assert 3 * E2 == 2 * g_m

print('noether_coefficients=ok')
print('chern_ratio=2/3')
print('divisibility_ray=(chi,K2,c2,E2)=(5,24,36,6)*m')
print('curve_genus=9*m+1')
print('hodge_profile=(pg,h11)=(5*m+1,26*m+4)')
print('intersection_form_ranks=(b2plus,b2minus)=(10*m+3,26*m+3)')
print('three_spin_degree_identity=3*deg(N)=2*g-2')
print('VERIFY_OK')
