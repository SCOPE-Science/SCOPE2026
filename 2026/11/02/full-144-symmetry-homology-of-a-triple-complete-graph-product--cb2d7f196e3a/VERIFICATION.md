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

# Reproducible checks

Run `python3 verify_triple_product.py` using Python 3.9 or later; no third-party packages are required. The program constructs the graph directly from the three-coordinate adjacency rule, enumerates 1,649 nonempty independent faces, checks exact mod-two boundary ranks, verifies 144 distinct adjacency-preserving coordinate actions, and computes their exact signed Lefschetz traces by graph-orbit deletion–contraction.

It verifies subgroup irreducible multiplicities, the three diagonal coordinate-exchange projector traces, the identity trace 14, the pure-layer trace 4, the pure-coordinate-exchange trace minus four, the combined-involution trace minus two, the index-two-subgroup invariant dimension one, and the full-group invariant dimension zero. It emits `TRIPLE_PRODUCT_144_EXACT_CHARACTER_AND_PROJECTORS_OK` on success.

The published integral homotopy classification in [1] supplies homology concentration; mod-two ranks alone do not prove torsion-freeness, nor do exact character calculations determine the integral representation lattice. No independent audit has been performed.
