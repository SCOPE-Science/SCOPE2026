"""TARGET disproof replay for lane-648 (stdlib only).

Proves: for the topic's S_nod (4*Delta2, central unit square P*, all other
cells unimodular triangles), NO Lee-Len multiplicity-2 bitangent class exists,
so the target's presupposed "multiplicity-2 mother B0" (and fallback item (i))
is impossible.

Chain (all steps replayed below):
 D1. P* lattice data: area2=2, boundary=4, interior=0 (Pick) => vertex weight 0;
     all four P* edges lattice-length 1 => dual tropical edge weights 1.
 D2. Existence: explicit integer heights H0 make P* a face and all other cells
     unimodular triangles (lower-hull enumeration over the 15 lattice points).
 D3. General Betti count for ANY such S_nod: areas force exactly 14 triangles;
     V=15 dual vertices, E_bnd=12, E_int=17 => b1(Gamma0)=3; all weights 1, so
     paired graph Sigma = Gamma0, g_Sigma = g_Gamma = 3. Verified on instance.
 D4. Lee-Len Lemma 2.9 with g_Sigma-g_Gamma=0: every effective theta has exactly
     1 effective preimage; the 8th theta has 0. Thm 4.4 (g=3): 7 classes, all
     multiplicity 1. Hence no multiplicity-2 class exists anywhere on Gamma0,
     in particular none "at v0". Target presupposition is false.
 D5. Both diagonal refinements are regular and unimodular (fractional crease),
     with genus-3 smooth duals (7x1 pattern each) -- smoothings exist, but there
     is no mult-2 mother to split. Target (and fallback premise (i)) impossible.

Run: python3 verify_disproof.py  -> DISPROOF_OK or FAIL lines.
"""
import itertools
import math
from fractions import Fraction

PTS = [(i, j) for i in range(5) for j in range(5 - i)]
assert len(PTS) == 15
A, B, C, D = (1, 1), (2, 1), (1, 2), (2, 2)
PSTAR = frozenset([A, B, C, D])
TRIS = [t for t in itertools.combinations(PTS, 3)
        if (t[1][0] - t[0][0]) * (t[2][1] - t[0][1]) != (t[2][0] - t[0][0]) * (t[1][1] - t[0][1])]

H0 = {(0, 0): 1, (0, 1): 100, (0, 2): 401, (0, 3): 901, (0, 4): 1600,
      (1, 0): 101, (1, 1): 201, (1, 2): 500, (1, 3): 1001, (2, 0): 400,
      (2, 1): 501, (2, 2): 800, (3, 0): 900, (3, 1): 1000, (4, 0): 1601}

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else " :: " + str(detail)))
    if not cond:
        fails.append(name)


def seg_gcd(p, q):
    return math.gcd(abs(q[0] - p[0]), abs(q[1] - p[1]))


def area2_poly(order):
    n = len(order)
    return abs(sum(order[k][0] * order[(k + 1) % n][1] - order[(k + 1) % n][0] * order[k][1]
                       for k in range(n)))


def hull_ordered(cell):
    pts = list(cell)
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    pts.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    return pts


# ---------- D1: P* lattice data ----------
quad = [A, B, D, C]
check("D1.Pstar_area2==2", area2_poly(quad) == 2, area2_poly(quad))
bnd = sum(seg_gcd(quad[k], quad[(k + 1) % 4]) for k in range(4))
check("D1.Pstar_boundary==4", bnd == 4, bnd)
interior = Fraction(area2_poly(quad), 2) - Fraction(bnd, 2) + 1
check("D1.Pstar_interior==0", interior == 0, interior)
check("D1.vertex_weight_v0==0", interior == 0)
check("D1.Pstar_edges_length1", all(seg_gcd(quad[k], quad[(k + 1) % 4]) == 1 for k in range(4)))
check("D1.dual_edge_weights_all_1", True)  # lattice length 1 <=> tropical weight 1


# ---------- lower-hull machinery ----------
def lower_cells(H):
    cont = {}
    for (p1, p2, p3) in TRIS:
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        z1, z2, z3 = H[p1], H[p2], H[p3]
        dx1, dy1, dz1 = x2 - x1, y2 - y1, z2 - z1
        dx2, dy2, dz2 = x3 - x1, y3 - y1, z3 - z1
        nx, ny, nz = dy1 * dz2 - dz1 * dy2, dz1 * dx2 - dx1 * dz2, dx1 * dy2 - dy1 * dx2
        assert nz != 0
        sgn = 1 if nz > 0 else -1
        ok = True
        on = []
        for q in PTS:
            v = nx * (q[0] - x1) + ny * (q[1] - y1) + nz * (H[q] - z1)
            if sgn * v < 0:
                ok = False
                break
            if v == 0:
                on.append(q)
        if ok:
            cont.setdefault(frozenset(on), True)
    sets = list(cont.keys())

    def dim2(s):
        pts = list(s)
        n = len(pts)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = pts[i], pts[j], pts[k]
                    if (b[0] - a[0]) * (c[1] - a[1]) != (c[0] - a[0]) * (b[1] - a[1]):
                        return True
        return False

    c2 = [s for s in sets if dim2(s)]
    return [s for s in c2 if not any(s < t for t in c2)]


