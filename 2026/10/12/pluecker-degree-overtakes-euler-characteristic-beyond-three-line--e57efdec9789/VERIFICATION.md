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
q=\min(k,n-k),
\qquad
c=n-q,
\]
the exact quantities are
\[
D(q,c)
=
\frac{(qc)!\,\prod_{i=1}^{q-1}i!}
{\prod_{j=c}^{c+q-1}j!}
\]
and
\[
E(q,c)=\binom{q+c}{q}.
\]

For \(q=2\), the checker confirms the Catalan specialization and the three exceptional values.

For \(q\ge3\), it confirms
\[
D(q,q)>E(q,q)
\]
and
\[
\frac{D(q,c+1)}{D(q,c)}
>
\frac{E(q,c+1)}{E(q,c)}
\]
through the stated finite verification range.

The proof itself supplies exact symbolic certificates for both inequalities: a \(3\times q\)-tableau injection at the square endpoint and strict rational ratio comparisons thereafter.

The finite computation is regression evidence only.
