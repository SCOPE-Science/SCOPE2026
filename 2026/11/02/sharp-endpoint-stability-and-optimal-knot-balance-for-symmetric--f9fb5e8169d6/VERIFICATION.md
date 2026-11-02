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
# Computational verification

The exact proof appears in RESULT.md. Run `python check.py` (Python 3 with SymPy, NumPy and SciPy). The checker reconstructs all basis inner products, inverts the Gram matrix, verifies the closed row-integral expressions and inequalities by symbolic identities, checks the derivative signs, minimizer and limiting values, then independently integrates the kernel and samples interior evaluation rows for 13 parameter values (533 quadrature/interior-row checks). All checks completed successfully in the submitted run. Quadrature is a finite cross-check, not an all-parameter proof. Independent audit is not performed.
