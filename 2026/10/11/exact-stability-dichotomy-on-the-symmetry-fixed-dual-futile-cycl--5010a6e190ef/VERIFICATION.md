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

The source's displayed six-dimensional reduced Jacobian was specialized only after imposing the eight positive derivative equalities exchanged by its \(\mathbb Z_2\) graph automorphism.

`artifacts/verify_symmetry_slice.py` performs exact symbolic checks of:

- the invertible symmetry-adapted change of basis and vanishing off-diagonal blocks;
- the two resulting \(3\times3\) matrices;
- both exact characteristic cubics;
- the factorization \(c_{3,-}=\alpha[\nu(\gamma+\rho+\tau)-\gamma\tau]\);
- the determinant identity \(\det G_{\mathrm{red}}=c_{3,+}c_{3,-}\);
- coefficientwise positivity of the symmetric-block Hurwitz margin, with 86 positive monomials;
- coefficientwise positivity of the antisymmetric-block Hurwitz margin, with 56 positive monomials.

The captured run is `artifacts/verify_output.txt` and ends in `VERIFY_OK`.

The proof of the unstable side is not a numerical eigenvalue test: for \(\Delta<0\), Descartes' rule gives exactly one positive real root of the antisymmetric cubic, and Vieta's relations force the other two roots to have negative real part. At \(\Delta=0\), the remaining quadratic has strictly positive coefficients and is Hurwitz. No claim is made about nonlinear dynamics beyond this local spectral statement.
