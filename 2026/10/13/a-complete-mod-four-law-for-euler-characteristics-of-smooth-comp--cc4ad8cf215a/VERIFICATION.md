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
The checker reconstructs
\[
\chi_{\mathrm{top}}(X)
=
D[t^n](1+t)^{n+c+1}\prod_i(1+d_it)^{-1}
\]
by exact truncated polynomial arithmetic.

For each tested multidegree it compares the exact integer residue modulo \(4\) with the symbolic branch theorem. It separately verifies:

\[
\chi_{\mathrm{top}}(X)\ \text{odd}
\iff
n\ \text{even and all defining degrees odd},
\]
and the two disjoint criteria for
\[
\nu_2(\chi_{\mathrm{top}}(X))=1.
\]

The finite range is
\[
1\le n\le12,\qquad
1\le c\le4,\qquad
2\le d_i\le9.
\]

Finite checks are regression evidence only. The infinite proof is the direct modulo-four reduction of the Chern-series coefficient.
