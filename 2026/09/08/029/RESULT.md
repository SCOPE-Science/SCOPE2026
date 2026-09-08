# Attained-volume spectrum of reflexive 3-polytopes with normalized volume at most 12

## Context

Reflexive lattice polytopes classify toric Fano varieties and drive Batyrev
mirror symmetry. In dimension 3, Ehrhart theory seeks sharp boundaries relating
normalized volume, lattice points, and h*-vectors. The Kreuzer-Skarke
classification gives counts (4319 reflexive 3-polytopes) but no sorted
attained-volume spectrum, maximal consecutive-gap witness, or Ehrhart/h* table
for a small-volume window.

## Definitions

- A lattice polytope `P ⊂ R^3` is the convex hull of finitely many points of `Z^3`.
- Normalized volume: `Vol(P) = 6 · vol_Eucl(P)`; the unimodular simplex has volume 1.
- `P` is reflexive if `0` is in its interior and every facet has lattice
  distance 1 from `0` (equivalently the polar is a lattice polytope). Then `0`
  is the unique interior lattice point.
- Ehrhart function `L_P(t) = |tP ∩ Z^3|`. In dimension 3,
  `L_P(t) = sum_{i=0}^{3} h_i* C(t+3-i,3)` with `h* = (h_0*,h_1*,h_2*,h_3*)`,
  `sum h_i* = Vol(P)`, `h_0* = 1`, and for reflexive `P`,
  `h_3* = |int(P) ∩ Z^3| = 1`.
  Ehrhart series: `sum_{t>=0} L_P(t) x^t
  = (h_0* + h_1* x + h_2* x^2 + h_3* x^3)/(1-x)^4`.
- Unimodal means `1 = h_0* <= h_1*` and the vector rises then falls;
  here palindromic `(1,a,a,1)` with `a >= 1` is unimodal.

## Result (theorem)

Let `R_12` be the set of reflexive lattice 3-polytopes with `Vol(P) <= 12`. Then:

- (a) Every `P ∈ R_12` has even normalized volume `>= 4`.
- (b) The attained-volume spectrum on `R_12` is exactly `{4, 6, 8, 10, 12}`;
  each value is realized by an explicit reflexive witness below.
- (c) The sorted spectrum has consecutive gaps `(2,2,2,2)`; the maximal
  consecutive gap is `G* = 2`, realized as a four-way tie by the intervals
  `[4,6], [6,8], [8,10], [10,12]`.
- (d) Every `P ∈ R_12` of volume `V` has `h* = (1, V/2-1, V/2-1, 1)`;
  hence every `h*` in the window is unimodal. Explicit table:

| Vol | h* | witness lattice points L(1),L(2),L(3) |
|-----|-----------|------------------------------------------|
| 4 | (1,1,1,1) | 5, 15, 35 |
| 6 | (1,2,2,1) | 6, 20, 49 |
| 8 | (1,3,3,1) | 7, 25, 63 |
| 10 | (1,4,4,1) | 8, 30, 77 |
| 12 | (1,5,5,1) | 9, 35, 91 |

Witnesses (vertices):

- `P_4 = conv{(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)}`, Vol 4.
- `P_6 = conv{(1,0,0),(0,1,0),(-1,-1,0),(0,0,±1)}`, Vol 6.
- `P_8 = conv{(±1,0,0),(0,±1,0),(0,0,±1)}`, Vol 8.
- `P_10`: bipyramid with apices `(0,0,±1)` over the reflexive pentagon
  `(1,0),(0,1),(-1,0),(-1,-1),(0,-1)`; Vol 10.
- `P_12`: bipyramid with apices `(0,0,±1)` over the reflexive hexagon
  `(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)`; Vol 12.

## Proof / evidence

Lemma 1 (parity). Every reflexive 3-polytope has even normalized volume.
Proof: write `P = ∪_F conv(0,F)` over facets `F`; since `0` is interior these
pyramids have disjoint interiors, and as each facet is at lattice distance 1
from `0`, `Vol_3(conv(0,F)) = Vol_2(F)`. Hence `Vol(P) = sum_F Vol_2(F)`.
By Pick's theorem `Vol_2(F) = 2I_F + B_F - 2`. Summing,
`sum_F B_F` counts every edge's lattice segments twice (each edge lies in
exactly two facets), so it is even; `2 sum_F I_F` and `2 #{F}` are even.
Thus `Vol(P)` is even.

