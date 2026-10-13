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

# Reproducibility and analytical limits

Run `python3 verify.py` with Python 3 standard library. The script uses `fractions.Fraction` to apply the finite-difference matrix, execute **two actual CG recurrences** from a zero start, reconstruct the two-dimensional Galerkin formula, and cross-check the symbolic moment identities against the direct matrix operations for 952 exact combinations of profile sizes, amplitudes, and padding. The exact integer load `(1,0,0,2,4,4,2,0,...)` has first component `-58/171` after two steps. It also checks signs of the zero- and unit-amplitude quartic endpoints. The checker was executed from the embedded artifact at packaging time.

Proof of the identities for every integer width and continuum of amplitudes is analytical in `RESULT.md`: the strict moment determinant uses the positive-definite inner product, the unique root uses a globally positive quartic second derivative, and the threshold asymptotic uses uniform coefficient expansion. The checker does not cover every real amplitude, all matrix sizes, finite-precision implementation, or arbitrary right-hand sides. Independent audit remains unperformed.
