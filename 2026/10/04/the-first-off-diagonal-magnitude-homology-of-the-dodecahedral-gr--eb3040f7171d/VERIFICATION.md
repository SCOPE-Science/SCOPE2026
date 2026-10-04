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

The verifier reconstructs the dodecahedral graph as \(GP(10,2)\) from 30 defining edges and computes its all-pairs shortest-path metric. For length \(4\), it exhaustively generates the magnitude chain bases in degrees \(2,3,4\), obtaining dimensions \(1440,3240,1620\). A separate dynamic-programming count reproduces all three dimensions.

The boundary deletes exactly smooth internal vertices. Over \(\mathbb F_2\), the resulting matrices have ranks \(1320\) and \(1560\). Each rank is recomputed after transposition, and every degree-4 boundary column is checked to map to zero under the degree-3 boundary. Thus the verified homology dimension is \((3240-1320)-1560=360\).

The verifier additionally finds two shortest paths of length \(4\) between vertices 0 and 4, certifying that this graph is not geodetic; this records why the general geodetic-space theorem does not subsume the calculation.

Limits: the replay proves only the stated \(\mathbb F_2\) bidegree. It does not prove an integral decomposition, absence of torsion, or any assertion about other bidegrees.
