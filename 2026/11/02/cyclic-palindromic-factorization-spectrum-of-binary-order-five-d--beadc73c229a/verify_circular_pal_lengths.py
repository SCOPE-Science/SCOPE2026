#!/usr/bin/env python3
"""Exact census of cyclic palindromic factorization of binary order-five de Bruijn cycles.

Pure Python 3; no data files or third-party packages are required.
"""
from collections import Counter, defaultdict

ORDER = 5
LENGTH = 1 << ORDER
EXPECTED_ROOT = {4: 384, 5: 3554, 6: 18266, 7: 29118,
                 8: 12138, 9: 2030, 10: 46}
EXPECTED_BEST = {4: 48, 5: 534, 6: 942, 7: 416, 8: 106, 9: 2}
EXPECTED_JOINT = {
    (4, 7): 48,
    (5, 7): 120, (5, 8): 350, (5, 9): 64,
    (6, 7): 118, (6, 8): 742, (6, 9): 74, (6, 10): 8,
    (7, 8): 254, (7, 9): 154, (7, 10): 8,
    (8, 9): 92, (8, 10): 14,
    (9, 10): 2,
}
EXPECTED_HARD = {
    '00000110100111110110001010111001',
    '00000100111010100011011111001011',
}


def feedback_cycles():
    result = set()
    for table in range(1 << 16):
        state, visited, bits = 0, 0, []
        for _ in range(LENGTH):
            if (visited >> state) & 1:
                break
            visited |= 1 << state
            bits.append(str(state >> 4))
            last = (state >> 4) ^ ((table >> (state & 15)) & 1)
            state = ((state << 1) & 31) | last
        if len(bits) == LENGTH and state == 0:
            word = ''.join(bits)
            assert word.startswith('00000')
            assert word not in result
            result.add(word)
    return result


def euler_cycles():
    """Independent enumeration: Euler tours in the order-four graph.

    Edge 00000 is fixed first, and other edges are visited once each.
    """
    found = set()

    def visit(vertex, mask, letters):
        if len(letters) == LENGTH:
            if vertex == 0:
                word = ''.join(letters)
                assert word not in found
                found.add(word)
            return
        for bit in (0, 1):
            edge = (vertex << 1) | bit
            if not ((mask >> edge) & 1):
                visit(edge & 15, mask | (1 << edge), letters + [str(vertex >> 3)])

    visit(0, 1, ['0'])
    return found


def direct_pal_length(word):
    """Independent root-local dynamic programming using an interval palindrome table."""
    n = len(word)
    palindrome = [[False] * n for _ in range(n)]
    for width in range(1, n + 1):
        for a in range(n - width + 1):
            b = a + width - 1
            palindrome[a][b] = word[a] == word[b] and (
                width <= 2 or palindrome[a + 1][b - 1]
            )
    cost = [0] + [n + 1] * n
    for b in range(1, n + 1):
        cost[b] = 1 + min(cost[a] for a in range(b)
                          if palindrome[a][b - 1])
    return cost[n]


def all_center_expansion_lengths(word):
    """Independent doubled-string center expansion and shortest path on cuts."""
    n = len(word)
    double = word + word
    pal_ends = [[] for _ in range(2*n)]
    for center in range(2*n):
        for offset in (0, 1):  # odd and even centers
            left, right = center, center + offset
            while left >= 0 and right < 2*n and double[left] == double[right]:
                if right - left + 1 <= n:
                    pal_ends[left].append(right + 1)
                left -= 1
                right += 1
    result = []
    for root in range(n):
        distance = [n + 1] * (n + 1)
        distance[0] = 0
        for j in range(n):
            for end in pal_ends[root + j]:
                if end <= root + n:
                    idx = end - root
                    if distance[idx] > distance[j] + 1:
                        distance[idx] = distance[j] + 1
        result.append(distance[n])
    return result


def verify():
    cycles1 = feedback_cycles()
    cycles2 = euler_cycles()
    assert cycles1 == cycles2 and len(cycles1) == 2048
    root_counts = Counter()
    best_counts = Counter()
    minmax_counts = Counter()
    hard = set()
    for word in sorted(cycles1):
        assert len({(word+word)[i:i+ORDER] for i in range(LENGTH)}) == LENGTH
        by_centers = all_center_expansion_lengths(word)
        by_intervals = [direct_pal_length(word[r:]+word[:r])
                        for r in range(LENGTH)]
        assert by_centers == by_intervals, word
        lo, hi = min(by_centers), max(by_centers)
        root_counts.update(by_centers)
        best_counts[lo] += 1
        minmax_counts[(lo, hi)] += 1
        if lo == 9:
            hard.add(word)
    assert dict(root_counts) == EXPECTED_ROOT, root_counts
    assert dict(best_counts) == EXPECTED_BEST, best_counts
    assert dict(minmax_counts) == EXPECTED_JOINT, minmax_counts
    assert hard == EXPECTED_HARD, hard
    a, b = sorted(hard)
    canonical = lambda t: min(t[k:] + t[:k] for k in range(len(t)))
    assert canonical(a[::-1]) == b
    assert canonical(''.join('1' if x == '0' else '0' for x in a)) == b
    assert sum(root_counts.values()) == 65536
    assert sum(best_counts.values()) == 2048
    print('VERIFY_OK')
    print('cycles:', len(cycles1), 'roots:', sum(root_counts.values()))
    print('rooted spectrum:', sorted(root_counts.items()))
    print('best-root spectrum:', sorted(best_counts.items()))
    print('joint min/max:', sorted(minmax_counts.items()))
    print('hardest canonical cycles:', sorted(hard))


if __name__ == '__main__':
    verify()
