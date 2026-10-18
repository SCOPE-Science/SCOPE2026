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

# Finite verification

Run `python3 verification/verify_desargues_character.py` using Python 3 with no third-party packages. This reconstructs the twenty-vertex Desargues inclusion graph from subsets of five symbols, with thirty edges and 6,212 independent subsets including the empty one. It checks all 6,211 nonempty faces and all 30,360 codimension-one cover incidences, verifies acyclicity of a 3,102-pair discrete-Morse matching, and computes the five integral Morse boundary coefficients exactly; each vanishes.

The program explicitly constructs 240 distinct graph automorphisms, verifies that each preserves adjacency, and recomputes the signed Lefschetz trace on each by both oriented stable simplices and independent orbit families. The seven cycle-type values and their negatives under complementation agree with the closed formula given in `RESULT.md`.

The mathematical deduction from the trace identity and the rank-one fourth homology to the two rational representations is written in full in `RESULT.md`. The finite program does not certify bibliographic originality, an integral fifth-homology permutation-lattice structure, results for larger graphs, or independent scientific audit.
