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
# Reproducibility of computational checks

Run `python3 verify.py` with the standard library. The verifier builds Cartesian rook graphs directly and recomputes distance-two pairs using breadth-first search; it then evaluates the defining hop total Roman conditions without invoking the classification.

The run checks 13 distinct boards from \((2,2)\) through \((6,6)\), enumerating **4,516,156** candidate labelings of weight at most six (including all ternary labelings for orders at most six). With more than six vertices, the no-defender case is impossible below weight seven because every cell must be positive. The output lines record the minimum weights, multiplicities, and incidence types, and the final line is `VERIFY_OK cases= 13 candidate_labelings_tested= 4516156`.

These are finite corroborating checks only. The arbitrary-parameter theorem and all cases of optimality are proved combinatorially in RESULT.md. The source paper's earliest verified online date is 2023-03-30; no independent mathematical audit was performed.
