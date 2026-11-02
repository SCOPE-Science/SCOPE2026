"""Exact finite-level checks of a quadratic attraction-depth transfer formula.

Uses direct graph traversal independently of the predicted valuation shell counts.
Python 3, standard library only. Run: python3 verify.py
"""
from collections import Counter

PRIMES = (3, 5, 7, 11, 13, 17, 19)
MAX_MODULUS = 500_000


def first_hits(p):
    result = {}
    for a in range(p):
        x, seen, steps = a, set(), 0
        while x != 0 and x not in seen:
            seen.add(x)
            x = (x * x - 1) % p
            steps += 1
        if x == 0:
            result[a] = steps
    return result


def shell_depth(k, valuation):
    threshold = (k + 1) // 2
    j = 0
    while (1 << j) * valuation < threshold:
        j += 1
    return j


def predicted_histogram(p, k):
    count = Counter()
    for r, t in first_hits(p).items():
        count[t - 1 if r == p - 1 else t] += 1
        for valuation in range(1, k):
            count[t + 1 + 2 * shell_depth(k, valuation)] += (
                (p - 1) * p ** (k - valuation - 1)
            )
    return count


def direct_histogram(p, k):
    modulus = p ** k
    residue_basin = first_hits(p)
    count = Counter()
    for x in range(modulus):
        if x % p not in residue_basin:
            continue
        y, depth = x, 0
        while y != 0 and y != modulus - 1:
            y = (y * y - 1) % modulus
            depth += 1
            if depth > 4 * k + p + 5:
                raise AssertionError((p, k, x, "missing cycle"))
        count[depth] += 1
    return count


def main():
    cases = 0
    examined = 0
    for p in PRIMES:
        k = 1
        while p ** k <= MAX_MODULUS:
            predicted = predicted_histogram(p, k)
            actual = direct_histogram(p, k)
            assert actual == predicted, (p, k, predicted, actual)
            assert sum(actual.values()) == len(first_hits(p)) * p ** (k - 1)
            if k >= 2:
                c = (k + 1) // 2
                j = 0
                while (1 << j) < c:
                    j += 1
                assert max(actual) == max(first_hits(p).values()) + 1 + 2 * j
            cases += 1
            examined += p ** k
            k += 1
    assert cases == 43 and examined == 1_696_943
    print(f"VERIFY_OK cases={cases} modulus_states_examined={examined}")


if __name__ == "__main__":
    main()
