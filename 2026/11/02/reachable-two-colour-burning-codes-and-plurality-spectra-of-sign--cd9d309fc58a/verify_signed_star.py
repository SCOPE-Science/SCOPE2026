#!/usr/bin/env python3
"""Direct spread-before-ignition census for signed star burning.
Only standard Python; exact arithmetic and exhaustive finite checks.
"""
from collections import deque, Counter
from math import comb


def reachable_by_process(spokes):
    n = len(spokes)
    neighbors = [[] for _ in range(n + 1)]
    for i, sig in enumerate(spokes, start=1):
        neighbors[0].append((i, sig))
        neighbors[i].append((0, sig))
    start = (0,) * (n + 1)
    seen = {start}
    queue = deque([start])
    finals = set()
    while queue:
        current = queue.popleft()
        if 0 not in current:
            finals.add(current)
            continue
        spread = list(current)
        for v, old in enumerate(current):
            if old == 0:
                score = sum(sign * current[u] for u, sign in neighbors[v])
                if score:
                    spread[v] = 1 if score > 0 else -1
        spread = tuple(spread)
        if 0 not in spread:
            finals.add(spread)
            continue
        for v, c in ((i, c) for i, old in enumerate(spread)
                     if old == 0 for c in (-1, 1)):
            nxt = list(spread)
            nxt[v] = c
            nxt = tuple(nxt)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return finals


def predicted_code(spokes):
    n = len(spokes)
    out = set()
    for center_color in (-1, 1):
        for exceptional in range(n + 1):
            colors = [center_color] + [center_color * s for s in spokes]
            if exceptional:
                colors[exceptional] *= -1
            out.add(tuple(colors))
    return out


def predicted_distance(n, q):
    return min(max(0, q - 1), max(1, n - q))


def verify():
    total_signings = 0
    total_states = 0
    for n in range(3, 9):
        histogram = Counter()
        for mask in range(1 << n):
            spokes = tuple(-1 if (mask >> i) & 1 else 1 for i in range(n))
            observed = reachable_by_process(spokes)
            expected = predicted_code(spokes)
            assert observed == expected, ('reachable-mismatch', n, mask, observed ^ expected)
            assert len(observed) == 2 * (n + 1), ('cardinality', n, mask)
            q = mask.bit_count()
            plurality = max(max(col.count(1), col.count(-1)) for col in observed)
            formula = n + 1 - predicted_distance(n, q)
            assert plurality == formula, ('plurality', n, mask, plurality, formula)
            histogram[plurality] += 1
            total_signings += 1
            total_states += len(observed)
        analytic = Counter()
        for q in range(n + 1):
            analytic[n + 1 - predicted_distance(n, q)] += comb(n, q)
        assert histogram == analytic, ('distribution', n, histogram, analytic)
        radius = max(predicted_distance(n, q) for q in range(n + 1))
        assert radius == max(1, (n - 1) // 2)
    # Larger cases cross-check exhaustive binary code (no process enumeration).
    for n in range(9, 16):
        code = predicted_code((1,) * n)
        assert len(code) == 2 * (n + 1)
        for mask in range(1 << n):
            target = (1,) + tuple(-1 if (mask >> i) & 1 else 1 for i in range(n))
            minimum = min(sum(a != b for a, b in zip(target, word)) for word in code)
            assert minimum == predicted_distance(n, mask.bit_count()), ('radius-distance', n, mask)
    print(f'VERIFY_OK full_signed_dynamics_star_n=3..8 signings={total_signings}'
          f' terminal_colorings_checked={total_states}'
          ' direct_code_distances_n=9..15 all_signings')


if __name__ == '__main__':
    verify()
