from fractions import Fraction
from itertools import product


def coeffs(panel_counts):
    xs = [Fraction(1, n*n) for n in panel_counts]
    out = []
    for k, xk in enumerate(xs):
        c = Fraction(1)
        for j, xj in enumerate(xs):
            if j != k:
                c *= -xj / (xk - xj)
        out.append(c)
    return out


def collected_weights(panel_counts):
    cs = coeffs(panel_counts)
    nd = panel_counts[-1]
    ws = []
    for i in range(nd + 1):
        w = Fraction(0)
        for c, n in zip(cs, panel_counts):
            stride = nd // n
            if i % stride == 0:
                w += c * Fraction(1, n) * (Fraction(1, 2) if i in (0, nd) else 1)
        ws.append(w)
    return cs, ws


def max_formula(panel_counts):
    nd = panel_counts[-1]
    p = Fraction(1, nd)
    for n in panel_counts[:-1]:
        p /= (1 - Fraction(n*n, nd*nd))
    return p


def moment(ws, power):
    n = len(ws) - 1
    return sum(w * Fraction(i, n) ** power for i, w in enumerate(ws))

# Mixed nested example: refinement factors 2 then 3.
cs, ws = collected_weights([1, 2, 6])
assert cs == [Fraction(1,105), Fraction(-1,6), Fraction(81,70)]
assert ws == [Fraction(5,84), Fraction(27,140), Fraction(27,140), Fraction(23,210), Fraction(27,140), Fraction(27,140), Fraction(5,84)]
assert max(ws) == Fraction(27,140) == max_formula([1,2,6])

# Exact finite corroboration across many variable nested chains.
chains = []
for depth in range(1,5):
    for ratios in product((2,3,4), repeat=depth):
        ns = [1]
        for r in ratios:
            ns.append(ns[-1]*r)
        chains.append(ns)
chains += [[2,6,12], [3,6,24,48], [1,5,10,30,120], [2,4,20,40,120]]

for ns in chains:
    cs, ws = collected_weights(ns)
    assert all(w > 0 for w in ws)
    assert sum(ws) == 1
    assert max(ws) == max_formula(ns)
    # Richardson cancellation gives exactness through degree 2d+1.
    d = len(ns) - 1
    for p in range(2*d + 2):
        assert moment(ws, p) == Fraction(1, p+1)
    # Signs alternate and |c_k| h_k grows strictly.
    bs = [abs(c) * Fraction(1,n) for c,n in zip(cs,ns)]
    assert all(bs[i+1] > bs[i] for i in range(len(bs)-1))
    assert all((c > 0) == (((d-k) % 2) == 0) for k,c in enumerate(cs))

# Nonnested boundary example: T_1, T_2, T_5 on [0,1].
cs = coeffs([1,2,5])
assert cs == [Fraction(1,72), Fraction(-16,63), Fraction(625,504)]
# x=1/2 occurs only in T_2 among these three grids, hence has negative weight.
midpoint_weight = cs[1] * Fraction(1,2)
assert midpoint_weight == Fraction(-8,63)

print('VERIFY_OK')
print('nested_chains_checked=', len(chains))
print('mixed_chain_max_weight=', max_formula([1,2,6]))
print('nonnested_midpoint_weight=', midpoint_weight)
