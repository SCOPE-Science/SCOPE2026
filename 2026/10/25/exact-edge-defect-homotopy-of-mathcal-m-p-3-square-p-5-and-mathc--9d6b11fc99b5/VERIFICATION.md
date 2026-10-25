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

# Verification

The standalone script `verify_grid_edge_defects.py` is part of this package, not an external dependency. Execute it with Python 3 (standard library). It enumerates all matchings, reconstructs every complete augmented face poset, constructs explicit Morse pairs from the 49 embedded orders, verifies the full directed Hasse acyclicity by topological sorting, checks each critical dimension/count, and checks Euler values independently through graph-vertex matching-polynomial recursion.

Observed output: `PASS 49 edge-deletion graphs; 774599 augmented faces; 4028730 directed cover incidences; 386842 Morse pairs`.

These computations prove only the 49 finite topological claims. They do not certify a formula for arbitrary grid width. No independent audit has been performed.
