import math

SQ2 = math.sqrt(2.0)
t_star = SQ2 - 1.0
z_star = math.atanh(t_star)

assert abs(z_star - 0.5 * math.log(1.0 + SQ2)) < 1e-14
assert abs((2.0 * t_star + t_star * t_star) - 1.0) < 1e-14
assert 2.0 * z_star < 1.0

# Coefficient-box replay at the exact boundary.
for ia in range(-100, 101):
    a = ia / 100.0
    for ib in range(-100, 101):
        b = ib / 100.0
        # Commuting, nonproportional pair: l1 Pauli coefficient bound.
        ta = math.tanh(z_star * a)
        tb = math.tanh(z_star * b)
        comm_l1 = abs(ta) + abs(tb) + abs(ta * tb)
        assert comm_l1 <= 1.0 + 1e-12

        # Anticommuting pair: exact two-Pauli coefficient sum.
        r = math.hypot(a, b)
        if r > 0.0:
            anti_l1 = math.tanh(z_star * r) * (abs(a) + abs(b)) / r
            assert anti_l1 < 1.0

# Sharp single-edge witness: minimum partial-transpose eigenvalue.
def pt_min(beta_j):
    t = math.tanh(beta_j)
    return (1.0 - 2.0 * t - t * t) / 4.0

assert abs(pt_min(z_star)) < 1e-14
assert pt_min(z_star - 1e-6) > 0.0
assert pt_min(z_star + 1e-6) < 0.0

# Bell-basis partial-transpose spectrum sums to one.
t = math.tanh(z_star * 0.73)
eigs = [
    (1.0 + 2.0*t - t*t)/4.0,
    (1.0 + t*t)/4.0,
    (1.0 + t*t)/4.0,
    (1.0 - 2.0*t - t*t)/4.0,
]
assert abs(sum(eigs) - 1.0) < 1e-14

print('VERIFY_OK')
