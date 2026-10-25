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

# Reproducibility

Run `python check.py` with Python 3, NumPy and SciPy. The script performs deterministic quadratures and determinant comparisons without randomness. In the completed review it printed `PASS 391 deterministic assertions`.

The proof does not use finite truncation as a substitute for its singular-value ordering, the all-mode exponential tilt, or the infinite-distance age saddle. Important limiting operations are controlled analytically in `RESULT.md`. The checker directly corroborates: the Volterra singular functions; the hyperbolic-cosine Gaussian-chaos transform; the off-mode product normalization; the principal Gaussian-product conditional balance; three parameterized saddle and universal-profile identities; and the large-parameter normal scale of the age saddle's asymptotic density. These tests do not constitute independent validation of the theorem.
