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

# Reproducibility and proof limits
The analytic result is fully contained in `RESULT.md`: the support calculation, exact Gaussian normalization, strict coupling argument, and the central-limit and law-of-large-numbers arguments establish its universal scope. A numerical experiment is not an infinite-dimensional certificate.

Run `python checks/mean_width_check.py` with Python 3, NumPy, and SciPy. The script has deterministic numerical inputs and requires no internet or external datasets. It verifies 1,920 direct vertex-support cases; an independently known triangle mean-width value of \( (2+\sqrt{2})/\pi \); finite-width reflection and strict balancing through total dimension twelve using quadrature; and five evaluations of the critical scaling function. On construction the checker returned all PASS messages. Numerical tolerances are explicit in the code; the analytic theorem has no dependence on them.

The one-dimensional Fourier integral is the chosen exact finite-dimensional evaluation. It converges without finite-data interpolation, and its quadrature in the checker is a numerical cross-check only. No independent review or external proof certification has been performed.
