"""Exact finite checks supplementing the fixed-length Zumkeller-sum theorem.

All arithmetic is over Python integers; the mathematical proof is separate.
"""

from math import prod

LIMIT = 4000
# Exact proper-divisor subset-sum definition, independent of tabulated values.
divisors = [[] for _ in range(LIMIT + 1)]
for d in range(1, LIMIT + 1):
    for n in range(d, LIMIT + 1, d):
        divisors[n].append(d)


def is_zumkeller(n):
    divs = divisors[n]
    s = sum(divs)
    if s % 2 or s < 2 * n:
        return False
    target = s // 2 - n
    reachable = 1
    for d in divs[:-1]:
        if d <= target:
            reachable |= reachable << d
            reachable &= (1 << (target + 1)) - 1
    return bool((reachable >> target) & 1)


Z = [n for n in range(1, LIMIT + 1) if is_zumkeller(n)]
zs = set(Z)
assert [n for n in Z if n < 24] == [6, 12, 20]
assert [n for n in Z if n % 2 and n <= 971] == [945]
assert {6, 12, 20, 24, 28, 30, 945}.issubset(zs)

# Independently verify the finite segment of the published even two-sum premise.
two = {a + b for a in Z for b in Z if a + b <= LIMIT}
assert all(n in two for n in range(40, LIMIT + 1, 2))
assert 38 not in two

# Check exactly k summands by bitset coefficient positivity.
mask = (1 << (LIMIT + 1)) - 1
reachable = 1
for k in range(1, 31):
    next_reachable = 0
    for z in Z:
        if z + 6 * (k - 1) > LIMIT:
            break
        next_reachable |= reachable << z
    reachable = next_reachable & mask
    if k >= 3:
        g = 983 if k == 3 else 6 * k + 955
        assert ((reachable >> g) & 1) == 0, (k, g)
        assert all((reachable >> n) & 1 for n in range(g + 1, LIMIT + 1)), k

# Verify every required four-summand base witness by exact membership and sums.
witnesses = {
    981: (945, 6, 6, 24),
    983: (945, 6, 12, 20),
    985: (945, 6, 6, 28),
    987: (945, 6, 6, 30),
    989: (945, 12, 12, 20),
}
for target, terms in witnesses.items():
    assert len(terms) == 4 and sum(terms) == target
    assert all(t in zs for t in terms)

# Exact, independent sigma bound on odd inputs up to the lower-bound window.
def sigma(n):
    return sum(divisors[n])
assert [n for n in range(1, 972, 2) if sigma(n) >= 2*n] == [945]

print('CHECK_OK')
print('Zumkeller counts up to 4000:', len(Z))
print('Even two-summand cases checked: 1981 (40..4000)')
print('Fixed-length k checked: 3..30, target ranges through 4000')
print('Unique odd n<=971 with sigma(n)>=2n: 945')
print('Four-summand boundary witnesses: 5')
