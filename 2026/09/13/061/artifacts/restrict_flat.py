"""Correct restriction computation: restrict arrangement to flat X (as subspace), not to hyperplane.
Method: pick exact basis of X = ker of flat-defining normals; quotient coordinates;
traces of all hyperplanes not containing X give restricted arrangement (exact Fractions,
primitive canonical integer vectors). Then chi via shiarr.char_poly.
Checks the l=3,k=1 witness flat and the general Z-flat family.
"""
from fractions import Fraction
from shiarr import char_poly, show_poly, primitive_canon, rank_int, build_cone


def ker_basis(normals, d):
    # normals: list of int tuples spanning X^perp; X = common kernel; return int basis of X
    # exact elimination
    M = [list(map(Fraction, n)) for n in normals]
    n = len(M)
    # RREF to find pivot cols, free vars
    R = [row[:] for row in M]
    pivots = []
    prow = 0
    for c in range(d):
        piv = None
        for i in range(prow, n):
            if R[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        R[prow], R[piv] = R[piv], R[prow]
        f = R[prow][c]
        R[prow] = [x / f for x in R[prow]]
        for i in range(n):
            if i != prow and R[i][c] != 0:
                g = R[i][c]
                R[i] = [x - g * y for x, y in zip(R[i], R[prow])]
        pivots.append(c)
        prow += 1
    free = [c for c in range(d) if c not in pivots]
    # RREF rows: R[i] has pivot at pivots[i]
    basis = []
    for f in free:
        v = [Fraction(0)] * d
        v[f] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -R[i][f]
        # clear denominators -> int
        dens = [x.denominator for x in v]
        from math import gcd
        L = 1
        for x in dens:
            L = L * x // gcd(L, x)
        basis.append(tuple(int(x * L) for x in v))
    return basis


def restrict_to_flat(N, flat_idx, d):
    # flat defined by normals of N[t], t in flat_idx; X = their common kernel
    defs = [N[t][1] for t in flat_idx]
    r = rank_int([list(x) for x in defs]) if defs else 0
    dimX = d - r
    B = ker_basis(defs, d)
    assert len(B) == dimX
    out = []
    names = []
    for t, (name, n) in enumerate(N):
        if all(sum(Fraction(n[i]) * B[s][i] for i in range(d)) == 0 for s in range(dimX)):
            continue  # contains X
        rr = tuple(sum(Fraction(n[i]) * B[s][i] for i in range(d)) for s in range(dimX))
        out.append(primitive_canon(rr))
        names.append(name)
    seen = []
    for v in out:
        if v not in seen:
            seen.append(v)
    return seen, dimX


# ---- test 1: the l=3,k=1 witness flat X = V(x2-x3, z) i.e. {x2=x3, z=0}
l, k = 3, 1
N = build_cone(l, k)
d = l + 1
idx_x2x3_0 = next(t for t, (nm, n) in enumerate(N) if nm == 'x2-x3=0z')
idx_z = next(t for t, (nm, n) in enumerate(N) if nm == 'z=0')
R, dimX = restrict_to_flat(N, [idx_x2x3_0, idx_z], d)
print("witness flat: dimX =", dimX, "|R| =", len(R))
p = char_poly(R, dimX)
print("chi =", show_poly(p))
# deconed affine lines = R minus the z=0 trace
print("R vecs:", sorted(R))

# ---- test 2: general Z-flat for l=4,5,6, k=1,2: X = V(x1..x_{l-2}, z)
for (l, k) in [(4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (3, 2), (3, 3)]:
    N = build_cone(l, k)
    d = l + 1
    flatsel = []
    for i in range(1, l - 1):
        # pick level-0 coordinate hyperplane x_i = 0
        flatsel.append(next(t for t, (nm, n) in enumerate(N) if nm == f'x{i}=0z'))
    flatsel.append(next(t for t, (nm, n) in enumerate(N) if nm == 'z=0'))
    R, dimX = restrict_to_flat(N, flatsel, d)
    p = char_poly(R, dimX)
    s = show_poly(p)
    print(f"l={l} k={k}: dimX={dimX} |R|={len(R)} chi={s[0]} = {s[1]}")
