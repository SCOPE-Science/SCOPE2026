"""Exact four-agent census of weak-majority top-cycle and Pareto cardinalities."""
from collections import Counter
import csv
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path


def census():
    orders = list(permutations(range(4)))
    ranks = [tuple(order.index(h) for h in range(4)) for order in orders]
    comparisons = []
    for a, b in combinations(range(24), 2):
        votes = tuple(tuple((r[h] < r[k]) - (r[h] > r[k]) for r in ranks)
                      for h, k in zip(orders[a], orders[b]))
        comparisons.append((a, b, votes))
    bits = tuple(1 << a for a in range(24))
    full = (1 << 24) - 1
    joint = Counter()
    for j, k, l in product(range(24), repeat=3):
        graph = list(bits)
        pareto = full
        for a, b, votes in comparisons:
            v = (votes[0][0], votes[1][j], votes[2][k], votes[3][l])
            margin = sum(v)
            if margin >= 0:
                graph[a] |= bits[b]
            if margin <= 0:
                graph[b] |= bits[a]
            if min(v) >= 0:
                pareto &= ~bits[b]
            if max(v) <= 0:
                pareto &= ~bits[a]
        top = 0
        for a in range(24):
            seen = todo = bits[a]
            while todo:
                cur = todo & -todo
                unseen = graph[cur.bit_length() - 1] & ~seen
                seen |= unseen
                todo = (todo ^ cur) | unseen
            if seen == full:
                top |= bits[a]
        assert not pareto & ~top
        joint[top.bit_count(), pareto.bit_count()] += 24
    return joint


if __name__ == '__main__':
    with Path(__file__).with_name('joint_counts.csv').open(newline='') as f:
        rows = list(csv.DictReader(f))
    expected = {(int(row['top_cycle_size']), int(row['pareto_size'])):
                int(row['labeled_profiles']) for row in rows}
    assert len(expected) == len(rows) == 35 and all(row['agents'] == '4' for row in rows)
    result = census()
    assert result == expected and sum(result.values()) == 24**4
    assert sum(c for (t, p), c in result.items() if t == 24) == 239040
    assert result[24, 3] == 18432
    assert Fraction(sum(c for (t, p), c in result.items() if t > p), 24**4) == Fraction(11663, 13824)
    assert Fraction(sum(t*c for (t, p), c in result.items()), 24**4) == Fraction(1299, 64)
    assert Fraction(sum(p*c for (t, p), c in result.items()), 24**4) == Fraction(1597, 288)
    print('VERIFY_OK', len(result), sum(result.values()))
