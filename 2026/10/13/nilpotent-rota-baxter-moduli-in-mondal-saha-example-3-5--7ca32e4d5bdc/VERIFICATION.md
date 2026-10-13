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
The bundled checker reconstructs
\[
[e_3,e_2]=e_2,\qquad [e_3,e_1]=e_1+e_2
\]
and the weight-zero Rota–Baxter identity.

It verifies symbolically that both displayed nilpotent planes have zero defect and square zero.

Over \(\mathbf F_3\), every \(3\times3\) matrix is tested, and the nilpotent Rota–Baxter locus agrees exactly with the two-plane union.

Over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,
\]
the checker constructs the full displayed automorphism group and computes all conjugacy orbits. It obtains
\[
15,\quad45,\quad91
\]
nilpotent operators and
\[
7,\quad11,\quad15
\]
orbits.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field classification and orbit theorem are symbolic.
