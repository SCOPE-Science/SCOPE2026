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
The proof is symbolic.

The packaged checker `artifacts/verify.py` evaluates
\[
C(G)=\{(1,1),(p,p^{2n}-1),(p^{n+1},p-1)\}
\]
for
\[
p\in\{2,3,5,7\},
\qquad
1\le n\le4.
\]

For each case it verifies the total number of irreducible characters and
\[
p^{2n}\cdot1^2+(p-1)(p^n)^2=p^{1+2n}.
\]
It then reconstructs \(p\), \(n\), and the group order from the pseudo-algebra alone.

The checker also verifies
\[
D_8,\ Q_8:
\quad
\{(1,1),(2,3),(4,1)\},
\]
and the order-\(27\) extraspecial pair:
\[
\{(1,1),(3,8),(9,2)\}.
\]

The checker returns `VERIFY_OK`.

Finite arithmetic checks are not used to prove the character-theoretic theorem.
