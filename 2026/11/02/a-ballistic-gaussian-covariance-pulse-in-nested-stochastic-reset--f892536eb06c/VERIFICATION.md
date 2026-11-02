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

The accompanying `verify_pulse.py` was run directly against the package candidate in a Python environment providing NumPy and SciPy. It reported `checks_passed 728`.

The program builds the stationary covariance independently from the finite-particle generator's second-moment balance, propagates its full covariance using an independent matrix exponential, and compares it with the closed first-to-depth forward and reverse covariance. It checks several combinations of chain depth, diffusivity, reset rate, and lag. It also tests the exact one-dimensional optimum identity and the large-depth Gaussian-pulse approximation numerically.

Analytically decisive checks are distinct: (i) independent-clock Brownian genealogy gives a unique finite-second-moment stationary law; (ii) the generator gives static covariances and conditional-mean dynamics; (iii) a strictly decreasing positive polynomial quotient has one positive root; (iv) a geometrically dominated asymptotic expansion locates the root; and (v) Stirling's formula and dominated convergence yield the Gaussian pulse. Finitely many numerical checks cannot establish the infinite-depth limit or priority.

Scientific restrictions: equal reset rate, finite-depth stationarity before the increasing-depth limit, independent Brownian coordinates, zero fixed first reset point, deterministic one-sided copying, and fixed positive diffusivity and reset rate. No independent audit has been performed.
