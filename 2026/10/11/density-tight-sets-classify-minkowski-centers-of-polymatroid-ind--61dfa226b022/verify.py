"""Exact finite corroboration of asymmetry and center geometry for polymatroid independence polytopes."""
from fractions import Fraction as F
from itertools import combinations, permutations
from random import Random


def independent_rank(columns, subset):
    basis = {}
    for i, col in enumerate(columns):
        if not (subset >> i) & 1:
            continue
        v = col
        while v:
            p = v.bit_length() - 1
            if p in basis:
                v ^= basis[p]
            else:
                basis[p] = v
                break
    return len(basis)


def matroid_rank(columns):
    return tuple(F(independent_rank(columns, s)) for s in range(1 << len(columns)))


def combine_rank(first, second, p, q, modular):
    n = len(modular)
    return tuple(p * first[s] + q * second[s] + sum(modular[i] for i in range(n) if (s >> i) & 1)
                 for s in range(1 << n))


def face_sum(x, s):
    return sum((z for i, z in enumerate(x) if (s >> i) & 1), F(0))


def greedy_vertices(f, n):
    seen = set()
    for perm in permutations(range(n)):
        x = [F(0)] * n
        s = 0
        for length in range(n + 1):
            seen.add(tuple(x))
            if length == n:
                break
            i = perm[length]
            new_s = s | (1 << i)
            x[i] = f[new_s] - f[s]
            s = new_s
    return seen


def test(f, n):
    masks = range(1, 1 << n)
    w = [f[1 << i] for i in range(n)]
    assert all(z > 0 for z in w)
    assert f[0] == 0
    assert all(f[s] <= f[t] for s in range(1 << n) for t in range(1 << n) if s & t == s)
    assert all(f[a] + f[b] >= f[a | b] + f[a & b] for a in range(1 << n) for b in range(1 << n))
    ratios = {s: face_sum(w, s) / f[s] for s in masks}
    rho = max(ratios.values())
    tight = {s for s in masks if ratios[s] == rho}
    U = 0
    for s in tight: U |= s
    assert U in tight
    h = lambda s: rho * f[s] - face_sum(w, s)
    R = ((1 << n) - 1) ^ U
    assert (U == (1 << n) - 1) == (rho == face_sum(w, (1 << n) - 1) / f[(1 << n) - 1])
    for s in range(1 << n):
        if s & U == 0 and s:
            assert h(U | s) > 0
        if s & U == 0:
            for t in range(1 << n):
                if t & U == 0:
                    assert h(U | s) + h(U | t) >= h(U | (s | t)) + h(U | (s & t))
    assert all((a | b in tight and (a & b == 0 or a & b in tight)) for a in tight for b in tight)
    c = tuple(z / (rho + 1) for z in w)
    vertices = greedy_vertices(f, n)
    allc = [c]
    for i in range(n):
        if U >> i & 1:
            continue
        delta = min((rho * f[s] - face_sum(w, s)) / (rho + 1)
                    for s in masks if (s >> i) & 1)
        assert delta > 0
        temp = list(c); temp[i] += delta / 2
        allc.append(tuple(temp))
    for cc in allc:
        for x in vertices:
            y = tuple((rho + 1) * cc[i] - x[i] for i in range(n))
            assert all(z >= 0 for z in y)
            assert all(face_sum(y, s) <= rho * f[s] for s in masks)
    for s in masks:
        if s in tight:
            assert all(c[i] == w[i] / (rho + 1) for i in range(n) if (s >> i) & 1)
    return len(vertices), len(allc), rho, U


def main():
    rng = Random(20491)
    total = total_centers = 0
    example = []
    cases = 0
    for n in range(1, 6):
        for j in range(22):
            columns1 = [rng.randint(1, (1 << max(1, n - 1)) - 1) for _ in range(n)]
            columns2 = [rng.randint(1, (1 << max(1, n - 1)) - 1) for _ in range(n)]
            f = combine_rank(matroid_rank(columns1), matroid_rank(columns2), F(rng.randint(1, 4), 2),
                             F(rng.randint(1, 3), 3), [F(rng.randint(0, 3), 4) for _ in range(n)])
            verts, centers, rho, U = test(f, n)
            total += verts
            total_centers += centers
            cases += 1
            if n == 4 and len(example) < 6:
                example.append((str(rho), bin(U), 4 - U.bit_count()))
    # Distinct graphic example: a triangle plus a bridge has a one-dimensional center set.
    graph_edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
    f = []
    for mask in range(16):
        par = list(range(4))
        def root(v):
            while v != par[v]: v = par[v]
            return v
        for i, (a, b) in enumerate(graph_edges):
            if mask & (1 << i):
                ra, rb = root(a), root(b)
                if ra != rb: par[ra] = rb
        f.append(F(len(set(root(i) for i in range(4)))))
    f = tuple(F(4) - k for k in f)
    v, c, rho, U = test(f, 4)
    assert rho == F(3, 2) and U == 7 and c == 2
    print('EXACT_VERIFY_PASS', 'polymatroids', cases, 'greedy_vertices_checked', total,
          'centers_checked', total_centers, 'triangle_bridge_density', str(rho),
          'triangle_bridge_free_coordinates', 4-U.bit_count())
    print('SAMPLE', example)


if __name__ == '__main__':
    main()
