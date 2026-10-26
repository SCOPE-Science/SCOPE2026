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

# Reproducibility and scientific limits
Run `python3 verify.py` using the standard library. It checks stable-Lévy normalization, the parameter specialization \(\alpha=1\) and \(\Lambda=1/3\), exact right/left mass normalization, conditional overshoot survival, and the factorization of the limiting transform.

The analytic proof in `RESULT.md`, specifically the single-excursion Doob bound, rare-jump boundary-strip estimate, and regenerative identity, is required for the limit. Finite code tests and numerical quadrature are consistency checks only; neither certifies an infinite-dimensional or asymptotic statement. General heavy-tailed metastability and resetting literature may contain wider results; independent priority verification has not been performed. The result does not extend as stated to Brownian flights or moving resetting parameters.
