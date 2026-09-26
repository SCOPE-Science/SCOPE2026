# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/088`  
**Audited source tree:** `68182f3619a84d319ffd7a24efdd9e51a2c1764f`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS — Replayed the permutation-model verifier: A5 has class sizes 1,15,20,12,12 and each nonidentity class is inverse-closed. The displayed character table satisfies row orthogonality; the four-class unions give exactly 15 nonempty normal symmetric sets. Character sums with multiplicities 1,9,9,16,25 match the 60-by-60 adjacency spectra. All 15 satisfy the Ramanujan inequality; the tightest is 2+2√5<2√11. Twelve are certified by the absolute-character bound and precisely the three stated unions are not. Simplicity gives connectedness. D*=12 means the smallest attainable degree; it is a vacuous threshold below 12 and is not accompanied by a non-Ramanujan lower-degree example.

## Originality

PASS, finite scope — Hirano–Katata–Yamasaki analyze Frobenius and dihedral families, and Yamasaki analyzes generalized quaternion groups. Those theorems do not supply the A5 normal-set spectra or the 12-versus-3 trivial-estimate split. The character formula and A5 character table themselves are standard; the new contribution is their complete finite evaluation here.

## Scientific value

PASS, bounded — The exact 15-case spectral table and explicit tight margin form a reproducible comparison point for normal Cayley graph methods. It gives no general bound for larger simple groups or nonnormal connection sets.

## Prior work and source access

- https://arxiv.org/abs/1503.04075
- https://arxiv.org/abs/1611.09977

## Scope of the decision

The verdict concerns “Complete Ramanujan classification of symmetric normal Cayley graphs of A5” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
