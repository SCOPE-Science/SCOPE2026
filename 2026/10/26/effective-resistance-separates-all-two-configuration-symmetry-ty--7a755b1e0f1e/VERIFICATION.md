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

# Exact finite verification

Execute `python3 verify.py` with Python 3 standard library. It reconstructs the Petersen graph by two definitions and checks the equality of their fifteen edges; constructs all 45 two-token states and 120 moves; calculates and checks a rational inverse of the 44-by-44 grounded Laplacian; enumerates all 990 pairs and all 120 induced label permutations; computes complete pair orbits, every rational effective resistance, distances by independent breadth-first search, and the Kirchhoff-index sum. Expected final output: `VERIFY_OK; 45 vertices; 120 edges; 990 unordered pairs; 17 orbits and 17 distinct resistances`. The executable is contained within the package and has no external dependencies.

The classification concerns only the specified 45-state finite graph, with unit edge resistors and pairwise effective resistance. The exact arithmetic and exhaustive loops do not assert a result for arbitrary token graphs. No independent audit was performed.
