"""Exact checks of prime-power valuations of Riordan numbers."""
from math import comb

def pvaluation(v, p):
    out = 0
    while v != 0 and v % p == 0:
        v //= p
        out += 1
    return out

def riordan_up_to(limit):
    a = [1, 0]
    for n in range(2, limit + 1):
        dividend = (n - 1) * (2 * a[-1] + 3 * a[-2])
        assert dividend % (n + 1) == 0
        a.append(dividend // (n + 1))
    return a

R = riordan_up_to(15626)
for n in range(0, 96):
    central = sum(comb(n, j) * ((-1) ** (n-j)) * (comb(2*j, j) // (j+1)) for j in range(n + 1))
    assert central == R[n], (n, central, R[n])
checks = 0
for p, upto in [(3, 8), (5, 6), (7, 4), (11, 3), (13, 3)]:
    for r in range(1, upto + 1):
        index = p ** r + 1
        if index >= len(R):
            continue
        expected = r + (1 if p == 5 and r % 2 == 0 else 0)
        assert pvaluation(R[index], p) == expected, (p, r, expected)
        checks += 1
for r in range(2, 7):
    d = 5 ** r
    assert R[d] % 25 == 1
    assert R[d - 1] % 25 == (21 if r % 2 == 0 else 3)
print('VERIFY_OK', 'valuation_instances', checks, 'trinomial_transform_instances', 96, 'mod25_towers', 5)
