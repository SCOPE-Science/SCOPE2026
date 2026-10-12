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

The all-sample-size derivation is analytic. `checker.py` supplies an independent finite consistency check only.

For every positive pair \(m,n\) with \(m+n\le14\), the checker enumerates every binary pooled-rank word with exactly \(m\) first-sample labels. Using exact rational arithmetic it verifies:

- the bridge-area identity \(\sum_j B_j=-NQ\);
- Anderson's normalization \(T=S/(mnN^2)\);
- \(\mathbb E Q^2=mn(N+1)/12\);
- \(\mathbb E S=mnN(N+1)/6\);
- the mixed moment \(\mathbb E(Q^2S)\) used in the proof;
- the raw and standardized covariance formulas.

The checker does not use floating point and does not infer the infinite theorem from finite enumeration.
