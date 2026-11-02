"""Independent finite checks for extremal involutive-antimorphism universal words.

Run with Python 3. No third-party packages are required.
"""
import itertools
import math


def representative_involution(q, f):
    assert 0 <= f <= q and (q - f) % 2 == 0
    image = list(range(q))
    for a in range(f, q, 2):
        image[a], image[a + 1] = a + 1, a
    return tuple(image)


def theta_words(q, pi, n):
    half = n // 2
    fixed = tuple(a for a in range(q) if pi[a] == a)
    for left in itertools.product(range(q), repeat=half):
        right = tuple(pi[a] for a in reversed(left))
        if n % 2:
            for c in fixed:
                yield left + (c,) + right
        else:
            yield left + right


def universal_by_greedy_arches(word, q, k):
    seen = set()
    arches = 0
    for a in word:
        seen.add(a)
        if len(seen) == q:
            arches += 1
            seen.clear()
            if arches >= k:
                return True
    return False


def universal_by_direct_subsequences(word, q, k):
    for target in itertools.product(range(q), repeat=k):
        p = 0
        for a in word:
            if a == target[p]:
                p += 1
                if p == k:
                    break
        if p != k:
            return False
    return True


def expected(q, f, k):
    d = (q - f) // 2
    m = k // 2
    if k % 2 == 0:
        return q * k, math.factorial(q) ** m
    if f == 0:
        return q * k, math.factorial(q) ** m * 2 ** d * math.factorial(d)
    return q * k + f - 1, (math.factorial(q) ** m
                              * f * 2 ** d * math.factorial(d + f - 1))


def test_case(q, f, k):
    pi = representative_involution(q, f)
    n0, expected_count = expected(q, f, k)
    for n in range(0, n0 + 1):
        observed = 0
        for word in theta_words(q, pi, n):
            by_arches = universal_by_greedy_arches(word, q, k)
            if by_arches:
                assert universal_by_direct_subsequences(word, q, k), (q, f, k, word)
                observed += 1
            elif q <= 3 and n <= 9:
                assert not universal_by_direct_subsequences(word, q, k), (q, f, k, word)
        goal = expected_count if n == n0 else 0
        assert observed == goal, (q, f, k, n, observed, goal)
    return q, f, k, n0, expected_count


def main():
    rows = []
    for q in range(2, 5):
        for f in range(q + 1):
            if (q - f) % 2:
                continue
            for k in (1, 2, 3):
                rows.append(test_case(q, f, k))
    for f in (1, 3, 5):
        for k in (1, 2):
            rows.append(test_case(5, f, k))
    for row in rows:
        print('q=%d f=%d k=%d min_length=%d count=%d' % row)
    print('VERIFY_OK cases=%d' % len(rows))


if __name__ == '__main__':
    main()
