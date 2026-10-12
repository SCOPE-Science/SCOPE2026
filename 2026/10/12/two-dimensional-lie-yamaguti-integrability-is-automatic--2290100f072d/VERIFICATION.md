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
The bundled checker represents arbitrary operations as
\[
[x,y]=\omega(x,y)b,\qquad
\{x,y,z\}=\omega(x,y)A(z),
\]
with arbitrary \(b\) and arbitrary \(A\). It verifies every component of the binary and ternary Nijenhuis defects for the standard nontrivial involution, the standard non-scalar map with square \(-I\), and arbitrary scalar maps.

It then enumerates every \(2\times2\) matrix over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,\quad\mathbf F_{11},
\]
checking \(E^2=I\), \(E\ne\pm I\), \(J^2=-I\), and \(JE=-EJ\). The resulting triples are
\[
(12,6,24),\quad(30,32,120),\quad(56,42,336),\quad(132,110,1320).
\]
The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence only; the theorem for arbitrary characteristic different from \(2\) is symbolic.
