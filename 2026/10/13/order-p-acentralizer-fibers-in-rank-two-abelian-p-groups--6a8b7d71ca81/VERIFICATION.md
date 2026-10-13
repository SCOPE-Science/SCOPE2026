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
The proof is symbolic and uses the standard automorphism matrix for
\[
C_{p^a}\oplus C_{p^b},
\qquad
a<b.
\]

The packaged checker `artifacts/verify.py` directly enumerates every automorphism and every group element for
\[
(p,a,b)
=
(2,1,2),
(2,1,3),
(2,2,3),
(3,1,2),
(3,1,3),
(3,2,3),
(5,1,2).
\]
For each automorphism it computes the fixed subgroup exactly. When that subgroup has order \(p\), the checker identifies the subgroup as \(U_\infty\) or one of the \(U_t\).

The exact observed multiplicities are
\[
(2,1,2):\quad (m_\infty,m_t)=(2,0),
\]
\[
(2,1,3):\quad (0,0),
\]
\[
(2,2,3):\quad (32,0),
\]
\[
(3,1,2):\quad (30,9),
\]
\[
(3,1,3):\quad (54,27),
\]
\[
(3,2,3):\quad (2430,486),
\]
and
\[
(5,1,2):\quad (380,75).
\]

For the \(C_p\oplus C_{p^2}\) cases, it also verifies that
\[
m_\infty+p\,m_t
=
p(2p^3-4p^2+1).
\]

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the formulas.
