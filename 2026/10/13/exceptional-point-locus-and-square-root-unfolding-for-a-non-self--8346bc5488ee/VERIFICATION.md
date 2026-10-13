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

The analytic checks use the exact characteristic objects of arXiv:2205.05005. Expanding
\[
\det\!\left(I+\frac{i}{2}AZ\right),
\qquad Z=\operatorname{diag}(\eta,\eta^{-1}),
\]
gives
\[
\det\!\left(I+\frac{i}{2}AZ\right)
=\frac{i}{2\eta}\left(\alpha\eta^2+\frac{i(\det A-4)}2\eta+\delta\right).
\]
The quadratic discriminant simplifies exactly to
\[
-\frac14\left((\det A-4)^2+16\alpha\delta\right).
\]
Heriban--Tušek's inverse formula gives \(z(\eta)=m(\eta^2+1)/(\eta^2-1)\), and direct differentiation gives \(z'(\eta)=-4m\eta/(\eta^2-1)^2\), which is nonzero for every admissible root.

The algebraic-multiplicity step was checked from the finite-dimensional Krein resolvent: the boundary matrix is analytic and the contour trace of the resolvent difference equals the logarithmic derivative of its determinant. Therefore the Riesz-projection rank equals the determinant zero order. This is the only operator-theoretic step beyond the scalar quadratic algebra.

The accompanying `verify.py` checks the symbolic determinant and discriminant identities, a defective matrix with rank-one boundary matrix at coalescence, a decoupled semisimple matrix with zero boundary matrix, and convergence of a transverse eigenvalue splitting to the stated Puiseux coefficient.

Limits: the script is corroborative and does not prove the contour-trace identity; that identity is supplied analytically above. No finite sampling is used to infer a global spectral statement. Threshold points and the spectral-flooding family are outside the claim.
