"""Independently enumerate order-two subsequence spectra and marked interval orders.

Run with Python 3: python check.py. No third-party dependencies.
Finite checks are corroboration, not a replacement for the theorem's proof.
"""
from collections import Counter, deque
from itertools import combinations


def spectra_by_bfs(alphabet_size):
    """Shortest signature representatives via all append transitions."""
    n = alphabet_size
    all_letters = (1 << n) - 1
    queue = deque([0])
    shortest = {0: 0}
    while queue:
        state = queue.popleft()
        present = state & all_letters
        pairs = state >> n
        for last in range(n):
            new_pairs = pairs
            for first in range(n):
                if present & (1 << first):
                    new_pairs |= 1 << (n * first + last)
            nxt = (new_pairs << n) | present | (1 << last)
            if nxt not in shortest:
                shortest[nxt] = shortest[state] + 1
                queue.append(nxt)
    return Counter(distance for state, distance in shortest.items()
                   if state & all_letters == all_letters)


def enumerate_orders(n):
    """All labeled interval orders: enumerate permutations of doubled endpoints."""
    orders = set()
    occurrences = [0] * n

    def visit(word):
        if len(word) == 2 * n:
            left = [word.index(v) for v in range(n)]
            right = [len(word) - 1 - word[::-1].index(v) for v in range(n)]
            orders.add(frozenset((u, v) for u in range(n) for v in range(n)
                                 if right[u] < left[v]))
            return
        for letter in range(n):
            if occurrences[letter] < 2:
                occurrences[letter] += 1
                word.append(letter)
                visit(word)
                word.pop()
                occurrences[letter] -= 1

    visit([])
    return orders


def markings_by_orders(n):
    result = Counter()
    for order in enumerate_orders(n):
        def incomparable(u, v):
            return u != v and (u, v) not in order and (v, u) not in order
        neighbors = [set(v for v in range(n) if incomparable(u, v))
                     for u in range(n)]
        simplicial = {u for u in range(n)
                      if all(incomparable(v, w) for v, w in combinations(neighbors[u], 2))}
        for marks in range(1 << n):
            selected = {u for u in range(n) if marks & (1 << u)}
            if not selected <= simplicial:
                continue
            if any(incomparable(u, v) for u, v in combinations(selected, 2)):
                continue
            result[2 * n - len(selected)] += 1
    return result


def main():
    expected_orders = [0, 1, 3, 19, 207, 3451]
    expected_full_hist = {
        1: {1: 1, 2: 1},
        2: {2: 2, 3: 6, 4: 3},
        3: {3: 6, 4: 36, 5: 51, 6: 19},
        4: {4: 24, 5: 240, 6: 672, 7: 660, 8: 207},
        5: {5: 120, 6: 1800, 7: 8400, 8: 15720, 9: 12385, 10: 3451},
    }
    for n in range(1, 6):
        orders = enumerate_orders(n)
        assert len(orders) == expected_orders[n], (n, len(orders))
        from_geometry = markings_by_orders(n)
        from_words = spectra_by_bfs(n)
        assert from_geometry == from_words == Counter(expected_full_hist[n]), (
            n, from_geometry, from_words)
        print(f"alphabet={n} orders={len(orders)} full_support_classes={sum(from_words.values())} "
              f"shortest_length_histogram={sorted(from_words.items())}")
    print("ALL_INTERVAL_MARKING_TESTS_PASSED")


if __name__ == "__main__":
    main()
