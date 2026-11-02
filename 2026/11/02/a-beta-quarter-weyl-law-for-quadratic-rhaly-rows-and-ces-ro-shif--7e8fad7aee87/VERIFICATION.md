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

The supplied `verify.py` is a reproducible supplementary checker for the Cesàro defect matrix coefficients, the finite triangular-block singular values, and the inverse tridiagonal model for finite Rhaly compressions. It also independently evaluates the beta integral by quadrature and tests a few finite-rank asymptotic approximations.

Run `python3 verify.py` with Python 3.10+, NumPy 1.24+, and SciPy 1.10+. The finite checker is not proof of asymptotic convergence for the infinite operator; proof of the Weyl coefficient rests on the block-counting and tail arguments in `RESULT.md`.

Self-review completed; independent audit and independent validation have not been performed.
