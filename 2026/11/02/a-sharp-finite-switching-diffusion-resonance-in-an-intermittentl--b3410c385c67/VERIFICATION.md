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
# Verification of the stated result

The accompanying `verify.py` is standalone Python source requiring `numpy`, `scipy` and `sympy`. Execute `python verify.py`. A completed execution produced `PASS 1478 independent quadratures, inequalities, symbolic checks` and the exact example rate and diffusion value.

The checker symbolically differentiates the rational Green–Kubo response and verifies the stated polynomial coefficients, critical threshold, quadratic-root characterization, and exact rational example. It separately computes a matrix-exponential velocity autocorrelation with `scipy.linalg.expm` and integrates it numerically over infinite time using `scipy.integrate.quad`, checking the resulting diffusion coefficient against the closed form on 80 independent parameter combinations. A family of monotonicity and unimodality probes supplements the exact sign argument. Near-threshold tests check the inverse-distance limit.

The analytical proof in `RESULT.md` establishes the claim for all quantified real parameters. These numerical tests are finite and do not establish results outside those hypotheses, test non-Poisson switching, prove historical priority or replace independent scientific validation.
