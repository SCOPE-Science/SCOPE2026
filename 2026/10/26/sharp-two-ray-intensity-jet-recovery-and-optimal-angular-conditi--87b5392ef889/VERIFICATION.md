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
The attached `checker.py` runs deterministic algebraic and numerical checks only. It compares exact forward Taylor intensities with triangular inverse reconstruction for each degree \(1\le N\le18\), the predicted smallest Jacobian singular value at every primitive-grid design in that range, the sine-product determinant identity, a dense angular grid for degrees \(1\le N\le12\), and an explicit pair of nonidentical resonant polynomials. Its execution returned `PASS 48078 deterministic checks including inverse, spectrum, optimal-angle upper bound, resonant ambiguity`.

The proof of the all-degree theorem is in `RESULT.md`: triangular coefficient identities, constant determinant, direct spectral diagonalization at the constant polynomial, and a circular nearest-neighbor equality argument. The finite grid cannot certify the continuum optimum and is used solely as a normalization check. Numerical tolerances use ordinary floating-point arithmetic; no external numerical certificate or independent validation is asserted.
