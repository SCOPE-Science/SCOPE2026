"""Independent exact census for majority top cycles of n=3,4 house-allocation markets."""
import itertools
import csv
from pathlib import Path
from collections import Counter


def census(n):
    orders = list(itertools.permutations(range(n)))
    assignments = orders
    m = len(orders)
    out = Counter()
    # Normalize house labels by fixing agent 0's order to identity.
    for suffix in itertools.product(range(m), repeat=n-1):
        rankings = (orders[0],) + tuple(orders[k] for k in suffix)
        ranks = tuple(tuple(o.index(h) for h in range(n)) for o in rankings)
        reach = []
        for a in assignments:
            succ = set()
            for bidx, b in enumerate(assignments):
                sign = sum((ranks[i][a[i]] < ranks[i][b[i]]) - (ranks[i][a[i]] > ranks[i][b[i]]) for i in range(n))
                if sign >= 0:
                    succ.add(bidx)
            reach.append(succ)
        # Alternative reachability: explore the graph from each vertex using ordinary BFS.
        tc = sum(len(path_reach(v, reach)) == m for v in range(m))
        po = 0
        for a in assignments:
            dominated = False
            for b in assignments:
                if b == a:
                    continue
                inequalities = [ranks[i][b[i]] <= ranks[i][a[i]] for i in range(n)]
                if all(inequalities) and any(ranks[i][b[i]] < ranks[i][a[i]] for i in range(n)):
                    dominated = True
                    break
            if not dominated:
                po += 1
        out[(tc, po)] += m  # m possible first-agent ranking orders.
    return out


def path_reach(start, neighbors):
    seen = {start}
    frontier = [start]
    for node in frontier:
        for nextnode in neighbors[node]:
            if nextnode not in seen:
                seen.add(nextnode)
                frontier.append(nextnode)
    return seen

def load_expected():
    with (Path(__file__).resolve().parent / 'joint_counts.csv').open(newline='', encoding='utf-8') as f:
        records = list(csv.DictReader(f))
    data = {3: Counter(), 4: Counter()}
    for r in records:
        n, tc, po, value = (int(r[k]) for k in ('agents', 'top_cycle_size', 'pareto_size', 'labeled_profiles'))
        data[n][(tc, po)] = value
    assert len(records) == len(data[3]) + len(data[4])
    return data

if __name__ == '__main__':
    targets = load_expected()
    for n in (3, 4):
        result = census(n)
        assert result == targets[n], f'joint law differs at n={n}'
        expected_total = len(list(itertools.permutations(range(n)))) ** n
        assert sum(result.values()) == expected_total
        tally = Counter()
        for (tc, po), count in result.items():
            assert 1 <= po <= tc <= __import__('math').factorial(n)
            tally[tc] += count
        print(n, sorted(tally.items()), sum(tc*cnt for tc,cnt in tally.items()), sum(result.values()))
        print('joint', sorted(result.items()))
