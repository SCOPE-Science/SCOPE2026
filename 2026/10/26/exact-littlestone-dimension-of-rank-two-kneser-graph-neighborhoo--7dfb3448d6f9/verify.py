"""Finite certificate for adaptive shattering of the pair-disjointness concepts.

Run from this directory: python3 verify.py
No nonstandard packages or network resources are needed.
"""
import itertools
import json
from pathlib import Path


def pair(obj, n):
    assert isinstance(obj, list) and len(obj) == 2
    assert all(isinstance(x, int) and 1 <= x <= n for x in obj)
    assert obj[0] < obj[1]
    return frozenset(obj)


def check_tree(node, n, expected_depth, path=()):
    """Return the number of verified distinct terminal paths."""
    if expected_depth == 0:
        assert set(node) == {"witness"}
        target = pair(node["witness"], n)
        for queried, is_overlap in path:
            assert bool(queried & target) == is_overlap
        return 1
    assert set(node) == {"query", "overlap", "disjoint"}
    queried = pair(node["query"], n)
    return (check_tree(node["overlap"], n, expected_depth - 1,
                       path + ((queried, True),))
            + check_tree(node["disjoint"], n, expected_depth - 1,
                         path + ((queried, False),)))


def main():
    data = json.loads(Path(__file__).with_name('witness_trees.json').read_text(encoding='utf-8'))
    assert set(data) == {'4', '5', '6', '7'}
    for n in range(4, 8):
        depth = n-3
        leaves = check_tree(data[str(n)], n, depth)
        assert leaves == 2 ** depth
        print(f'n={n}: verified depth-{depth} full tree with {leaves} realized paths')

    # Optional secondary diagnostic: the adaptive depth-four witness at n=7
    # is stronger than fixed-sample shattering on four vertices of KG(7,2).
    U = list(itertools.combinations(range(1, 8), 2))
    concepts = [sum(1 << j for j, x in enumerate(U) if set(x).isdisjoint(y)) for y in U]
    count4 = 0
    for indices in itertools.combinations(range(len(U)), 4):
        count4 += 1
        traces = {sum(((mask >> i) & 1) << bit for bit, i in enumerate(indices)) for mask in concepts}
        assert len(traces) != 16
    assert count4 == 5985
    print('n=7: all 5,985 four-point subsets fail ordinary VC shattering')
    print('Certificate verification succeeded.')


if __name__ == '__main__':
    main()
