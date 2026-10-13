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
For
\[
X_{\mathbf a}
=
\mathbb P^{a_1}\times\cdots\times\mathbb P^{a_r},
\qquad
N=\sum_i a_i,
\]
the checker evaluates
\[
D(\mathbf a)=\frac{N!}{\prod_i a_i!}
\]
and
\[
E(\mathbf a)=\prod_i(a_i+1).
\]

It independently checks
\[
\frac{D(\mathbf a+\mathbf e_j)/E(\mathbf a+\mathbf e_j)}
{D(\mathbf a)/E(\mathbf a)}
=
\frac{N+1}{a_j+2}
\]
using exact integer arithmetic after cross multiplication.

It also enumerates unordered dimension tuples in a finite test box and verifies the complete below/equal/above classification.

Finite checks are regression evidence only. The all-parameter theorem follows from the exact coordinate-growth identity and the symbolic base cases.
