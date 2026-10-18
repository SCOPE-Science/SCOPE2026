"""Independent direct checks for the two 18-element distributive lattices."""
from collections import Counter
from itertools import combinations
import networkx as nx

A = (0, 0, 1, 3, 5, 15, 23, 63)
B = (0, 0, 1, 3, 5, 15, 23, 95)


def ideal_sets(pred):
    result = []
    for k in range(len(pred) + 1):
        for idx in combinations(range(len(pred)), k):
            s = frozenset(idx)
            if all(set(j for j in range(len(pred)) if pred[i] >> j & 1) <= s
                   for i in s):
                result.append(s)
    return result


def order_graph(pred):
    G = nx.DiGraph()
    G.add_nodes_from(range(len(pred)))
    for b in range(len(pred)):
        for a in range(b):
            if pred[b] >> a & 1:
                G.add_edge(a, b)
    return G


def principal_profile(ideals):
    d = []
    for x in ideals:
        d.append((sum(y < x for y in ideals), sum(x < y for y in ideals)))
    return Counter(d)


def c2_rounds(IA, IB):
    n = len(IA)
    both = IA + IB
    below = [[j for j, y in enumerate(both) if y < x and ((i < n) == (j < n))]
             for i, x in enumerate(both)]
    above = [[j for j, y in enumerate(both) if x < y and ((i < n) == (j < n))]
             for i, x in enumerate(both)]
    colors = [0] * (2 * n)
    equal = []
    for step in range(4):
        keys = [(colors[i], tuple(sorted(Counter(colors[j] for j in below[i]).items())),
                 tuple(sorted(Counter(colors[j] for j in above[i]).items())))
                for i in range(2 * n)]
        ids = {k: j for j, k in enumerate(sorted(set(keys)))}
        colors = [ids[k] for k in keys]
        equal.append(Counter(colors[:n]) == Counter(colors[n:]))
    return equal


def chain_height(pred):
    n = len(pred)
    return max((len(t) for k in range(1, n + 1)
                for t in combinations(range(n), k)
                if all(pred[j] >> i & 1 for i, j in zip(t, t[1:]))), default=0)


def main():
    IA = ideal_sets(A)
    IB = ideal_sets(B)
    assert len(IA) == len(IB) == 18
    a, b = principal_profile(IA), principal_profile(IB)
    assert a == b and sum(a.values()) == 18
    assert not nx.is_isomorphic(order_graph(A), order_graph(B))
    assert (chain_height(A), chain_height(B)) == (4, 5)
    same = c2_rounds(IA, IB)
    assert same[0] and not same[1], same
    print('PROFILE=', sorted(a.items()))
    print('POSETS_CHAIN_HEIGHT_A_B=4,5')
    print('COLOUR_HIST_EQUAL_AFTER_ROUND_1=True')
    print('COLOUR_HIST_EQUAL_AFTER_ROUND_2=False')
    print('VERIFY_WITNESS_OK')


if __name__ == '__main__':
    main()
