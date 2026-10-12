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

# Verification

Run `python verify.py` with Python 3 and SymPy. The checker available within this package was executed before packaging, returning `VERIFY_OK 520 exact rational cases; critical persistence between 0.043 and 0.044`.

The checker verifies the moment-transfer determinant and cubic, discriminant factorization, strict exact root bracket, and rational examples. The 520 rational parameter comparisons check the relation between determinant positivity and the two-state spectral threshold for persistence below one half. The theorem's all-real-parameter statements follow from the analytical root, continuity and convexity proof in `RESULT.md`, not from the finite grid.

A complete independent mathematical audit has not been performed. Earlier literature may contain an equivalent specialized phase diagram, and the conference-paper comparison remains abstract-only.
