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

Run `python3 verify.py` from the extracted package root; it requires only the Python 3 standard library. The exact-rational checker verifies the two specialized closed-form cell variance identities for 200 consecutive cell indices and the resulting finite-sample variance formulas for seven sample sizes. It also verifies the analytic power-grid optimization constant in a separate rational parameter case and compares that constant with two nonoptimal supercritical admissible power grades. Last run produced:

`VERIFY_OK exact cell variances; exact finite-n laws; optimal-grade benchmark`

The actual infinite-series and Gaussian limits are proved in RESULT.md via finite-variance summability, bounded-innovation estimates, Hoeffding's lemma, and the Lindeberg–Feller theorem. The checker is not presented as a certificate of infinite claims. No independent scientific audit or verification has been performed. The principal remaining scientific issue is independent comparison against potentially overlooked classical graded stochastic-quadrature literature.
