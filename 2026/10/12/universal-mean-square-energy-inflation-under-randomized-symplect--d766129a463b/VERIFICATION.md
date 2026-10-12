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

# Reproducibility and scientific boundaries

Run `python verify.py` under Python 3.10 or later; only standard-library `fractions` and `itertools` are required. The program verifies exact covariance conjugation and fixed-step invariant forms for six rational steps, the rational mixed-step moment matrix, all three characteristic coefficients and positivity of the witness root, decay of the mean-state matrix, 762 explicitly enumerated finite histories across 21 expected squared-norm checks, and exact jitter Rayleigh-quotient identities at ten rational parameter pairs. The program prints `verification passed` upon success.

The all-distribution spectral-radius assertion uses finite-dimensional proper-cone Perron–Frobenius theory, strict determinant concavity, and the absence of real eigenvectors for elliptic step matrices; finite enumerations do not certify the universal quantifier. The eigenvalue expansion is a local analytical perturbation statement; the checked rational identities are its inputs, not a replacement for perturbation theory. No claim is made about almost-sure divergence, elapsed-time scaling, or nonlinear oscillators. No independent audit has been conducted.
