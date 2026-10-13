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

The theorem is proved analytically for every \(n\ge2\).

`checker.py` carries out two exact-rational replays. It first enumerates every permutation for \(2\le n\le9\), computes the footrule, squared displacement, and Spearman coefficient, and verifies the stated means, variances, covariance, and correlation-squared identity.

It then constructs the \(L^1\) and squared \(L^2\) displacement arrays for every \(2\le n\le60\), double-centers them exactly, and checks the closed covariance and variance formulas directly from the permutation-linear-statistic identity.

No bounded enumeration is used as a proof of the universal statement.
