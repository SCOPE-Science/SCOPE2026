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
# Verification

`verify.py` embeds all \(99\) tetrahedra and reconstructs the face vector \((16,115,198,99)\).

After contracting a fixed spanning tree, the graph cycle lattice has rank \(100\). Unimodular unit-pivot reduction of the \(198\) facial relations produces \(97\) identity pivots; the residual block has one nonzero column with gcd \(2\). Hence the Smith invariants are \(1^{97},2\) with two zero columns, so
\[
H_1(X;\mathbb Z)\cong\mathbb Z^2\oplus\mathbb Z/2.
\]

Two integral cocycles are checked against every facial relation and give free coordinate test cycles \((-1,0)\) and \((0,1)\). A mod-two cocycle is checked against every relation and detects a cycle with free coordinates \((0,0)\), thereby identifying the unique order-two kernel.

Every three-vertex clique is then enumerated. There are \(495\) graph triangles, \(198\) facial triangles, and \(297\) nonfacial triangles. None has zero homology coordinates. Up to orientation, the exact class multiplicities are
\[
55,54,41,40,38,36,33.
\]

Exact successful output:

`VERIFY_OK f=16,115,198,99 H1_Z=Z^2+Z/2 graph_triangles=495 facial3=198 empty3=297 all_empty3_nonzero=yes torsion_systoles=55 primitive_infinite_systoles=242 classes_up_to_sign=7 counts=55,54,41,40,38,36,33 free_directions=01|10|1-1 torsion_lifts=both`
