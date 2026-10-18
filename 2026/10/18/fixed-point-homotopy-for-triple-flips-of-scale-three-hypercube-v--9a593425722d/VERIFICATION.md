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

# Verification record

The theorem's infinite-dimensional assertion is established by the explicit orbit identification, a triangle-free base-graph argument, and integral homotopy pushouts of cross-polytope boundaries. No external independent audit or machine-checked proof is claimed.

Run `python check_fixed.py` (Python 3 standard library only). The script constructs the involution-orbit complex from the original binary vertex set and Hamming distances, enumerates all cliques, calculates exact mod-two boundary ranks by integer bit elimination, and separately checks the derived orbit-adjacency equivalence. Its reported nonzero reduced mod-two Betti pairs for \(n=4,5,6,7\) are \((0,1),(1,4),(5,12),(17,32)\). These are finite corroborations, not exhaustive checks for all \(n\).

The asserted sphere wedges, including integral freeness and fundamental groups, follow from the uniform topological proof rather than solely from computational ranks. The ambient group-representation results in the cited literature are not claimed as new.
