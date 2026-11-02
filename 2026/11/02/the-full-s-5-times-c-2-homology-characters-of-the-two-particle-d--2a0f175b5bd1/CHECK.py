#!/usr/bin/env python3
"""Exact cellular and character verification for the Desargues two-point result.

Pure Python 3, standard library only. No hidden files, internet, or optional modules.
"""
import collections
import itertools
import math

GROUND = frozenset(range(5))
VERTICES = tuple(frozenset(s) for k in (2, 3) for s in itertools.combinations(range(5), k))
VINDEX = {s: i for i, s in enumerate(VERTICES)}
EDGES = tuple((i, j) for i, a in enumerate(VERTICES)
              for j, b in enumerate(VERTICES) if i < j and (a < b or b < a))
EINDEX = {z: i for i, z in enumerate(EDGES)}
ZERO = tuple(itertools.combinations(range(len(VERTICES)), 2))
ZINDEX = {p: i for i, p in enumerate(ZERO)}
ONE = tuple((v, ei) for v in range(len(VERTICES))
            for ei, (a, b) in enumerate(EDGES) if v != a and v != b)
OINDEX = {p: i for i, p in enumerate(ONE)}
TWO = tuple((ei, fi) for ei in range(len(EDGES))
            for fi in range(ei + 1, len(EDGES)) if len(set(EDGES[ei] + EDGES[fi])) == 4)


def boundary1(c):
    v, ei = ONE[c]
    a, b = EDGES[ei]
    return {ZINDEX[tuple(sorted((v, a)))]: -1, ZINDEX[tuple(sorted((v, b)))]: 1}


def boundary2(ei, fi):
    a, b = EDGES[ei]
    c, d = EDGES[fi]
    return {OINDEX[(b, fi)]: 1, OINDEX[(a, fi)]: -1,
            OINDEX[(d, ei)]: -1, OINDEX[(c, ei)]: 1}


def mod_rank(matrix_columns, p):
    piv = {}
    for col in matrix_columns:
        z = {k: v % p for k, v in col.items() if v % p}
        while z:
            k = max(z)
            if k not in piv:
                inv = pow(z[k], -1, p)
                piv[k] = {j: (t * inv) % p for j, t in z.items()}
                break
            lead = z[k]
            for j, t in piv[k].items():
                h = (z.get(j, 0) - lead * t) % p
                if h:
                    z[j] = h
                else:
                    z.pop(j, None)
    return len(piv)


def action(sigma, antipodal):
    vm = []
    for subset in VERTICES:
        image = frozenset(sigma[v] for v in subset)
        if antipodal:
            image = GROUND - image
        vm.append(VINDEX[image])
    em, signs = [], []
    for a, b in EDGES:
        new_a, new_b = vm[a], vm[b]
        em.append(EINDEX[tuple(sorted((new_a, new_b)))])
        signs.append(1 if new_a < new_b else -1)
    return vm, em, signs


def perm_type(sigma):
    seen, parts = set(), []
    for i in range(5):
        if i not in seen:
            c, j = 0, i
            while j not in seen:
                seen.add(j)
                c += 1
                j = sigma[j]
            parts.append(c)
    return tuple(sorted(parts, reverse=True))


def partitions(n, maximum=None):
    if n == 0:
        yield ()
    else:
        for t in range(min(n, n if maximum is None else maximum), 0, -1):
            for remainder in partitions(n - t, t):
                yield (t,) + remainder


def specht_char(lam, cycles):
    if not cycles:
        return int(not lam)
    step, remaining = cycles[0], cycles[1:]
    answer = 0
    for mu in partitions(sum(lam) - step):
        if len(mu) > len(lam) or any(mu[i] > lam[i] for i in range(len(mu))):
            continue
        skew = {(i, j) for i, k in enumerate(lam)
                for j in range(k) if j >= (mu[i] if i < len(mu) else 0)}
        if len(skew) != step:
            continue
        if any((i + 1, j) in skew and (i, j + 1) in skew and (i + 1, j + 1) in skew
               for i, j in skew):
            continue
        found = {next(iter(skew))}
        frontier = list(found)
        while frontier:
            i, j = frontier.pop()
            for neighbor in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if neighbor in skew and neighbor not in found:
                    found.add(neighbor)
                    frontier.append(neighbor)
        if len(found) == step:
            answer += (-1) ** (len({i for i, j in skew}) - 1) * specht_char(mu, remaining)
    return answer


def graph_cycle_basis_lengths():
    graph = [set() for _ in VERTICES]
    for a, b in EDGES:
        graph[a].add(b)
        graph[b].add(a)
    queue = collections.deque([0])
    parent = {0: None}
    depth = {0: 0}
    while queue:
        v = queue.popleft()
        for w in sorted(graph[v]):
            if w not in parent:
                parent[w] = v
                depth[w] = depth[v] + 1
                queue.append(w)
    assert len(parent) == len(VERTICES)
    tree = {tuple(sorted((v, p))) for v, p in parent.items() if p is not None}
    cycles = []
    for a, b in EDGES:
        if (a, b) in tree:
            continue
        from_a = {}
        c = a
        while c is not None:
            from_a[c] = True
            c = parent[c]
        c, branch = b, []
        while c not in from_a:
            branch.append(c)
            c = parent[c]
        lca = c
        length = len(branch) + 1
        while a != lca:
            a = parent[a]
            length += 1
        cycles.append(length)
    return cycles


