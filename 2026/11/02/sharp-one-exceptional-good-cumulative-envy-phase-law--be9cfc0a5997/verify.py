"""Exact checks for two-agent cumulative-maximum-envy with one exceptional good.
No external inputs or dependencies. All arithmetic is integral and exact.
Run: python3 verify.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product


def expected(r, h):
    h = Fraction(h)
    if r < 1 or h < 1:
        raise ValueError("Requires r>=1 and H>=1")
    if r % 2:
        return Fraction((r - 1) // 2) + h
    return Fraction(r // 2) + min(h, max(Fraction(1), 2*h - 3))


def independent_dp(r, h):
    """Try every remaining item type and both assignments, no prespecified order."""
    h = Fraction(h)
    unit, exceptional = h.denominator, h.numerator

    @lru_cache(None)
    def best(unit_left, exceptional_left, gap):
        if not unit_left and not exceptional_left:
            return 0
        candidates = []
        if unit_left:
            for sign in (-1, +1):
                d = gap + sign * unit
                candidates.append(abs(d) + best(unit_left - 1, exceptional_left, d))
        if exceptional_left:
            for sign in (-1, +1):
                d = gap + sign * exceptional
                candidates.append(abs(d) + best(unit_left, 0, d))
        return min(candidates)

    result = best(r, 1, 0)
    return Fraction(result, h.denominator), best.cache_info().currsize


def exhaustive(r, h):
    """Independent full enumeration over exceptional positions and recipient bitstrings."""
    h = Fraction(h)
    low = None
    for pos in range(r + 1):
        weights = [Fraction(1)] * (r + 1)
        weights[pos] = h
        for signs in product((-1, 1), repeat=r + 1):
            gap = Fraction(0)
            cost = Fraction(0)
            for w, sign in zip(weights, signs):
                gap += sign * w
                cost += abs(gap)
            if low is None or cost < low:
                low = cost
    return low


def terminal_unit_minimum(k, d):
    """Independent DP for k signed unit steps with prescribed terminal gap -d."""
    reach = {0: 0}
    for _ in range(k):
        new = {}
        for x, val in reach.items():
            for y in (x - 1, x + 1):
                candidate = val + abs(y)
                if y not in new or candidate < new[y]:
                    new[y] = candidate
        reach = new
    return reach[-d]


def main():
    checks = 0
    states = 0
    hs = {Fraction(p, q) for q in range(1, 9) for p in range(q, 9*q + 1)}
    for r in range(1, 19):
        for h in hs:
            found, size = independent_dp(r, h)
            want = expected(r, h)
            assert found == want, (r, h, found, want)
            checks += 1
            states += size
    brute = 0
    for r in range(1, 7):
        for h in (Fraction(1), Fraction(4, 3), Fraction(3, 2), Fraction(2), Fraction(9, 4), Fraction(3), Fraction(4), Fraction(7)):
            got = exhaustive(r, h)
            assert got == expected(r, h), (r, h, got, expected(r, h))
            brute += 1
    prefix = 0
    for k in range(1, 22, 2):
        for d in range(1, k+1, 2):
            got = terminal_unit_minimum(k, d)
            want = (k + d*d) // 2
            assert got == want, (k, d, got, want)
            prefix += 1
    print(f"VERIFY_OK rational_dp_cases={checks} rational_h_values={len(hs)} memo_states={states} independently_enumerated_cases={brute} terminal_prefix_cases={prefix}")

if __name__ == '__main__':
    main()
