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

# Verification and reproducibility

Run `python verify_two_level_tree.py` in a Python 3 environment with NumPy, SciPy and mpmath. The code independently builds the graph by breadth-first search. Exact rational and integer arithmetic check the full quadratic form against the invariant-block identities for multiple trees and integer powers. Numerical full-matrix inertia is checked immediately below and above the predicted endpoint for 30 tree sizes; a separate high-precision calculation tests the diagonal scaling against the analytic constant.

Recorded successful run:

```
EXACT_POWERED_DISTANCE_DECOMPOSITION_OK 600
CRITICAL_FULL_MATRIX_INERTIA_OK 30
ROOTED_BINARY_DEPTH_TWO_OK 1.527173088279971
INVERSE_SQUARE_BRANCHING_CONSTANT_OK 5.885848553716
ALL_TWO_LEVEL_TREE_CHECKS_OK
```

The exact code checks are finite diagnostics; the strict positive definiteness of the two-by-two Hankel kernel is proved by a Laplace-transform integral, uniqueness of the critical point uses strict-downward negative-type propagation, and the asymptotic limit follows from uniform Taylor estimates. None of these universal claims rests solely on numerical tests.

Scientific reproducibility is provided; independent mathematical audit and external validation have not been performed.
