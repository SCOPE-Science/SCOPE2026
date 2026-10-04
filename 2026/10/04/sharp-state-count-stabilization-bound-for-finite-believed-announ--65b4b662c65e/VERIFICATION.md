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

For a relation \(R\) and a target truth set \(S\), the believed-announcement update is
\[
R'=R\cap(W\times S).
\]

The key finite invariant is the active-target set
\[
T(R)=\{v:\exists u\ (u,v)\in R\}.
\]
Whenever \(R'\ne R\), some active target lies outside \(S\), and all arrows to that target are removed. Hence
\[
T(R')\subsetneq T(R).
\]

The bundled checker exhaustively verifies this implication for every one-agent relation and every target truth set on carriers of size at most four.

It separately implements the sharp cycle model with
\[
\varphi=p\land\neg\Box\bot
\]
and verifies for
\[
1\le n\le12
\]
that all stages
\[
0,\ldots,n-1
\]
are strict and that
\[
M^n=M^{n+1}.
\]

The script prints `VERIFY_OK`.

## Limits

The finite computation corroborates the set-theoretic proof. The upper bound applies to arbitrary agent sets because the published update uses the same target truth set for every agent relation. The sharpness construction is not a \(K45\) lower bound.
