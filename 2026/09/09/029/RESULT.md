# Exact GF(3)-Representation Uniqueness Census for Simple Rank-3 Matroids on 7 Points

## Context

Whether a representable matroid is uniquely representable over a given finite
field, and how many inequivalent coordinatizations highly symmetric small
types admit, drives stabilizer, fragility, and representation-search questions
in Rota-type structural theory (Geelen–Whittle inequivalent-representations
program). Rank 3 on 7 points is the first window where ternary
representability is nontrivial (Fano obstruction, non-Fano and Pappus
fragments), so the exact uniqueness-versus-multiplicity boundary there is a
natural classification question and a benchmark for coordinatization
algorithms.

Nearest prior results give no exact per-type table for this slice:
Geelen–Whittle prove a finiteness bound f(p) for 4-connected/k-coherent
matroids over GF(p) (arXiv:1101.4683); Kingan defines geometric equivalence
(row operations, column scaling, permutations/automorphisms) and a generation
method (arXiv:1202.2247); Mayhew–Royle catalogue all matroids to 9 elements
with counts and representability labels (math/0702316). Focused searches for
inequivalent/uniquely representable matroids return only GF(5)/Hydra
partial-field classifications or asymptotic/structural theorems.

## Definitions

- Ground set {0,...,6}. A simple rank-3 matroid is encoded by its family of
  nontrivial lines (maximal collinear sets of size >= 3); every pair lies in
  at most one line (pair-cover / linear-space axiom). Bases are the triples
  contained in no line; nonbases are the triples contained in some line.
- A 3x7 matrix over GF(3) coordinatizes a type if its zero-determinant column
  triples equal exactly the type's nonbases.
- Normalized frame: fix an ordered basis B, normalize B -> I_3, remaining 4
  columns range over the 13 points of PG(2,3) (13^4 = 28561 candidates per
  basis, 35 triples per type). Simple types exclude repeated / frame-point
  free columns.
- Labeled inequivalence: row operations + column scaling. Once a frame basis
  is fixed, the residual action is the V4 diagonal group (8 diagonal
  scalings modulo overall scalar, order 4). Geometric inequivalence further
  quotients by the matroid automorphism group (Kingan's notion).

## Result

Regeneration from the rank-3 pair-cover axioms gives 8390 pair-covers total:
1 rank-2 (single 7-line) plus 8389 labeled simple rank-3 families, falling
into 23 isomorphism types (full-S_7 orbit-sum check sum 5040/|Aut| = 8389).
Every type passes an explicit symmetric basis-exchange check.

**Theorem (machine-checked).** Of the 23 simple rank-3 types on 7 points:

- Exactly 4 types are GF(3)-representable (artifact ids 18, 19, 20, 21 below).
- Each ternary type admits exactly 4 normalized frames per basis, forming a
  single V4 orbit — hence exactly 1 labeled inequivalent representation and
  exactly 1 geometric inequivalent representation. Every ternary type in this
  slice is uniquely GF(3)-representable under both notions; there is no
  multiplicity maximizer strictly above 1 (all four ternary types tie at
  multiplicity 1).
- The remaining 19 types are certified non-GF(3)-representable: the
  exhaustive all-35-bases scan finds zero frames for every basis, which is a
  complete proof since any representation has some basis normalizable to I_3.

Explicit representatives (columns 0–6; frame basis {0,1,2} = I_3; rows shown
left to right, entries in {0,1,2} = GF(3)):

| type | nontrivial lines | |Aut| | #bases | matrix |
|---|---|---|---|---|
| 18 | 0456, 124, 135, 236 | 6 | 28 | `1001011 / 0101121 / 0011212` |
| 19 | 0456, 1234 | 72 | 27 | `1000011 / 0101112 / 0011221` |
| 20 | 034, 056, 135, 146, 236, 245 | 24 | 29 | `1001111 / 0101221 / 0011212` |
| 21 | 034, 056, 123, 145, 246 | 12 | 30 | `1000111 / 0101121 / 0011112` |

Total normalized frames (all bases): {112, 108, 116, 120} = n_bases x 4.
Type 22 (non-ternary) is the Fano plane F_7 (seven 3-lines, 28 bases, |Aut| =
168), the classical ternary obstruction. Type 0 is U(3,7) (no lines, 35
bases, |Aut| = 5040), non-ternary.

## Proof / Evidence

Exhaustive enumeration, replayed by an independent verifier (fresh code path)
printing VERIFY_OK (re-executed by the auditor):

1. Pair-cover backtracking enumerates 8390 covers (= 8389 rank-3 + 1 rank-2);
   full-S_7 canonical dedup gives 23 pairwise non-isomorphic types with
   orbit-sum 8389; symmetric basis-exchange checked per type.
2. Full-S_7 automorphism orders recomputed and matched; labeled counts
   5040/|Aut| cross-checked by the orbit-sum identity.
3. All-bases ternary scan (35 bases x 28561 candidates per type) replayed:
   ternary types 18–21 with per-basis frame count exactly 4 (one V4 orbit);
   all other types zero frames on every basis. Auditor independently
   re-enumerated every basis of the 4 ternary types and confirmed exactly 4
   frames each.
4. Explicit 3x7 matrices replayed: zero-determinant triples equal exactly the
   listed nonbases. Auditor decoded stored repquads to row strings and
   confirmed the table above.

Completeness argument: any GF(3)-representation has some ordered basis
normalizable to I_3, so scanning every basis with all PG(2,3) free-column
choices is exhaustive; non-representability certificates are the empty scan
on all bases.

## Limitations

- GF(3)-specific; no claim about other fields.
- Equivalence follows Kingan's labeled/geometric notion (row operations,
  column scaling, optionally matroid automorphisms); other coarsenings of
  "inequivalent" are not addressed.
- Types are unlabeled-isomorphism classes on a fixed 7-set; labeled counts
  are 5040/|Aut| orbit sizes. Type ids 0–22 are artifact-local, not standard
  catalogue numbers; cite line families, not bare ids.
- The "maximizer" is degenerate (4-way tie at multiplicity 1); the
  substantive headline is the uniqueness classification itself.

## Reproducibility

- `output/artifacts/full_census.json`: 23-type table (lines, |Aut|,
  n_bases, ternary flag, allframes totals, repquad, labeled/geometric counts).
- `output/artifacts/verify.py`: independent verifier (pair-cover validity,
  exchange axioms, full-S_7 Aut orders, fresh backtrack count 8390,
  all-bases ternary replay, per-basis single-V4-orbit check, matrix
  basis-equality). Run from the record root: `python3
  output/artifacts/verify.py` prints `VERIFY_OK`.

## References

- J. Geelen, G. Whittle, Inequivalent Representations of Matroids over Prime
  Fields, arXiv:1101.4683.
- S. R. Kingan, Unlabeled equivalence for matroids representable over finite
  fields, arXiv:1202.2247.
- D. Mayhew, G. F. Royle, Matroids with nine elements, arXiv:math/0702316.
- R. A. Pendavingh, S. H. M. van Zwam, Confinement of matroid representations
  to subsets of partial fields, arXiv:0806.4487; Lifts of matroid
  representations over partial fields, arXiv:0804.3263 (GF(5)/Hydra-k
  inequivalent-representation classifications — different field).