def main():
    assert (len(VERTICES), len(EDGES), len(ZERO), len(ONE), len(TWO)) == (20, 30, 190, 540, 375)
    assert all(len(z) == 4 for z in (boundary2(*ef) for ef in TWO))
    assert all(sum(t * x for y, t in boundary2(*ef).items()
                   for z, x in boundary1(y).items() if z == zi) == 0
               for ef in TWO for zi in range(len(ZERO)))
    # The 1-skeleton is connected, giving rank(d1)=189.
    adjacent = [set() for _ in ZERO]
    for k in range(len(ONE)):
        a, b = boundary1(k)
        adjacent[a].add(b)
        adjacent[b].add(a)
    reached, queue = {0}, collections.deque([0])
    while queue:
        v = queue.popleft()
        for w in adjacent[v] - reached:
            reached.add(w)
            queue.append(w)
    assert len(reached) == 190
    # 11 fundamental cycles shorter than 20, so each permits a parked particle.
    loops = graph_cycle_basis_lengths()
    assert len(loops) == 11 and max(loops) < 20
    # This yields rank(d2) <= 540-189-11 = 340 over Q.
    matrix = [boundary2(*ef) for ef in TWO]
    assert mod_rank(matrix, 3) == 340   # rank(d2) >= 340 over Q.
    print('CELLS (190,540,375); rank(d1)=189; rank(d2)=340; rational Betti (1,11,35)')
    print('TREE CYCLE LENGTHS', sorted(loops))

    classes = collections.defaultdict(list)
    for sigma in itertools.permutations(range(5)):
        for antipodal in (0, 1):
            vm, em, signs = action(sigma, antipodal)
            for ei, fi in TWO:
                ee, ff = em[ei], em[fi]
                orientation = signs[ei] * signs[fi] * (1 if ee < ff else -1)
                left = collections.defaultdict(int)
                for k, val in boundary2(ei, fi).items():
                    v, edge = ONE[k]
                    left[OINDEX[(vm[v], em[edge])]] += val * signs[edge]
                right = {k: orientation * val for k, val in boundary2(*sorted((ee, ff))).items()}
                assert all(left[k] == right.get(k, 0) for k in set(left) | set(right))
            c0 = sum({vm[a], vm[b]} == {a, b} for a, b in ZERO)
            c1 = sum(signs[e] for v, e in ONE if vm[v] == v and em[e] == e)
            c2 = sum(signs[ei] * signs[fi] * (1 if em[ei] < em[fi] else -1)
                     for ei, fi in TWO if {em[ei], em[fi]} == {ei, fi})
            h1 = 1 - sum(vm[i] == i for i in range(20)) + sum(signs[e] for e in range(30) if em[e] == e)
            h2 = c0 - c1 + c2 - 1 + h1
            classes[(perm_type(sigma), antipodal)].append((c0, c1, c2, h1, h2))
    assert len(classes) == 14
    for cl, data in classes.items():
        assert len(set(data)) == 1
    classes = {k: (len(v), v[0]) for k, v in classes.items()}
    print('GROUP CONJUGACY TABLE: type, antipodal, class size, (tr C0, tr C1, tr C2, tr H1, tr H2)')
    for k, (size, data) in sorted(classes.items()):
        print(k[0], k[1], size, data)
    assert sum(sz for sz, data in classes.values()) == 240
    parts = sorted(partitions(5), reverse=True)
    expected = {
        ('H1', '+'): {(3, 1, 1): 1},
        ('H1', '-'): {(2, 2, 1): 1},
        ('H2', '+'): {(3, 1, 1): 1, (2, 2, 1): 1, (2, 1, 1, 1): 1},
        ('H2', '-'): {(4, 1): 1, (3, 2): 1, (3, 1, 1): 1, (2, 2, 1): 1},
    }
    for deg, ix in [('H1', 3), ('H2', 4)]:
        for parity in (0, 1):
            multiplicities = {}
            for sh in parts:
                total = 0
                for part in parts:
                    sz, a = classes[(part, 0)]
                    sz2, b = classes[(part, 1)]
                    assert sz == sz2
                    num = a[ix] + (1 if parity == 0 else -1) * b[ix]
                    assert num % 2 == 0
                    total += sz * (num // 2) * specht_char(sh, part)
                assert total % 120 == 0
                if total:
                    multiplicities[sh] = total // 120
            tag = (deg, '+' if parity == 0 else '-')
            assert multiplicities == expected[tag], (tag, multiplicities)
            print('IRREP', tag, multiplicities)
    for name, subset in [('all', [(t, z) for t in parts for z in (0, 1)]),
                         ('rotations_S5', [(t, 0) for t in parts]),
                         ('central_C2', [((1, 1, 1, 1, 1), z) for z in (0, 1)])]:
        size = sum(classes[c][0] for c in subset)
        b = tuple(sum(classes[c][0] * classes[c][1][j] for c in subset) // size for j in (3, 4))
        expected_b = {'all': (0, 0), 'rotations_S5': (0, 0), 'central_C2': (6, 15)}[name]
        assert b == expected_b
        print('QUOTIENT', name, (1,) + b)
    print('DESARGUES_B2_FULL_S5_C2_SPECHT_CHECKS_OK')


if __name__ == '__main__':
    main()
