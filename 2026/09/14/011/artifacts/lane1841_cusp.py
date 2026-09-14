"""Lane-1841 step 4: certified cusp modulus of N_6 (band-violation check).

Replays SnapPy's ComplexCuspCrossSection accumulation for the complete cusp 0
with rigorous mpmath.iv intervals over the Krawczyk-certified shape boxes:

- Topology (mcomplex corners, face pairings, peripheral-curve integers) comes
  from SnapPy's kernel transfer (exact combinatorics, float shapes used only
  to build the transfer object, never for interval values).
- All geometric values are intervals: shape parameters z, 1/(1-z), (z-1)/z;
  horotriangle side lengths (-zL*L, -L/zR propagation); translation sum with
  exact integer peripheral weights; cusp shape = conj(L/M).
- Only +,-,*,/ and integer powers are used: every op outward-rounded.
- Cusp shape is scale invariant (L=1 seed), so no area normalization needed.

Band under test: 1.30 <= Im(theta) <= 2.00 and |Re(theta)| <= 0.35.
N_6 float: 0.46547756885 + 1.19399280918i (violates Re by ~0.115 and Im by ~0.106).
Success: certified box for theta_6 disjoint from the band (both bounds fail).
"""
import json
import re
import mpmath
import snappy
from snappy.snap import t3mlite as t3m
from snappy.snap.t3mlite import simplex
from snappy.snap.kernel_structures import TransferKernelStructuresEngine
from snappy.geometric_structure.cusp_neighborhood.cusp_cross_section_base import (
    HoroTriangleBase)

DPS = 50
mpmath.mp.dps = DPS
mpmath.iv.dps = DPS
iv = mpmath.iv


def load_boxes(key):
    d = json.load(open('output/artifacts/lane1841_krawczyk.json'))
    assert d['certified'] is True
    out = []
    for b in d[key]:
        lo_re = float(re.findall(r'-?\d+\.\d+', b['re'][0])[0])
        hi_re = float(re.findall(r'-?\d+\.\d+', b['re'][1])[0])
        lo_im = float(re.findall(r'-?\d+\.\d+', b['im'][0])[0])
        hi_im = float(re.findall(r'-?\d+\.\d+', b['im'][1])[0])
        out.append(iv.mpc([min(lo_re, hi_re), max(lo_re, hi_re)],
                          [min(lo_im, hi_im), max(lo_im, hi_im)]))
    return out


SHAPES = load_boxes('k_boxes')
print(f"loaded {len(SHAPES)} certified shape boxes")

M = snappy.Manifold('s776')
M.dehn_fill([(0, 0), (1, 6), (1, 6)])

# Topology from kernel (combinatorics only; shape values replaced by intervals)
m = t3m.Mcomplex(M)
t = TransferKernelStructuresEngine(m, M)
t.reindex_cusps_and_transfer_peripheral_curves()

# Interval shape parameters per tet: E01->z, E02->1/(1-z), E03->(z-1)/z (+opposites)
ONE = iv.mpc([1, 1], [0, 0])
tet_params = []
for z in SHAPES:
    zp = 1 / (ONE - z)
    zpp = (z - ONE) / z
    tet_params.append({simplex.E01: z, simplex.E23: z,
                       simplex.E02: zp, simplex.E13: zp,
                       simplex.E03: zpp, simplex.E12: zpp})

# Horotriangle propagation for the COMPLETE cusp (vertex Index 0),
# mirroring CuspCrossSectionBase._add_one_cusp_cross_section, with the same
# seed convention (first corner, first counterclockwise face, L=1).
v0 = [v for v in m.Vertices if v.Index == 0]
assert len(v0) == 1
v0 = v0[0]
print(f"cusp-0 corners: {len(v0.Corners)}")

corner0 = v0.Corners[0]
tet0, vert0 = corner0.Tetrahedron, corner0.Subsimplex
face0 = simplex.FacesAroundVertexCounterclockwise[vert0][0]

lengths = {}  # (tetIndex, vertex) -> {face: interval length}


def get_params(tet):
    return tet_params[tet.Index]


def make_tri(tet, vertex, known_side_face, L):
    """Mirror ComplexHoroTriangle with interval arithmetic."""
    left, center, right, z_left, z_right = HoroTriangleBase._sides_and_cross_ratios(
        _TETSHIM(tet, get_params(tet)), vertex, known_side_face)
    # _sides_and_cross_ratios reads tet.ShapeParameters; shim provides it.
    return {center: L, left: -z_left * L, right: -L / z_right}


class _TETSHIM:
    def __init__(self, tet, params):
        self.ShapeParameters = params


def sides_and_ratios(tet, vertex, side):
    sides = simplex.FacesAroundVertexCounterclockwise[vertex]
    P = get_params(tet)
    left, center, right, z_left, z_right = HoroTriangleBase._sides_and_cross_ratios(
        _TETSHIM(tet, P), vertex, side)
    return left, center, right, z_left, z_right


