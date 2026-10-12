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

# Exact checks and boundaries

The script `verify.py` is self-contained and needs Python 3's standard library only. Run `python3 verify.py` from the directory containing this file. It is designed to finish immediately and emits `VERIFY_OK rational_choi=passed unitary_all_angles=passed bernstein=passed` on success.

The verifier checks all entries of the rational conditional Choi state, its positive trace and negative partial-transpose principal minor. It also reconstructs all four elementary symmetric functions for the partial transpose of the unitary-interleaved Choi state, using polynomial arithmetic with the symbolic identity \(w^2=p(1-u^2)\). The quartic is independently re-expanded in the Bernstein basis; strictly positive Bernstein coefficients certify it for the entire closed interval. The analytic implication from positive elementary symmetric functions to a positive-definite Hermitian matrix is proved in `RESULT.md`.

The computation is exact finite symbolic algebra. It does not certify unrelated noise models, non-diagonal filters, multiple intermediate channel uses, general deterministic operations or independence of review.
