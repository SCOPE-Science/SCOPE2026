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

# Reproducibility and verification limits

Both executable verifiers were run from their standalone files with Python 3 and require no external library. Running `python verify_desargues_direct.py --emit certificate.json` reproduces all labelled colourings and the exact switching graph; `python verify_desargues_matchings.py` independently reconstructs the cubic graph as the bipartite double cover of the Petersen graph and recomputes all claimed statistics.

Observed completion markers: `DESARGUES_DIRECT_PASS 192 504 [120, 12, 12, 12, 12, 12, 12] C4 180 C5 288`; `DESARGUES_INDEPENDENT_PASS matchings=60 states=192 edges=504 components=1x120+6x12`. The second program also prints the two distance-sphere profiles and verifies the claimed parity and chromatic distinction.

Exhaustiveness follows from the explicit backtracking branch invariants and the independent matching/alternating-cycle enumeration described in `RESULT.md`; finite output counts alone would not prove exhaustiveness. The certificate contains the full state/adjacency graph, a five-cycle in each nonbipartite component, a three-colouring of each such component, and a distance-five pair in the large component. The equality of the regenerated certificate bytes can be checked with a standard SHA-256 or byte comparison.

The scientific scope is the one finite Desargues graph and the stated single-cycle Kempe move. Literature priority remains subject to independent scholarly assessment. No independent audit or external certification has been performed.
