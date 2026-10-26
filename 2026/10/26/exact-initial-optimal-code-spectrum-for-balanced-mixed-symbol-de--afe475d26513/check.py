"""Finite exact verification of balanced mixed-symbol deletion code profiles.

Python 3, standard library only.  The subset search is exhaustive;
its greedy-coloring bound is a mathematical upper bound, not a heuristic.
"""
from itertools import combinations
from collections import Counter


def words_of_weight(n, k):
    out = []
    for pos in combinations(range(n), k):
        word = ['0'] * n
        for p in pos:
            word[p] = '1'
        out.append(''.join(word))
    return sorted(out)


def outputs(word):
    n = len(word)
    return {word[:a] + word[a+1:b] + word[b+1:]
            for a in range(n) for b in range(a + 1, n)
            if word[a] != word[b]}


def graph(n):
    assert n >= 2 and n % 2 == 0
    words = words_of_weight(n, n//2)
    possible = words_of_weight(n-2, n//2-1)
    shadows = [outputs(w) for w in words]
    assert all(s <= set(possible) for s in shadows)
    inv = {y: [] for y in possible}
    for i, shadow in enumerate(shadows):
        for y in shadow:
            inv[y].append(i)
    N = len(words)
    conflict = [0]*N
    for support in inv.values():
        mask = sum(1<<i for i in support)
        for i in support:
            conflict[i] |= mask & ~(1<<i)
    full = (1<<N)-1
    compatible = [full & ~(conflict[i] | (1<<i)) for i in range(N)]
    assert all((compatible[i] >> i)&1 == 0 for i in range(N))
    assert all(bool((compatible[i]>>j)&1)==bool((compatible[j]>>i)&1)
               for i in range(N) for j in range(N))
    return words, shadows, compatible


def exact_codes(compatible, target):
    """Enumerate each target-sized clique exactly once, using a valid color bound.

    Every color class is independent in the compatibility graph; therefore
    a clique takes at most one vertex from each class. Within a recursion,
    candidates removed before an index are never visited again at that node.
    """
    full = (1<<len(compatible))-1
    found = []
    nodes = 0

    def color_order(pool):
        ordered, color_bound = [], []
        c = 0
        while pool:
            c += 1
            remaining = pool
            while remaining:
                low = remaining & -remaining
                v = low.bit_length()-1
                ordered.append(v)
                color_bound.append(c)
                pool &= ~low
                remaining &= ~low
                remaining &= ~compatible[v]
        return ordered, color_bound

    def visit(pool, chosen):
        nonlocal nodes
        nodes += 1
        if len(chosen) == target:
            found.append(tuple(sorted(chosen)))
            return
        if not pool:
            return
        order, bound = color_order(pool)
        for i in range(len(order)-1,-1,-1):
            if len(chosen)+bound[i] < target:
                break
            v = order[i]
            visit(pool & compatible[v], chosen + (v,))
            pool &= ~(1<<v)

    visit(full, ())
    assert len(found) == len(set(found))
    return found, nodes


def orbits(codes, words):
    code_set = set(codes)
    ids = {w:i for i,w in enumerate(words)}
    reverse = [ids[w[::-1]] for w in words]
    complement = [ids[''.join('1' if c=='0' else '0' for c in w)] for w in words]
    visited = set()
    sizes = Counter()
    for code in codes:
        if code in visited:
            continue
        orbit = {code, tuple(sorted(reverse[i] for i in code)),
                 tuple(sorted(complement[i] for i in code)),
                 tuple(sorted(complement[reverse[i]] for i in code))}
        assert orbit <= code_set
        visited.update(orbit)
        sizes[len(orbit)] += 1
    assert len(visited)==len(code_set)
    return dict(sorted(sizes.items()))


def main():
    expected = {
        2: (1, 2, {2:1}),
        4: (2, 1, {1:1}),
        6: (2, 40, {1:2,2:5,4:7}),
        8: (6, 3, {1:1,2:1}),
        10: (10, 666, {2:15,4:159}),
    }
    for n,(optimum,number,orbhist) in expected.items():
        words,shadows,adj=graph(n)
        codes, nodes = exact_codes(adj,optimum)
        strictly_larger, no_nodes=exact_codes(adj,optimum+1)
        assert len(codes)==number,(n,len(codes),number)
        assert not strictly_larger,(n,'larger code exists')
        assert orbits(codes,words)==orbhist,(n,orbits(codes,words))
        # Replay every complete code directly against the channel, not the graph.
        for code in codes:
            assert len(set().union(*(shadows[i] for i in code))) == sum(len(shadows[i]) for i in code)
        print('n=%d code_size=%d labeled_maxima=%d orbit_sizes=%s source_count=%d output_count=%d nodes=(%d,%d)' %
              (n,optimum,number,orbhist,len(words),len(words_of_weight(n-2,n//2-1)),nodes,no_nodes))
    print('BALANCED_MIXED_DELETION_EXACT_PASS')

if __name__ == '__main__':
    main()
