"""Exact finite checks for balanced two-color single-peaked Schelling swaps.

No third-party packages are required. Fractions model the normalized
piecewise-linear single-peaked representative. Strict ordinal equivalence
with every admissible utility is proved in RESULT.md.
"""

from fractions import Fraction
from itertools import combinations
from math import comb


def normalized_utility(t, peak):
    return min(t / peak, (1 - t) / (1 - peak))


def local_utility(colors, vertex, peak):
    n = len(colors) // 2
    opposite = range(n, 2 * n) if vertex < n else range(n)
    same = 1 + sum(colors[u] == colors[vertex] for u in opposite)
    return normalized_utility(Fraction(same, n + 1), peak)


def predicted_clock(n, x, peak):
    if peak < Fraction(1, 2):
        return min(x, n - x)
    if peak == Fraction(1, 2):
        return 0
    return max(0, n // 2 - x, x - (n + 1) // 2)


def predicted_equilibrium(n, x, peak):
    if peak < Fraction(1, 2):
        return x in (0, n)
    if peak == Fraction(1, 2):
        return True
    return n // 2 <= x <= (n + 1) // 2


def check_exact_deviation(n):
    denominator = comb(2 * n, n)
    direct = sum(
        Fraction(abs(2 * x - n) * comb(n, x) ** 2, 2 * denominator)
        for x in range(n + 1)
    )
    central = comb(n, n // 2) ** 2
    if n % 2 == 0:
        closed = Fraction(n * central, 4 * denominator)
    else:
        closed = Fraction((n + 1) ** 2 * central, 4 * n * denominator)
    assert direct == closed, (n, direct, closed)
    return direct


def main():
    checked_states = 0
    checked_moves = 0
    peaks = (
        Fraction(1, 8), Fraction(1, 4), Fraction(2, 5),
        Fraction(1, 2), Fraction(3, 5), Fraction(3, 4), Fraction(7, 8),
    )
    for n in range(2, 8):
        for peak in peaks:
            stable = 0
            for red_positions in combinations(range(2 * n), n):
                coloring = tuple(int(v in red_positions) for v in range(2 * n))
                x = sum(coloring[:n])
                length = predicted_clock(n, x, peak)
                initial = [local_utility(coloring, v, peak) for v in range(2 * n)]
                has_profitable_swap = False
                for a in range(2 * n):
                    for b in range(a + 1, 2 * n):
                        if coloring[a] == coloring[b]:
                            # A like-color pair only exchanges old utilities;
                            # both cannot strictly improve.
                            continue
                        changed = list(coloring)
                        changed[a], changed[b] = changed[b], changed[a]
                        # Original agent at a moves to b, and conversely.
                        both_gain = (
                            local_utility(changed, b, peak) > initial[a]
                            and local_utility(changed, a, peak) > initial[b]
                        )
                        if both_gain:
                            has_profitable_swap = True
                            checked_moves += 1
                            new_x = sum(changed[:n])
                            assert predicted_clock(n, new_x, peak) == length - 1
                assert (not has_profitable_swap) == predicted_equilibrium(n, x, peak)
                stable += int(not has_profitable_swap)
                checked_states += 1
            if peak < Fraction(1, 2):
                expected = 2
            elif peak == Fraction(1, 2):
                expected = comb(2 * n, n)
            else:
                expected = sum(
                    comb(n, j) ** 2
                    for j in range(n // 2, (n + 1) // 2 + 1)
                )
            assert stable == expected, (n, peak, stable, expected)
            print(f"n={n} peak={peak}: stable={stable}, predicted={expected}")
    assert checked_states == 32928, checked_states
    assert checked_moves == 215664, checked_moves
    for n in range(2, 13):
        print(f"n={n}: E|X-n/2|={check_exact_deviation(n)}")
    print(f"PASS; {checked_states} colorings/peaks; {checked_moves} profitable swaps")


if __name__ == "__main__":
    main()
