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

## Reproduction
Run `python3 verify.py` in the same directory. It has no third-party dependencies. It reports exact polynomial and rational-integral checks plus independent numerical checks of spherical-support integration. The check code tests selected rational parameters and the polynomial identity coefficient-wise; the proof for all real parameters is in RESULT.md.

## Verified steps and boundaries
The normalized polar-section integral and its antiderivative are written explicitly in RESULT.md. The code checks the exact antiderivative evaluation at rational parameters and the all-parameter polynomial identity. The monotonicity derivative is shown algebraically and tested at rational parameters. The cylinder limit follows from uniform support-function convergence and is not inferred from numerical samples.

## Limits of verification
No external mathematical audit has been performed. The standalone checker does not certify the uniqueness of the Santaló point, the general Fubini theorem, the global historical novelty assessment, or any theorem outside the exact three-dimensional capsule family. Those facts are justified analytically or stated as residual uncertainty in the proof and review.
