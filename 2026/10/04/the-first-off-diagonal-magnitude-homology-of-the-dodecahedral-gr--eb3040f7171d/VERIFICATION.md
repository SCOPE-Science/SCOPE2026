---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

I independently rebuilt \(GP(10,2)\), its all-pairs shortest-path metric, and all magnitude chains of length \(4\) in homological degrees \(2,3,4\). The chain dimensions are \(1440,3240,1620\). Direct bit-exact elimination over \(\mathbb F_2\) gives \(\operatorname{rank}\partial_3=1320\) and \(\operatorname{rank}\partial_4=1560\), hence \(3240-1320-1560=360\). The frozen verifier uses the same definitions but independently cross-checks chain counts by dynamic programming and ranks by both column and transposed-row elimination; its certificate agrees. This is exhaustive finite linear algebra, not an extrapolation.

## originality

PASS

Asao--Hiraoka--Kanazawa prove first-off-diagonal vanishing only when girth is at least seven; the dodecahedral graph has girth five, so their theorem is inapplicable. Gu's full paper computes trees, pawful graphs, the icosahedral graph, and cycles, not the dodecahedral graph. Asao--Wakatsuki determine geodetic spaces, but the dodecahedral graph is not geodetic, as the assigned verifier exhibits two shortest paths between a pair at distance four. Resultary searches found no published exact \((3,4)\) value for this graph.

## value

PASS

The dodecahedral graph is a canonical distance-regular polyhedral graph lying outside the easiest geodetic and high-girth regimes. Its first off-diagonal magnitude-homology rank is a natural exact benchmark for testing the sharpness and scope of general structure theorems, and the complete finite computation is nontrivial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
