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

# Computational verification

Run `python3 verify_triangular_strip.py` using only Python 3 standard-library modules. The procedure constructs each open-neighborhood tetrahedron from the graph's exact coordinate adjacency, materializes all faces, and tests each free-face deletion against the faces **currently present**. It verifies the surviving triangle list explicitly, counts every edge incidence, checks each vertex link is a connected six-cycle, propagates consistent integral triangle orientations across all edges, verifies dual connectedness and Euler characteristic, and checks the excluded four-cycle's full face vector.

Exhaustive finite inputs tested: \(n=3\) and all \(5\le n\le40\); the program checks 37 examples and 4,878 individual collapse pairs. The exceptional \(n=4\) has face vector \((12,42,48,12)\) and Euler characteristic six. The exact recorded output is embedded as `verification_output.txt`.

**Limits.** The finite checks establish only the enumerated cases. The all-integer theorem depends on the written unique-common-neighbor proof and the deck-translation plane-quotient proof, which are not replaced by code. No independent mathematical audit has been performed.
