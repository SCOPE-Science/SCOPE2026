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

# Reproducibility and mathematical scope

Run `python verify.py` with Python, `sympy==1.14.0`, and `mpmath==1.3.0` (versions in `requirements.txt`). The checker performs exact rational Schur-complement and Frobenius-loss reconstructions on a systematic collection of small dimensions, and high-precision special-function evaluations of the stated asymptotic regimes and fixed-threshold tail. Expected output: `PASS 957 exact-algebra and high-precision checks`.

The universal probability statements follow from the Gaussian Schur complement, beta-gamma independence and integral arguments in `RESULT.md`. In particular, 957 finite checks do not exhaust all sketches, dimensions or positive moment orders. No full-scale numerical performance benchmark, independent audit, or finite-precision numerical-stability guarantee is asserted.
