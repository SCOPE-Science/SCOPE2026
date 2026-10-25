#!/usr/bin/env python3
"""Independent finite checks for a classification of minimal connected dominating sets of ladders.
Run: python3 verify_ladder.py
Only Python's standard library is required.
"""
from collections import Counter
from itertools import product


def adjacency(n):
    result = []
    for col in range(n):
        for row in range(2):
            mask = 1 << (2 * col + 1 - row)
            if col:
                mask |= 1 << (2 * (col - 1) + row)
            if col + 1 < n:
                mask |= 1 << (2 * (col + 1) + row)
            result.append(mask)
    return result


def connected_dominating(selected, adj):
    if not selected:
        return False
    union = selected
    pending = selected
    while pending:
        bit = pending & -pending
        pending -= bit
        union |= adj[bit.bit_length() - 1]
    if union != (1 << len(adj)) - 1:
        return False
    reached = selected & -selected
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        v = bit.bit_length() - 1
        new = adj[v] & selected & ~reached
        reached |= new
        frontier |= new
    return reached == selected


def minimal_cds(selected, adj):
    if not connected_dominating(selected, adj):
        return False
    pending = selected
    while pending:
        bit = pending & -pending
        pending -= bit
        if connected_dominating(selected ^ bit, adj):
            return False
    return True


def encode(word):
    result = 0
    for col, char in enumerate(word):
        if char in ('T', 'B'):
            result |= 1 << (2 * col)
        if char in ('D', 'B'):
            result |= 1 << (2 * col + 1)
    return result


def permitted_word(word):
    n = len(word)
    if n == 2:
        return word in ('TT', 'DD', 'B.', '.B')
    if n < 3:
        return False
    left = next((i for i, c in enumerate(word) if c != '.'), None)
    if left is None:
        return False
    right = max(i for i, c in enumerate(word) if c != '.')
    if left not in (0, 1) or right not in (n - 2, n - 1):
        return False
    if any(word[i] == '.' for i in range(left, right + 1)):
        return False
    if left == 0:
        if word[0] not in 'TD' or word[1] != word[0]:
            return False
    elif word[1] != 'B':
        return False
    if right == n - 1:
        if word[-1] not in 'TD' or word[-2] != word[-1]:
            return False
    elif word[-2] != 'B':
        return False
    for i in range(left + 1, right):
        if word[i] == 'B':
            if not (word[i - 1] in 'TD' and word[i + 1] in 'TD'
                    and word[i - 1] != word[i + 1]):
                return False
        elif word[i] in 'TD':
            if (word[i - 1] in 'TD' and word[i - 1] != word[i]) or (
                    word[i + 1] in 'TD' and word[i + 1] != word[i]):
                return False
    if left == right:
        return n == 3 and word == '.B.'
    # Connection across every intercolumn cut: adjacent occupied columns share a row.
    for i in range(left, right):
        a, b = word[i], word[i + 1]
        if (a, b) in (('T', 'D'), ('D', 'T')):
            return False
    return True


def predicted(n):
    if n == 2:
        return {encode(w) for w in ('TT', 'DD', 'B.', '.B')}
    result = set()
    # At most one empty column at each end, never in the middle.
    for left in (0, 1):
        for right in (n - 2, n - 1):
            if right < left:
                continue
            for middle in product('TDB', repeat=right - left + 1):
                word = '.' * left + ''.join(middle) + '.' * (n - right - 1)
                if permitted_word(word):
                    result.add(encode(word))
    return result


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def analytic_count(n):
    return {2: 4, 3: 3, 4: 7}.get(n, 2 * fibonacci(n))


def main():
    all_checked = 0
    for n in range(2, 11):
        adj = adjacency(n)
        actual = {mask for mask in range(1, 1 << (2 * n))
                  if minimal_cds(mask, adj)}
        proposed = predicted(n)
        assert actual == proposed, (
            n, sorted(actual - proposed)[:4], sorted(proposed - actual)[:4])
        assert len(actual) == analytic_count(n)
        size_counts = sorted(Counter(m.bit_count() for m in actual).items())
        all_checked += (1 << (2 * n)) - 1
        print(f'n={n:2d}, checked={((1 << (2 * n))-1):7d}, minimal={len(actual):4d}, size_profile={size_counts}')
    # Verify the numerator/denominator recurrence of the generating function.
    counts = [0, 0]
    for n in range(2, 51):
        counts.append(counts[n-1] + counts[n-2] + {2:4, 3:-1, 6:-1}.get(n, 0))
        assert counts[n] == analytic_count(n), (n, counts[n])
    print(f'exhaustive_subsets={all_checked}; rational_GF_coefficients_checked=49; PASS')


if __name__ == '__main__':
    main()
