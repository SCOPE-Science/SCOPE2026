# Real elevator factorization for one floor cut on Hirzebruch F2 (genus 0, a=2)

## Context

Complex Severi degrees of Hirzebruch surfaces admit Caporaso-Harris type
recursions and floor-diagram / Fock-space descriptions. Over the reals the
situation is fragmentary: real Caporaso-Harris recursions with Welschinger
signs are recorded for the plane and for toric del Pezzo surfaces, while
F2 = P(O+2O) is non-del Pezzo (it contains a (-2)-section) and is
explicitly excluded from those theorems. No quantitative real recursion
step with an explicit Welschinger-sign ledger was recorded for F2.
This record supplies the first such one-floor step at marked-floor-diagram
level.

## Definitions and conventions

We use the Brugalle-Mikhalkin planar floor-diagram calculus
(arXiv:0812.3354, Definitions 3.1-3.8, Theorems 3.6 and 3.9).
For F2 in class aC+bF (C the negative section, F a fibre; DRAFT writes B=C),
the h-transverse polygon is Delta_{2,a,b} with vertices
(0,0), (2a+b,0), (b,a), (0,a).
Hence d_- = 2a+b bottom leaves (weight 1), d_+ = b top leaves (weight 1),
and left/right divergence data force every floor vertex v to satisfy
div(v) = 2.

Genus g = 0 with vertically stretched point conditions, so contributing
tropical curves are floor-decomposed and every diagram is a tree.
Point count: s = |partial Delta| + g - 1 = 4a + 2b - 1.
Concretely s = 7, 9, 11 for a = 2, b = 0, 1, 2
(DRAFT labels 9/11/13 are a +2 typo corrected here; the enumerated posets
satisfy Card(Vert)+Card(Edge) = s with the corrected s).

Complex multiplicity: mu_C(D) = prod_e w(e)^2.
The r-real multiplicity (Def 3.8) is
  mu_r^R(D,m) = (-1)^{o_r} prod_{e in A} w(e)
if (D,m) is r-real and every even-weight edge meets m(Im(m,r)), else 0,
where A = Edge(D) \\ m({1,...,s-2r}) and o_r is half the number of vertices
in m(Im(m,r)) of odd divergence.

Key structural fact on F2: every floor divergence equals 2 (even), so for
r = 0 (Im empty) o_r = 0 identically and the sign is always +1. The entire
r = 0 real ledger is therefore the even-edge annihilation rule:
a diagram contributes iff all its edge weights are odd.

## Result (headline claim)

For genus-zero classes 2C+bF on F2, b = 0, 1, 2, with stretched point
conditions, the Welschinger-signed (r = 0) marked floor-diagram count
factorizes through the single internal elevator cut of weight x as:

- complex contribution per diagram: markings(D) * x^2 (standard gluing,
  both sides see the cut leaf of weight x);
- real contribution per diagram: markings(D) * f(x),
  with parity elevator-sign rule f(x) = 1 if x odd, 0 if x even,
  and sign (-1)^{o_r} = +1 throughout (all F2 floor divergences are 2).

Totals (complex N, real r=0 W):
  b=0: (N,W) = (10,6); b=1: (93,45); b=2: (636,252).
Even elevators (x=2 with mu_C=4, x=4 with mu_C=16) are annihilated really
(contribute 0), so no raw-weight product rule x or x^2 holds really;
the parity indicator f is the exact elevator-sign rule.
The factor f(x) depends only on the cut weight x, verified constant across
all top-floor shapes sharing x (b=2: x=1 over 3 shapes, x=2 over 3 shapes,
x=3 over 2 shapes).

Per-type census (L1,L2,U1,U2,x; m=markings; complex/real):
b=0: (3,1,0,0,1) m=6 -> 6/6; (4,0,0,0,2) m=1 -> 4/0.
b=1: (3,2,0,1,1) m=21 -> 21/21; (4,1,0,1,2) m=7 -> 28/0;
     (4,1,1,0,1) m=23 -> 23/23; (5,0,0,1,3) m=1 -> 9/1;
     (5,0,1,0,2) m=3 -> 12/0.
