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

# Reproducibility and limitations

Run `python checker.py` with Python 3 and numpy installed. The program constructs truncated monomial matrices of exponential-weight affine compositions and checks both cross-product orders against the derived geometric singular-value formulas. Five parameter pairs generate 60 individual tests of the first five singular values and two factor norms; four more checks test equal-slope unit-norm order reversal. The observed result is `PASS: 64 finite numerical assertions`. The formula itself is proved analytically in RESULT.md by exact Weyl–dilation factorization; the computation is neither exhaustive in parameters nor an infinite-dimensional certificate. Independent mathematical audit has not been performed. Publication priority is not independently certified.
