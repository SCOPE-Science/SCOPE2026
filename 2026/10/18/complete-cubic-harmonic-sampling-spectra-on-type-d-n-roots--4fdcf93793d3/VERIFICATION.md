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
# Verification of the cubic root-sampling identities

The proof has two logically separate derivations: root inner-product arithmetic diagonalizes the zonal degree-three evaluation Gram, and coefficientwise Laplacian equations independently characterize its image and polynomial nullspace. Both are symbolic in every integer \(n\ge4\).

Run `python3 check.py` with Python 3 standard library only. This enumerates every signed root for dimensions \(n=4,5,6,7,8,9,10,12\) and calculates the normalized degree-three kernel exactly using integer dot products. It verifies the second-moment root identity, every Gram entry of the two-projector decomposition, each coordinate eigenspace, exact rational inversion of a nontrivial odd sample vector, and the claimed rank by modular elimination. At \(n=10\) it also verifies exact vanishing of kernel entries away from antipodal coincidence. All eight cases passed on the supplied code.

These calculations do not establish the theorem for untested dimensions. That conclusion follows from the full symbolic proof in RESULT.md. The cited earlier spherical-harmonic addition theorem is standard, but mathematical novelty still depends on whether an earlier source included the specialized type-\(D_n\) equality classification. The full 1977 association-scheme paper was not accessible for complete comparison.
