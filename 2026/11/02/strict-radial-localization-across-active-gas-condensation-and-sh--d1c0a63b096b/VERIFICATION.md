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

Run `python3 verify_quantile.py` with Python 3. No packages beyond the standard library are used. The independent numerical implementation inverts the gas-profile logarithmic equation by bisection, instead of computing it from the mass quantile expression, and then checks that the survival probabilities at the analytical quantiles equal their target levels.

The saved script passed 3,123 deterministic assertions, checking \(m\in\{4,5,10,20\}\), reset-scale parameters straddling the phase boundary, interior and tail survival levels, strict stochastic order, supersaturated gas versus droplet order, a universal quantile derivative jump, gas mass normalization, the exterior-density translation identity, and the small-reset first-order total-variation coefficient. Numerical quadrature estimated \(\Delta_4\approx0.3784\), \(\Delta_5\approx0.4721\), \(\Delta_{10}\approx0.6761\), and \(\Delta_{20}\approx0.8046\). Bisection and quadrature checks are finite supporting consistency tests, not proofs that inequalities hold for uncountably many parameter values.

The complete analytical argument is in `RESULT.md`. Its critical steps are the gas current-mass identity \(d(g-g^2/m)/dy=-g\), continuity and positivity of the piecewise quantiles, the explicit sign of their derivatives, exact translated-tail equality, and uniform small-reset analytic inversion. The claim is limited to the normalized symmetric stationary continuum mean-field density under instantaneous local resetting; no claim about microscopic finite-particle stationary distributions, independence of external audit, or temporal convergence is made.
