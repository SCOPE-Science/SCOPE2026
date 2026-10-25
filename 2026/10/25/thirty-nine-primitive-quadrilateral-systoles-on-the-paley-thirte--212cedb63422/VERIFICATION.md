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

# Reproduction and limits

Run `python3 verify.py` with Python's standard library. The exact expected output is included as `verification_output.txt`. The script reconstructs the specified Paley graph and its face complex, verifies all 13 six-cycle vertex links and absence of a four-clique, enumerates all 26 triangles and 78 unoriented simple four-cycles, partitions the latter as 39 induced and 39 chorded, computes integral lattice-displacement homology coordinates for every cycle, and verifies three translation orbits and the 78-element affine symmetry group's 39-element orbit. The determinant-one calculation certifies integral, rather than solely rational, generation of first homology.

The proof in RESULT.md derives the covering lattice and the simple-cycle count mathematically; the program exhaustively corroborates the finite case. The scope is a single finite graph and its clique torus. The files do not claim an independent audit, classification of all higher-length nontrivial cycles, or coverage of unrelated tori.
