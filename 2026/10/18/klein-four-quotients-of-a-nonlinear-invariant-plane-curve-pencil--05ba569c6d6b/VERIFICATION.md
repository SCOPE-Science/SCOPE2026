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

# Verification and scope

The affine invariant-field identities were reconstructed symbolically using the defining recurrence of \(T_h\). The polynomial identity after clearing denominators was checked for \(q=3,5,7,9,11,13\); the characteristic-three elliptic transformation and modular-invariant formula were checked modulo three; and fixed-point polynomial squarefreeness was computed in several relevant prime fields. Execute `python verify.py` with SymPy installed to replay these exact calculations.

These computations verify algebraic identities and finite characteristic samples only. The proof for all odd prime powers uses the independent smoothness argument for the first quotient, quadratic reconstruction of the fixed field, a complete fixed-point count, and Riemann–Hurwitz. Tests do not constitute exhaustive parameter enumeration. The genus result concerns smooth normalizations; the affine equation may be singular. The characteristic-three modular map extends rationally over degenerate parameters but the excluded original curves do not thereby become smooth.

Independent audit: not performed.
