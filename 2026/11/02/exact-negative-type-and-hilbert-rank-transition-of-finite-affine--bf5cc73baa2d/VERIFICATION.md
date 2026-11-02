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

# Verification of affine-plane incidence negative type

The theorem's algebra uses only the affine-plane axioms, the exact distance block matrix and the identity \(BB^{\mathsf T}=qI+J\). The class-contrast, mixed, and global quadratic sectors sum to the full zero-sum dimension. At the claimed exponent the mixed determinant inequality, global negativity inequality, and parallel-line equality are analytic for all eligible orders; the order-two case has a direct four-coordinate realization.

Run `python3 verify_affine_negative_type.py` with Python 3.9 or later; no third-party dependencies are needed. The script builds five finite-field affine planes independently, compares every graph-theoretic shortest-path distance with the formula, and checks centered Gram inertia below, at, and above the sharp exponent. The matrix diagonalization is numerical and is explicitly limited to these five cases. The proof, not the numerical checks, establishes the universal quantifiers. No independent scientific audit or external certification is asserted.
