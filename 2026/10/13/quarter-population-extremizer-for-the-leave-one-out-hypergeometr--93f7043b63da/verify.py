from fractions import Fraction
from math import comb

def H(N, L):
    return Fraction(N ** (N - 1), comb(N, L) * (L ** L) * ((N - L) ** (N - L - 1)))

for N in range(3, 301):
    K = (N + 1) // 4
    vals = {L: H(N, L if L <= N // 2 else N - L) for L in range(1, N)}
    mx = max(vals.values())
    winners = [L for L, v in vals.items() if v == mx]
    assert winners == [K, N - K], (N, K, winners)
    for k in range(1, N // 2):
        left = H(N, k + 1) > H(N, k)
        right = N >= 4 * k + 3
        assert left == right, (N, k, left, right)
print("VERIFY_OK N=3..300")
