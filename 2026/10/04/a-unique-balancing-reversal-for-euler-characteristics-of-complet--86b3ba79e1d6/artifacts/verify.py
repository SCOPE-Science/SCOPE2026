from itertools import combinations_with_replacement
from math import comb

def h2(vals):
    return sum(vals[i] * vals[j] for i in range(len(vals)) for j in range(i, len(vals)))

def euler_shifted(ds):
    xs = [d - 1 for d in ds]
    D = 1
    for d in ds:
        D *= d
    T = sum(xs)
    return D * (3 - 2 * T + h2(xs))

def euler_chern(ds):
    c = len(ds)
    S = sum(ds)
    D = 1
    for d in ds:
        D *= d
    c2_coeff = comb(c + 3, 2) - (c + 3) * S + h2(ds)
    return D * c2_coeff

def predicted_extrema(c, S):
    q, r = divmod(S, c)
    balanced = tuple(sorted([q] * (c - r) + [q + 1] * r))
    one_heavy = tuple([2] * (c - 1) + [S - 2 * (c - 1)])
    if c == 2 and S == 6:
        return (2, 4), (3, 3)
    return balanced, one_heavy

families = 0
tuples_checked = 0
moves_checked = 0
for c in range(2, 8):
    for S in range(2 * c, 2 * c + 19):
        fam = [ds for ds in combinations_with_replacement(range(2, S + 1), c) if sum(ds) == S]
        assert fam
        families += 1
        vals = []
        for ds in fam:
            a = euler_shifted(ds)
            b = euler_chern(ds)
            assert a == b
            vals.append((a, ds))
            tuples_checked += 1
            xs = [d - 1 for d in ds]
            for i in range(c):
                for j in range(i + 1, c):
                    x, y = xs[i], xs[j]
                    if x < y - 1:
                        ys = xs[:]
                        ys[i] += 1
                        ys[j] -= 1
                        before = a
                        after = euler_shifted(tuple(z + 1 for z in ys))
                        delta = y - x - 1
                        B = (x + 1) * (y + 1)
                        C = 3 - 2 * sum(xs) + h2(xs)
                        P = 1
                        for k, z in enumerate(xs):
                            if k not in (i, j):
                                P *= z + 1
                        assert after - before == P * delta * (C - B - delta)
                        if c == 2 and (x, y) == (1, 3):
                            assert after < before
                        else:
                            assert after > before
                        moves_checked += 1
        maxv = max(v for v, _ in vals)
        minv = min(v for v, _ in vals)
        max_ds = [ds for v, ds in vals if v == maxv]
        min_ds = [ds for v, ds in vals if v == minv]
        pmax, pmin = predicted_extrema(c, S)
        assert max_ds == [pmax], (c, S, max_ds, pmax)
        assert min_ds == [pmin], (c, S, min_ds, pmin)

assert euler_shifted((2, 4)) == 64
assert euler_shifted((3, 3)) == 63
print('VERIFY_OK', families, tuples_checked, moves_checked)
