from math import sqrt

N = 50_000
LEFT = 1.413519
RIGHT = 1.4135200


def partial_R(s, n_max=N):
    return sum(1.0 / ((n - 1) * (n + 1) ** (2.0 * s)) for n in range(2, n_max + 1))


def tail_upper_R(s, n_max=N):
    # For n > N, (n+1)^(-2s)/(n-1) <= (n-1)^(-(2s+1)).
    # Setting m=n-1, the omitted terms start at m=N.
    p = 2.0 * s + 1.0
    return N ** (-p) + N ** (1.0 - p) / (p - 1.0)


def H_bounds(s):
    rp = partial_R(s)
    rt = tail_upper_R(s)
    base = 2.0 ** (1.0 - s)
    return base + sqrt(rp) - 1.0, base + sqrt(rp + rt) - 1.0


left_lo, left_hi = H_bounds(LEFT)
right_lo, right_hi = H_bounds(RIGHT)

print(f"H({LEFT}) in [{left_lo:.12e}, {left_hi:.12e}]")
print(f"H({RIGHT}) in [{right_lo:.12e}, {right_hi:.12e}]")

assert left_lo > 0.0
assert right_hi < 0.0

# The second multiplier condition follows already for sigma >= 1.4:
# sum_{m=3}^infty (m-2)/m^(2 sigma)
# < sum_{m=3}^infty m^(-1.8)
# <= 3^(-1.8) + integral_3^infty x^(-1.8) dx.
j_upper = 3.0 ** (-1.8) + 3.0 ** (-0.8) / 0.8
print(f"crude J upper bound at sigma >= 1.4: {j_upper:.12f}")
assert j_upper < 1.0

print(f"enclosure from positive partial sums and tail bound: {LEFT} < sigma_* < {RIGHT}")
