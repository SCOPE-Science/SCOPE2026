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
The bundled `verify.py` uses only the Python standard library. It reconstructs the standard 5-regular Clebsch graph from even-weight vectors of \(\mathbb F_2^5\), verifies the strongly regular parameters \((16,5,0,2)\), and exhaustively enumerates all matchings.

The face counts including the empty face are
\[
(1,40,620,4760,19190,39640,37740,12840,705).
\]
The same matching counts are independently recomputed by a vertex-deletion recurrence.

For the mod-\(2\) simplicial chain complex, the exact boundary ranks from degrees \(1\) through \(7\) are
\[
(39,581,4179,15011,24629,12135,705).
\]
The verifier computes each rank with both highest-pivot and lowest-pivot elimination and requires agreement. It also checks \(\partial^2=0\) on every simplex of cardinality at least three. These values give reduced Betti vector
\[
(0,0,0,0,0,976,0,0)
\]
in degrees \(0\) through \(7\). The reduced Euler characteristic from the face vector is independently \(-976\).

Limits: this verification is finite and exhaustive for the stated graph and coefficient field. It does not compute integral Smith normal forms, torsion, or homotopy type.
