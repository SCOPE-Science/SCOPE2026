"""Exact finite proof checks for rank-product/egalitarian stable marriage."""
from collections import Counter
from itertools import permutations, product


def evaluate(profile):
    n = len(profile) // 2
    assert all(tuple(sorted(row)) == tuple(range(n)) for row in profile)
    stable = []
    for match in permutations(range(n)):
        inverse = [match.index(j) for j in range(n)]
        if any(profile[i][j] < profile[i][match[i]] and
               profile[n+j][i] < profile[n+j][inverse[j]]
               for i in range(n) for j in range(n) if j != match[i]):
            continue
        ranks = [profile[i][match[i]] for i in range(n)] + [
            profile[n+j][inverse[j]] for j in range(n)]
        total = sum(ranks)
        product_utility = 1
        for rank in ranks:
            product_utility *= n - rank
        stable.append((match, total, product_utility))
    assert stable
    egal = min(v[1] for v in stable)
    nash = max(v[2] for v in stable)
    e_set = {v[0] for v in stable if v[1] == egal}
    n_set = {v[0] for v in stable if v[2] == nash}
    return stable, e_set, n_set


def census(n):
    orders = list(permutations(range(n)))
    # Each strict preference list is encoded by inverse ranking.
    rank_tables = [tuple(row.index(j) for j in range(n)) for row in orders]
    counts = Counter()
    for profile_ids in product(range(len(orders)), repeat=2*n):
        profile = tuple(rank_tables[t] for t in profile_ids)
        stable, e_set, n_set = evaluate(profile)
        assert n_set <= e_set
        relation = 'equal' if n_set == e_set else 'proper_nash_subset'
        counts[(len(stable), relation)] += 1
    assert sum(counts.values()) == (len(orders))**(2*n)
    return counts


def example_four():
    ranks = ((2,3,0,1),(0,3,2,1),(1,2,3,0),
             (3,0,1,2),(0,1,3,2),(0,1,2,3),
             (3,1,0,2),(3,1,2,0))
    stable, e_set, n_set = evaluate(ranks)
    assert [(v[0],v[1],v[2]) for v in stable] == [
        ((0,1,2,3),11,768),
        ((0,2,1,3),11,1536),
        ((0,3,1,2),11,1728),
        ((2,0,3,1),9,1536)]
    assert e_set == {(2,0,3,1)}
    assert n_set == {(0,3,1,2)}
    assert not e_set & n_set
    return stable


if __name__ == '__main__':
    assert census(1) == Counter({(1,'equal'):1})
    assert census(2) == Counter({(1,'equal'): 14, (2,'equal'): 2})
    result = census(3)
    assert result == Counter({
      (1,'equal'):34080,
      (2,'equal'):9180,
      (2,'proper_nash_subset'):2304,
      (3,'equal'):468,
      (3,'proper_nash_subset'):624,
    }),result
    example_four()
    print('PASS: exhaustive n<=3; all n=3 46656 profiles; exact disjoint n=4 witness')
    print(result)
