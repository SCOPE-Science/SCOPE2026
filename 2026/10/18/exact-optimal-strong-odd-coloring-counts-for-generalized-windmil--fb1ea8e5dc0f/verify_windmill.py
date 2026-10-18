"""Finite independent checks of strong-odd colorings on clique windmills.

All choices of distinct colors on a blade correspond to one r-subset of
noncentral colors, with r! orders. Parity at the common hub is the XOR of
subset masks. The verifier compares independent subset-XOR dynamic
programming with a signed binomial transform and checks actual vertices.
"""
from math import comb, factorial
from itertools import combinations


def palette_size(r, t):
    assert r >= 2 and t >= 1
    return r if t % 2 else 2 * ((r * t + 2 * (t - 1) - 1) // (2 * (t - 1)))


def transform_count(r, t, p):
    total = 0
    for j in range(p + 1):
        krawtchouk = sum((-1) ** h * comb(j, h) * comb(p - j, r - h)
                         for h in range(max(0, r - p + j), min(j, r) + 1))
        total += (-1) ** j * comb(p, j) * krawtchouk ** t
    assert total % (1 << p) == 0
    return total // (1 << p)


def xor_dp_count(r, t, p):
    masks = [sum(1 << i for i in group) for group in combinations(range(p), r)]
    v = [0] * (1 << p)
    v[0] = 1
    for _ in range(t):
        nxt = [0] * (1 << p)
        for state, count in enumerate(v):
            if count:
                for mask in masks:
                    nxt[state ^ mask] += count
        v = nxt
    return v[-1]


def cyclic_witness(r, t, p):
    if t % 2:
        sets = [list(range(p)) for _ in range(t)]
    else:
        counts = [1] * p
        to_add = (r * t - p) // 2
        for i in range(p):
            take = min(to_add, (t - 2) // 2)
            counts[i] += 2 * take
            to_add -= take
        assert to_add == 0
        sets = [[] for _ in range(t)]
        k = 0
        for color, multiplicity in enumerate(counts):
            for _ in range(multiplicity):
                sets[k % t].append(color)
                k += 1
    assert all(len(s) == r and len(set(s)) == r for s in sets)
    assert all(sum(color in s for s in sets) % 2 == 1 for color in range(p))
    # Check properness and every neighborhood explicitly on the graph.
    # Hub has color p, vertex (blade, index) has the indicated color.
    vertices = [('hub', 0)] + [(blade, i) for blade in range(t) for i in range(r)]
    names = {('hub', 0): p}
    names.update({(blade, i): sets[blade][i] for blade in range(t) for i in range(r)})
    def adjacent(a, b):
        if a == b: return False
        if a[0] == 'hub' or b[0] == 'hub': return True
        return a[0] == b[0]
    for a in vertices:
        counts_here = {}
        for b in vertices:
            if adjacent(a, b):
                assert names[a] != names[b]
                counts_here[names[b]] = counts_here.get(names[b], 0) + 1
        assert all(mult % 2 for mult in counts_here.values())


def run():
    cases = 0
    print('r,t,p,ordered_subset_tuples,named_optimum_colorings')
    for r in range(2, 6):
        for t in range(1, 9):
            p = palette_size(r, t)
            cyclic_witness(r, t, p)
            if p <= 10 and comb(p, r) * (1 << p) * t < 4000000:
                for candidate in range(r, p):
                    assert xor_dp_count(r, t, candidate) == 0
                via_dp = xor_dp_count(r, t, p)
                via_transform = transform_count(r, t, p)
                assert via_dp == via_transform > 0, (r, t, p, via_dp, via_transform)
                named = (p + 1) * factorial(r) ** t * via_dp
                print(f'{r},{t},{p},{via_dp},{named}')
                cases += 1
    assert cases >= 15
    print('PASS', cases, 'exact finite cases; independent graph witnesses for all 32 profiles')

if __name__ == '__main__':
    run()
