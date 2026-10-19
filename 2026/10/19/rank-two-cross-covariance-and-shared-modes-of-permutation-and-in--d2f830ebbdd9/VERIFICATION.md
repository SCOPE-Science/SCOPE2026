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

# Reproducibility

Run `python3 verify.py` with a Python 3 interpreter; it uses only standard-library modules. The code enumerates the complete permutation spaces through size seven and compares the exact rational cross moments against the formula for every position pair and value pair. It separately checks weighted-inversion displacement identities on every enumerated permutation, exact covariance-matrix ranks for small sizes, and algebraic positive rank-two structure for sizes 3–64. The executed package script returned `PASS: 812 exhaustive cross-covariance entries, 372 structural checks.`

The unrestricted claims derive from the detailed conditioning argument and finite-dimensional Gram/projection reasoning in RESULT.md, not from numerical extrapolation. The tests do not establish general-distribution, nonlinear-independence, or priority claims. No external validation or independent audit has been performed.
