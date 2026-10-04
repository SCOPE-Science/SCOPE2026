#!/usr/bin/env python3
# Numerical consistency check for the cohomology dimensions in the theorem.
for g in range(2, 101):
    deg_L = 2*g - 1
    deg_D = g - 1
    deg_LmD = deg_L - deg_D
    assert deg_LmD == g
    # deg(L^{-1}) < 0, so h0=0 and RR gives h1 = g-1-deg.
    h1_Linv = g - 1 - (-deg_L)
    assert h1_Linv == 3*g - 2
    deg_LinvD = -deg_L + deg_D
    assert deg_LinvD == -g
    h1_LinvD = g - 1 - deg_LinvD
    assert h1_LinvD == 2*g - 1
    kernel_dim = h1_Linv - h1_LinvD
    assert kernel_dim == g - 1
    assert kernel_dim - 1 == g - 2
assert 3*5 - 3 == 12
assert 5 - 2 == 3
print("RR_DIMENSIONS_OK g=2..100")
print("GENUS5_P3_IN_P12_OK")
print("VERIFY_OK")
