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

`verify.py` reconstructs the polynomial Jacobian directly and checks exact closure, squared amplitudes, the quintic characteristic polynomial, its five rational Hurwitz determinants, and its global-rotation kernel. The checker uses SymPy symbolic differentiation and exact arithmetic. This is a finite algebraic certificate of the spectral calculation; the weak-coupling instability and orbital convergence are proved analytically in RESULT.md.

No independent audit or external certification has been performed.
