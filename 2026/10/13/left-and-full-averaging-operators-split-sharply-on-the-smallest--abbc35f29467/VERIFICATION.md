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
The proof is symbolic and valid over every field.

The packaged checker `artifacts/verify.py` exhaustively treats
\[
q\in\{2,3,5,7\}.
\]
For each field it enumerates all linear endomorphisms and checks both averaging identities on all ordered basis pairs. It independently enumerates all invertible product-preserving maps, constructs conjugacy orbits, and verifies
\[
\#\operatorname{LAvg}(L)=2q^2-q,
\qquad
\#(\operatorname{LAvg}(L)/\operatorname{Aut}(L))=q^2+q,
\]
and
\[
\#\operatorname{Avg}(L)=3q-2,
\qquad
\#(\operatorname{Avg}(L)/\operatorname{Aut}(L))=2q.
\]

It also verifies the full-averaging rank distribution, exactly three idempotents, and exactly \(q\) square-zero full averaging operators.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.
