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

The proof was replayed from the definitions of the two component norms and the Lebesgue decomposition of a signed regular Borel measure.

1. The diagonal embedding of \(C(K)\) into the \(\ell_1\)-sum of the sup-norm completion and the \(L^1(\nu)\) completion gives the dual quotient norm
\[
\inf_{g\in L^\infty(\nu)}\max\{\|\lambda-g\nu\|_{TV},\|g\|_\infty\}.
\]
2. For \(\lambda=h\nu+\lambda_s\), mutual singularity gives
\[
\|\lambda-g\nu\|_{TV}=\|\lambda_s\|_{TV}+\int|h-g|\,d\nu.
\]
3. Under \(\|g\|_\infty\le t\), pointwise clipping minimizes the integral residual and yields \(\int(|h|-t)_+\,d\nu\).
4. The resulting scalar residual-minus-threshold function is continuous and strictly decreasing, giving one unique positive root for every nonzero \(\lambda\).
5. Equality in the two component dual bounds gives exactly the stated norm-attainment conditions, and those conditions are also sufficient.
6. If \(\lambda\perp\nu\), the root is \(\|\lambda\|_{TV}\), while norm attainment would require a nonzero continuous function vanishing \(\nu\)-almost everywhere. Full support rules this out.

Checked boundaries: zero measure separately; purely singular measures; absolutely continuous measures; an evaluation at a point with positive \(\nu\)-mass; an evaluation at a \(\nu\)-null point; and the difference of two evaluations under nonatomic \(\nu\). The evaluation norm specializes to \(1/(1+\nu(\{t\}))\), matching the lattice-homomorphism formula in the focal source. No independent audit has been performed.
