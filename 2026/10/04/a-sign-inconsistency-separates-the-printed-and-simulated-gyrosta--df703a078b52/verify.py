from fractions import Fraction as Q

Ix, Iy, Iz = Q(3), Q(2), Q(1)
F1 = (Iy - Iz) / Ix
F3 = (Ix - Iy) / Iz
F2_printed = (Ix - Iz) / Iy
F2_table = (Iz - Ix) / Iy

assert F1 == Q(1, 3)
assert F3 == Q(1)
assert F2_printed == Q(1)
assert F2_table == Q(-1)

cubic_table = 3 * F1 + 2 * F2_table + F3
cubic_printed = 3 * F1 + 2 * F2_printed + F3
assert cubic_table == Q(0)
assert cubic_printed == Q(4)

b12 = Q(7933, 10000)
b21 = Q(119, 100)
b13 = Q(957, 5000)
b31 = Q(2871, 5000)
assert 3 * b12 - 2 * b21 == Q(-1, 10000)
assert 3 * b13 - b31 == Q(0)

print("VERIFY_OK")
