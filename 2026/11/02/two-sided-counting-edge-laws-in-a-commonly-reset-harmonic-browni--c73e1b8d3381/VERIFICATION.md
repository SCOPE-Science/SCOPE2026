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

# Reproduction and mathematical limits

The proof is in `RESULT.md`. Run `python verify_counting.py` with Python 3 and SciPy. The script uses only deterministic numerical integrations and binomial probabilities. It checks the beta-age-to-occupation CDF inversion, normalization of finite-population binomial mixtures, the lower-edge Taylor coefficient, the Gaussian rounding integral and its gamma closed form, and relative convergence of the inverse-logarithmic all-inside probability.

These checks are finite and numerical. They do not establish the conditional strong law, the infinite-population limit or asymptotic equivalence; those are proved analytically in `RESULT.md`. Approximate convergence is slow at the upper edge and may be especially slow for large reset-to-relaxation ratios. The program records its assertion count at successful completion. No external files or network access are required.
