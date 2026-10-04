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
The universal argument is algebraic and does not rely on finite enumeration.

The critical identities are
\[
[g(a,b,c),g(a',b',c')]=g(0,0,ab'+a'b)
\]
and, in characteristic \(2\),
\[
g(a,b,c)^2=g(0,0,ab).
\]
These identities imply
\[
H(q)'=Z(H(q))=\Phi(H(q))\cong C_2^m
\]
and reduce the order distribution to the exact count of pairs satisfying \(ab=0\).

The packaged checker `artifacts/verify.py` implements the finite fields of orders \(2,4,8,16\), enumerates all group elements from the multiplication law, and determines each element order from repeated multiplication rather than from the closed count. It verifies
\[
(q,n_2,n_4,\psi)
=(2,5,2,19),
(4,27,36,199),
(8,119,392,1807),
(16,495,3600,15391).
\]
It also checks that every central coordinate is realized both by a commutator and by a square.

The checker returns `VERIFY_OK`.

The finite replay verifies examples only; the all-\(m\) claim is proved by the symbolic group-law argument above.
