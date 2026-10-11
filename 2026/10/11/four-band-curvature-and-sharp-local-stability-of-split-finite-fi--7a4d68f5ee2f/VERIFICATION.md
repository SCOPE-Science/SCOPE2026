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

The proof is finite-field exact and requires only that the characteristic be odd. The script `hessian_check.py` enumerates ordered convolution fibers, computes the second Taylor coefficient from them, and independently computes its predicted Fourier diagonalization. A clean run prints `PASS 88 quadratic-form tests over F_3, F_5, F_7 and F_9`.

All four quoted eigenvalues are coefficients of \(t^2\) in the deficit, not its ordinary second derivative. Constants form a two-dimensional real kernel. There is no global coercivity claim. The finite checks do not exhaust finite fields or replace the formula's algebraic proof.
