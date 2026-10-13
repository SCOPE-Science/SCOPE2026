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
# Verification

## Analytic claim-to-evidence checks

For any \(n\ge1\) and \(0<t<1\), conditioning on a uniform sample maximum leaves \(n-1\) iid uniforms on \((0,t)\). Binomial first and second moments give the stated closed integral. The ordered-log representation has a strictly positive second derivative in \(t\), and its boundary log terms force a unique interior minimum. Two separate beta covariance calculations yield the exact harmonic covariance, including \(n=1\) and strict negativity for \(n\ge2\). No claim beyond the proved finite-sample null is needed.

## Finite diagnostic checks

Execute `python3 checker.py`; a successful run prints `VERIFY_OK`. The bundled checker performs 100 comparisons of the closed conditional mean with a beta-order-statistic series, verifies the covariance identity as exact fractions for 500 integer sample sizes, and executes 12 separately implemented seeded conditional Monte Carlo cases. It has no nonstandard dependencies. Numerical and finite checks do not establish an infinite theorem; that follows from the displayed algebra and inequalities in `RESULT.md`.

## Scope and limits

All variables are under a fully specified continuous null after probability-integral transformation. The formulas do not apply as stated after estimating null parameters from the same observations. External scholarly comparison remains subject to the risk of undiscovered equivalent presentations. Independent audit has not been performed.
