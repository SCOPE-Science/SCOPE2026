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

Execute `python3 verify.py` from this directory. The checker constructs shortest-path distances by breadth-first search, independently enumerates all scale-one and scale-two simplices for six small part configurations, and computes their mod-two Betti numbers by exact bitwise Gaussian elimination. Six additional configurations test the complete distance partition and scale-two join graph. The checker returns `VERIFY_OK` only after every assertion succeeds.

Checked homology configurations are `(2,2)`, `(2,3)`, `(2,4)`, `(3,3)`, `(2,2,2)`, `(2,2,3)`. Checked distance-only configurations are `(2,3,4)`, `(2,2,2,2)`, `(3,3,3)`, `(2,4,5)`, `(2,2,2,3)`, `(2,2,2,2,2)`. The exact code and full inputs are included in this package.

The all-parameter statement and integer representation are proved mathematically in `RESULT.md`; finite mod-two computations are not an exhaustive test of all sizes or an independent certificate of integral homotopy. The verification and scientific review are not independent audits.
