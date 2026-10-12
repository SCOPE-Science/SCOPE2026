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

The all-\(m,N,k\) proof is combinatorial. The checker supplies exact finite consistency tests only.

For every \(2\le m\le6\) and \(2\le N\le7\), `checker.py` enumerates every multinomial count vector, assigns its exact rational probability, conditions on every feasible occupied-cell count \(K=k\), and computes the exact conditional mean and variance of Pearson's statistic. It then compares those values to the Stirling-number formulas.

The checker also verifies the affine pair-collision representation used by the proof. No bounded enumeration is used to justify the infinite quantifiers.
