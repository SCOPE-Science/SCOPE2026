---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the sharp single-edge damage theorem

The result follows from a self-contained induction on the total number of old graph edges. Its nonstandard ingredient is the deterministic statement that deleting one vertex reduces the matching cardinality of ordered-edge greedy matching by either zero or one, when the same relative order is retained. The exact first-edge recursion then shows the added-edge difference satisfies an affine recursion over strictly smaller graphs. The analysis splits according to whether the inserted edge's endpoints have at most one incident old edge or at least two.

The standalone file `verify_greedy_matching.py` checks the first-edge recurrence using exact rational arithmetic for all labeled simple graphs with \(2\) through \(6\) vertices; all missing-edge insertions; all single-vertex deletions; direct edge-order enumeration for smaller graphs; and exact sharp witnesses. Running `python verify_greedy_matching.py` on the reviewed file yields `PASS: exact assertions 945204 cached expectations 33866`. The checker's finite scope does not imply universal correctness by itself; the proof supplies that step.

The claim's limits: unweighted simple graphs and uniform random edge-order greedy matching; one inserted nonedge; only expectation, not realized pathwise matching size. Full historical priority, especially against older inaccessible literature, remains unproved. No independent mathematical audit has been conducted.
