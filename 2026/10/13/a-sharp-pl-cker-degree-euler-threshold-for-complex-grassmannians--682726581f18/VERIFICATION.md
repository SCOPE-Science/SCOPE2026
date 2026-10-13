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
For every tested
\[
2\le n\le100,
\qquad
1\le k\le n-1,
\]
the checker evaluates
\[
D_{k,n}
=
\frac{(k(n-k))!\prod_{i=1}^{k-1}i!}
{\prod_{j=0}^{k-1}(n-k+j)!}
\]
with exact integer arithmetic and compares it with
\[
E_{k,n}=\binom nk.
\]

It verifies the full strict classification and confirms that equality never occurs.

On the \(k=2\) edge it verifies the Catalan specialization and the exact normalized adjacent ratio. Toward the center it verifies the exact factorial quotient for
\[
D_{k+1,n}/D_{k,n}.
\]
It also verifies
\[
D_{3,n}>\binom n{\lfloor n/2\rfloor}
\]
through the finite range.

Finite checks are regression evidence only. The infinite theorem follows from the symbolic ratio inequalities in the accompanying result.
