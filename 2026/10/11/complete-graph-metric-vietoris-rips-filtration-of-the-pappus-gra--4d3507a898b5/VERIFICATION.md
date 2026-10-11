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
The verification target is the complete inclusive shortest-path Vietoris–Rips filtration of the 18-vertex Pappus graph in LCF form \([5,7,-7,7,-7,-5]^3\).

`artifacts/pappus_rips_verify.py` uses only the Python standard library. It verifies:

- the reconstructed graph has \(18\) vertices, \(27\) edges, degree \(3\) at every vertex, and diameter \(4\);
- the unordered distance-shell counts are \(27,54,54,18\) at distances \(1,2,3,4\);
- at scale \(2\), all \(225\) nonempty faces are enumerated and have face vector \((18,81,108,18)\);
- the stated successive-toggle matching contains \(99\) pairs, leaves one critical \(0\)-cell and \(26\) critical \(2\)-cells, and is acyclic after orienting every Hasse cover;
- an independent mod-\(2\) boundary computation gives Betti vector \((1,0,26,0)\) at scale \(2\);
- the distance-\(4\) graph is exactly six disjoint triangles;
- at scale \(3\), all \(4095\) nonempty faces are enumerated, with face vector \((18,135,540,1215,1458,729)\), and an independent mod-\(2\) boundary computation gives Betti vector \((1,0,0,0,0,64)\).

The mod-\(2\) computations are cross-checks rather than substitutes for the homotopy argument. The scale-\(2\) homotopy type follows from the verified acyclic discrete-Morse matching, and the scale-\(3\) type follows from the exact join decomposition induced by the six farthest-distance triangles.
