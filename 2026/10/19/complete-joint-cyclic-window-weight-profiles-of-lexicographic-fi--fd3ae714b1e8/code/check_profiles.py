#!/usr/bin/env python3
"""Exact finite checks for natural-order affine binary window-weight profiles.

Enumerates actual affine truth tables; independently reads cyclic runs and
cyclic windows. The arbitrary-dimension theorem is established by the proof.
"""
from collections import Counter


def affine_words(m):
    n = 1 << m
    for a in range(1 << m):
        bits = [((a & i).bit_count() & 1) for i in range(n)]
        for c in (0, 1):
            yield tuple(v ^ c for v in bits)


def zero_runs(word):
    n = len(word)
    if not any(word):
        return [n]
    if all(word):
        return []
    result = []
    for i in range(n):
        if word[i] == 0 and word[(i - 1) % n] == 1:
            j = 0
            while word[(i + j) % n] == 0:
                j += 1
            result.append(j)
    return result


def observed_joint(m):
    n = 1 << m
    frequencies = Counter()
    for word in affine_words(m):
        if not any(word):
            vector = (0,) * n
        elif all(word):
            vector = (n,) * n
        else:
            runs = zero_runs(word)
            vector = tuple(n - sum(max(l - b + 1, 0) for l in runs)
                           for b in range(1, n + 1))
        frequencies[vector] += 1
    return frequencies


def predicted_joint(m):
    n = 1 << m
    frequencies = Counter({(0,) * n: 1, (n,) * n: 1})
    for s in range(m):
        r = 1 << s
        k = m - s - 1
        upper = 0 if k == 0 else 1 << (k - 1)
        for t in range(upper + 1):
            if k == 0 or t == 0 or t == upper:
                multiplicity = 2
            else:
                multiplicity = 4
            zr = [r] * ((1 << k) - 2 * t) + [2 * r] * t
            vector = tuple(n - sum(max(l - b + 1, 0) for l in zr)
                           for b in range(1, n + 1))
            frequencies[vector] += multiplicity
    return frequencies


def direct_marginal(m, b):
    n = 1 << m
    output = Counter()
    for word in affine_words(m):
        all_zero = sum(all(word[(i + j) % n] == 0 for j in range(b))
                       for i in range(n))
        output[n - all_zero] += 1
    return output


def model_marginal(m, b):
    n = 1 << m
    output = Counter({0: 1, n: 1})
    for s in range(m):
        r = 1 << s
        k = m - s - 1
        upper = 0 if k == 0 else 1 << (k - 1)
        for t in range(upper + 1):
            multiplicity = 4 if 0 < t < upper else 2
            z = ((1 << k) - 2 * t) * max(r - b + 1, 0)
            z += t * max(2 * r - b + 1, 0)
            output[n - z] += multiplicity
    return output


def main():
    for m in range(1, 9):
        actual = observed_joint(m)
        predicted = predicted_joint(m)
        assert actual == predicted, (m, "joint profile mismatch")
        assert len(actual) == (1 << (m - 1)) + 2
        assert Counter(actual.values()) == Counter({
            1: 2, 2: 1, 4: (1 << (m - 1)) - 1
        })
        assert sum(actual.values()) == 1 << (m + 1)
        print("joint PASS", m, len(actual), sorted(Counter(actual.values()).items()))
    for m in range(1, 8):
        n = 1 << m
        for b in range(1, n + 1):
            assert direct_marginal(m, b) == model_marginal(m, b), (m, b)
        print("all marginal windows PASS", m, n)


if __name__ == "__main__":
    main()
