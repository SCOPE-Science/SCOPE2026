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
M=\frac{n(n+1)}2,
\]
the checker evaluates
\[
D_n
=
M!\frac{\prod_{j=1}^{n-1}j!}{\prod_{j=1}^{n}(2j-1)!}
\]
and
\[
E_n=2^n.
\]

It independently computes the shifted-tableau count using
\[
\frac{M!}{\prod_i\rho_i!}
\prod_{i<j}\frac{\rho_i-\rho_j}{\rho_i+\rho_j},
\qquad
\rho=(n,n-1,\ldots,1),
\]
and checks that it equals \(D_n\).

It verifies the exact adjacent ratio
\[
\frac{D_{n+1}}{D_n}
=
\frac{\binom{M+n+1}{n+1}}{\binom{2n+1}{n+1}}
\]
and the complete strict comparison with \(E_n\) for
\[
1\le n\le30.
\]

Finite checks are regression evidence only. The infinite proof is the Schubert-cell count, shifted hook-length formula, and symbolic adjacent-ratio argument.
