"""Exact finite-space mapping-poset collapse certificate checker.

Usage: python3 verify.py
Reads `collapse_certificate.txt` from the same directory. No dependencies
outside the Python standard library. Indexing is deterministically generated.
"""
from itertools import product
from pathlib import Path

C = tuple(range(4))
CYCLE = (0, 2, 1, 3, 0)


def le_c(a, b):
    return a == b or (a < 2 and b >= 2)


def le_t(a, b):
    return all(le_c(x, y) for x, y in zip(a, b))


def comps(vertices, selected):
    """Components of the induced comparability graph, in fixed index order."""
    seen = set()
    result = []
    for i in selected:
        if i in seen:
            continue
        seen.add(i)
        stack = [i]
        comp = []
        while stack:
            j = stack.pop()
            comp.append(j)
            for k in selected:
                if k not in seen and (le_t(vertices[j], vertices[k])
                                      or le_t(vertices[k], vertices[j])):
                    seen.add(k)
                    stack.append(k)
        result.append(tuple(comp))
    return result


def enumerate_maps():
    """All isotone maps from the product circle to the circle, once each."""
    tt = tuple(product(C, repeat=2))
    n = len(tt)
    lower = [sum(1 << j for j, q in enumerate(tt) if le_t(q, x))
             for x in tt]
    index = tuple(range(n))
    maps = []
    ideals = 0
    profile = {}
    for mask in range(1 << n):
        if any(mask & (1 << i) and (mask & lower[i]) != lower[i]
               for i in index):
            continue
        ideals += 1
        down = tuple(i for i in index if mask & (1 << i))
        up = tuple(i for i in index if not mask & (1 << i))
        cs_down = comps(tt, down)
        cs_up = comps(tt, up)
        cs = cs_down + cs_up
        signature = (len(cs_down), len(cs_up))
        profile[signature] = profile.get(signature, 0) + 1
        for coloring in product((0, 1), repeat=len(cs)):
            h = [None] * n
            for j, comp in enumerate(cs):
                color = coloring[j] + (0 if j < len(cs_down) else 2)
                for i in comp:
                    h[i] = color
            maps.append(tuple(h))
    return tt, maps, ideals, profile


def enumerate_maps_recursive(tt):
    """Independent exhaustive generation in a linear extension of the source."""
    assert len(tt) == 16
    predecessors = [tuple(j for j in range(i) if le_t(tt[j], tt[i]))
                    for i in range(16)]
    assert all(not le_t(tt[i], tt[j]) for i in range(16)
               for j in range(i) if i != j)
    maps = []
    current = []

    def visit(i):
        if i == 16:
            maps.append(tuple(current))
            return
        for value in C:
            if all(le_c(current[j], value) for j in predecessors[i]):
                current.append(value)
                visit(i + 1)
                current.pop()
    visit(0)
    return maps


def planes(h):
    """Bit planes: level (min/max), within-level choice."""
    return (sum((v >> 1) << i for i, v in enumerate(h)),
            sum((v & 1) << i for i, v in enumerate(h)))


def map_le(p, q, coord_mask=(1 << 16) - 1):
    hp, lp = p
    hq, lq = q
    return not (hp & ~hq) and not ((lp ^ lq) & ~(hp ^ hq) & coord_mask)


def degree(h):
    return sum((1 if (h[u], h[v]) == (0, 2)
                else -1 if (h[u], h[v]) == (2, 0) else 0)
               for u, v in zip(CYCLE, CYCLE[1:]))


def main():
    tt, maps, ideals, profile = enumerate_maps()
    n = len(maps)
    assert ideals == 430 and n == 2836 and len(set(maps)) == n
    expected_ideals = {(0, 1): 1, (1, 0): 1, (1, 1): 228,
                       (1, 2): 82, (1, 3): 16, (1, 4): 1,
                       (2, 1): 82, (2, 2): 2, (3, 1): 16,
                       (4, 1): 1}
    assert profile == expected_ideals
    assert sum(v * (2 ** (a + b)) for (a, b), v in profile.items()) == n
    assert set(maps) == set(enumerate_maps_recursive(tt))
    for h in maps:
        assert all(not le_t(a, b) or le_c(h[i], h[j])
                   for i, a in enumerate(tt) for j, b in enumerate(tt))

    endos = [h for h in product(C, repeat=4)
             if all(not le_c(a, b) or le_c(h[a], h[b])
                    for a in C for b in C)]
    autos = [h for h in endos if abs(degree(h)) == 1]
    assert len(endos) == 36 and len(autos) == 4
    projections = {tuple(alpha[point[axis]] for point in tt)
                   for axis in range(2) for alpha in autos}
    constants = {tuple(v for _ in tt) for v in C}
    assert len(projections) == 8 and len(constants) == 4

    encoded = [planes(h) for h in maps]
    greater = [0] * n
    lesser = [0] * n
    for i in range(n):
        pi = encoded[i]
        for j in range(i + 1, n):
            pj = encoded[j]
            if map_le(pi, pj):
                greater[i] |= 1 << j
                lesser[j] |= 1 << i
            if map_le(pj, pi):
                greater[j] |= 1 << i
                lesser[i] |= 1 << j

    certificate = Path(__file__).with_name('collapse_certificate.txt').read_text('utf-8')
    lines = certificate.splitlines()
    assert len(lines) == 2824
    alive = (1 << n) - 1
    for step, line in enumerate(lines, start=1):
        terms = line.split()
        assert len(terms) == 3, (step, line)
        i, witness = map(int, terms[:2])
        direction = terms[2]
        assert 0 <= i < n and 0 <= witness < n and i != witness
        assert (alive >> i) & 1 and (alive >> witness) & 1
        if direction == 'up':
            above = greater[i] & alive
            assert (above >> witness) & 1
            # Every surviving element above i is >= the witness.
            assert above & ~(greater[witness] | (1 << witness)) == 0, step
        elif direction == 'down':
            below = lesser[i] & alive
            assert (below >> witness) & 1
            # Every surviving element below i is <= the witness.
            assert below & ~(lesser[witness] | (1 << witness)) == 0, step
        else:
            raise AssertionError((step, direction))
        alive ^= 1 << i

    survivors = [i for i in range(n) if (alive >> i) & 1]
    assert len(survivors) == 12
    assert {maps[i] for i in survivors} == projections | constants
    for i in survivors:
        for j in survivors:
            if i == j:
                continue
            relation = ((greater[i] >> j) & 1) != 0
            if maps[i] in projections or maps[j] in projections:
                assert not relation
            else:
                assert relation == le_c(maps[i][0], maps[j][0])
    nonzero = 0
    for h in maps:
        homology = tuple(degree(tuple(h[tt.index((v, 0))] for v in C))
                         if axis == 0 else
                         degree(tuple(h[tt.index((0, v))] for v in C))
                         for axis in range(2))
        if homology != (0, 0):
            assert h in projections
            nonzero += 1
    assert nonzero == 8
    print('VERIFY_OK maps=2836 ideals=430 two_enumerations=true beat_deletions=2824 '
          'core=4_point_circle_plus_8_isolates nonzero_maps=8')


if __name__ == '__main__':
    main()
