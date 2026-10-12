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
The proof is symbolic and characteristic-free.

The packaged checker `artifacts/verify.py` exhaustively treats
\[
q\in\{2,3,5,7\}.
\]

For both \(A_2\) and \(A_3\), it:
1. enumerates all \(q^4\) linear endomorphisms;
2. checks the Nijenhuis identity directly on all four ordered basis pairs;
3. verifies that the solutions are exactly
\[
c=0,\qquad b(a-d)=0;
\]
4. enumerates all invertible product-preserving linear maps and recovers
\[
\operatorname{Aut}(A_i)=\{\operatorname{diag}(1,s):s\ne0\};
\]
5. constructs every conjugacy orbit and verifies the unique representative set
\[
\{D_{a,d}\}\sqcup\{J_a\}.
\]

For \(q=5\), each algebra has \(45\) Nijenhuis operators in \(30\) orbits: \(25\) singleton diagonal orbits and \(5\) shear orbits of size \(4\).

The checker also verifies that there are exactly \(q\) square-zero Nijenhuis operators in two orbits and exactly four idempotent Nijenhuis operators.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.
