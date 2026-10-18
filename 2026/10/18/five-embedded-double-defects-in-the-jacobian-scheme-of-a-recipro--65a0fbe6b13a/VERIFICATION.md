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

# Reproduction and limits

Run `python3 check.py` from the same directory as `RESULT.md`. The script has no third-party dependencies. It computes the exact rank of the four local Jacobian quadrics among the six squarefree quadratic monomials, verifies a \(16\times16\) integer multiplication-matrix determinant of \(48\) by Bareiss elimination, and verifies the reduced Hilbert monomial count in degrees one through nine. It exhaustively enumerates projective \(\mathbb F_5\) and \(\mathbb F_7\) points, finding \(45\) and \(65\) singular points, respectively, with exactly the predicted coordinate support. On success the output ends in `VERIFY_OK`.

The proof of the general characteristic-zero result is the direct localization and symbolic sheaf argument in `RESULT.md`. The finite-field enumerations are consistency checks only. The determinant computation is exact over the integers and gives the needed invertibility specifically in characteristic zero; no claims are made in characteristic two or three. No independent audit is asserted.
