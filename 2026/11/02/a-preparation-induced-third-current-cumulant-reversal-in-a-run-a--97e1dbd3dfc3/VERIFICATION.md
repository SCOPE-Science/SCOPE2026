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

The `verify.py` program independently evaluates conditional crossing probabilities using a Poisson flip-count/beta-mixture representation and a Bessel-propagator integral. It checks sampled cumulant values and the exact difference polynomial, short-time coefficients and the Gaussian-limit integral. Its finite collection of parameter tests does not prove the full parameter-uniform statements: the proof uses exact algebra, Poisson one-flip expansions and the bounded-jump martingale central limit theorem.

An approximate numerical zero near \(\gamma t=0.6703493\) is a diagnostic, not a certified unique zero. The analytical theorem asserts only existence of at least one finite-time zero. Scientific publication priority and independent review have not been determined.
