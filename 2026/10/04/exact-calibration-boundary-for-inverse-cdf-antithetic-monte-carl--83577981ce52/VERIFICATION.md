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

`verify.py` checks, in exact rational arithmetic for \(1\le B\le200\), the beta-binomial identity, total probability one, the support-point CDF, the first failing support threshold, and the maximal additive excess. It also checks the \(B=1\) mass vector \((1/4,1/2,1/4)\).

These finite checks are supplementary. The theorem for arbitrary \(B\) is proved analytically in `RESULT.md`. No claim is made for arbitrary antithetic permutations, discrete null laws, or estimated null distributions.
