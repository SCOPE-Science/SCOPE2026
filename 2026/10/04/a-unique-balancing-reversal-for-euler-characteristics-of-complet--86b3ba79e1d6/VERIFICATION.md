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
The source-backed identity
\[
c(TX)=\frac{(1+H)^{c+3}}{\prod_i(1+d_iH)}
\]
is expanded independently in the checker to obtain the \(H^2\) coefficient. That result is compared against the shifted-degree formula
\[
\chi_{\mathrm{top}}(X)=\left(\prod_i d_i\right)\left(3-2T+h_2(\mathbf x)\right).
\]

The infinite classification is proved symbolically in RESULT.md by evaluating the exact change under one balancing move. The checker does not substitute for that proof. It exhaustively enumerates bounded fixed-sum families only as regression evidence, checking the predicted unique maxima/minima and every available balancing step.

The cohomological corollary uses the Lefschetz hyperplane theorem: for a smooth complete-intersection surface, \(b_1=b_3=0\), so \(b_2=\chi_{\mathrm{top}}-2\).

Limits: smooth complex complete-intersection surfaces, fixed codimension, fixed sum of defining degrees, and all defining degrees at least two.
