# N4 has an F7^−-fragile double-deletion pair (0,1) — a certified fragile seed above the dyadic census

## Context

Dyadic matroids (representable over both GF(3) and GF(5)) are a central open
Rota-type frontier. Brettell–Pendavingh enumerate the dyadic excluded minors up
to 15 elements (U2,5, U3,5, F7, F7*, AG(2,3)\e family, T8, N1, N2, N3) and exhibit
a single 16-element excluded minor N4 = [I8 | A4] (Section 5), the first
obstruction beyond the census. The general excluded-minors-are-almost-fragile
program (Brettell–Clark–Oxley–Semple–Whittle) predicts fragility only up to
Δ–Y equivalence with bounded alternatives, and explicitly flags dyadic
F7^−-fragile structure as "some way off". No source publishes a concrete
fragile deletion pair for N4.

## Definitions

- N4 = [I8 | A4] over GF(3), rank 8, 16 elements, with A4 (rows in order):
  ```
  2 0 2 1 2 1 0 0
  2 1 0 2 0 2 2 0
  2 0 2 0 0 1 0 0
  2 0 2 2 2 2 2 2
  0 1 1 1 1 1 1 1
  2 1 0 0 0 2 0 0
  2 0 0 2 2 2 2 0
  1 0 1 2 1 2 1 1
  ```
  Ground set: 0..7 = identity columns, 8..15 = A4 columns in row order.
  N4 is self-dual, so transpose conventions give an isomorphic copy.
- F7^− (non-Fano) reference model over GF(3):
  e1, e2, e3, (1,1,0), (0,1,1), (1,0,1), (1,1,1);
  rank 3, 29 bases, exactly 6 three-point lines
  (0,1,3),(0,2,5),(0,4,6),(1,2,4),(1,5,6),(2,3,6), degree sequence [2,2,2,3,3,3,3].
  Six lines (not seven) certifies non-Fano.
- Minor rank oracle: r_{M/C\D}(X) = r(X ∪ C) − r(C) over GF(3).
- 3-connected: no X with 2 ≤ |X| ≤ |E|−2 and λ(X) = r(X)+r(E\X)−r(E) < 2.
- N-fragile: has an N-minor and every element is non-flexible (for each e, at
  least one of M\e, M/e has no N-minor).

## Result (headline claim)

Let N4 be the 16-element dyadic excluded minor above, with the labelling
convention stated. The ordered pair (a,b) = (0,1) satisfies:

1. N4\0\1 (14 elements, rank 8) is 3-connected (full-subset min-λ = 2);
2. N4\0\1 has an F7^− minor via S = [2,3,4,5,6,12,13] (kept),
   C = [9,10,11,14,15] (contracted), D = [7,8] (deleted), with permutation
   perm = [0,3,1,4,2,5,6] carrying the 29 minor bases exactly onto the F7^− bases;
3. N4\0\1 is F7^−-fragile, with the complete table:

| e | delete has F7^− | contract has F7^− | fragile |
|---|---|---|---|
| 2 | yes | no | yes |
| 3 | yes | no | yes |
| 4 | no | yes | yes |
| 5 | yes | no | yes |
| 6 | yes | no | yes |
| 7 | yes | no | yes |
| 8 | yes | no | yes |
| 9 | no | yes | yes |
| 10 | no | yes | yes |
| 11 | no | yes | yes |
| 12 | no | yes | yes |
| 13 | no | yes | yes |
| 14 | no | yes | yes |
| 15 | no | yes | yes |

In words: {2,3,5,6,7,8} are delete-only, {4,9,10,11,12,13,14,15} contract-only;
all 14 elements fragile.

## Proof / evidence (exact computation)

- Rank is exact GF(3) Gaussian elimination on bitmask column sets (memoized).
- 3-connectivity is the full subset λ scan (2^14 = 16384 subsets, no sampling):
  min-λ = 2; no loops, no parallel pairs. N4 itself re-scanned 3-connected.
- F7^− minor search is exhaustive: every 7-subset S × every contraction subset C
  of the complement, with simplicity + rank-3 check, line-count/degree prefilter,
  and full S7 (5040) permutation bases-set isomorphism against the F7^− model.
  The stored certificate additionally satisfies exact perm-carried bases equality.
- Fragility runs the exhaustive minor search on all 28 single-element
  deletion/contraction sides; every "negative" side is certified by exhaustive
  failure over all (S,C) models, so the verdict is exact, not heuristic.
- Three independent code paths agree: finder `n4_fragile.py` (search + writer),
  independent verifier `verify_n4.py` (separate code path, re-searches all 28
  sides), and the audit's fresh-path replay `audit_replay.py`
  (AUDIT_REPLAY_OK: rank 8, min-λ 2, 14/14 rows, table_match=True).

## Limitations

- Element names (0,1) refer to the stated [I8|A4] column order; an isomorphic
  copy of N4 carries the corresponding pair under the isomorphism.
- The general ≥17-element spikey-exclusion (splice) target is NOT proved here;
  it was separately exited BLOCKED. Only the fallback fragile-seed headline is
  certified.
- Fragility negatives are certified by exhaustive search over the stated GF(3)
  representation's minor models; matroid minor existence is
  representation-independent and the search enumerates all deletion/contraction
  models, so the verdict is exact.

## Reproducibility

- `python3 output/artifacts/n4_fragile.py` — search + certificate writer
  (logged CHOSEN_PAIR 0 1, FRAGILE_ALL True; writes n4_certificate.json).
- `python3 output/artifacts/verify_n4.py` — independent verifier, separate code
  path (logged VERIFY_OK: pair (0,1), 14/14 fragile rows).
- `python3 output/artifacts/audit_replay.py` — audit's fresh-path replay
  (AUDIT_REPLAY_OK). Pure Python 3 stdlib, exact GF(3) arithmetic, seconds-scale.
- SageMath was unavailable in the execution environment, so replay is pure-stdlib
  exact computation certifying the identical three clauses with stronger
  auditability (exhaustive search + bases-set equality) than a CAS transcript.

## References

- N. Brettell, R. Pendavingh, Computing excluded minors for classes of matroids
  representable over partial fields, arXiv:2302.13175v2. (§5 N4; Thm 1.1 census;
  Thm 2.9 trichotomy; Cor 3.3 GF(11) proxy.)
- N. Brettell, B. Clark, J. Oxley, C. Semple, G. Whittle, Excluded minors are
  almost fragile, arXiv:1603.09713v2. (Thm 1.1 bounded-or-fragile up to Δ–Y;
  intro p.2 dyadic F7^− barrier.)
- B. Clark, Fragility and excluded minors (PhD thesis). (Conditional fragility;
  U2,5/U3,5-fragile structure for U2/H5 fields.)
- N. Brettell, The excluded minors for GF(5)-representability on 10 elements,
  Matroid Union. (A1–A4 matrices; N1–N4 account; stabilizers of interest.)
