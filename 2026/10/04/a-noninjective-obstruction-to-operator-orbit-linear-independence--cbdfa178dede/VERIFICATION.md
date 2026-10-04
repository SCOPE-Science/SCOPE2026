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

The construction was checked directly from the definitions in arXiv:2305.08182v1.

For every \(f\in H\), the negative-index contribution is
\[
\sum_{n=0}^{\infty}\|2^{-n}U_nf\|^2=\frac43\|f\|^2,
\]
and the positive-index contribution is
\[
\sum_{k=1}^{\infty}\|2^{-k}U_+f\|^2=\frac13\|f\|^2.
\]
Thus the frame identity is exact and does not depend on finite truncation.

The operator action was checked on every orthogonal block. It gives \(T\Theta_k=\Theta_{k+1}\) for all \(k\in\mathbb Z\), while \(T(U_0x-U_+x)=0\) for nonzero \(x\), so no inverse exists. The dependence \(\Theta_2=\Theta_1/2\) is exact. Infinite-dimensionality of the operator span follows because finite linear combinations of the maps \(U_n\) have orthogonal ranges and therefore have unique coefficients.

For the repaired proposition, the only nonstandard step is backward propagation. If \(TA=0\) for a finite linear combination of the \(\Theta_k\), then \(A(H)\) lies in the algebraic span of the \(M_k\). Injectivity of \(T\) on that span forces \(A=0\). Iterating this argument places every negative translate of a finite relation in the same finite-dimensional operator span, yielding the contradiction.

The journal article associated with DOI:10.1007/s11868-023-00546-2 was accessible only at abstract/preview level for this comparison. Therefore the theorem-level counterclaim is restricted to arXiv:2305.08182v1. No independent audit has been performed.
