# Integral-homology torsion census for pure 2-complexes on six vertices

## Context
Six vertices are the classical extremal boundary where the real projective
plane first triangulates (the minimal 6-vertex 10-triangle triangulation of
`RP^2`). Integral torsion, minimal triangulations, and torsion growth in
2-complexes are a recognized program (Lutz/Sulanke surface enumeration,
Benedetti–Lutz library, Lofano–Lutz Hadamard torsion, Hatcher UCT theory).
Nearby sources give only manifold censuses (3 triangulated surfaces on
6 vertices), the single fact `H_1(RP^2) = Z/2`, general SNF/UCT methods, and
isolated torsion examples at `n >= 8` — not a closed torsion table over all
pure 2-complexes on 6 vertices.

## Definitions
- Vertex set `{0,...,5}`. The 20 possible triangles in lexicographic order
  are indexed 0–19:
  `012,013,014,015,023,024,025,034,035,045,123,124,125,134,135,145,234,235,245,345`.
- A *pure 2-complex* (in this scope) is a family `F` of triangles, taken with
  its full simplicial closure (all edges/vertices of the triangles). A mask
  is the 20-bit integer with bit `i` set iff triangle `i` is present.
- Two families are equivalent under the natural `S_6` action on vertices.
  A family *covers* if every vertex lies in some triangle.
- For a representative with `E` edges and `T` triangles, integer boundary
  maps `d_1` (6 × E) and `d_2` (E × T) use the orientation induced by the
  vertex order (`+1` on `(a,b)`, `-1` on `(a,c)`, `+1` on `(b,c)` for triangle
  `(a,b,c)`). With `r_1 = rank d_1`, `r_2 = rank d_2`:
  `H_1 = Z^(E-r_1-r_2) × Tors`, `H_2 = Z^(T-r_2)`, where `Tors` is read from
  the nonzero Smith-normal-form diagonal of `d_2`.

## Result
1. **Type count.** There are exactly **2136** `S_6`-isomorphism types of
   triangle families on six labelled vertices (including the empty family),
   of which exactly **2102** cover all six vertices. Burnside checksum over
   the covering representatives:
   `sum 720/|Stab| = 1042642` = number of covering labelled masks
   (direct brute-force count of the `2^20 = 1048576` masks).
2. **Homology.** Every covering representative's integral homology was
   computed from `d_1, d_2` by Smith normal form over `ZZ`. All 2102 rows
   pass mod-`p` universal-coefficient replay (`p = 2,3,5`):
   `dim H_1(-;F_p) = b_1 + #{torsion invariants divisible by p}`,
   `dim H_2(-;F_p) = b_2 + #{torsion invariants divisible by p}`.
3. **Unique torsion type.** Exactly **one** of the 2102 types carries
   integral torsion, hence it is simultaneously the minimal-vertex `Z/2`
   witness and the maximal-torsion-gap type (torsion order 2 vs 1, unique
   attainer): mask **242467** (bits `0,1,5,8,9,12,13,15,16,17`), i.e.
   triangles `012,013,024,035,045,125,134,145,234,235`, with `E = 15`,
   `T = 10`, `SNF(d_2) = (1,1,1,1,1,1,1,1,1,2)`, `H_1 = Z/2`, `H_2 = 0`,
   `b_0 = 1`. It is a closed triangulated surface (every edge in exactly two
   triangles, every vertex link a 5-cycle, `χ = 6-15+10 = 1`): the classical
   minimal 6-vertex triangulation of `RP^2` (classical object; new content is
   the exhaustive uniqueness and certificate).
4. **Certified 2-torsion relation.** With the triangle/edge orders in
   `artifacts/witness.json`, `s = (1,...,1)` and
   `c = (1,0,0,0,-1,1,1,0,-1,1,0,0,1,1,1)` satisfy `d_1(c) = 0`,
   `d_2(s) = 2c`, `c ≠ 0`; the `F_2`-row vector
   `w = (1,1,0,0,0,0,1,0,0,0,1,0,1,0,0)` satisfies `w·d_2 = 0 (mod 2)` and
   `w·c = 1 (mod 2)`, so `[c]` is nonzero in `H_1` of order 2. Bareiss
   determinantal-divisor replay confirms SNF `(1^9,2)`.
