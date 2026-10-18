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

The embedded files `check_matching.py` and `check_homology_symmetry.py` are self-contained Python 3 standard-library programs. Their corresponding `.out` files record successful program output. The first program checks every face and every codimension-one inclusion against the explicit acyclic matching, rather than relying solely on the critical-cell counts. The second verifies face reconstruction from connected induced triples, all mod-two boundary ranks, and signed dihedral Lefschetz traces. All five graphs (8, 10, 12, 14, and 16 vertices) were checked. The Morse matching proves integral sphere-wedge types, while mod-two homology corroborates them independently.

The full finite arithmetic and matching are reproducible by running both programs; no external package or file is required. No claim is made for larger graphs, for integral equivariant decompositions, or for independent scientific validation.
