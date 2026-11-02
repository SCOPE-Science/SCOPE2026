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

# Verification notes

Run `python verify.py` with Python 3 and its standard library. The checker constructs normalized Gaussian weights, computes local means, uses the exact unbiased covariance denominator, and performs the source-defined deterministic update independently of the reduced iteration. It checks gridwise agreement for many interior positions, amplitudes, radii, and strictly positive ridges; invariant interval and basin behavior; and critical square-root convergence at a large finite iteration count. On the reviewed script it reports `PASS: 2095 supplementary checks; critical predicted sqrt(n) amplitude 1.858735590337`.

An exact symbolic calculation of the finite three-point weighted sums gave the displayed covariance expressions and positive denominator. The proof in `RESULT.md` supplies the genuinely infinite assertions: strict concavity for the full fixed-point diagram, convex relaxation for global convergence, asymptotic inverse-square increments for the critical rate, and the analytic inversion identity for both branch asymptotics.

No finite script certifies every real parameter or proves that no stronger historical result exists. The theorem is for an exact fixed positive ridge without stochastic observation perturbations. Independent external audit and experimental validation are not performed.
