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

# Reproducible verification

Unpack all files from the result package into one directory, then execute `python3 VERIFY.py` with Python 3.9 or newer. No external Python packages, network, proprietary software, or precomputed external table is required. `CERTIFICATES.json` stores the twelve coordinate vectors, the boundary triangulation, the 4 and 12 preliminary elementary pairs, the 12 core-to-boundary pairs, and the full 140-pair collapse of the larger Rips complex onto the same boundary triangulation.

The executable enumerates every one of the \(2^{12}-1=4095\) nonempty vertex subsets at the largest distance level, checking the exact integer squared distances \(8,24,32,40\) and respective edge multiplicities \(18,24,12,12\). It verifies that the convex hull has four triangular and four hexagonal supporting faces, that the indicated triangulation has face vector \((12,30,20)\) and all vertex links single cycles, and that the Euler characteristic is two. The free-face replay verifies at each step that the deleted face has exactly one remaining strict coface (its paired upper simplex), stronger than merely consulting a log. The reduced one-dimensional stage is connected with twelve vertices and fourteen edges; the two higher-stage collapses and the four-cell relative attachment argument establish the integral homotopy types.

All 24 coordinate-permutation/even-sign transformations are independently reconstructed, classified by their action on the four original tetrahedral corners, and evaluated by signed fixed-simplex traces. Their conjugacy-class traces must match the complete rational representation decomposition. The program outputs `VERIFY_OK`, `COLLAPSES_OK`, `GEOMETRIC_SPHERE_OK`, `S4_CHARACTERS_OK`, and `INTEGRAL_PERSISTENCE_OK` on success.

These checks verify the precise finite certificate, the symbolic topological deductions, and the stated group action. They do not establish a classification of other solids, an equivariant sequence of elementary collapses, an integral identification of the kernel lattice with the four-point permutation lattice, or absolute uniqueness in historical literature. No independent external scientific audit has occurred.
