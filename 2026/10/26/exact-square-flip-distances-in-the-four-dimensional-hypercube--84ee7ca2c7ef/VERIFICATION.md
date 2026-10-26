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

# Exact verification procedure

Run `python3 verify.py` in a directory containing this file and the standalone checker. The checker has no external data or library dependencies. It constructs all \(272\) perfect matchings by two independent recursive algorithms; it constructs the adjacency graph using both coordinate-square flips and the four-edge symmetric-difference criterion; it compares these complete adjacency representations; and it exhausts all \(264\) BFS source states.

The exact expected integer checks are: component sizes \(264,1,1,1,1,1,1,1,1\); unordered pair distances \(768,2640,6032,9360,9504,5296,1104,12\) for distances \(1\) to \(8\); eccentricity multiplicities \(252\) at \(7\) and \(12\) at \(8\); and three antipodal connected components, each a four-cycle. It checks automorphism-orbit sizes and degrees under all \(384\) geometric symmetries.

A successful run prints `VERIFY_OK` and an explicit distance-eight matching pair. Exhaustiveness is finite; this does not prove any analogous property for larger hypercubes. The published \(272\)/\(264\)/eight-frozen census is independently recreated, not attributed as new. No independent audit has been performed.
