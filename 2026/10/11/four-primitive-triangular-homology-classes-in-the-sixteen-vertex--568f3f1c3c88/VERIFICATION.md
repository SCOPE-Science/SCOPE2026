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

`verify.py` embeds the complete \(94\)-tetrahedron presentation and uses only the Python standard library.

The one-skeleton has \(110\) edges. Contracting the fixed spanning tree leaves \(95\) cycle generators. The \(188\) triangular-face boundaries form an integral relation matrix. Unimodular unit-pivot reduction produces exactly \(93\) identity pivots with zero residual block, proving
\[
H_1(K;\mathbb Z)\cong\mathbb Z^2
\]
without torsion.

Two explicit integral cocycles annihilate all \(188\) facial relations. Their evaluations on two cycles are \((1,0)\) and \((0,1)\), so they give exact integral homology coordinates.

The verifier enumerates every three-vertex clique. It finds \(449\) graph triangles, of which \(188\) are faces and \(261\) are nonfacial. Up to sign, their coordinates have the exact multiplicities
\[
(0,0):43,\quad (0,1):86,\quad (1,1):66,\quad (1,0):65,\quad (1,2):1.
\]
It checks that all \(218\) nonzero vectors are primitive and that the singleton class is represented only by \(\{2,4,16\}\).

Exact successful output:

`VERIFY_OK f=16,110,188,94 H1_Z=Z^2 graph_triangles=449 facial3=188 empty3=261 null_empty3=43 primitive_systoles=218 unoriented_class_counts=86,66,65,1 class_vectors=01|11|10|12 singleton=2,4,16`