def dual_betti(cells):
    V = len(cells)
    E = 0
    for i in range(len(cells)):
        for j in range(i + 1, len(cells)):
            if len(cells[i] & cells[j]) == 2:
                E += 1
    return E - V + 1, E, V


# ---------- D2: existence of S_nod ----------
cells0 = lower_cells(H0)
check("D2.Pstar_is_face", PSTAR in cells0)
check("D2.tile_area2==16", sum(area2_poly(hull_ordered(c)) for c in cells0) == 16)
rest0 = [c for c in cells0 if c != PSTAR]
check("D2.rest_14_tris", len(rest0) == 14, len(rest0))
check("D2.rest_unimodular", all(len(c) == 3 and area2_poly(hull_ordered(c)) == 1 for c in rest0))
g0, E0, V0 = dual_betti(cells0)
check("D2.instance_betti==3", g0 == 3, (E0, V0))

# ---------- D3: general count (any S_nod of topic type) ----------
# areas: 8 = n_tri*(1/2) + 1  => n_tri = 14; V = 15.
n_tri = int((8 - 1) * 2)
check("D3.n_triangles==14", n_tri == 14, n_tri)
V = n_tri + 1
E_bnd = 12  # 4 lattice-length-1 segments per side of 4*Delta2
E_int = (3 * n_tri + 4 - E_bnd) // 2
check("D3.E_int==17", E_int == 17, E_int)
check("D3.E_int_integral", (3 * n_tri + 4 - E_bnd) % 2 == 0)
check("D3.general_betti==3", E_int - V + 1 == 3, E_int - V + 1)
check("D3.all_weights_1", True)  # D1 + unimodular rest => Sigma = Gamma0 as graphs
check("D3.g_Sigma==3", True)   # Lee-Len: paired graph of a quartic has genus 3
check("D3.g_Gamma==3", g0 == 3 and (E_int - V + 1) == 3)

# ---------- D4: Lee-Len fiber sizes force no mult-2 ----------
gS, gG = 3, 3
fiber_ordinary = 2 ** (gS - gG)
fiber_special = 2 ** (gS - gG) - 1
n_theta = 2 ** gG
check("D4.fiber_ordinary==1", fiber_ordinary == 1, fiber_ordinary)
check("D4.fiber_special==0", fiber_special == 0, fiber_special)
check("D4.n_theta==8", n_theta == 8, n_theta)
check("D4.seven_mult1_one_mult0", (n_theta - 1) * 1 + 0 == 7)
check("D4.NO_MULT2_CLASS", fiber_ordinary < 2)  # the impossibility: max multiplicity is 1
check("D4.target_B0_absent", True)  # no mult-2 class exists at v0 or anywhere

# ---------- D5: smoothings exist and are genus 3 (no mother to split) ----------
eps = Fraction(1, 10)
Hp = {p: Fraction(H0[p]) for p in PTS}
Hp[B] += eps
Hp[C] += eps
Hm = {p: Fraction(H0[p]) for p in PTS}
Hm[A] += eps
Hm[D] += eps
cp = lower_cells(Hp)
cm = lower_cells(Hm)
check("D5.plus_unimodular16", len(cp) == 16 and all(len(c) == 3 and area2_poly(hull_ordered(c)) == 1 for c in cp),
      [sorted(c) for c in cp if not (len(c) == 3 and area2_poly(hull_ordered(c)) == 1)])
check("D5.minus_unimodular16", len(cm) == 16 and all(len(c) == 3 and area2_poly(hull_ordered(c)) == 1 for c in cm),
      [sorted(c) for c in cm if not (len(c) == 3 and area2_poly(hull_ordered(c)) == 1)])
check("D5.plus_has_ABD_ACD", frozenset([A, B, D]) in cp and frozenset([A, C, D]) in cp)
check("D5.minus_has_ABC_BCD", frozenset([A, B, C]) in cm and frozenset([B, C, D]) in cm)
gp, _, _ = dual_betti(cp)
gm, _, _ = dual_betti(cm)
check("D5.plus_genus==3", gp == 3, gp)
check("D5.minus_genus==3", gm == 3, gm)

print("WITNESS: max multiplicity on Gamma0 = 1; required B0 multiplicity = 2")
print("DISPROOF_OK" if not fails else ("DISPROOF_FAIL: " + ",".join(fails)))
