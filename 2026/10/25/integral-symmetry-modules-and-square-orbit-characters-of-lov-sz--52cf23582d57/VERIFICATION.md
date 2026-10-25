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

# Verification and reproducibility

`verify.py` requires Python 3 and NetworkX as recorded in `requirements.txt` and runs with `python verify.py`. It invokes no external network service and no randomness. The observed output was:

```
PASS: 126 connected graph-isomorphism types (all from the Graph Atlas, <=7 vertices).
PASS: 386 automorphism actions; simplicial Lefschetz versus signed square-cell trace.
Graph types: 109 non-bipartite; 17 bipartite.
PASS: 12 additional graph-automorphism checks on eight- and nine-vertex constructions.
```

The verifier's neighborhood-side calculation enumerates every simplex from the actual open neighborhoods and computes the signed simplicial Lefschetz number. The comparison-side calculation independently enumerates every four-cycle as an edge set, enforces edge-disjointness, constructs both oriented lifted-square boundaries, checks that their original edge supports are disjoint, and verifies the action on their orientations. It checks identity Euler characteristics and all automorphism traces; a mismatch raises an exception.

The finite checks corroborate the sign conventions, topology and algebra. They do not enumerate all finite graphs. The universal result instead follows from the unique-center lemma, explicit equivariant retractions, the cellular square-boundary injection, and Euler's trace identity. Independent audit has not been performed.