b=2: x=1: (3,3,0,2,1) m=56 -> 56/56; (4,2,1,1,1) m=128 -> 128/128;
         (5,1,2,0,1) m=56 -> 56/56;
     x=2: (4,2,0,2,2) m=28 -> 112/0; (5,1,1,1,2) m=34 -> 136/0;
          (6,0,2,0,2) m=6 -> 24/0;
     x=3: (5,1,0,2,3) m=8 -> 72/8; (6,0,1,1,3) m=4 -> 36/4;
     x=4: (6,0,0,2,4) m=1 -> 16/0.
Base a=1: one diagram per b with mu_C = mu_0^R = 1, N = W = 1.

## Proof / evidence

Divergence equations for a=2 with one internal elevator x:
  L1+L2 = 2a+b, U1+U2 = b, L1-U1-x = 2, L2+x-U2 = 2.
Exhaustive integer solutions give 2/5/9 diagram types for b=0/1/2.
Marking counts are exact linear-extension counts of the diagram poset
(VL<e<VU, down leaves below their floor, up leaves above, VL<VU)
divided by leaf-factorial symmetries L1! L2! U1! U2!; the script asserts
exact divisibility and was spot-checked by brute-force permutation count
(36 extensions for the (3,1,0,0,1) type before division).
Complex totals sum markings*x^2; real r=0 totals sum markings*[x odd]
by Def 3.8 (o_r=0, even-kill). verify_cut.py checks f(x) is constant on
fibres of x, i.e. factorization through the cut. Summation reproduces
6, 45, 252 (real) and 10, 93, 636 (complex). All scripts replayed by the
auditor with identical output.

## Limitations

- Diagram-level signed ledger identity only. F2 is not Fano/del Pezzo, so
  Welschinger invariance for r>0 is not available (cf. Remark 4.17 of the
  BM source); no invariant recursion is claimed.
- Genus zero, classes a=1 (base) and a=2 with b=0,1,2 exhaustively
  enumerated; cut mechanism (single elevator, o_r=0, even-kill) proved for
  a=2. No claim beyond a=2 or higher b by computation alone.
- r=0 ledger exhaustive; r>=1 per-marking tables not enumerated.
- Uses (not reproves) the BM planar correspondence Theorems 3.6/3.9.
- Glue-sym formula markings(top)*markings(bottom)/sym is schematic;
  the certified content is the per-diagram parity identity and totals.

## Reproducibility

Run from the attempt root:
  python3 inputs/artifacts/enumerate.py
  python3 inputs/artifacts/verify_cut.py
  python3 inputs/artifacts/cut_analysis.py
Copies are preserved in output/artifacts/. All totals and per-type rows
above must reproduce exactly. Dependencies: Python 3 stdlib only
(bitmask DP, exact integer arithmetic).

## References

- E. Brugalle, G. Mikhalkin, Floor decompositions of tropical curves:
  the planar case, arXiv:0812.3354 (Gokova 2008 proceedings).
- F. Ardila, E. Brugalle, The double Gromov-Witten invariants of
  Hirzebruch surfaces are piecewise polynomial, arXiv:1412.4563.
- L. Cavalieri, H. Markwig et al. / Y. Cooper, Fock-space Severi theory
  for Hirzebruch surfaces (complex/descendant setting).
- I. Itenberg, V. Kharlamov, E. Shustin, A Caporaso-Harris type formula
  for Welschinger invariants of real toric Del Pezzo surfaces,
  math/0608549 (del Pezzo only; excludes F2).
- E. Brugalle et al., Recursive formulas for Welschinger invariants of
  the projective plane, IMRN rnq096 (plane only).
