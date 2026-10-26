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

# Verification

The supplied `verify.py` independently forms the 3-by-3 covariance propagation matrix by applying the noise moment update and the deterministic heat propagator to three symmetric covariance basis matrices. It checks agreement with the analytic Perron formula at 576 deterministic parameter combinations. It also verifies both fixed-mesh step values, the strict cutoff comparison, and small- and large-step asymptotics. Captured stdout is `check_output.txt`. Dependencies: Python 3, NumPy, mpmath.

Reproduce with `python verify.py`; proof of the infinite-horizon assertion is analytic in RESULT.md, not inferred from sampled steps. The spatial basis is continuous and compactly supported; the result does not assume additional spatial smoothness of this noise beyond the stated construction.
