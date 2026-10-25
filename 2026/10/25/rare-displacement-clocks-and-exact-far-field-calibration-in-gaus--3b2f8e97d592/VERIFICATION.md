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

The theorem is derived analytically in `RESULT.md`, using stationary regenerative reward, Gaussian convolution, Poisson summation, exponential-mode domination, and a random-index central limit theorem. The exact conditional weights and all coefficients are displayed there, including the dependence on the arbitrary competing-clock distributions.

`checks/verify.py` is a standalone standard-library verifier. Run `python checks/verify.py` from the package root. It passed 186 deterministic comparisons in the assembled draft: stationary Fourier identities, far-field density constants, the conditional jump-count mean and variance, Gaussian count profiles, exact time–position transforms with exponential clocks, conditional reset-age gamma-mixture moments, and a non-exponential clock example.

Numerical comparisons at finitely many parameters cannot establish the global theorem or its unbounded limits. They serve to catch normalization, derivative, and calibration errors. The Poisson-summation argument is essential for the exponentially small remainder in the count expansions; the finite moment assumption on the jump-labelled duration is essential for the age central limit theorem.

Self-review: passed. Independent audit: not yet performed.
