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

Run `python verify.py` in the same directory as the result files with Python 3 and SciPy available. The script calculates finite Laplace-convolution densities in two mathematically equivalent but independently implemented ways (partial fractions and numerical Fourier inversion), checks the original negative-rescaling hitting-time relation after determining its previously unknown boundary constant, checks the previously known positive-rescaling formula, and tests rigorous error enclosures at finite truncation depths. The finite suite is a numerical consistency test, not a proof for all reset parameters; the mathematical proof and explicit error inequalities are in `RESULT.md`.

The certified inequalities are valid in exact real arithmetic. Finite floating-point error and ill-conditioning near the contraction boundary are not themselves covered by the mathematical certificate; arbitrary-precision arithmetic or rigorous interval arithmetic is required for machine-verified numerical enclosures near difficult parameters. No independent scientific audit has been performed.
