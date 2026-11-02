"""Exact finite verifier for blocking-neutrality in perfect roommate markets.

Pure Python 3, no external dependencies. All agents prefer any roommate to being
single. A matching is blocking-neutral if no other feasible perfect matching
blocking-neutrally dominates it as defined in Takahashi (2026, Def. 1).
"""
from itertools import permutations, product
from collections import Counter


def matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
    else:
        i = vertices[0]
        for j in vertices[1:]:
            for remainder in matchings(v for v in vertices[1:] if v != j):
                yield ((i, j),) + remainder


def partner(pairs, n):
    p = [None] * n
    for i, j in pairs:
        p[i], p[j] = j, i
    assert None not in p
    return tuple(p)


def outcomes(preferences):
    n = len(preferences)
    assert n % 2 == 0
    for i, row in enumerate(preferences):
        assert sorted(row) == [j for j in range(n) if j != i]
    ranks = [{j: pos for pos, j in enumerate(row)} for row in preferences]
    pairs = tuple(matchings(range(n)))
    partners = [partner(m, n) for m in pairs]
    blockers = []
    for p in partners:
        B = set()
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] != j and ranks[i][j] < ranks[i][p[i]] and ranks[j][i] < ranks[j][p[j]]:
                    B.add((i, j))
        blockers.append(frozenset(B))
    blocking_agents = [frozenset(v for pair in B for v in pair) for B in blockers]

    def dominates(j, i):
        """Whether matching j blocking-neutrally dominates matching i."""
        if i == j:
            return False
        improves_a_blocker = any(ranks[v][partners[j][v]] < ranks[v][partners[i][v]]
                                 for v in blocking_agents[i])
        worsens_a_new_blocker = any(ranks[v][partners[i][v]] < ranks[v][partners[j][v]]
                                    for v in blocking_agents[j])
        return improves_a_blocker and not worsens_a_new_blocker

    def pareto_dominates(j, i):
        if i == j:
            return False
        return (all(ranks[v][partners[j][v]] <= ranks[v][partners[i][v]] for v in range(n))
                and any(ranks[v][partners[j][v]] < ranks[v][partners[i][v]] for v in range(n)))

    doms = {(i, j) for i in range(len(pairs)) for j in range(len(pairs)) if dominates(j, i)}
    pd = {(i, j) for i in range(len(pairs)) for j in range(len(pairs)) if pareto_dominates(j, i)}
    bn = tuple(i for i in range(len(pairs)) if not any(a == i for a, b in doms))
    po = tuple(i for i in range(len(pairs)) if not any(a == i for a, b in pd))
    return pairs, blockers, bn, po, doms, pd


def four_person_census():
    all_orders = [list(permutations(j for j in range(4) if j != i)) for i in range(4)]
    census = Counter()
    examples = {}
    for p in product(*all_orders):
        matches, blockers, bn, po, doms, _ = outcomes(p)
        s = sum(not b for b in blockers)
        census[s, len(bn), len(po)] += 1
        examples.setdefault((s, len(bn), len(po)), p)
        if not s:
            assert len(bn) == 3 and len(po) == 3
            assert all(len(b) == 1 for b in blockers)
            assert len(set(blockers)) == 3
            assert not doms
    assert sum(census.values()) == 6**4 == 1296
    assert sum(k[0] == 0 and v or 0 for k, v in census.items()) == 48
    assert all(k[0] != 0 or k[1:] == (3, 3) for k in census)
    print('FOUR-CENSUS', sorted(census.items()))
    print('UNSOLVABLE', 48, 'out of', 1296, 'all 3 BN and PO')


P_0 = ((1, 2, 3, 4, 5), (2, 0, 3, 4, 5), (0, 1, 3, 4, 5),
       (4, 5, 0, 1, 2), (5, 3, 0, 1, 2), (3, 4, 0, 1, 2))
P_1 = ((2, 1, 3, 4, 5),) + P_0[1:]


def six_person_transition():
    pre = outcomes(P_0)
    post = outcomes(P_1)
    assert len(pre[0]) == len(post[0]) == 15
    assert all(pre[1]) and all(post[1])
    assert len(pre[2]) == len(pre[3]) == 9
    assert len(post[2]) == 6 and len(post[3]) == 9
    assert post[2] == (3, 4, 5, 6, 9, 12)
    assert post[3] == (0, 1, 2, 3, 4, 5, 6, 9, 12)
    assert all(i in post[3] for i in post[2])
    assert all((i, i + 3) in post[4] for i in (0, 1, 2))
    assert all((i, i + 3) not in post[5] for i in (0, 1, 2))
    for i, matching in enumerate(post[0]):
        print(f'M{i:02d}', str(matching), 'blocks', sorted(post[1][i]),
              'PO', i in post[3], 'BN', i in post[2])
    print('INITIAL', 'PO', pre[3], 'BN', pre[2])
    print('ONE-SWAP', 'PO', post[3], 'BN', post[2])
    print('NON-PARETO-EXCLUSION CERTIFICATE', [(i, i + 3) for i in (0, 1, 2)])

if __name__ == '__main__':
    four_person_census()
    six_person_transition()
    print('ALL ASSERTIONS PASSED')
