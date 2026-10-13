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
The checker builds Eulerian numbers from
\[
A(m,j)
=
(m-j)A(m-1,j-1)+(j+1)A(m-1,j)
\]
with
\[
A(1,0)=1.
\]

For every
\[
2\le n\le120,
\qquad
1\le k\le n-1,
\]
it compares
\[
D=A(n-1,k-1)
\]
with
\[
E=\binom nk
\]
and verifies the claimed strict classification.

For every tested interior parameter it also verifies
\[
A(n-1,k-1)\ge2^{n-1}-n,
\]
and for every tested \(n\ge5\),
\[
2^{n-1}-n>\binom n{\lfloor n/2\rfloor}.
\]

Finite checks are regression evidence only. The infinite proof is the toric volume and orbit-stratification computation followed by the Eulerian recurrence and parity-class inequalities.
