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

# Reproduction and scientific limits

Run `python verify.py` with Python 3 and the standard library; the observed output was `PASS: 8472 checks (finite diagnostics; infinite-family claims proved analytically)`.

The checks rebuild reset distributions from chords through their prescribed mean, verify first and second Fourier moments for interior and boundary points, test isotropic optimal protocols across both sides of the critical rate, and compare fixed-angle effective diffusivities with the equations of Baouche et al. (2024). Direct random sampling of an exponential stationary reset age and Gaussian rotational displacement independently tests the first two angular harmonics for four reset rates. The exact four-angle example is checked as well.

The program intentionally checks finitely many parameter values and random seeds only. It is **not** a computational proof of the universal feasible disk, angular-law uniqueness, or the all-time covariance formula. Those follow from the explicit angular generator, a Markov semigroup calculation, the sharp complex-variance inequality and exact finite-dimensional convex constructions written in `RESULT.md`. The isotropy statement refers to the *centered covariance*, not the entire displacement law. No external independent audit has been conducted.
