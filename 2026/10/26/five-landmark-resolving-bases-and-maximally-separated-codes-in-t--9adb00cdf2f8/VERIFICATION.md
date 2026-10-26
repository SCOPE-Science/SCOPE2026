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

# Reproducible finite verification

Run `python3 verify_resolving_petersen.py`. All computations use exact integers and the Python standard library. The script reconstructs the 45-state token graph from the five-label Kneser definition, recomputes all pair distances using breadth-first search, checks every four- and five-landmark set, enumerates the full induced 120-element group action and its orbits, and performs exhaustive clique counts for distance at least three. The verifier additionally checks distance signatures for all 30 extremal separated landmark sets.

Expected terminal line: `VERIFY_OK; 45 states; 120 moves; metric dimension 5; 189540 bases; 1627 S5-orbits; 30 optimal distance-separated bases`.

A full enumerative finite certificate is supplied, not merely a precomputed data table. This verification is same-source reproducibility and is not an independent audit. Potential unindexed prior computations remain a scientific originality risk.
