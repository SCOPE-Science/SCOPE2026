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
# Reproduction and scope of verification

The independent graph-search verifier, `verify.py`, uses the original adjacency predicate (both row and column unequal) rather than the asserted structural characterization. From every vertex subset it computes connected components using graph search, compares the entire disconnected-by-size distribution with the closed formula, and independently tests whether a disconnected set remains disconnected after any single missing cell is restored.

The exact verified dimension pairs are `(3,3)`, `(3,4)`, `(3,5)`, `(4,4)` and `(4,5)`, totaling 1,151,488 subsets. Expected inclusion-maximal disconnected subsets are generated separately as all full row-column crosses and all four-cell rectangles; the exhaustive graph-search predicate matched those sets exactly. The completed command was `python verify.py` with `ALL PASS; 1151488 subsets checked`. No third-party data or package is required.

The finite experiments independently corroborate the formulas only in the tested cases. They do not establish the all-parameter theorem or novelty; those claims depend respectively on the supplied proof and the documented literature comparisons. An independent mathematical audit has not been performed.
