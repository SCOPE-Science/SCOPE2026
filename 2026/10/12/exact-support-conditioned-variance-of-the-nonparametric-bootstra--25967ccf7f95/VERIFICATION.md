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

The proof is exact for every \(N\ge2\), every resample size \(b\ge1\), every feasible support size \(k\), and every fixed real dataset with finite empirical variance.

`checker.py` enumerates every bootstrap sequence for \(2\le N\le6\) and \(1\le b\le7\). Within every support-size stratum it verifies the exact conditional mean and conditional mean-squared fluctuation. It also verifies the unconditional support-size/squared-error covariance for every \((N,b)\) pair.

All verification arithmetic is exact. The finite census is supplementary and does not establish the universal quantifiers.
