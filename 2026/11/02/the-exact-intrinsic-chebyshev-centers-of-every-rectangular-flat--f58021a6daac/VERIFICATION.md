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

# Reproducibility and verification

The analytic proof of sharpness and uniqueness is the five-step argument in `RESULT.md`. It requires no computational completeness assumption.

The standalone script `verify.py` uses only Python's standard library (`fractions`, `math`) and checks exact rational circumcenter/covering identities at seven rational aspect ratios. It additionally evaluates a finite \(80\times80\) grid of targets on each corresponding torus. Run with `python3 verify.py`; the required terminal marker is `VERIFY_OK`. The discrete grid cannot establish universal coverage, and the rational examples cannot establish every real aspect ratio or optimizer uniqueness. The inequalities, triangle covering certificate, and limiting-fiber rigidity supply those analytical proofs.

Independent audit has not been performed.
