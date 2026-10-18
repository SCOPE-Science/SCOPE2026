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
# Reproducibility and verification

Run the embedded standalone program with `python verify_curvature.py` in a Python environment providing `sympy` and `mpmath`. It checks the base orbit formulas, the Jacobian-product trace and determinant, the exact reduction of four orbit equations, the factorization and roots of the curvature, and high-precision solutions of the five defining equations for couplings \(-4/5\), \(-1/2\), and \(-1/5\), at two small mismatch magnitudes. It printed `VERIFY_OK` when executed from this package's source contents.

The checker is a finite consistency test, not a certificate of the analytic implicit-function theorem. The proof in RESULT.md handles the entire parameter interval and all sufficiently small mismatches for each fixed coupling; the unspecified neighborhood may shrink at endpoints. No external scientific audit or separate validation has been performed. Historical completeness, resonance behavior and fourth-order response at the two curvature zeros are unproved.
