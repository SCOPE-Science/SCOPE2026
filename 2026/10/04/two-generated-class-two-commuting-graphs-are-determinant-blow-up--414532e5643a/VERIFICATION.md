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
The proof is symbolic and uses only the standard class-two commutator identities and elementary arithmetic in
\[
(\mathbb Z/c\mathbb Z)^2.
\]

The packaged checker `artifacts/verify.py` constructs explicit groups
\[
G(A,B,c)
\]
with multiplication
\[
(u,v,w)(u',v',w')
=
(u+u',v+v',w+w'-vu')
\]
in the corresponding cyclic coordinates.

It verifies the parameter triples
\[
(2,2,2),\ (3,3,3),\ (4,4,2),\ (8,2,2),\ (8,4,4),\ (12,6,6).
\]
For every case it checks the center, commutator subgroup, determinant commutation criterion, every degree, and the complete histogram
\[
scd-1
\]
with multiplicity
\[
sJ_2(c/d).
\]

It also checks that
\[
G(8,2,2)
\quad\text{and}\quad
G(4,4,2)
\]
have the same pair
\[
(c,s)=(2,8)
\]
and hence the same predicted commuting graph while having different abelianization invariant factors.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.