Lemma 2 (lower bound). Every reflexive 3-polytope has `Vol >= 4`.
Proof: `P` has at least 4 facets and each facet, a non-degenerate lattice
polygon, has `Vol_2(F) >= 1` (minimum: unimodular triangle). Summation as
above gives `Vol(P) >= 4`.

Hence any reflexive volume `<= 12` lies in `{4,6,8,10,12}` with no
classification needed.

Witness certification (machine-verified, exact integer arithmetic): for each
witness, facets enumerated by brute force over vertex triples with exact
primitive normals; all facet lattice distances equal 1; origin strictly
interior and unique interior lattice point (bounding-box scan with exact facet
inequalities); normalized volume by fan triangulation from the origin; Ehrhart
counts `L(1),L(2),L(3)` by exact scaled-inequality enumeration; solved `h*`
palindromic with sum agreeing with the fan volume. Volumes `[4,6,8,10,12]`,
gaps `[2,2,2,2]`, all_reflexive/all_vol_agree/all_palindromic true.

Gap conclusion: by (a) the attained spectrum lies in `{4,6,8,10,12}`; by (b)
all five occur. Hence the spectrum equals that set, gaps are `(2,2,2,2)`,
`G* = 2` (four-way tie).

For (d): reflexive `h*` is palindromic (Hibi's theorem, cited), so
`h* = (1,a,a,1)` with `Vol = 2+2a`, i.e. `a = V/2-1`; all five vectors satisfy
`1 <= a` hence are unimodal. Computed `L(1..3)` and `h*` of the witnesses agree
exactly. Inversion used: `h_1 = L_1-4`, `h_2 = L_2-10-4h_1`,
`h_3 = L_3-20-10h_1-4h_2` from `L(t) = sum h_i C(t+3-i,3)`.

## Limitations

- Maximal gap is a four-way tie (`G* = 2`); this is the admission-anticipated
  fallback case, not a unique-winner extremal census.
- No enumeration of all `GL(3,Z)`-classes with `Vol <= 12` is claimed; no
  per-volume class counts or inequivalence certification across the window.
  The gap statistic is proved via parity plus witnesses without a full
  classification.
- Part (d) uses Hibi's palindromicity theorem as a cited result; parity is
  proved elementarily and independently of Hibi.
- No KS database/PALP/Sage was used or needed; witnesses are explicit and the
  replay is stdlib-only.

## Reproducibility

```
python3 output/artifacts/verify_census.py
```

Expected: volumes `[4,6,8,10,12]`, gaps `[2,2,2,2]`,
all_reflexive/all_vol_agree/all_palindromic true; per-witness facet distances
all 1, unique interior origin, `h*` as tabulated. Artifacts:
`output/artifacts/verify_census.py`, `output/artifacts/census_result.json`,
`output/artifacts/verify.log`.

## References

- M. Kreuzer, H. Skarke, Classification of reflexive polyhedra in three
  dimensions, hep-th/9805190. 4319 polytopes; counts/connectivity only.
- M. Kreuzer, H. Skarke, On the classification of reflexive polyhedra,
  hep-th/9512204. Weight-system/matrix method.
- V. Batyrev, Dual polyhedra and mirror symmetry for Calabi-Yau hypersurfaces
  in toric varieties, alg-geom/9310003. Mirror-duality motivation.
- B. Nill, A. Paffenholz, On the equality case in Ehrhart's volume conjecture,
  arXiv:1205.1270. General sharp upper bound.
- C. Amendola, J. Oldekop, Likelihood geometry of reflexive polytopes,
  arXiv:2311.13572. ML degrees over the same 4319; different statistic.
- Sage reference: Lattice and reflexive polytopes / PALP database,
  https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/lattice_polytope.html.
  Toolchain documentation only.
