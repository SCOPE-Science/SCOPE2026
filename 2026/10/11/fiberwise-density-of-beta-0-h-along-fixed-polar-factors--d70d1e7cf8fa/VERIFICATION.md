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

The claim was checked symbolically from the spectral theorem and polar decomposition. The critical points are:

1. On \(H_0=N(T)^\perp\), the zero spectral projection of \(A=|T||_{H_0}\) is zero even when \(0\in\sigma(A)\) continuously.
2. Finite Borel cells covering \(\sigma(A)\setminus\{0\}\) can be assigned strictly positive representatives with uniform error below \(\varepsilon\); choosing the top-cell representative to be \(\|T\|\) preserves the norm.
3. The resulting \(A_\varepsilon\) is bounded below on \(H_0\), hence its extension \(B\) has support exactly \(P_{H_0}=U^*U\).
4. Therefore \((UB)^*(UB)=B^2\), so \(|UB|=B\), and the support equality makes \(U\) the actual polar partial isometry.
5. Finite-spectrum self-adjoint operators lie in \(\beta(H)\) by the focal source, so \(UB\in\beta_0(H)\).

No computational certificate is required. The unstructured density of \(\beta_0(H)\) is already implicit in the focal source proof and is not treated as the originality-bearing portion of the finding. The verified new content is the simultaneous fixed-polar-factor, kernel-preserving, and exact-norm-preserving approximation.
