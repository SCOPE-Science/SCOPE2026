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

# Verification of the explicit tetrablock spectral-set obstruction

For the stated closed tetrablock, the established scalar derivative-ball theorem identifies the permissible normalized first derivatives with the unit ball of \(\ell_1^2\oplus_\infty\mathbb C\). The explicit linear map from this ball has norm one by the \(2\times2\) golden-ratio singular-value calculation. The disk Möbius transform and block Schur complement cover arbitrary scalar rational functions, including a nonzero constant term.

The matrix rational function has denominator \(1-\rho^2z_1z_2\), which is nonvanishing throughout a neighborhood of the compact domain because \(\rho<1\). On the distinguished boundary, its Cayley-type factorization gives an explicit positive defect and hence norm at most one. When \(|q|=1\), the value is a diagonal unitary, giving the matching lower bound.

The exact rational checker `verify_tetrablock.py` verifies the square-zero block products, the amplified matrix eigenvector identities, and the sign of the golden-ratio comparison at \(\rho=3/4\). It does not test the continuum of boundary points; that continuum is covered analytically by the defect identity. It also does not independently establish the two published geometric input theorems or exclude unknown prior literature.

No independent audit or external certification has been performed.
