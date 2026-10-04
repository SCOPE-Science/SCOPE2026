from fractions import Fraction
from itertools import product

def suffix_max(xs):
    out = [None] * len(xs)
    cur = None
    for i in range(len(xs) - 1, -1, -1):
        cur = xs[i] if cur is None or xs[i] > cur else cur
        out[i] = cur
    return out

def prefix_min(xs):
    out = []
    cur = None
    for x in xs:
        cur = x if cur is None or x < cur else cur
        out.append(cur)
    return out

def compatible(lo, hi):
    return all(a <= b for a, b in zip(suffix_max(lo), prefix_min(hi)))

def exact_bounds(lo, hi):
    assert compatible(lo, hi)
    return suffix_max(lo), prefix_min(hi)

def direct_grid_bounds(lo, hi, grid):
    feas = []
    for g in product(grid, repeat=len(lo)):
        if all(lo[i] <= g[i] <= hi[i] for i in range(len(lo))) and all(g[i] >= g[i+1] for i in range(len(lo)-1)):
            feas.append(g)
    if not feas:
        return None
    lows = [min(g[i] for g in feas) for i in range(len(lo))]
    highs = [max(g[i] for g in feas) for i in range(len(lo))]
    return lows, highs

grid = [Fraction(k, 2) for k in range(-2, 5)]
for R in (2, 3):
    intervals = [(a, b) for a in grid for b in grid if a <= b]
    for box in product(intervals, repeat=R):
        lo = [x[0] for x in box]
        hi = [x[1] for x in box]
        form_ok = compatible(lo, hi)
        brute = direct_grid_bounds(lo, hi, grid)
        assert form_ok == (brute is not None)
        if form_ok:
            f_lo, f_hi = exact_bounds(lo, hi)
            b_lo, b_hi = brute
            assert f_lo == b_lo
            assert f_hi == b_hi

taus = [Fraction(1, 2), Fraction(1, 4), Fraction(0)]
for R in (2, 3):
    tau = taus[:R]
    intervals = [(a, b) for a in grid for b in grid if a <= b]
    for box in product(intervals, repeat=R):
        lo_gamma = [x[0] for x in box]
        hi_gamma = [x[1] for x in box]
        lo = [lo_gamma[i] + tau[i] for i in range(R)]
        hi = [hi_gamma[i] + tau[i] for i in range(R)]
        if not compatible(lo, hi):
            continue
        low_g, high_g = exact_bounds(lo, hi)
        possible_formula = all(x <= 0 for x in lo_gamma)
        possible_order = all(low_g[i] <= tau[i] for i in range(R))
        assert possible_formula == possible_order
        certified_formula = all(high_g[i] <= tau[i] for i in range(R))
        assert certified_formula == all(prefix_min(hi)[i] <= tau[i] for i in range(R))

tau = [Fraction(1, 5), Fraction(1, 10)]
A_lo_gamma = [Fraction(-4, 25), Fraction(-1, 10)]
A_hi_gamma = [Fraction(-3, 25), Fraction(1, 5)]
B_lo_gamma = [Fraction(-1, 20), Fraction(-1, 20)]
B_hi_gamma = [Fraction(1, 5), Fraction(1, 5)]

def status(lo_gamma, hi_gamma):
    lo = [lo_gamma[i] + tau[i] for i in range(2)]
    hi = [hi_gamma[i] + tau[i] for i in range(2)]
    assert compatible(lo, hi)
    _, high_g = exact_bounds(lo, hi)
    possible = all(x <= 0 for x in lo_gamma)
    rect_cert = all(x <= 0 for x in hi_gamma)
    iso_cert = all(high_g[i] <= tau[i] for i in range(2))
    return possible, rect_cert, iso_cert, high_g

A = status(A_lo_gamma, A_hi_gamma)
B = status(B_lo_gamma, B_hi_gamma)
assert A[0] and not A[1] and A[2]
assert B[0] and not B[1] and not B[2]
assert A[3][1] == Fraction(2, 25)
assert A[3][1] - tau[1] == Fraction(-1, 50)

cost = {"A": Fraction(1), "B": Fraction(2)}
possible = {"A": A[0], "B": B[0]}
rect_cert = {"A": A[1], "B": B[1]}
iso_cert = {"A": A[2], "B": B[2]}

def projected(cert):
    cert_costs = [cost[m] for m in cost if cert[m]]
    q = min(cert_costs) if cert_costs else None
    if q is None:
        return {m for m in cost if possible[m]}
    return {m for m in cost if possible[m] and cost[m] <= q}

assert projected(rect_cert) == {"A", "B"}
assert projected(iso_cert) == {"A"}

print("VERIFY_OK")
