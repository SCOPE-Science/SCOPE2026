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
The packaged checker `artifacts/verify.py` performs exact symbolic verification.

It first checks all eleven associative-trialgebra identities for the symbolic multiplication table \(T_2^8(a,b)\).

It then verifies the basis changes
\[
f_1=a^{-1}e_1+ba^{-2}e_2,\qquad f_2=e_2
\]
for \(a\ne0\), and
\[
f_1=e_1,\qquad f_2=b e_2
\]
for \(a=0,\ b\ne0\).

Finally it constructs the complete linear systems defining derivations and centroids for the three representatives
\[
T_2^8(1,0),\qquad T_2^8(0,1),\qquad T_2^8(0,0)
\]
and computes their exact nullspaces.

The derivation dimensions are
\[
1,\quad2,\quad4,
\]
and the centroid dimensions are
\[
1,\quad2,\quad4.
\]

The checker also confirms the operation-image dimension triples
\[
(2,2,1),\quad(0,0,1),\quad(0,0,0).
\]

It returns `VERIFY_OK`.
