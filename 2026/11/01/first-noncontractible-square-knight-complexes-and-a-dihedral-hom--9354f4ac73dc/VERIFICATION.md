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

Run `python3 verify_knight_complex.py` in a clean directory with Python 3.9 or later; it requires no third-party packages. The script constructs the knight graphs directly from coordinate moves, checks that every edge is symmetric, enumerates the full face posets by two independently coded methods, and compares the enumerations exactly. It builds every Morse matching pair by deterministic vertex toggling, constructs the entire directed Hasse diagram, verifies that the global directed graph is acyclic by consuming all nodes with Kahn's algorithm, and verifies the critical masks and dimensions.

The same program independently applies all eight geometric board symmetries, verifies graph-adjacency preservation, computes oriented fixed-face signed Lefschetz traces, and checks the indicated dihedral character decompositions and invariant dimensions. It verifies that boards of size one and two have no knight edges and that the central vertex of the three-by-three graph is isolated. The successful recorded run ended in the literal string `VERIFY_OK`, saved in `verification_output.txt`.

These finite exhaustive checks prove the bounded mathematical claim through the explicit matching and Lefschetz argument; they do not establish a formula for arbitrary larger boards. A scientific literature search does not prove uniqueness of the result.
