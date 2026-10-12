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
The proof is symbolic and uses only cyclicity of the multiplicative group of a finite field.

The packaged checker `artifacts/verify.py` writes every nonzero field element as a power of a generator of
\[
\mathbf F_q^\times\cong C_{q-1}.
\]
In exponent coordinates, the scalar recurrence for a rotation is an exact linear congruence.

For the complete coefficient spaces in
\[
(q,n)=(4,3),\ (7,2),\ (8,3),\ (5,4),
\]
the checker compares every ordered pair of weighted cycles. It solves the scalar recurrence for every rotation and confirms that an isomorphism exists exactly when the two \(\Delta\)-classes lie in one doubling orbit.

For
\[
(q,n)=(7,2),\ (8,3),\ (16,4),\ (9,3),
\]
it enumerates every coefficient tuple and independently verifies the idempotent congruence and automorphism lifts. It confirms
\[
N_{2,7}=2,
\qquad
N_{3,8}=3,
\qquad
N_{4,16}=5.
\]

For
\[
(q,n)=(16,4),
\]
the five quotient orbits are
\[
\{0\},\ \{1,2,4,8\},\ \{3,6,9,12\},\ \{5,10\},\ \{7,11,13,14\},
\]
with automorphism-group orders
\[
60,\ 15,\ 15,\ 30,\ 15.
\]

The checker returns `VERIFY_OK`.

The computation uses the multiplicative cyclic group only, so extension-field orders are tested without choosing a polynomial model of the field. Finite computation is not used to prove the general theorem.
