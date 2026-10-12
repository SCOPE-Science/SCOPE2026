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

The packaged checker `artifacts/verify.py` constructs the ring
\[
R_{n,q}=\mathbf F_2I_n\oplus N_n(\mathbf F_q)
\]
for
\[
(q,n)=(2,2),(2,3),(2,4),(4,2),(4,3).
\]
It checks ring closure and directly enumerates inverses to verify that the unit set is exactly
\[
I_n+N_n(\mathbf F_q).
\]

For odd fields \(\mathbf F_3\) and \(\mathbf F_5\), it also verifies directly that
\[
I_n+E_{12}
\quad\text{and}\quad
I_n+E_{23}
\]
do not commute for \(n=3\), confirming the nonabelian family-side hypothesis used with the published odd-primary realizability theorem.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the classification.
