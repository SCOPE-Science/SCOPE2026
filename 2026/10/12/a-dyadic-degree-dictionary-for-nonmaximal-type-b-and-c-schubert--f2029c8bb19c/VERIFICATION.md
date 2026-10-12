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
The symbolic proof uses three source-level ingredients:

1. The common \(t\)-strict Schubert indexing for
\[
\operatorname{IG}(r,2n)
\quad\text{and}\quad
\operatorname{OG}(r,2n+1).
\]

2. The class scaling
\[
\tau_\lambda
\longmapsto
2^{-\ell_t(\lambda)}\sigma_\lambda.
\]

3. For \(t\ge1\), the Pluecker divisor is the unscaled special class indexed by \((1)\).

The unique top partition has \(r\) parts above \(t\), so comparison of the top coefficients gives
\[
\deg(X^B_\lambda)
=
2^{r-\ell_t(\lambda)}
\deg(X^C_\lambda).
\]

The bundled checker independently evaluates type \(B_n\) and type \(C_n\) Weyl products for all
\[
2\le n\le18,
\qquad
1\le r<n,
\]
and verifies the ambient ratio \(2^r\). It also checks the size and \(t\)-length of the top partition.

The finite computation is regression evidence only and is not used as proof of the Schubert-wide theorem.
