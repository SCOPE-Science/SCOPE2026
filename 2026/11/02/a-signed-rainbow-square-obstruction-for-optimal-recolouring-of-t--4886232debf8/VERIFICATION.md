---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Enumerated all proper states with an independently implemented backtracking routine from the 24-edge graph: 18,024 colourings and 64,320 Hamming-one edges. Independent adjacency traversal found two connected sectors of 9,012; evaluating the 11 oriented signed rainbow squares at all states gave exactly ±3 and no crossing Hamming-one edges. Enumerating cross-sector Hamming-distance-2 pairs gave 11,616 supported on 20 graph edges. Inspected chvatal_verifier_a.py and chvatal_verifier_b.py at exact Git blobs: program A checks graph automorphisms, 108 colour-symmetry orbits and representative BFS eccentricities (16..20), and B independently enumerates partitions and crossing pairs. Their exhaustive finite coverage is a proof method for this fixed finite graph, although the eccentricity aggregation was not independently rerun in this execution. 5-colour connectivity follows from the published Δ+1 theorem and impossibility of frozen 5-colourings because 5 does not divide 12. Domain is this specific fixed labelled finite graph, not all 4-chromatic graphs.

## originality

PASS

The new claim is the explicit signed 11-square invariant, exact two sectors, distances and minimal simultaneous crossing; the prior 18,024 count and Δ+1 connectivity are excluded as prior art. Relevant primary recolouring literature addresses generic graphs/three-colour winding obstructions, not this exact four-colour Chvátal partition in the inspected material.

## value

PASS

This smallest triangle-free 4-regular 4-chromatic benchmark has a mathematically natural recolouring configuration space. The exact disconnected-sector certificate, complete finite metric and sharp two-vertex escape inform concrete reconfiguration behavior; these results are more than recomputing a known chromatic polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
