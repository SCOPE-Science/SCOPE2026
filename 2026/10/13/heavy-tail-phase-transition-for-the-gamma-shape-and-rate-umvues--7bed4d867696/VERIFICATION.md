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

The proof was reconstructed from the exact public formulas rather than from numerical fitting. The following checks were carried out.

1. The public preprint was inspected for the density \(f_Y(y)=K(\alpha)y^{\alpha-1}(1-y)^{(n-3)/2}G(y)\), the power-series expansion of \(G\), and the signs \(G>0\), \(G'<0\).
2. Theorem 2.1 was inspected for \(U_0=(n-3)Y/(2(1-Y))-YG'(Y)/G(Y)\) and for the published finite-variance threshold.
3. The proof's lower-endpoint estimate \(y^{\beta+1}|G'(y)|\to0\) for every \(\beta>0\) was checked and generalized only by choosing \(\beta<\alpha/q\); no unproved uniformity in \(q\) is used.
4. Corollary 2.1 was inspected for \(U_1=(nU_0-1)/X\), \(X\perp Y\), and the unbiasedness domain \(\alpha>1/n\).
5. The inverse-Gamma identity \(\mathbb E[X^{-q}]=\lambda^q\Gamma(n\alpha-q)/\Gamma(n\alpha)\) for \(q<n\alpha\) follows directly by integrating the Gamma density.
6. In the critical product case, the logarithm comes from \(\mathbb E[B^p;B\le t]\sim pC_B\log t\) when \(\Pr\{B>t\}\sim C_Bt^{-p}\); the remaining product-event regions are lower order after fixed truncation.
7. Setting \(q=2\) recovers exactly the source conditions \(n\ge6\) for the shape estimator and \(\alpha>2/n\) for the rate estimator when \(n\ge6\).

The argument does not establish bounded exponential moments, subexponential constants beyond the displayed power-law equivalents, or optimality among competing estimators. No finite numerical experiment is used to infer an infinite-domain statement.
