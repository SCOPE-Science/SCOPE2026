# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/004`  
**Audited source tree:** `cac6a5153987a36a62601848779997e90085ec5a`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS — Directly enumerating the four involutions 123,132,213,321 at n=3 gives A/B occurrence multiset {0:2,1:1,2:1} and C/D {0:1,1:2,2:1}; the displayed per-permutation rows reproduce this. This finite counterexample alone refutes four-way involution equidistribution. Replaying enumerate.py agrees on S7–S9 full-group distributions and the involution split through n=9, but those finite windows do not prove all-n two-class equivalence or settle the full-group conjecture.

## Originality

PASS — Fang et al. explicitly state Conjecture 1 that Class 69 remains equidistributed on involutions. Its n=3 counterexample is a new direct refutation of that exact proposition; the full-permutation Class 69 question remains open in their paper.

## Scientific value

PASS — A hand-checkable minimal counterexample removes a false conjectural direction while preserving the distinct full-group question. The two-class statement is evidenced only through n=9, not asserted as an all-n theorem.

## Prior work and source access

- https://arxiv.org/pdf/2606.14367
- https://arxiv.org/abs/2605.19429

## Scope of the decision

The verdict concerns “Refutation of the involution equidistribution conjecture for Class-69 length-2 mesh patterns” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
