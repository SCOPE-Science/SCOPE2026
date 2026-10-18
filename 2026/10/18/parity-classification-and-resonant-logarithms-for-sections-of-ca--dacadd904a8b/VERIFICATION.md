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

# Reproducibility and limitations

Run `python verify.py` with Python 3, SymPy and mpmath installed. The recorded command returned:

`VERIFY_OK exact_polynomial=1 exact_log_coefficients=3 numerical_log_profiles=3`

Exact SymPy polynomial integration checks the pushforward density for two 3-balls at equal unnormalized projected radii. Exact generalized-binomial and gamma-function simplifications check the first nonzero logarithmic coefficients for dimension pairs `(2,2)`, `(2,4)`, and `(4,4)`. Three high-precision numerical quadratures, fitted to the analytical expansion, independently check the same coefficients within a specified tolerance. Computation does not prove transcendence or the classification for all integer dimension pairs; those follow from the inverse-sine monodromy and endpoint-logarithm analysis in RESULT.md. No independent external mathematical audit has been performed. The verification script requires only common Python packages and no external data, network or privileged access.
