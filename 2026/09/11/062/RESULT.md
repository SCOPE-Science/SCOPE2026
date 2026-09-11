# One-descendant psi-marked floor-diagram ledger for Hirzebruch bidegree (3,4)

## Context and motivation

Stationary descendant Gromov-Witten invariants with psi classes extend the refined
tropical correspondence toward mirror symmetry (J-function coefficients) and logarithmic
GW theory with descendants. General machinery exists: tropical psi-classes (Markwig-Rau),
psi-floor diagrams with Caporaso-Harris recursion (Block-Gathmann-Markwig), stationary
descendant floor/Fock correspondence for toric and Hirzebruch surfaces
(Cavalieri-Johnson-Markwig-Ranganathan), descendant log-GW/tropical correspondence
(Mandel-Ruddat), and recursive descendant-with-line formulas in the plane
(Blomme-Markwig). What was missing was a concrete Hirzebruch multifloor cell with a
psi insertion: a first exact ledger tests whether the psi-marking rule stays purely
combinatorial at interacting size and supplies a reusable descendant benchmark for
generating-series and log-descendant comparisons at adjacent bidegrees.

## Definitions and fixed data

- Surface: F0 = P^1 x P^1 (Hirzebruch parameter k_surf = 0); class beta = 3B + 4F (a = 3, b = 4).
- Genus g = 0, n = 4 floor vertices. Relative data in CJMR Notation 2.2 / Definition 4.1
  conventions: ordered phi = (-2,-2,1,3), i.e. n1 = 4 fixed non-thick ends (two left ends
  of weight 2, right ends of weights 1 and 3); mu = () (n2 = 0 moving ends).
- Descendant vector: exactly one vertex carries k = 1 (psi^1 insertion); others k = 0.
  The plus-line condition is the fixed horizontal-line (y-coordinate) condition selecting
  the floor-decomposed position in the horizontally-stretched setup; every other insertion
  is tau_0(pt).
- Dimension check: n2 + 2a + g - 1 = 0 + 6 + 0 - 1 = 5; n + sum(k) = 4 + 1 = 5. Balanced.
- Sizes s_V in {0,1} with sum s_V = a = 3 (three 1's, one 0). Thickened-half counts
  t_V = k_V + 2 - 2 s_V (g = 0) are nonnegative and sum to 3 = number of compact edges of
  a tree on 4 vertices. Divergence: signed compact-edge-weight sum equals
  -k_surf * s_V = 0 at every vertex (k_surf = 0).

## Local rule (stated verbatim)

Each floor diagram is: an ordered tree on vertices V0..V3, a size pattern (position of the
unique s = 0), an attachment map from the 4 distinct marked ends to vertices, positive
integer compact-edge weights solving the vertex-balance equations (signed compact weights
+ signed end weights = 0 at every vertex), and a thickening orientation (one thickened
side per compact edge) realizing the prescribed thick counts t_V. An s = 0 primary
(k = 0) vertex must carry exactly 2 flags, both thickened, of opposite directions and
equal weights. Vertex multiplicity rule: genus-0 one-point relative invariant at each
vertex; for the small degrees in this census every admissible primary vertex has
multiplicity 1, and the psi-vertex multiplicity for the occurring flag data equals 1.
Hence mult(D) = product of compact-edge weights (unrefined), refined weight = product of
quantum integers [w]_q = (q^{w/2}-q^{-w/2})/(q^{1/2}-q^{-1/2}). The ledger sums over
psi-marked diagrams (psi position p in {0,1,2,3} distinguished):
D(q) = sum_D prod_e [w(e)]_q, D(1) = sum_D prod_e w(e).

## Result (headline claim)

For the above F0 (3,4) data with one psi^1 insertion (dimension 5 = 5), the psi-marked
refined floor-diagram census yields 168 diagrams with unrefined total D(1) = 1464:

| psi position p | # diagrams | D(1) contribution |
|---|---|---|
| 0 | 43 | 352 |
| 1 | 41 | 376 |
| 2 | 41 | 384 |
| 3 | 43 | 352 |
| total | 168 | 1464 |

Refined ledger D(q), t = q^{1/2}, exponents -9..9, symmetric with D(q) = D(q^{-1}):
-9:4, -8:2, -7:18, -6:12, -5:54, -4:44, -3:136, -2:118, -1:244, 0:200,
+1:244, +2:118, +3:136, +4:44, +5:54, +6:12, +7:18, +8:2, +9:4.
In particular D(q)(1) = 1464. Machine-readable table in output/artifacts/ledger.json.

## Proof and evidence

Exhaustive census: 16 ordered Cayley trees x 4^4 end attachments x 4 size patterns x
bounded weights/thickenings, pruned by balance + thick counts + s = 0 rule.
Two independent code paths agree exactly:
(a) enumerate.py (tree-first, fractional Gaussian elimination) gives per-psi
(43,352),(41,376),(41,384),(43,352), total 168 diagrams, D(1) = 1464;
(b) recount2.py (attachments-outer loop order, compact weights by bounded brute force
1..4 with no shared linear solver, independently rewritten thickening/s=0 checks)
reproduces all numbers plus the identical symmetric D(q) table and prints RECOUNT2_OK.
verify.py audits vertex balance on every diagram. Reproduction:
python3 output/artifacts/enumerate.py, python3 output/artifacts/recount2.py,
python3 output/artifacts/verify.py (prints VERIFY_OK for recount + partition).
Recursion/degeneration step: partition by attachment vertex of the distinguished
weight-3 right end R2 gives disjoint exhaustive unrefined weights
{V0: 4, V1: 26, V2: 116, V3: 1318} summing to 1464 = D(1); per-(psi,R2) refinement in
ledger.json. A 3-vertex truncation with ends (-2,-2,1) was tested as a smaller-data
partner and found dimension-mismatched (total 0), so it is explicitly NOT used; the
certified recursion identity is the exact R2-end partition verified numerically.

## Limitations

- The certified object is the psi-marked floor-diagram ledger under the rule above; its
  equality to the geometric descendant GW invariant additionally invokes the general
  floor-diagram degeneration correspondence (CJMR Theorem 4.9 style) and the genus-0
  vertex remark, cited not re-proved here.
- "No (3,4) psi-line ledger exists" is a literature-triage statement, not a theorem.
- Convention-sensitive filters (e.g. extra 4-total-flag or s_p = 1 requirements at the
  psi vertex) give different sub-ledgers (256 resp. 200) and are not the headline; the
  headline uses the full psi-marked census with no extra flag filter.
- The R2-partition is an internal same-census consistency decomposition, not an
  independent smaller-data derivation.

## Reproducibility

Stdlib-only Python 3 scripts; deterministic exhaustive loops; no external packages.
Artifacts: enumerate.py, recount2.py, verify.py, ledger.json. All scripts print
deterministic summaries; recount2.py asserts 168/1464 and symmetry; verify.py asserts
balance per diagram and partition sum.

## References

- Cavalieri-Johnson-Markwig-Ranganathan, Counting curves on Hirzebruch surfaces:
  tropical geometry and the Fock space, arXiv:1706.05401.
- Markwig-Rau, Tropical descendant Gromov-Witten invariants, doi:10.1007/s00229-009-0256-5.
- Blomme-Markwig, Tropical descendant invariants with line constraints, doi:10.1112/jlms.12806.
- Block-Gathmann-Markwig, Psi-floor diagrams and a Caporaso-Harris type recursion,
  doi:10.1007/s11856-011-0216-0.
- Mandel-Ruddat, Descendant log Gromov-Witten invariants for toric varieties and
  tropical curves, doi:10.1090/tran/7936.
