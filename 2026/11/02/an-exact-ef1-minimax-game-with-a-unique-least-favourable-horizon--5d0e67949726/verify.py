"""Exact rational checks of the stated finite online-EF1 adversarial family.

Run with Python 3.10 or newer: python verify.py
No third-party packages are needed. This finite test supports but does not replace
proofs quantified over all integers n and all real K > 1.
"""
from fractions import Fraction
from itertools import product


def instance(n, K, target, long):
    columns = [tuple(Fraction(1) for _ in range(n)) for _ in range(n - 1)]
    columns.append(tuple(K if i == target else 1 / K for i in range(n)))
    if long:
        columns.append(tuple(K if i == target else Fraction(1) for i in range(n)))
    return columns


def ef1_score(columns, recipients):
    n = len(columns[0])
    assert len(columns) == len(recipients)
    score = Fraction(1)
    for i in range(n):
        own = sum((g[i] for g, r in zip(columns, recipients) if r == i), Fraction(0))
        for j in range(n):
            if i == j:
                continue
            other = [g[i] for g, r in zip(columns, recipients) if r == j]
            if other:
                reduced = sum(other, Fraction(0)) - max(other)
                if reduced > 0:
                    score = min(score, own / reduced)
    return score


def predicted_value(weights):
    n = len(weights) // 2
    q = [weights[2 * a] + weights[2 * a + 1] for a in range(n)]
    return max(
        q[b] + sum(max(weights[2 * a], weights[2 * a + 1])
                   for a in range(n) if a != b)
        for b in range(n)
    )


def exhaustive_policy_value(n, K, alpha, weights):
    short = [instance(n, K, a, False) for a in range(n)]
    long = [instance(n, K, a, True) for a in range(n)]
    best = Fraction(-1)
    for prefix in product(range(n), repeat=n - 1):
        total = Fraction(0)
        for a in range(n):
            best_for_a = Fraction(-1)
            for r in range(n):
                s_ok = ef1_score(short[a], prefix + (r,)) >= alpha
                l_ok = any(ef1_score(long[a], prefix + (r, t)) >= alpha
                           for t in range(n))
                value = weights[2 * a] * s_ok + weights[2 * a + 1] * l_ok
                best_for_a = max(best_for_a, value)
            total += best_for_a
        best = max(best, total)
    return best


def equalizer_check(n, K):
    # The random empty agent b, followed by a fair coin when a != b,
    # produces the same exact EF1 success probability for every fixed input.
    p = Fraction(n + 1, 2 * n)
    for a in range(n):
        short = instance(n, K, a, False)
        long = instance(n, K, a, True)
        ps = pl = Fraction(0)
        for b in range(n):
            prefix = tuple(i for i in range(n) if i != b)
            c = next(i for i in range(n) if i != b)
            if a == b:
                ps += Fraction(ef1_score(short, prefix + (b,)) == 1, n)
                pl += Fraction(ef1_score(long, prefix + (b, c)) == 1, n)
            else:
                # In short mode g_n goes to b; in long mode g_n goes to a.
                ps += Fraction(ef1_score(short, prefix + (b,)) == 1, 2 * n)
                pl += Fraction(ef1_score(long, prefix + (a, b)) == 1, 2 * n)
        assert ps == pl == p, (n, K, a, ps, pl, p)
        # For alpha <= 1/K, the same simple deterministic rule succeeds.
        for b in range(n):
            prefix = tuple(i for i in range(n) if i != b)
            c = next(i for i in range(n) if i != b)
            assert ef1_score(short, prefix + (b,)) == 1
            assert ef1_score(long, prefix + (b, c)) >= 1 / K


def check():
    tested = 0
    for n in range(2, 9):
        for K in (Fraction(2), Fraction(3), Fraction(5), Fraction(13)):
            equalizer_check(n, K)
            tested += 2 * n

    # Exhaustive finite policies (including repeated common-good recipients)
    # under multiple nonuniform input distributions, computed independently
    # of the mathematical closed form.
    brute_cases = 0
    for n in (2, 3, 4):
        for K in (Fraction(2), Fraction(5)):
            alphas = (Fraction(1), Fraction(1, K), Fraction(1, 2 * K))
            raw_vectors = [tuple([1] * (2 * n))]
            raw_vectors += [tuple(1 + ((i + 2 * j + j * j) % 7)
                                  for i in range(2 * n)) for j in range(4)]
            for raw in raw_vectors:
                z = sum(raw)
                weights = tuple(Fraction(v, z) for v in raw)
                for alpha in alphas:
                    expected = predicted_value(weights) if alpha > 1 / K else Fraction(1)
                    got = exhaustive_policy_value(n, K, alpha, weights)
                    assert got == expected, (n, K, alpha, weights, expected, got)
                    brute_cases += 1
    print('VERIFY_OK equalizer_input_checks=', tested,
          'exhaustive_weighted_policy_games=', brute_cases,
          'max_agents_bruteforce=4 exact_rational=True')

if __name__ == '__main__':
    check()
