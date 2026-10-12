from fractions import Fraction as F

sigma1 = F(451, 3688)
sigma2 = F(58907, 445121)
sigma3 = F(13, 84)
delta12 = F(520, 445121)
nu = F(832, 5227)
k0 = F(12) + nu
baseline_slope = F(1,8)

# Exponent envelopes obtained by replacing 12 with k in the three
# level-set expressions used in the source proof of its twelfth-moment bound.
def E1(k):
    return F(1) + (k-F(4))*sigma1

def E2(k):
    return F(1070,619) + (k-F(6164,619))*sigma2

def E3a(k):
    return F(1) + (k-F(6))*sigma3

def E3b_at_sigma2(k):
    return F(593,288) + (k-F(3587,288))*sigma2

def baseline(k):
    return F(1) + (k-F(4))*baseline_slope

def delta(k):
    return delta12 - (sigma2-baseline_slope)*(k-F(12))

assert sigma1 < sigma2 < sigma3
assert E2(F(12)) == F(2)-delta12
assert E3b_at_sigma2(F(12)) == E2(F(12))
assert E3b_at_sigma2(k0) == E2(k0)  # identical affine functions
assert E1(F(12)) < E2(F(12))
assert sigma1 < sigma2                # E1 falls farther behind as k grows
assert E3a(F(12)) < E2(F(12))
assert E3a(k0) < E2(k0)               # affine comparison suffices on interval
assert k0 < F(3587,288)               # the second high-value exponent decreases in sigma
assert delta(F(12)) == delta12
assert delta(k0) == 0
assert sigma2-baseline_slope == F(26135,3560968)
assert nu == delta12/(sigma2-baseline_slope)
assert nu == F(832,5227)
assert baseline(k0) == E2(k0)

# Dense exact rational sampling is supplementary, not the proof.
for j in range(1001):
    k = F(12) + nu*F(j,1000)
    mx = max(E1(k), E2(k), E3a(k), E3b_at_sigma2(k))
    assert mx == E2(k)
    assert baseline(k)-mx == delta(k)
    assert delta(k) >= 0

print('VERIFY_OK',
      f'sigma1={sigma1}',
      f'sigma2={sigma2}',
      f'nu={nu}',
      f'k0={k0}',
      f'delta12={delta12}',
      f'samples=1001')
