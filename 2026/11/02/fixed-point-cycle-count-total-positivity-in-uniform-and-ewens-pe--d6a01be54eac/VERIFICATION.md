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
Extract `verify.py` from this package and run `python3 verify.py`; no external dependencies.

The test performs 867,572 exact integer/rational checks: all joint minors for the full finite index range through 27, independent generation of each permutation through 8, checks of the recurrence identities and log-concavity through 160, and uniform covariance checks. The test prints a PASS line only after all checks succeed.

The general theorem for all integers follows from the explicit symbolic proof in RESULT.md, including the real-symmetric tridiagonal matrix argument, the coupled determinant recurrences and positive-support propagation. A finite enumeration does not certify all sizes. The independent audit has not been performed.
