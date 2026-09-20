from fractions import Fraction
from itertools import product
from math import comb, pi, sqrt


def path_range(steps):
    s = 0
    lo = 0
    hi = 0
    for x in steps:
        s += x
        lo = min(lo, s)
        hi = max(hi, s)
    return hi - lo


def fork_gap(n):
    """Exact standard expected-range gap P_n minus the fork T_n."""
    L = n - 3
    path_sum = Fraction(0)
    fork_sum = Fraction(0)
    for spine in product((-1, 1), repeat=L):
        s = sum(spine)
        vals = [0]
        cur = 0
        for z in spine:
            cur += z
            vals.append(cur)
        for x, y in product((-1, 1), repeat=2):
            pvals = vals + [s + x, s + x + y]
            tvals = vals + [s + x, s + y]
            path_sum += max(pvals) - min(pvals)
            fork_sum += max(tvals) - min(tvals)
    den = 2 ** (L + 2)
    return (path_sum - fork_sum) / den


def fork_formula(n):
    L = n - 3
    if L % 2:
        prob = Fraction(comb(L, (L + 1) // 2), 2 ** L)  # P(S_L=1)
    else:
        prob = Fraction(comb(L, (L + 2) // 2), 2 ** L)  # P(S_L=2)
    return prob / 2


def cycle_delta_formula(m):
    return Fraction(3 * m - 1, 2 * (2 * m - 1)) - Fraction(2 ** m, comb(2 * m, m))


def cycle_delta_bruteforce(m):
    # Weighted height-increment law on the auxiliary cycle with lambda_e=2.
    # Each increment is in {-1,0,1}, with weight 2 for zero and 1 otherwise,
    # conditioned on the cycle sum being zero.
    total_w = 0
    rank_sum = 0
    for xs in product((-1, 0, 1), repeat=m):
        if sum(xs):
            continue
        z = xs.count(0)
        w = 2 ** z
        q = m - 1 if z == m else z
        total_w += w
        rank_sum += w * q
    Eq = Fraction(rank_sum, total_w)
    return Eq - Fraction(m - 1, 2)


print("fork identity")
for n in range(4, 13):
    a = fork_gap(n)
    b = fork_formula(n)
    assert a == b
    print(n, a, float(a), "gap*sqrt(n)=", float(a) * sqrt(n))

print("\ncycle auxiliary rank surplus")
for m in range(3, 9):
    a = cycle_delta_bruteforce(m)
    b = cycle_delta_formula(m)
    assert a == b
    print(m, a, float(a))
assert all(cycle_delta_formula(m) >= Fraction(2, 5) for m in range(3, 200))

print("\npublic constants")
standard_branch = 1 / (12 * pi * sqrt(2))
standard_cycle = 3 / (10 * pi)
lazy_cycle = (Fraction(2, 7) - Fraction(37125, 131072)) / (pi * sqrt(2))
print("1/(12*pi*sqrt(2)) =", standard_branch, "> 1/60 =", 1 / 60)
print("3/(10*pi) =", standard_cycle, "> 1/60 =", 1 / 60)
print("lazy cyclic coefficient =", float(lazy_cycle), "> 1/2000 =", 1 / 2000)
assert standard_branch > 1 / 60
assert standard_cycle > 1 / 60
assert float(lazy_cycle) > 1 / 2000

print("\nall checks passed")
