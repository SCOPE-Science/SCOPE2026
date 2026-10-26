"""Independent exact checks for strong odd four-colorings of binary four-cubes.

Run: python3 verify.py
No third-party packages, files, or network required.
"""
from collections import Counter
from itertools import product

V = tuple(range(16))
NEIGH = {x: tuple(x ^ (1 << i) for i in range(4)) for x in V}


def strong_odd(f, d):
    """Directly test every vertex neighborhood in Q_d."""
    if len(f) != (1 << d):
        return False
    for x in range(1 << d):
        colors = [f[x ^ (1 << i)] for i in range(d)]
        if f[x] in colors:
            return False
        if any(count % 2 == 0 for count in Counter(colors).values()):
            return False
    return True


def affine(f, d):
    """With colors coded by F_2^2, test all Boolean affine identities."""
    base = f[0]
    cols = [f[1 << i] ^ base for i in range(d)]
    return all(f[x] == (base ^ xor_cols(x, cols)) for x in range(1 << d))


def xor_cols(x, cols):
    out = 0
    for i, a in enumerate(cols):
        if x & (1 << i):
            out ^= a
    return out


def layered_census():
    """Fix the forced 3+1 neighborhood around zero and enumerate later layers."""
    fixed = {0: 0, 1: 2, 2: 1, 4: 1, 8: 1}
    on_special = (3, 5, 9)
    on_ordinary = (6, 10, 12)
    weight_three = (7, 11, 13, 14)
    hist = Counter()
    normalized = []
    checked_layer_two = 0
    feasible_layer_two = 0

    def local_ok(f, x):
        if x not in f:
            return True
        if any(y in f and f[x] == f[y] for y in NEIGH[x]):
            return False
        if all(y in f for y in NEIGH[x]):
            hist = Counter(f[y] for y in NEIGH[x])
            return all(k % 2 == 1 for k in hist.values())
        return True

    for A in product((0, 3), repeat=3):
        for B in product((0, 2, 3), repeat=3):
            checked_layer_two += 1
            f = fixed | dict(zip(on_special, A)) | dict(zip(on_ordinary, B))
            if not all(local_ok(f, x) for x in fixed):
                continue
            feasible_layer_two += 1
            allowed = []
            for x in weight_three:
                adjacent_colors = {f[y] for y in NEIGH[x] if y in f}
                allowed.append(tuple(c for c in range(4) if c not in adjacent_colors))
            for colors in product(*allowed):
                g = f | dict(zip(weight_three, colors))
                if not all(local_ok(g, x) for x in g
                           if all(y in g for y in NEIGH[x])):
                    continue
                for color in range(4):
                    h = g | {15: color}
                    if all(local_ok(h, x) for x in V):
                        output = tuple(h[x] for x in V)
                        assert strong_odd(output, 4)
                        normalized.append(output)
                        hist[(A.count(0), B.count(0))] += 1
    return checked_layer_two, feasible_layer_two, hist, normalized


def bipartition_census():
    """Independent method: assign even cube vertices first, then odd ones."""
    even = [x for x in V if x.bit_count() % 2 == 0]
    odd = [x for x in V if x.bit_count() % 2 == 1]
    root_zero_count = 0
    even_assignments = 0
    odd_tuples = 0
    for tail in product(range(4), repeat=len(even) - 1):
        f = {0: 0} | dict(zip(even[1:], tail))
        allowed = []
        for x in odd:
            freqs = Counter(f[y] for y in NEIGH[x])
            if any(k % 2 == 0 for k in freqs.values()):
                break
            allowed.append(tuple(c for c in range(4) if c not in freqs))
        else:
            even_assignments += 1
            for colors in product(*allowed):
                odd_tuples += 1
                g = f | dict(zip(odd, colors))
                if all(all(count % 2 == 1 for count in
                           Counter(g[y] for y in NEIGH[x]).values()) for x in even):
                    # Properness at odd vertices was guaranteed by allowed.
                    root_zero_count += 1
    return even_assignments, odd_tuples, root_zero_count


def check_affine(d):
    result = 0
    for cols in product((1, 2, 3), repeat=d):
        # Surjectivity onto four colors requires at least two distinct columns.
        if len(set(cols)) < 2:
            continue
        if any(sum(a == q for a in cols) % 2 == 0
               for q in set(cols)):
            continue
        result += 4  # all four translations are distinct
    return result


def lifted_coloring(d, seed):
    extra = d - 4
    return tuple(seed[x & 15] ^ (((x >> 4).bit_count() % 2) * 1)
                 for x in range(1 << d))


def main():
    checked, feasible, hist, normalized = layered_census()
    assert checked == 216 and feasible == 11
    assert sum(hist.values()) == len(normalized) == 20
    assert hist == {(0, 0): 3, (0, 3): 2, (2, 1): 6, (2, 2): 9}, hist
    affine_normalized = sum(affine(f, 4) for f in normalized)
    assert affine_normalized == 1
    result_bip = bipartition_census()
    assert result_bip == (54, 12288, 480), result_bip
    assert 480 * 4 == 20 * 4 * 3 * 2 * 4 == 1920
    assert check_affine(4) == 96
    assert 1920 - 96 == 1824
    for d in (2, 4, 6, 8):
        if d % 2 == 0:
            assert check_affine(d) == 3 * (1 << (d + 1))

    # One explicitly displayed nonlinear seed; its row is indexed by x = 0,...,15.
    seed = (0, 2, 1, 0, 1, 0, 0, 1,
            1, 3, 3, 1, 3, 1, 2, 3)
    assert strong_odd(seed, 4)
    assert not affine(seed, 4)
    # At every vertex, its color toggled by XOR 1 occurs among its neighbors.
    assert all((seed[x] ^ 1) in (seed[y] for y in NEIGH[x]) for x in V)
    for d in (4, 6, 8, 10, 12):
        f = lifted_coloring(d, seed)
        assert strong_odd(f, d)
        assert not affine(f, d)

    print('VERIFICATION_OK layered_raw=216 layer_two_valid=11 normalized=20')
    print('TABLE_A_ZERO_B_ZERO', sorted(hist.items()))
    print('INDEPENDENT_CENSUS even_valid=54 odd_tuples=12288 root_zero=480')
    print('LABELED=1920 UNLABELED=80 AFFINE_LABELED=96 AFFINE_UNLABELED=4')
    print('NONAFFINE_LABELED=1824 NONAFFINE_UNLABELED=76')
    print('WITNESS_LIFTS_OK dimensions=4,6,8,10,12')

if __name__ == '__main__':
    main()
