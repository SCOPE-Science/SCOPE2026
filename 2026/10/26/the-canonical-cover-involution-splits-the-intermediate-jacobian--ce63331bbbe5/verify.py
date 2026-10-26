#!/usr/bin/env python3
"""Exact arithmetic check for the characteristic-class and eigenspace counts."""
a = [1, 7, 21, 35]       # (1+H)^7 through H^3
b = [1, -6, 24, -80]     # (1+2H)^(-3) through H^3
c3 = sum(a[i] * b[3-i] for i in range(4))
assert c3 == -3
degree = 8
euler = c3 * degree
assert euler == -24
b3 = 4 - euler
assert b3 == 28
trace_h3 = 4 - 8
assert trace_h3 == -4
plus, minus = (b3 + trace_h3)//2, (b3 - trace_h3)//2
assert (plus, minus) == (12, 16)
h21, trace_h21 = 14, trace_h3//2
h21_plus, h21_minus = (h21 + trace_h21)//2, (h21 - trace_h21)//2
assert (h21_plus, h21_minus) == (6, 8)
print("VERIFY_OK", {"c3_coefficient":c3,"euler":euler,"b3":b3,
 "trace_H3":trace_h3,"H3_eigenspaces":(plus,minus),
 "H21_eigenspaces":(h21_plus,h21_minus)})
