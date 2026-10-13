"""Exact finite-history checks for the two-scale elephant-walk identities.

Run: python elephant_joint_checker.py (standard library only).
Finite checks are diagnostic; the functional limit needs the analytic proof.
"""
from fractions import Fraction as Q


def history_statistics(word, q):
    w = 0
    s = 0
    u = Q(0)
    z = Q(0)
    a = Q(1)
    for index, step in enumerate(word, start=1):
        if index > 1:
            z += q * ((-1) ** (index - 1)) * Q(w, index - 1)
            eps = Q(step) - q * Q(w, index - 1)
            a *= 1 + q / (index - 1)
        else:
            eps = Q(step)
        u += ((-1) ** (index - 1)) * eps
        w += step
        s += ((-1) ** (index - 1)) * step
    assert Q(s) == u + z
    return Q(w), Q(s), u, z, a


def check(q, bound=10):
    assert Q(1, 2) < q < 1
    states = {(1,): Q(1, 2), (-1,): Q(1, 2)}
    ew2 = Q(1)
    esw = Q(1)
    es2 = Q(1)
    count = 0
    prior = []
    for n in range(1, bound + 1):
        total = sum(states.values(), Q(0))
        assert total == 1
        v2 = c = r = mixed = Q(0)
        for word, probability in states.items():
            w, s, u, z, a = history_statistics(word, q)
            v2 += probability * w * w
            c += probability * s * w
            r += probability * s * s
            mixed += probability * (w / a) * z
            assert (w / a) == Q(w) / a
            count += 2
        assert (v2, c, r) == (ew2, esw, es2)
        expected_mixed = q * sum(((-1) ** k) * v / (k * a) for k, v, a in prior)
        assert mixed == expected_mixed
        if n >= 2:
            assert prior[-1][1] / (prior[-1][0] * prior[-1][2]) >= v2 / (n * a)
        count += 2
        if n == bound:
            break
        successors = {}
        for word, prob in states.items():
            w = sum(word)
            plus = (1 + q * Q(w, n)) / 2
            successors[word + (1,)] = prob * plus
            successors[word + (-1,)] = prob * (1 - plus)
            assert 0 <= plus <= 1
            count += 3
        prior.append((n, v2, a))
        new_ew2 = (1 + 2 * q / n) * ew2 + 1
        new_esw = (1 + q / n) * esw + ((-1) ** n) * (1 + q * ew2 / n)
        new_es2 = es2 + 1 + 2 * ((-1) ** n) * q * esw / n
        ew2, esw, es2 = new_ew2, new_esw, new_es2
        states = successors
    return count


def main():
    total = 0
    for q in (Q(3, 5), Q(2, 3), Q(4, 5), Q(9, 10)):
        total += check(q)
    print('EXACT_CHECKS_PASS', total)

if __name__ == '__main__':
    main()
