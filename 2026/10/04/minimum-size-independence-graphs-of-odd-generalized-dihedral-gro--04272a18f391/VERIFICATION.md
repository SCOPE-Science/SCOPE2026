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
The universal proof is independent of finite enumeration.

The critical reduction is that a generating set containing a reflection \(a_0s\) may replace every other reflection \(a_is\) by the rotation \(a_i-a_0\) without changing the generated subgroup. Hence a minimum generating set consists, after normalization, of one reflection and \(d(A)\) rotations generating \(A\).

A prescribed \(k\)-tuple of rotations extends to \(d(A)\) generators exactly when its images in every Sylow Frattini quotient have rank at least
\[
r_p-d(A)+k.
\]
The cases \(k=1\) and \(k=2\) give the complete pair classification.

The packaged checker `artifacts/verify.py` independently enumerates every three-element subset in the two cases
\[
A=C_9\times C_3
\quad\text{and}\quad
A=C_3\times C_3\times C_5,
\]
uses exact additive subgroup closure to decide whether the normalized rotations generate \(A\), reconstructs every edge of \(\Gamma_3(G)\), and compares the result against the theorem's direct rank conditions.

It obtains respectively
\[
13608\text{ generating triples},
\qquad
0^3,45^{24},48^{27},
\]
and
\[
60480\text{ generating triples},
\qquad
0^5,69^8,75^{32},80^{45}.
\]
It also checks \(|g|\mid\deg(g)\) for every vertex and returns `VERIFY_OK`.

Finite computation is not used to prove the universal theorem.
