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

The current primary preprint was checked directly at the defining braid, parameter theorem, genus computation and fixed-parent filling construction. It gives the following exact data for the relevant range:
\[
b(K_{m,n})=m+2,
\qquad
g(K_{m,n})=rac{(m^2+3m+2)n}{2}+m+3.
\]

The displayed positive braid contains
\[
(m+1)((m+2)n+2)+(m+1)+4
=
(m+1)(m+2)n+3m+7
\]
crossings.

For every knot, Yamada's theorem plus the canonical Seifert surface gives
\[
c(K)\ge2g(K)+b(K)-1.
\]
Substitution gives exact equality with the displayed braid length.

The same preprint identifies a fixed hyperbolic parent \(M\cong S^3\setminus L14n61770\) whose parameter-dependent Dehn fillings give the knot complements. Since those complements are hyperbolic for \(m\ge3,n\ge1\), strict hyperbolic Dehn-filling volume decrease gives
\[
\operatorname{Vol}(S^3\setminus K_{m,n})<\operatorname{Vol}(M).
\]

The bundled arithmetic regression prints:

`VERIFY_OK pairs=10000 crossing_identity=true n1_square_identity=true`

It checks only algebraic identities, not the general topological theorems.

The independent-audit channel has not been performed.
