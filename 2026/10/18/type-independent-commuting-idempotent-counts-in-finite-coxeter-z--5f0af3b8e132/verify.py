#!/usr/bin/env python3
"""Standalone integer checks of finite Coxeter zero-Hecke idempotent pairs.

Only standard-library modules are required.  The exhaustive tests are finite
checks; the arbitrary-rank result requires the proof in RESULT.md.
"""
from itertools import combinations, product
from collections import defaultdict


def predicted(n):
    a, b = 1, 4
    if n == 0:
        return a
    for _ in range(2, n + 1):
        a, b = b, 4 * b - 2 * a
    return b


def edges_type(n, typ):
    if typ == 'A':
        return {(i, i+1) for i in range(n-1)}
    edges = {(i, i+1) for i in range(1, n-1)}
    edges.add((0, n-1 if typ == 'B' else n-2))
    return edges


def components(n, edges, K):
    unseen = {i for i in range(n) if K & (1 << i)}
    while unseen:
        v = unseen.pop()
        size = 0
        todo = [v]
        while todo:
            v = todo.pop()
            size += 1
            for a, b in edges:
                nxt = b if a == v else a if b == v else -1
                if nxt in unseen:
                    unseen.remove(nxt)
                    todo.append(nxt)
        yield size


def graph_weight(n, edges):
    ans = 0
    for K in range(1 << n):
        term = 1
        for c in components(n, edges, K):
            term *= (1 << (c + 1)) - 1
        ans += term
    return ans


def criterion(I, J, n, edges):
    K = I | J
    unseen = {i for i in range(n) if K & (1 << i)}
    while unseen:
        root = unseen.pop()
        cc = {root}
        todo = [root]
        while todo:
            v = todo.pop()
            for a, b in edges:
                nxt = b if a == v else a if b == v else -1
                if nxt in unseen:
                    unseen.remove(nxt)
                    cc.add(nxt)
                    todo.append(nxt)
        if not (all(I & (1 << v) for v in cc) or
                all(J & (1 << v) for v in cc)):
            return False
    return True


def direct_states(n, edges):
    ans = 0
    for state in product(range(4), repeat=n):
        I = sum((1 << i) for i, s in enumerate(state) if s & 1)
        J = sum((1 << i) for i, s in enumerate(state) if s & 2)
        ans += criterion(I, J, n, edges)
    return ans


# Type A: Demazure right multiplication in the ordinary symmetric group.
def Astep(w, i):
    v = list(w)
    if v[i] < v[i+1]:
        v[i], v[i+1] = v[i+1], v[i]
    return tuple(v)


def Alongest_word(I, n):
    w = tuple(range(n+1))
    reduced = []
    while True:
        for i in range(n):
            if I & (1 << i):
                v = Astep(w, i)
                if v != w:
                    w = v
                    reduced.append(i)
                    break
        else:
            return w, reduced


def Apro(I, J, n, words):
    w = tuple(range(n+1))
    for i in words[I] + words[J]:
        w = Astep(w, i)
    return w


# Signed permutation realization and positive-root Coxeter length in B and D.
def is_negative_root(w, terms):
    image = [0] * len(w)
    for i, coeff in terms:
        a = w[i]
        image[abs(a)-1] += coeff if a > 0 else -coeff
    return next((v < 0 for v in image if v != 0), False)


def signed_length(w, typ):
    n = len(w)
    roots = []
    if typ == 'B':
        roots += [[(i, 1)] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            roots += [[(i,1),(j,1)],[(i,1),(j,-1)]]
    return sum(is_negative_root(w, root) for root in roots)


def signed_simple(w, i, typ):
    v = list(w)
    if i > 0:
        v[i-1], v[i] = v[i], v[i-1]
    elif typ == 'B':
        v[-1] *= -1
    else:
        v[-2], v[-1] = -v[-1], -v[-2]
    return tuple(v)


def signed_longest_word(I, n, typ):
    w = tuple(range(1, n+1))
    word = []
    while True:
        old_length = signed_length(w, typ)
        for i in range(n):
            if I & (1 << i):
                v = signed_simple(w, i, typ)
                if signed_length(v, typ) > old_length:
                    w = v
                    word.append(i)
                    break
        else:
            return w, word


def signed_pro(I, J, n, typ, words):
    w = tuple(range(1, n+1))
    for i in words[I] + words[J]:
        v = signed_simple(w, i, typ)
        if signed_length(v, typ) > signed_length(w, typ):
            w = v
    return w


def coxeter_test(typ, n):
    edges = edges_type(n, typ)
    if typ == 'A':
        words = {mask: Alongest_word(mask, n)[1] for mask in range(1 << n)}
        multiply = lambda I, J: Apro(I, J, n, words)
    else:
        words = {mask: signed_longest_word(mask, n, typ)[1]
                 for mask in range(1 << n)}
        multiply = lambda I, J: signed_pro(I, J, n, typ, words)
    num = 0
    for I in range(1 << n):
        for J in range(1 << n):
            actual = multiply(I, J) == multiply(J, I)
            rule = criterion(I, J, n, edges)
            assert actual == rule, (typ,n,I,J,actual,rule)
            num += actual
    assert num == graph_weight(n, edges) == predicted(n)
    return num


def prufer_edges(seq, n):
    degree = [1] * n
    for x in seq:
        degree[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf,x))
        degree[leaf] -= 1
        degree[x] -= 1
    remaining = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(remaining))
    return edges


def subcubic_trees():
    count = 0
    for n in range(2,7):
        for seq in product(range(n), repeat=n-2):
            edges = prufer_edges(seq,n)
            degree = [0] * n
            for a,b in edges:
                degree[a] += 1
                degree[b] += 1
            if max(degree) <= 3:
                actual = graph_weight(n,edges)
                assert actual == predicted(n), (n,seq,actual)
                count += 1
                if n <= 4:
                    assert direct_states(n, edges) == actual
    return count


def main():
    assert graph_weight(5,[(0,i) for i in range(1,5)]) == 564
    assert predicted(5) == 560
    for typ,n in [('A',2),('A',3),('A',4),('A',5),('A',6),
                  ('B',3),('B',4),('D',4),('D',5)]:
        result = coxeter_test(typ,n)
        print(f'{typ}{n}: {result} ordered commuting pairs, criterion PASS')
    tests = subcubic_trees()
    print(f'All {tests} labelled subcubic trees of size 2 through 6: PASS')
    for arms in ((2,2,2),(3,3,3),(1,2,4),(1,1,5)):
        edges=[];node=1
        for length in arms:
            parent=0
            for _ in range(length):
                edges.append((parent,node))
                parent=node;node+=1
        assert graph_weight(node,edges) == predicted(node)
    print('Selected larger branched trees: PASS; degree-four star sharpness: PASS')
    print('VERIFY_OK_COXETER_TREE')

if __name__ == '__main__':
    main()
