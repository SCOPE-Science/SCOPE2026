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

# Reproducibility

The attached `verify_symbolic.py` recomputes the genus-two Cartier matrix from \(F_w(x)^5\), its determinant, the elliptic Hasse coefficient, the two special quartic restrictions, the excluded-parameter gcds, their squarefreeness, and five rank witnesses. Run `python3 verify_symbolic.py` with SymPy installed. Its success marker is `EXACT_CHAR11_GENUS5_HOWE_CARTIER_FACTORS_16_2_OK`.

The attached `verify_fields.py` independently implements arithmetic in \(\mathbb F_{11}[t]/(t^2-2)\) and computes all three quotient matrices by direct polynomial powers, not by calling the symbolic formulas. Run `python3 verify_fields.py`. It checks all \(13{,}806\) admissible ordered coefficient pairs over \(\mathbb F_{121}\) and prints `GF121_DIRECT_GENUS5_CARTIER_RANKS_16_2_OK`, with rank counts \(2,16,448,566,12774\) for ranks one through five. It also counts \(2,8,16,12,18\) admissible pairs over the prime field for those ranks.

Neither finite-field enumeration proves a classification over the algebraic closure. The unrestricted proof depends on the published separable generalized Howe isogeny and exact characteristic-eleven polynomial factorization, including the absence of excluded or multiple roots in the sixteen-point zero-dimensional scheme. No external independent audit is asserted.
