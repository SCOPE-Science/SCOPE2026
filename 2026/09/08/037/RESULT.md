# Exact Mahler spectrum over the 16 reflexive lattice polygons, with the centrally symmetric gap

## Context
The symmetric Mahler volume product is M(K) = vol(K)·vol(K°), K = −K ⊂ R².
Continuously the 2D minimum is 8, attained exactly by parallelograms
(Mahler 1939; Reisner equality; Harrell–Henrot–Lamboley local-minimizer
analysis). Reflexive lattice polygons — lattice polygons with 0 as unique
interior lattice point and lattice polar — form a finite classification of
16 GL(2,Z)-classes, central to toric Fano geometry and mirror symmetry.
Their polars are lattice by definition, so their Mahler products are exact
rationals of structural interest. No prior source tabulates the Mahler
spectrum over these 16 classes or the symmetric-subfamily gap.

## Definitions
- Lattice polygon P ⊂ R² with 0 strictly interior; polar
  P° = {y : ⟨x,y⟩ ≤ 1 ∀ x ∈ P}.
- Reflexive: P° is a lattice polygon (equivalently facet lattice-distance 1
  from origin and unique interior lattice point 0).
- GL(2,Z)-equivalence: unimodular maps, det ±1, integral.
- Volumes are Euclidean areas; M(P) = vol(P)·vol(P°).
- Centrally symmetric: P = −P as sets. Parallelogram: 4 vertices with
  coincident diagonal midpoints.

## Result
Up to GL(2,Z), the Mahler products on reflexive polygons take exactly the
values {27/4, 8, 35/4, 9}, with multiplicities 2 / 6 / 4 / 4:
- minimum 27/4, attained precisely by the dual triangle pair (representatives
  (−3,−2),(0,1),(3,1) and (−3,−2),(1,1),(2,1));
- maximum 9, attained precisely by four classes with 3, 4, 5, 6 vertices
  (representatives (−3,−2),(−1,0),(3,1); (−3,−2),(−2,−1),(1,0),(3,2);
  (−3,−2),(−2,−1),(1,0),(1,1),(2,1);
  (−3,−2),(−2,−1),(−1,−1),(1,1),(2,1),(3,2)).
Exactly 3 of the 16 classes are centrally symmetric: two parallelograms with
M = 8 ((−3,−2),(−2,−1),(2,1),(3,2) and (−3,−2),(−1,0),(1,0),(3,2)) and one
hexagon with M = 9 (the 6-vertex representative above). Hence for centrally
symmetric reflexive P, M(P) ∈ {8, 9}; M(P) = 8 iff P is a parallelogram.
A symmetric non-parallelogram reflexive polygon satisfies M ≥ 9: sharp
stability gap G = 1 above the symmetric minimum 8 within this family.
Full 16-row table (n, B, B°, vol, vol-polar, M, symmetry, vertices) is in
output/artifacts/mahler_table.json/.csv.

## Proof / evidence
Exact rational computation per GL-class, machine-certified:
- Polar vertices from facet lines: u_i = (dy_i, −dx_i)/det(v_i, v_{i+1});
  integrality verified (reflexivity) per class.
- Areas by exact shoelace over 2; reflexivity also certified by
  bounding-box scan (unique interior lattice point 0).
- Duality involution P°° = P verified vertex-for-vertex per class; each dual
  re-enters the table up to GL with equal M.
- Cross-checks per class: Pick's relation 2A = B (I = 1) and Twelve-Point
  relation B(P) + B(P°) = 12.
- GL(2,Z)-equivalence by exact complete search: every source pair and ordered
  target pair determines at most one integer matrix via adjugate over det V,
  accepted iff integral, det ±1, mapping vertex set onto vertex set. 16
  representatives certified reflexive and pairwise inequivalent.
- Symmetry/parallelogram labels by exact set equality (P = −P) and diagonal
  midpoint coincidence; gap G = 9 − 8 = 1 is a certified finite-case
  consequence.
- Independent audit re-ran the stdlib verifier (1148488 subsets, 828
  reflexive vertex-sets, 16 classes, ~4 s, all assertions pass) and
  separately recomputed hulls, areas, duals, Mahler values, gcd boundary
  counts, symmetry, parallelogram status, and all 120 pairwise
  inequivalences.

## Limitations
- Completeness (exactly these 16 classes) matches the representatives against
  the published 16-class reflexive-polygon theorem count; the box subset
  search is the discovery route, not a from-scratch finiteness proof.
- Gap G = 1 is a certified enumeration within the reflexive family, not a
  general analytic stability estimate, and does not extend beyond reflexive
  polygons.
- No originality claimed for the 16-polygon classification, the Twelve-Point
  theorem, or the classical minima 8 and 27/4 (background).
- Volumes are Euclidean areas; normalized volumes are 4× larger.

## Reproducibility
Stdlib-only Python (fractions, itertools, math):
  python3 output/artifacts/mahler_reflexive.py
Scans 1148488 subsets, asserts 16 classes and all reflexivity / Pick /
Twelve-Point / involution / duality-pairing certificates, writes
mahler_table.json / mahler_table.csv. Runtime seconds.

## References (background)
- Batyrev, Dual polyhedra and mirror symmetry for Calabi–Yau hypersurfaces.
- Kreuzer–Skarke, Complete classification of reflexive polyhedra in four
  dimensions, arXiv:hep-th/0002240 (classification program).
- Kasprzyk–Nill, Reflexive polytopes of higher index and the number 12,
  arXiv:1107.4945 (16 polygons; Twelve-Point context).
- Mahler 1939; Reisner (equality); Harrell–Henrot–Lamboley, On the local
  minimizers of the Mahler volume, arXiv:1104.3663.
- Bäuerle, Sharp volume and multiplicity bounds for Fano simplices,
  arXiv:2308.12719 (nearest lattice-Mahler prior: simplices bounds only).