5. **Minimality.** Exhaustive SNF scans over all triangle families on
   `n = 3` (2 masks), `n = 4` (16), `n = 5` (1024) find zero torsion cases;
   six vertices are minimal for integral torsion in this class.
6. **Signature table.** The 2102 types realize exactly 25 `(b_1,b_2,torsion)`
   signatures: `(0,0):{324 free, 1 [2]}`; `(0,k)` free for `k=1..10`:
   `400,329,209,113,50,22,8,3,1,1`; `(1,k)` free: `252,158,63,19,5,1`;
   `(2,k)` free: `90,28,5,1`; `(3,k)` free: `16,2`; `(4,0)` free: `1`.
   Full 2102-row table in `artifacts/census_2102.csv`.

## Proof / evidence
Machine-enumeration theorem with exact independent replay (not an analytic
general theorem):
- Enumeration: `2^20` masks classified under all 720 vertex permutations;
  auditor recomputed canonical minima, stabilizers, and the Burnside sum
  `1042642`; conjugacy-class Burnside gives 2136 orbits incl. empty.
- Homology: `sympy` ZZ-SNF on `d_1,d_2` for all 2102 masks matches the table
  with 0 mismatches; exact `F_2,F_3,F_5` elimination confirms UCT on all
  rows; `d_1·d_2 = 0` on all rows.
- Witness: direct integer identities above plus Bareiss-minor SNF replay;
  closed-surface check (edge degrees, link cycles, Euler characteristic).
- Minimality: complete `n ≤ 5` scans. Stdlib-only `artifacts/verify.py`
  replays the headline checks and prints `VERIFY_OK`.

## Limitations
- "Pure" means families of triangles with simplicial closure; lower-dimensional
  maximal faces are not separately modelled. Homology uses that closure.
- Uniqueness/minimality hold inside the enumerated scope (all triangle
  families on `≤ 6` vertices up to `S_6` equivalence), verified by replayable
  logs — not a general topological theorem beyond that scope.
- Census correctness rests on exact machine replay rather than
  human-checkable case analysis.

## Reproducibility
- `output/artifacts/census_2102.csv`: 2102 rows
  (`mask,n_tri,n_edge,b0,b1,b2,torsion_H1,snf_d2,uct_ok`).
- `output/artifacts/witness.json`, `torsion_row.json`,
  `census_signatures.json`, `enum_stats.json`: witness vectors, torsion row,
  signature cells, enumeration stats.
- `output/artifacts/verify.py`: stdlib-only verifier (covering count,
  Burnside count, canonical/Burnside replay, witness identities,
  closed-surface check, Bareiss SNF, UCT spot checks) → `VERIFY_OK`.
- Triangle bit order is the lexicographic list in Definitions above.

## References
- F. H. Lutz, Manifold Page: Surfaces (triangulated-surface census; 3 types
  on 6 vertices; manifold tables to n=12).
  https://page.math.tu-berlin.de/~lutz/stellar/surfaces.html
- nLab, real projective space (homology/cohomology; `H_1(RP^2) = Z/2`).
  https://ncatlab.org/nlab/show/real+projective+space
- B. Benedetti / F. H. Lutz, Library of Triangulations (torsion examples at
  n≥8, e.g. `d2_n8_3torsion`, `d2_n8_4torsion`, `d2_n9_5torsion`, Hadamard
  `HMT_*`). https://page.math.tu-berlin.de/~lutz/stellar/library_of_triangulations
- F. H. Lutz, Enumeration and random realization of triangulated surfaces
  (arXiv:math/0506316); T. Sulanke / F. H. Lutz, Isomorphism-free
  lexicographic enumeration (arXiv:math/0610022) — manifold-only scope.
- A. Hatcher, Algebraic Topology, Ch. 2–3 (simplicial homology, SNF, UCT
  background methods).
