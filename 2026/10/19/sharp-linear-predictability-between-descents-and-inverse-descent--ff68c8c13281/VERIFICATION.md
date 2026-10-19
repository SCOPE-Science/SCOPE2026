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

Run `python3 verify.py` using Python 3 and the standard library. The deterministic script enumerates all \(n!\) permutations for \(2\le n\le8\), computes the joint covariance blocks with exact rational arithmetic, inverts the tridiagonal marginal covariance independently, and checks the proposed exact canonical correlations and Cauchy–Schwarz bounds. In the recorded execution it passed **497 exact assertions**. No random simulation or numerical tolerance is needed.

The finite enumeration checks are corroboration. The general proof uses the value-swap involution, three-rank covariance calculation, and a solved tridiagonal recurrence. No machine-checked formal proof or independent audit is asserted.
