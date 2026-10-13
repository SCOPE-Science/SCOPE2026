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
2\le m\le n,\qquad 1\le r\le m-1,
\]
the checker evaluates the classical generic determinantal degree product
\[
\deg D_{m,n}^{\le r}
=
\prod_{i=0}^{m-r-1}
\frac{(n+i)!\,i!}{(r+i)!(n-r+i)!}.
\]

At
\[
r=m-1
\]
it verifies the exact specialization
\[
\deg M_{m,n}=\binom{n}{m-1}.
\]

The topological proof is symbolic: a generic diagonal one-parameter action has exactly \(mn\) projective coordinate fixed points, all of rank \(1\), so every nontrivial rank locus has Euler characteristic \(mn\).

The package verifies the complete degree--Euler classification on
\[
2\le m\le40,\qquad m\le n\le100,
\]
and checks the exact adjacent-\(n\) ratio.

Finite checks are regression evidence only. The theorem for all parameters follows from the fixed-point theorem, Thom--Porteous, and the symbolic ratio argument.
