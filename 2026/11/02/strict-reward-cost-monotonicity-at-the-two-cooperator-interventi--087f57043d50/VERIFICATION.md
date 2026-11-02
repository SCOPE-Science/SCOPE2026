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

The `check.py` supplied with the theorem performs exact-rational absorbing-chain calculations independently of the scale-function closed form. Execute with `python3 check.py` (standard library only). The observed test output was:

`PASS: 182 exact-rational Green-kernel cases; 10000 positive-derivative numerical cases; analytic intermediate bounds.`

The finite tests cover \(N=4,\ldots,10\) for exact rational transition kernels and sampled larger populations for numerical derivatives. They are supplementary to the general symbolic proof in `RESULT.md`; no machine-formal proof, exhaustive real-parameter search, or independent scientific audit has been performed. All modeled probabilities stay strictly positive for finite parameters; absorbing-chain expectations are finite.
