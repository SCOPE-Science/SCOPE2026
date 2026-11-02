#!/usr/bin/env python3
"""Recompute parity-restricted comparison-shattering data from first principles.

Standard-library only: python3 verify_even_orders.py trees.json
"""
import itertools
import json
import math
import sys
from functools import lru_cache

EXPECTED = {1: 0, 2: 0, 3: 1, 4: 3, 5: 5, 6: 8, 7: 10}

def even_words(n):
    ans = []
    for w in itertools.permutations(range(1, n + 1)):
        if sum(w[i] > w[j] for i in range(n) for j in range(i + 1, n)) % 2 == 0:
            ans.append(w)
    return ans

def make_instance(n):
    words = even_words(n)
    domain = list(itertools.combinations(range(1, n + 1), 2))
    qmasks = []
    signatures = []
    for word in words:
        pos = {x: i for i, x in enumerate(word)}
        signatures.append(sum((1 << k) for k, (a, b) in enumerate(domain) if pos[a] < pos[b]))
    for i, (a, b) in enumerate(domain):
        qmasks.append(sum(1 << j for j, sig in enumerate(signatures) if (sig >> i) & 1))
    return words, domain, qmasks, signatures

def exact_search(n):
    words, domain, qmasks, sigs = make_instance(n)
    full = (1 << len(words)) - 1
    @lru_cache(None)
    def feasible(mask, depth):
        if depth == 0:
            return bool(mask)
        if mask.bit_count() < (1 << depth):
            return False
        for q in qmasks:
            yes = mask & q
            no = mask ^ yes
            if yes.bit_count() < (1 << (depth - 1)) or no.bit_count() < (1 << (depth - 1)):
                continue
            if feasible(yes, depth - 1) and feasible(no, depth - 1):
                return True
        return False
    d = EXPECTED[n]
    assert feasible(full, d)
    assert not feasible(full, d + 1), (n, d + 1)
    return words, domain, qmasks, sigs, full, feasible

def check_tree(n, tree):
    words, domain, masks, sigs = make_instance(n)
    full = (1 << len(words)) - 1
    index = {tuple(w): j for j, w in enumerate(words)}
    query_index = {tuple(q): i for i, q in enumerate(domain)}
    seen_leaves = set()
    internal_nodes = 0
    def visit(node, mask, level):
        nonlocal internal_nodes
        assert mask != 0 and level <= EXPECTED[n]
        if level == EXPECTED[n]:
            assert isinstance(node, dict) and set(node) == {'witness'}
            w = tuple(node['witness'])
            assert w in index and ((mask >> index[w]) & 1)
            assert w not in seen_leaves
            seen_leaves.add(w)
            return
        assert isinstance(node, dict) and set(node) == {'query', '0', '1'}
        q = tuple(node['query'])
        assert q in query_index
        yes = mask & masks[query_index[q]]
        no = mask ^ yes
        assert yes and no
        internal_nodes += 1
        visit(node['0'], no, level + 1)
        visit(node['1'], yes, level + 1)
    visit(tree, full, 0)
    assert len(seen_leaves) == (1 << EXPECTED[n])
    assert internal_nodes == (1 << EXPECTED[n]) - 1
    return internal_nodes, len(seen_leaves)

def graph_is_forest(n, subset, domain):
    parent = list(range(n + 1))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i in subset:
        a, b = domain[i]
        a, b = find(a), find(b)
        if a == b:
            return False
        parent[a] = b
    return True

def forecast_shattering(n, subset, domain):
    if not graph_is_forest(n, subset, domain):
        return False
    if len(subset) < n - 1:
        return True
    deg = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for i in subset:
        a, b = domain[i]
        deg[a] += 1
        deg[b] += 1
        adj[a].append(b)
        adj[b].append(a)
    if not (deg.count(1) == 2 and all(t in (1,2) for t in deg[1:])):
        return True
    if n % 4 not in (0, 1):
        return False
    head = next(i for i in range(1,n+1) if deg[i] == 1)
    path = [head]
    last = 0
    while len(path) < n:
        nxt = next(x for x in adj[path[-1]] if x != last)
        last, head = head, nxt
        path.append(head)
    return sum(path[i] > path[j] for i in range(n) for j in range(i+1,n)) % 2 == 0

def brute_shattering(n):
    words, domain, masks, sigs = make_instance(n)
    q = len(domain)
    counts = [0] * n
    for k in range(n):
        for sub in itertools.combinations(range(q), k):
            traces = set()
            for sig in sigs:
                traces.add(sum(1 << j for j, i in enumerate(sub) if (sig >> i) & 1))
                if len(traces) == (1 << k):
                    break
            actual = len(traces) == (1 << k)
            predicted = forecast_shattering(n, sub, domain)
            assert actual == predicted, (n, sub, actual, predicted)
            counts[k] += int(actual)
    return counts

def main():
    filename = sys.argv[1] if len(sys.argv)>1 else 'trees.json'
    with open(filename, encoding='utf8') as f:
        trees = json.load(f)
    assert set(trees) == {str(n) for n in EXPECTED if EXPECTED[n] > 0}
    total_nodes = total_leaves = 0
    for n in EXPECTED:
        words, domain, masks, sigs, full, feasible = exact_search(n)
        if n > 1:
            assert len(words) == math.factorial(n) // 2
        if EXPECTED[n] > 0:
            x,y = check_tree(n, trees[str(n)])
            total_nodes += x
            total_leaves += y
        print('LDIM', n, EXPECTED[n], 'concepts', len(words), 'states', feasible.cache_info().currsize)
    for n in range(2, 7):
        hist = brute_shattering(n)
        assert hist[-1] == ({2:0,3:0,4:10,5:95,6:936}[n]), (n,hist)
        print('VC',n, max(i for i,x in enumerate(hist) if x), 'top_count',hist[-1])
    print('ALTERNATING_COMPARISON_ALL_CHECKS_PASS', total_nodes, total_leaves)

if __name__ == '__main__':
    main()