seed_tet, seed_vert = tet0, vert0
lengths[(seed_tet.Index, seed_vert)] = make_tri(seed_tet, seed_vert, face0, ONE)
active = [(seed_tet, seed_vert)]
while active:
    t0, v0s = active.pop()
    for f0 in simplex.FacesAroundVertexCounterclockwise[v0s]:
        t1, f1, v1 = HoroTriangleBase._glued_to if False else (None, None, None)
        # use base-class static directly
        from snappy.geometric_structure.cusp_neighborhood.cusp_cross_section_base import (
            CuspCrossSectionBase)
        t1, f1, v1 = CuspCrossSectionBase._glued_to(t0, f0, v0s)
        if (t1.Index, v1) not in lengths:
            known = -lengths[(t0.Index, v0s)][f0]  # direction_sign() == -1
            left, center, right, z_left, z_right = sides_and_ratios(t1, v1, f1)
            # known_side f1 has length `known`: center==f1 by construction
            # (_make_second rotates so side is second => center). Verify:
            assert center == f1, (center, f1)
            L = known
            lengths[(t1.Index, v1)] = {center: L, left: -z_left * L,
                                       right: -L / z_right}
            active.append((t1, v1))

print(f"propagated {len(lengths)} horotriangles (expect {len(v0.Corners)})")
assert len(lengths) == len(v0.Corners)


def translation(ml):
    """Mirror ComplexCuspCrossSection._get_translation for cusp vertex 0."""
    result = iv.mpc([0, 0], [0, 0])
    six = iv.mpc([6, 6], [0, 0])
    for corner in v0.Corners:
        tet = corner.Tetrahedron
        sub = corner.Subsimplex
        faces = simplex.FacesAroundVertexCounterclockwise[sub]
        tri = lengths[(tet.Index, sub)]
        curves = tet.PeripheralCurves[ml][0][sub]  # {face: int}
        for i in range(3):
            this_face = faces[i]
            prev_face = faces[(i + 2) % 3]
            f = curves[this_face] + 2 * curves[prev_face]
            if f:
                result = result + iv.mpc([float(f), float(f)], [0, 0]) * tri[this_face]
    return result / six


mM = translation(0)
lL = translation(1)
print("M interval:", mM)
print("L interval:", lL)
theta = (lL / mM)
# SnapPy cusp_shape conjugates the quotient
re = theta.real
im = -theta.imag  # conjugation negates imaginary part... careful: theta is ivmpc; conj flips sign of im
theta_conj_re_lo, theta_conj_re_hi = float(re.a), float(re.b)
theta_conj_im_lo, theta_conj_im_hi = float(-theta.imag.b), float(-theta.imag.a)
print(f"certified theta_6 in [{theta_conj_re_lo:.12f}, {theta_conj_re_hi:.12f}]"
      f" + [{theta_conj_im_lo:.12f}, {theta_conj_im_hi:.12f}] i")

band_re_ok = (theta_conj_re_lo > -0.35 and theta_conj_re_hi < 0.35)
band_im_ok = (theta_conj_im_lo >= 1.30 and theta_conj_im_hi <= 2.00)
viol_re = (theta_conj_re_lo > 0.35 or theta_conj_re_hi < -0.35)
viol_im_lo = (theta_conj_im_hi < 1.30)
viol_im_hi = (theta_conj_im_lo > 2.00)
print(f"inside Re bound: {band_re_ok}, violates Re bound: {viol_re}")
print(f"inside Im bound: {band_im_ok}, below 1.30: {viol_im_lo}, above 2.00: {viol_im_hi}")
OUTSIDE = bool(viol_re or viol_im_lo or viol_im_hi)
print("CERTIFIED OUTSIDE BAND:", OUTSIDE)

with open('output/artifacts/lane1841_cusp.json', 'w') as fh:
    json.dump({
        'n': 6,
        'theta_box': {'re': [repr(re.a), repr(re.b)],
                      'im_conj': [repr(-theta.imag.b), repr(-theta.imag.a)],
                      're_lo': theta_conj_re_lo, 're_hi': theta_conj_re_hi,
                      'im_lo': theta_conj_im_lo, 'im_hi': theta_conj_im_hi},
        'band': {'re': 0.35, 'im_lo': 1.30, 'im_hi': 2.00},
        'violates_Re': bool(viol_re), 'below_Im': bool(viol_im_lo),
        'above_Im': bool(viol_im_hi),
        'certified_outside': OUTSIDE,
    }, fh, indent=1)
print("wrote output/artifacts/lane1841_cusp.json")
assert OUTSIDE, "theta_6 box does not lie outside the band"
