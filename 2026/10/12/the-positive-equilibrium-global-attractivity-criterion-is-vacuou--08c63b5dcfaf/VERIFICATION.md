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
The bundled checker verifies the exact expansion
\[
bU_1^y-(r_0-d)
=
bhm+
\frac{bh-a}{a}(r_0-d)+
b(h+1)\varepsilon.
\]

The theorem's first inequality implies
\[
D=r_0-d>0,
\]
and its second implies
\[
P=bh-a>0.
\]
With these positive quantities, the difference becomes
\[
bhm+
\frac{P}{a}D+
b(h+1)\varepsilon,
\]
a sum of strictly positive terms.

No finite parameter enumeration, simulation, or numerical optimization is used to prove the contradiction.
