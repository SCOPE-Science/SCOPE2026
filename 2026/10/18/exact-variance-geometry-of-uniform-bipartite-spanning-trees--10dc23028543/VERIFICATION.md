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

The finite computation in `verify_covariance.py` uses only standard Python (`fractions`, `itertools`). It generates all spanning trees for the six graph sizes \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\), checks that the counts agree with the bipartite tree-count formula, constructs all one-edge and two-edge moments exactly, and verifies the claimed covariance projector decomposition entry by entry. The exact weight-cost variance is independently evaluated by averaging over all enumerated trees.

Observed output: six graph sizes passed; 4657 spanning trees; 597 covariance-entry comparisons; 2388 projector/eigenvalue comparisons. No probabilistic simulation or floating-point tolerance is used.

These finite checks do not verify arbitrary graph orders. The all-size argument uses the transfer-current theorem and symbolic manipulations of four projector spaces, detailed in RESULT.md. No external independent validation has occurred.
