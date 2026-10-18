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

Execute `python VERIFY.py` with SymPy, NumPy and SciPy installed. The exact-symbolic section checks the two endpoint derivatives and the equal-price identities. Direct full-matrix determinants are constructed independently of the spectral formula, including rational gain values and both boundary cases. A deterministic finite grid checks the three support regimes against one-dimensional numerical maximization, and sampled full matrices independently check determinant and positive definiteness.

The observed output was `PASS: 6682 symbolic, matrix, and finite optimization checks`. Re-run the program from the extracted package path to reproduce this result. The finite calculations do not constitute a proof for all network dimensions, budgets or price levels; the theorem is proved analytically in RESULT.md. There is no independent external audit or formal certification.
