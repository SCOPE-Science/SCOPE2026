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

# Reproducibility of the quadratic variance comparison

Run the included standard-library-only `verify.py` via `python3 verify.py`. It computes the stationary polynomial generator recurrence for all monomials through total degree four, verifies the quadratic Poisson equation, and compares two separate variance formulas: a centered Green–Kubo/Poisson inner product and a jump-plus-diffusion predictable quadratic-variation expectation. It evaluates the Gaussian fourth-order fluctuation rate both from its closed form and by direct integration of the squared known autocovariance, treating coincident relaxation and reset rates separately.

The program ran successfully on the packaged source with **150 exact-rational parameter tuples**, checking variable confinement rates, reset rates, diffusivities and couplings. It checks the exact benchmark at unit parameters, positivity at sampled positive rationals and the algebraic branch of the monotonicity certificate. Its stdout reads:

```
PASS: 150 exact rational parameter tuples; 2 independent Green-Kubo identities
PASS: 2 covariance-matched Gaussian integrals; positivity and monotonicity certificates
PASS: unit-rate variances and universal ratio 68/15
```

The complete continuous-parameter positivity proof, uniqueness of stationary law and central limit theorem are analytic arguments in `RESULT.md`. Rational tests alone do not constitute those proofs. No independent or external audit was conducted.
