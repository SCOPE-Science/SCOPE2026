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

The included `verify.py` uses only the Python standard library and exhaustively enumerates the relevant subsets of the eight cube vertices.

It verifies:

- the cube adjacency relation from Hamming distance one;
- exactly \(32\) disconnected four-sets with parity profile \(1,12,6,12,1\);
- exactly \(8\) disconnected five-sets;
- face vectors \((8,28,56,32)\) for \(\Delta_4(Q_3)\) and \((8,12,8)\) for \(\Delta_5(Q_3)\);
- the complete two-skeleton of \(\Delta_4(Q_3)\);
- exact rational ranks \((7,21,32)\) of \(\partial_1,\partial_2,\partial_3\);
- a specified \(32\times32\) minor of \(\partial_3\) with determinant \(-1\);
- the eight level-five facets as exactly the two tetrahedral boundaries on the parity classes;
- both parity tetrahedra as level-four simplices, giving explicit three-ball extensions of the two sphere inclusions.

The finite checks imply the integral homology used in the proof. The final equivalence \(\Delta_4(Q_3)\simeq\bigvee^3S^2\) uses standard Hurewicz and homological Whitehead theorems after simple connectivity is established from the complete two-skeleton. The null-homotopy is proved by the explicit filling tetrahedra and target connectedness.

No claim is made for higher-dimensional cubes or for cut levels other than those stated.
