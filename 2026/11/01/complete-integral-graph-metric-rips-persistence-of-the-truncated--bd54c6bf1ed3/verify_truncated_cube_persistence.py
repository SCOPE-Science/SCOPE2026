#!/usr/bin/env python3
"""Exact integral cellular cancellations and mod-two persistence for the 24-vertex truncated-cube graph.

Run with Python 3.10 or later; the Python standard library is sufficient.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
import heapq

VERTICES = tuple(range(24))  # encode (cube vertex x, incident coordinate i) as 3*x+i
EDGES = set()
for x in range(8):
    for i, j in combinations(range(3), 2):
        EDGES.add(tuple(sorted((3*x+i, 3*x+j))))
    for i in range(3):
        EDGES.add(tuple(sorted((3*x+i, 3*(x ^ (1 << i))+i))))
assert len(EDGES) == 36
ADJ = [set() for _ in VERTICES]
for u, v in EDGES:
    ADJ[u].add(v); ADJ[v].add(u)
assert all(len(a) == 3 for a in ADJ)

DIST = []
for v in VERTICES:
    ds = {v: 0}; queue = [v]
    for x in queue:
        for y in sorted(ADJ[x]):
            if y not in ds:
                ds[y] = ds[x]+1; queue.append(y)
    assert len(ds) == 24
    DIST.append(tuple(ds[j] for j in VERTICES))
assert max(map(max, DIST)) == 6
assert all([j for j in VERTICES if DIST[i][j] == 6] == [3*(7 ^ (i//3)) + i%3] for i in VERTICES)


def boundary(f):
    result = {}; z = f; pos = 0
    while z:
        bit = z & -z; z -= bit
        if f != bit: result[f-bit] = 1 if pos % 2 == 0 else -1
        pos += 1
    return result


def maximal_cliques(radius):
    neighbors = []
    for i in VERTICES:
        neighbors.append(sum(1 << j for j in VERTICES if j != i and DIST[i][j] <= radius))
    out = []
    def rec(R, P, X):
        if not (P | X):
            out.append(R); return
        ux = P | X
        pivot = (ux & -ux).bit_length()-1
        # Bron-Kerbosch with pivoting; the clique graph has at most 24 vertices.
        candidates = P & ~neighbors[pivot]
        while candidates:
            bit = candidates & -candidates; candidates -= bit
            v = bit.bit_length()-1
            rec(R | bit, P & neighbors[v], X & neighbors[v])
            P -= bit; X |= bit
    rec(0, (1 << 24)-1, 0)
    return out


def faces_at(radius):
    if radius == 0:
        return set(1 << i for i in VERTICES)
    faces = set()
    for maximal in maximal_cliques(radius):
        sub = maximal
        while sub:
            faces.add(sub); sub = (sub-1) & maximal
    return faces


def simplex_collapses(faces):
    left = set(faces)
    upper = defaultdict(set)
    for f in left:
        for q in boundary(f): upper[q].add(f)
    heap = []
    for f in left:
        if len(upper[f]) == 1: heapq.heappush(heap, (-f.bit_count(), f))
    pairs = []
    while heap:
        _, s = heapq.heappop(heap)
        if s not in left or len(upper[s]) != 1: continue
        t = next(iter(upper[s]))
        assert t in left and t.bit_count() == s.bit_count()+1
        assert abs(boundary(t)[s]) == 1
        for f in (s, t):
            for q in boundary(f):
                if q in left:
                    upper[q].discard(f)
                    if len(upper[q]) == 1: heapq.heappush(heap, (-q.bit_count(), q))
            left.remove(f)
        pairs.append((s, t))
    assert len(left) + 2*len(pairs) == len(faces)
    return left, pairs


class IntegralComplex:
    def __init__(self, faces):
        self.faces = set(faces)
        self.d = {f: boundary(f) for f in self.faces}
        self.upper = defaultdict(set)
        for f, bd in self.d.items():
            for q in bd:
                assert q in self.faces
                self.upper[q].add(f)

    def cancel(self, s, t):
        """Integral chain contraction at the unit incident coefficient [t:s]."""
        assert s in self.faces and t in self.faces
        dt = self.d[t]; a = dt[s]
        assert a in (1, -1)
        sources = {u: self.d[u][s] for u in self.upper[s] if u != t}
        for u, value in sources.items():
            col = self.d[u]; factor = value*a
            for row, x in dt.items():
                y = col.get(row, 0)-factor*x
                if y:
                    col[row] = y; self.upper[row].add(u)
                else:
                    col.pop(row, None); self.upper[row].discard(u)
        for row in dt: self.upper[row].discard(t)
        for row in self.d[s]: self.upper[row].discard(s)
        for u in list(self.upper[t]): self.d[u].pop(t, None)
        self.upper.pop(s, None); self.upper.pop(t, None)
        del self.d[s], self.d[t]
        self.faces.remove(s); self.faces.remove(t)
        return (s, t, a, dict(dt), sources)

    def verify_d_squared(self):
        for f, d in self.d.items():
            composition = Counter()
            for q, c in d.items():
                assert q in self.d
                for z, b in self.d[q].items(): composition[z] += c*b
            assert all(v == 0 for v in composition.values())


def reduced(radius):
    full = faces_at(radius)
    core, elementary = simplex_collapses(full)
    steps = []
    for s, t in elementary:
        dt = boundary(t)
        steps.append((s, t, dt[s], dt, {}))
    reduced_chain = IntegralComplex(core)
    algebraic_count = 0
    while True:
        best = None; best_score = 10**20
        for t, bd in reduced_chain.d.items():
            for s, a in bd.items():
                if abs(a) != 1: continue
                score = (len(reduced_chain.upper[s])-1)*(len(bd)-1)
                if score < best_score:
                    best, best_score = (s, t), score
                    if score == 0: break
            if best_score == 0: break
        if best is None: break
        steps.append(reduced_chain.cancel(*best)); algebraic_count += 1
    reduced_chain.verify_d_squared()
    assert not any(reduced_chain.d.values())
    assert len(full) == 2*len(steps)+len(reduced_chain.faces)
    return full, reduced_chain, steps, len(elementary), algebraic_count


def lift(cycle, steps):
    """Chain inclusion from the final reduced basis to the original basis."""
    vector = {cycle: 1}
    for s, t, a, dt, sources in reversed(steps):
        term = sum(vector.get(q, 0)*b for q, b in sources.items())
        if term:
            vector[t] = vector.get(t, 0)-term*a
            if vector[t] == 0: del vector[t]
    return vector


def project(vector, steps):
    """Chain projection onto final reduced basis (reverse of contraction)."""
    vector = dict(vector)
    for s, t, a, dt, sources in steps:
        vector.pop(t, None)
        bs = vector.pop(s, 0)
        if bs:
            for q, b in dt.items():
                if q == s: continue
                z = vector.get(q, 0)-bs*b*a
                if z: vector[q] = z
                else: vector.pop(q, None)
    return vector


def check_cycle(vector):
    result = Counter()
    for f, c in vector.items():
        for q, b in boundary(f).items(): result[q] += c*b
    return all(v == 0 for v in result.values())


def determinant(a):
    n = len(a)
    result = 0
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = 1 if inversions % 2 == 0 else -1
        for i in range(n): term *= a[i][p[i]]
        result += term
    return result


def birth(f):
    vertices = []
    while f:
        a = f & -f; f -= a; vertices.append(a.bit_length()-1)
    return max((DIST[i][j] for i, j in combinations(vertices, 2)), default=0)


def independent_mod2_barcode(full4):
    ss = sorted(full4, key=lambda f: (birth(f), f.bit_count(), f))
    indices = {f: i for i, f in enumerate(ss)}
    bd = [birth(f) for f in ss]
    pivots = {}; pairs = []; cycle_births = set()
    for j, f in enumerate(ss):
        x = 0
        for q in boundary(f): x ^= 1 << indices[q]
        while x:
            k = x.bit_length()-1
            if k in pivots: x ^= pivots[k]
            else:
                pivots[k] = x; pairs.append((k, j)); break
        if not x: cycle_births.add(j)
    paired = {i for i, j in pairs}
    nonzero_intervals = Counter((ss[i].bit_count()-1, bd[i], bd[j]) for i, j in pairs if bd[i] != bd[j])
    unpaired = Counter((ss[i].bit_count()-1, bd[i]) for i in cycle_births-paired)
    return nonzero_intervals, unpaired


def main():
    expected = {
        1: (68, {0: 1, 1: 5}, 31),
        2: (212, {0: 1, 1: 5}, 103),
        3: (1092, {0: 1, 2: 1, 3: 6}, 542),
        4: (19442, {0: 1, 3: 1, 5: 2}, 9719),
    }
    data = {}
    for r in (1, 2, 3, 4):
        full, chain, steps, elementary, algebraic = reduced(r)
        assert len(full) == expected[r][0]
        critical = dict(sorted(Counter(f.bit_count()-1 for f in chain.faces).items()))
        assert critical == expected[r][1]
        assert len(steps) == expected[r][2]
        data[r] = (chain, steps)
        print('scale', r, 'faces', len(full), 'elementary', elementary,
              'integral_unit_cancellations', algebraic, 'integral_betti', critical)
    for r in (1, 2, 3):
        source, steps0 = data[r]; target, steps1 = data[r+1]
        for k in sorted(set(f.bit_count()-1 for f in source.faces)):
            if k == 0: continue
            columns = sorted(f for f in source.faces if f.bit_count()-1 == k)
            rows = sorted(f for f in target.faces if f.bit_count()-1 == k)
            matrix_columns = []
            for f in columns:
                v = lift(f, steps0)
                assert check_cycle(v)
                projected = project(v, steps1)
                assert set(projected) <= target.faces
                assert all(x.bit_count()-1 == k for x in projected)
                matrix_columns.append(projected)
            matrix = [[d.get(g, 0) for d in matrix_columns] for g in rows]
            print('inclusion', r, 'to', r+1, 'degree', k, 'matrix', matrix)
            if r == 1 and k == 1:
                assert determinant(matrix) in (1, -1)
                print('degree_one_unimodular_determinant', determinant(matrix))
            if r == 3:
                assert all(all(v == 0 for v in row) for row in matrix)
    assert all(len([j for j in VERTICES if DIST[i][j] == 6]) == 1 for i in VERTICES)
    # At scale five, the only forbidden edges are twelve disjoint antipodal pairs.
    # Their clique complex is the 12-fold join of the 0-sphere, namely S^11.
    bars, unpaired = independent_mod2_barcode(faces_at(4))
    assert bars == Counter({(0, 0, 1): 23, (1, 1, 3): 5, (2, 3, 4): 1, (3, 3, 4): 6})
    assert unpaired == Counter({(0, 0): 1, (3, 4): 1, (5, 4): 2})
    print('independent_mod_two_finite_bars_to_scale_four', sorted(bars.items()))
    print('independent_mod_two_live_at_scale_four', sorted(unpaired.items()))
    print('scale_five_sphere_dimension', 11, 'scale_six_contractible', True)
    print('TRUNCATED_CUBE_INTEGRAL_PERSISTENCE_VERIFIED')


if __name__ == '__main__': main()
