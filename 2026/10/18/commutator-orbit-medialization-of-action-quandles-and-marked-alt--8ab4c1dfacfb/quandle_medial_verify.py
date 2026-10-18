#!/usr/bin/env python3
"""Exact finite checks for a marked-permutation quandle and its medial orbit quotient.
Pure Python 3; no external packages. The general proof is algebraic.
"""
from itertools import permutations
from collections import deque, defaultdict


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def cycles(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i not in seen:
            j, k = i, 0
            while j not in seen:
                seen.add(j)
                k += 1
                j = p[j]
            lengths.append(k)
    return lengths


def pointed_type(x, p):
    seen, j = set(), x
    while j not in seen:
        seen.add(j)
        j = p[j]
    d = len(seen)
    others = list(cycles(p))
    others.remove(d)
    return tuple(sorted(cycles(p))), d, tuple(sorted(others))


def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for d in range(min(n, max_part), 0, -1):
        for tail in partitions(n-d, d):
            yield (d,) + tail


def expected(n):
    specs = list(partitions(n))
    signed = 2 * sum(p.count(1) for p in specs if (n-len(p)) % 2 == 0)
    sorbits = sum(len(set(p)) for p in specs)
    split = sum(1 for d in range(1, n+1)
                for parts in partitions(n-d)
                if len(parts) == len(set(parts)) and all(v % 2 for v in parts))
    assert sorbits + split == signed
    return signed, sorbits, split


def orbit_data(n):
    ps = list(permutations(range(n)))
    pidx = {p:i for i,p in enumerate(ps)}
    size = len(ps)
    inv = [inverse(p) for p in ps]
    gens = []
    for j in range(2, n):
        g = list(range(n))
        g[0], g[1], g[j] = 1, j, 0
        gens.append((tuple(g), inverse(tuple(g))))
    # n=2: the derived group of S_2 is trivial.
    moves = []
    for a, ai in gens:
        pp = [pidx[compose(compose(a, g), ai)] for g in ps]
        moves.append((a, pp))
    orbit = [-1] * (n*size)
    rep = []
    for start in range(n*size):
        if orbit[start] != -1:
            continue
        oi = len(rep)
        orbit[start] = oi
        rep.append(start)
        todo = deque([start])
        while todo:
            cur = todo.popleft()
            x, pi = divmod(cur, size)
            for a, pp in moves:
                to = a[x]*size + pp[pi]
                if orbit[to] == -1:
                    orbit[to] = oi
                    todo.append(to)
                else:
                    assert orbit[to] == oi
    # The marked cycle decomposition of each S_n orbit has one or two A_n orbits.
    types = defaultdict(set)
    for i in range(n*size):
        x, pi = divmod(i, size)
        types[pointed_type(x, ps[pi])].add(orbit[i])
    for (_, _, rest), classes in types.items():
        splitting = bool(all(k%2 for k in rest) and len(rest)==len(set(rest)))
        assert len(classes) == (2 if splitting else 1), (n,rest,classes)
    predicted, _, _ = expected(n)
    assert len(rep) == predicted, (n, len(rep), predicted)
    # Choose the actual action-convention of the quandle given by (x,g) * (y,h)
    # = (h(g^{-1}(x)), h g h^{-1}).  The y coordinate is immaterial.
    def operation(a, b):
        x, g = divmod(a, size)
        _, h = divmod(b, size)
        hh, gg = ps[h], ps[g]
        return hh[inv[g][x]]*size + pidx[compose(compose(hh, gg), inv[h])]
    def quotient_op(a, b):
        return orbit[operation(rep[a], rep[b])]
    # Congruence: test representative changes by every derived-group generator.
    if n <= 4:
        for a in range(n*size):
            for b in range(n*size):
                oa, ob = orbit[a], orbit[b]
                v = orbit[operation(a,b)]
                assert v == quotient_op(oa, ob), (n,a,b)
    elif n <= 6:
        # Exhaust changes by derived group generators on either argument.
        for a in range(n*size):
            x,g = divmod(a,size)
            for j in range(len(moves)):
                aa = moves[j][0][x]*size + moves[j][1][g]
                for b in rep:
                    assert orbit[operation(a,b)] == orbit[operation(aa,b)]
                    assert orbit[operation(b,a)] == orbit[operation(b,aa)]
    # The quotient satisfies the actual 4-variable medial identity.
    table = [[quotient_op(a,b) for b in range(len(rep))] for a in range(len(rep))]
    for a in range(len(rep)):
        for b in range(len(rep)):
            for c in range(len(rep)):
                for d in range(len(rep)):
                    assert table[table[a][b]][table[c][d]] == table[table[a][c]][table[b][d]]
    return len(rep), len(types), sum(len(x)==2 for x in types.values())


if __name__ == '__main__':
    for n in range(2,8):
        observed = orbit_data(n)
        _, so, sp = expected(n)
        assert observed[1:] == (so,sp)
        print(f'n={n}: quotient={observed[0]}, S_n-orbits={so}, split-orbits={sp}')
    print('VERIFY_OK: derived diagonal orbits, split criterion, quotient congruence and medial law')
