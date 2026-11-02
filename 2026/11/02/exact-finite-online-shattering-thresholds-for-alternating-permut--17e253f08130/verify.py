"""Exact finite comparison-shattering verifier for up-down permutations.
Run: python verify.py certificate.json
Standard Python library only.
"""
import itertools
import json
import sys
from functools import lru_cache

EXPECTED_COUNTS = {2: 1, 3: 2, 4: 5, 5: 16, 6: 61, 7: 272, 8: 1385}
EXPECTED_LDIM = {2: 0, 3: 1, 4: 2, 5: 4, 6: 5, 7: 7, 8: 9}

def updown(p):
    return all((p[i] < p[i + 1] if i % 2 == 0 else p[i] > p[i + 1])
               for i in range(len(p) - 1))

def hypothesis_data(n):
    objects = tuple(p for p in itertools.permutations(range(n)) if updown(p))
    # Adjacent comparisons are fixed by the up-down condition; omit them.
    queries = tuple((i, j) for i in range(n) for j in range(i + 2, n))
    masks = tuple(sum(1 << k for k, p in enumerate(objects) if p[i] < p[j])
                  for i, j in queries)
    return objects, queries, masks

def independent_extensions(n):
    # A second construction: topological sorts of the height-two zigzag poset.
    before = [0] * n
    for i in range(n - 1):
        low, high = (i, i + 1) if i % 2 == 0 else (i + 1, i)
        before[high] |= 1 << low
    result = set()
    def walk(used, order):
        if len(order) == n:
            values = [None] * n
            for rank, pos in enumerate(order): values[pos] = rank
            result.add(tuple(values))
            return
        for pos in range(n):
            if not (used >> pos & 1) and (before[pos] & ~used) == 0:
                walk(used | (1 << pos), order + (pos,))
    walk(0, ())
    return result

def lit_dimensional_rank(masks, whole):
    @lru_cache(None)
    def rank(state):
        if state.bit_count() < 2: return 0
        best = 0
        for column in masks:
            yes = state & column
            no = state ^ yes
            if not yes or not no:
                continue
            if yes.bit_count() < (1 << best) or no.bit_count() < (1 << best):
                continue
            candidate = 1 + min(rank(yes), rank(no))
            if candidate > best: best = candidate
        return best
    root = rank(whole)
    return root, rank

def independent_depth_decision(masks, state, depth):
    @lru_cache(None)
    def possible(state, depth):
        if depth == 0: return True
        if state.bit_count() < (1 << depth): return False
        for column in masks:
            yes = state & column
            no = state ^ yes
            if yes and no and possible(yes, depth - 1) and possible(no, depth - 1):
                return True
        return False
    answer = possible(state, depth)
    return answer, possible.cache_info().currsize

def make_tree(queries, masks, state, depth, rank):
    if depth == 0:
        index = (state & -state).bit_length() - 1
        return {'leaf': index}
    for index, column in enumerate(masks):
        yes = state & column; no = state ^ yes
        if yes and no and rank(yes) >= depth - 1 and rank(no) >= depth - 1:
            return {'query': index,
                    'no': make_tree(queries, masks, no, depth - 1, rank),
                    'yes': make_tree(queries, masks, yes, depth - 1, rank)}
    raise AssertionError('No witnessed query for required depth')

def check_tree(tree, masks, state, depth):
    if depth == 0:
        assert set(tree) == {'leaf'}
        assert state >> tree['leaf'] & 1
        return (0, 1, {tree['leaf']})
    assert set(tree) == {'query', 'no', 'yes'}
    query = tree['query']; assert 0 <= query < len(masks)
    yes, no = state & masks[query], state & ~masks[query]
    assert yes and no
    a = check_tree(tree['no'], masks, no, depth - 1)
    b = check_tree(tree['yes'], masks, yes, depth - 1)
    assert not (a[2] & b[2])
    return (a[0] + b[0] + 1, a[1] + b[1], a[2] | b[2])

def verify(certificate_path=None, generate=None):
    root_tree = None
    for n in range(2, 9):
        objects, queries, masks = hypothesis_data(n)
        assert len(objects) == EXPECTED_COUNTS[n]
        assert set(objects) == independent_extensions(n)
        whole = (1 << len(objects)) - 1
        support = []
        for parity in (0, 1):
            positions = list(range(parity, n, 2))
            support += [(positions[0], j) for j in positions[1:]]
        assert len(support) == n - 2
        patterns = {tuple(int(p[i] < p[j]) for i, j in support) for p in objects}
        assert len(patterns) == 1 << (n - 2)
        print('STATIC_SHATTERING_PASS', n, len(support), len(patterns))
        value, rank = lit_dimensional_rank(masks, whole)
        assert value == EXPECTED_LDIM[n], (n, value)
        if n == 8:
            possible10, states = independent_depth_decision(masks, whole, 10)
            assert not possible10
            print('DEPTH_TEN_IMPOSSIBILITY_PASS', 'states', states)
            if generate is not None:
                root_tree = make_tree(queries, masks, whole, 9, rank)
                with open(generate, 'w', encoding='utf-8') as file:
                    json.dump(root_tree, file, separators=(',', ':'))
                    file.write('\n')
            if certificate_path is not None:
                with open(certificate_path, encoding='utf-8') as file: tree = json.load(file)
                nodes, leaves, witnesses = check_tree(tree, masks, whole, 9)
                assert (nodes, leaves, len(witnesses)) == (511, 512, 512)
                print('DEPTH_NINE_TREE_PASS', nodes, leaves)
        print('EXACT_DIMENSION_PASS', n, len(objects), value, 'states', rank.cache_info().currsize)
    print('ZIGZAG_ALL_CHECKS_PASS')

if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--generate':
        verify(generate=sys.argv[2])
    elif len(sys.argv) == 2:
        verify(certificate_path=sys.argv[1])
    else:
        raise SystemExit('Usage: python verify.py certificate.json')
