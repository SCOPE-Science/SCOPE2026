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

# Reproducing the finite topological and equivariant computations

Use Python 3 and run `python3 verify.py`. No external packages, remote data, or supplemental certificates are required. The program reconstructs all fourteen vertices and twenty-one incidence edges, checks each of the 16,384 vertex masks, enumerates and validates all nonempty simplices, and constructs the deterministic fourteen-pivot discrete-Morse matching. It checks all 10,150 Hasse cover incidences and establishes that reversing the matched edges produces a directed acyclic graph; the remaining cells are one vertex and thirteen five-cells, giving an integral thirteen-sphere wedge by Forman's theorem. A separate mod-two boundary reduction recomputes the homology ranks.

For the equivariant part, the program enumerates the 168 invertible binary matrices, adds the 168 point–line exchanging symmetries, and checks the signed oriented simplex Lefschetz traces via two distinct parity computations for all 336 permutations. The exact trace-class distributions and representation identity are asserted. Compare stdout to `verification-output.txt`; success ends with the literal line `VERIFY_OK`.

The entire argument concerns this finite simplicial complex, including all cells and incidences. Mod-two agreement by itself does not establish integral homotopy; the complete acyclic matching does. The group character follows from the Hopf trace identity and the proven integral homology concentration. Neither an external audit nor a verification of absence from all possible prior literature has been performed.
