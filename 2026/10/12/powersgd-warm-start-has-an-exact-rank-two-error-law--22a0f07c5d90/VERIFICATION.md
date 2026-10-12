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
The package reconstructs rank-one PowerSGD on a fixed rank-two matrix.

`verify.py` checks the direct matrix compression against the pointwise residual formula for multiple singular-value ratios and reuse depths. It then integrates over the isotropic Gaussian direction and compares with the exact expected-error factor
\[
1+\frac{\kappa^2-1}{\kappa^{2t-1}+1}.
\]

It separately checks the random-start geometric-mean residual and the one-reuse simplification.

Numerical integration is a transcription guard only. The expectation is evaluated analytically in `RESULT.md`.
