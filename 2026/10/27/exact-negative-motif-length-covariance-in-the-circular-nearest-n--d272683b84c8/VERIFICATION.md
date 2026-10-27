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

# Verification record

The standalone `verify.py` uses exact `fractions.Fraction` arithmetic and enumerates every cyclic gap rank permutation of size \(n=5,6,7,8\), checking the mutual-nearest-neighbor pair mean, variance, the conditional mean of the total directed length, and their mixed covariance. The Dirichlet order-statistic mean is calculated from a harmonic sum, not estimated by simulation.

The script also verifies rational constants for the local exponential moments and the aggregate variance and covariance algebra. Those checks are finite diagnostics; the proof in `RESULT.md` establishes all integer \(n\ge5\) using exponential spacings and finite exact integrals. No external audit or formal certification was performed.
