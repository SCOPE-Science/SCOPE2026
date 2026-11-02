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

# Reproducibility and limits

Run `python3 checker.py` using the standard Python 3 library. The checker independently enumerates full weighted attachment histories for integer reinforcement exponents and coefficients, compares exact rational distributions with the reduced Markov count, and checks exact moments and numerical asymptotic scales. Its recorded outcome is `VERIFIED 856 independent exact/numeric assertions`.

The proof is in `RESULT.md`. The finite checker verifies sample instances and arithmetic, but does not certify an almost-sure theorem, a central limit theorem, or infinite-time tail asymptotics; these follow from the stated martingale and Bonferroni arguments. The two papers with time-varying and nonlinear reinforcement use distinct mechanisms, and none of the cited research constitutes an independent priority or proof audit. No independent audit has been performed.
