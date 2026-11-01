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

Run `python verify_integral_lattice.py` with SymPy and NetworkX installed. The script enumerates the eight-arrow simplices, constructs a canonical spanning tree and nine fundamental integral cycles, forms all eight triangle boundary rows, checks Smith invariants, then computes symmetry matrices by applying graph automorphisms to signed oriented edges. It confirms the dihedral relations, the full integral rank-three cocycle basis, the unimodular conjugacy with the natural \(A_3\) coordinate-permutation action, and the determinant-two gluing index.

The reported cochain matrices are forward pullbacks; the theorem uses inverse pullback as a left action. The checker explicitly verifies that convention. There is no approximation, randomized verification, external proof assistant, or claim beyond this finite graph. The result remains subject to independent mathematical review.
