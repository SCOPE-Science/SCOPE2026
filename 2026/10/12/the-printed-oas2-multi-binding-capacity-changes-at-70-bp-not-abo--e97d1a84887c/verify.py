#!/usr/bin/env python3
from math import floor, log

lengths = [40, 50, 60, 70, 80, 90, 120]
diameter = 35
capacity = [floor(L/diameter) for L in lengths]
assert capacity == [1, 1, 1, 2, 2, 2, 3]

K_formula = [2*n + 2 for n in capacity]
K_table = [4, 4, 4, 4, 6, 6, 8]
assert K_formula == [4, 4, 4, 6, 6, 6, 8]

mismatch = [L for L,kf,kt in zip(lengths,K_formula,K_table) if kf != kt]
assert mismatch == [70]

M = 25
RSS = 199.9
K = 4
AICc = M*log(RSS/M) + 2*K*M/(M-K-1)
assert abs(AICc - 61.97353541595384) < 1e-12
assert abs(AICc - 61.98) < 0.01

print("VERIFY_OK")
print("capacity", capacity)
print("K_formula", K_formula)
print("K_table", K_table)
print("mismatch_bp", mismatch)
print("AICc_70bp_source_K4", AICc)
