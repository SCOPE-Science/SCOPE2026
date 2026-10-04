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

Run `python3 verify.py` with a standard Python 3 interpreter. The script reconstructs the 20-vertex, 30-edge cubic graph \(G(10,2)\), exhaustively enumerates every matching, constructs the augmented simplicial boundary maps over \(\mathbb F_2\), and performs exact bitset Gaussian elimination. It checks the complete matching-count vector, all ten boundary ranks, the reduced Betti vector, and the reduced Euler characteristic.

The verified terminal marker is `DODECAHEDRAL_MATCHING_F2_VERIFY_OK`.

The calculation is finite and exhaustive. It does not verify integral homology, torsion, cup products, or homotopy type, and none of those are part of the claim.
