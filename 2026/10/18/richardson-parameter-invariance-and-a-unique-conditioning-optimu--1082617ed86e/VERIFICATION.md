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

# Verification of the stated result

Run `python check.py` with Python 3.9 or later; only the standard library is required. The script constructs 23 explicit nonsingular matrices and corresponding residuals with linearly independent first two Krylov vectors. For eight positive rational smoothing weights each, it evaluates the exact scalar two-grid presmoothing and two-column coarse correction using `fractions.Fraction`, and independently solves the two-step GMRES normal equations in the \(\{r,Ar\}\) basis. It verifies exact equality of the resulting corrections and of all coarse-matrix entries, determinant and trace. Additional numerical checks test the analytic optimum and the leading small-weight asymptotic.

The observed standalone output is:

`PASS: 1242 rational identity and numerical conditioning assertions across 23 matrices`

`Diagnostic: A=diag(1,2,4), r=(1,1,1): u=21, v=73, w=273, Delta=404, omega_star=sqrt(2/13).`

**Limits of verification.** The finite tests do not certify the infinite-dimensional quantifiers or the universal positive-weight range. These follow from the symbolic affine-space, determinant, completed-square, and eigenvalue calculations in `RESULT.md`. No floating-point implementation stability test or independent audit has been performed.
