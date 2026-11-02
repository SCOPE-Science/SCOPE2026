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
Run `python verify.py` with Python 3 and no external dependencies. The script computes finite-field arithmetic and polynomial gcds directly. The checker verifies all tested quartic squarefree-pair counts against the character formula, exact intercept independence, and the slope means and second moments. The recorded successful execution was:

`VERIFY_OK field_orders= [3, 5, 7, 11, 13, 9, 25, 27] direct_shifts= 62 quartic_tests= 628254 slope_moment_terms= 92`

The finite test cases are not exhaustive over field sizes and cannot prove the unrestricted theorem. The proof derives the universal identity via Hermite interpolation, incidence multiplicities and multiplicative-character orthogonality. Independent audit and independent validation have not been performed.
