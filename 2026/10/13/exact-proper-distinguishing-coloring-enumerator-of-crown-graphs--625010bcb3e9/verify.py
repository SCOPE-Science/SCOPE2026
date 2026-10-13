"""Reproducible finite checks for a crown-graph proper-coloring enumerator.

Run with Python 3.9+: python verify.py
The general result is proved mathematically; finite checks are corroboration.
"""
from itertools import permutations, product
from math import comb, factorial, isqrt


def fall(x, r):
    if x < r:
        return 0
    v = 1
    for h in range(r):
        v *= x - h
    return v


def onto_rectangle(a, b, r):
    return sum((-1) ** (a + b - i - j) * comb(a, i) * comb(b, j) *
               fall(i * j, r)
               for i in range(a + 1) for j in range(b + 1))


def predicted_by_shared(n, q, t):
    if t < 0 or t >= n or t > q:
        return 0
    total = 0
    for a in range(1, q - t + 1):
        for b in range(1, q - t - a + 1):
            palettes = (factorial(q - t) //
                        (factorial(a) * factorial(b) * factorial(q - t - a - b)))
            total += palettes * onto_rectangle(a, b, n - t)
    return comb(n, t) * fall(q, t) * total


def predicted(n, q):
    return sum(predicted_by_shared(n, q, t) for t in range(n))


def exact_by_automorphisms(n, q):
    """Directly test all 2*n! automorphisms, not the pair-injectivity lemma."""
    perms = tuple(permutations(range(n)))
    counts = [0] * n
    proper = 0
    for colors in product(range(q), repeat=2 * n):
        aa, bb = colors[:n], colors[n:]
        if any(aa[i] == bb[j] for i in range(n)
               for j in range(n) if i != j):
            continue
        proper += 1
        preserved = False
        for p in perms:
            if any(p[i] != i for i in range(n)) and all(
                    aa[i] == aa[p[i]] and bb[i] == bb[p[i]]
                    for i in range(n)):
                preserved = True
                break
            if all(aa[i] == bb[p[i]] and bb[i] == aa[p[i]]
                   for i in range(n)):
                preserved = True
                break
        if not preserved:
            t = sum(aa[i] == bb[i] for i in range(n))
            assert t < n
            counts[t] += 1
    return proper, counts


def threshold(n):
    k = isqrt(4 * n)
    if k * k < 4 * n:
        k += 1
    return k


def mixed_optimal_closed(n):
    k = threshold(n)
    first = (k - 1) * (k - 1) // 4 + 1
    if n != first:
        return 0
    return sum(factorial(k) * factorial(n) // (factorial(a) * factorial(k - 1 - a))
               for a in range(1, k - 1)
               if a * (k - 1 - a) == n - 1)


def main():
    enumerated = 0
    proper_count = 0
    for n, max_q in ((3, 5), (4, 5)):
        for q in range(max_q + 1):
            proper, classes = exact_by_automorphisms(n, q)
            proper_count += proper
            enumerated += q ** (2 * n)
            for t in range(n):
                assert classes[t] == predicted_by_shared(n, q, t), (n, q, t)
            assert sum(classes) == predicted(n, q)
    for n in range(4, 24):
        k = threshold(n)
        assert predicted(n, k - 1) == 0
        assert predicted(n, k) > 0
        assert sum(predicted_by_shared(n, k, t) for t in range(1, n)) == mixed_optimal_closed(n)
        assert all(predicted_by_shared(n, k, t) == 0 for t in range(2, n))
    # Exceptional order three can have two shared labels in an optimal coloring.
    assert predicted(3, 4) == 408
    assert [predicted_by_shared(3, 4, t) for t in range(3)] == [192, 144, 72]
    assert predicted_by_shared(5, 5, 1) == 3600
    assert predicted_by_shared(7, 6, 1) == 604800
    print("VERIFY_OK exhaustive_orders=3,4 palette_ranges=0..5", 
          "assignments=", enumerated, "proper_checked=", proper_count,
          "threshold_orders=4..23", "order3_optimal=408",
          "order5_mixed_optimal=3600", "order7_mixed_optimal=604800")


if __name__ == "__main__":
    main()
