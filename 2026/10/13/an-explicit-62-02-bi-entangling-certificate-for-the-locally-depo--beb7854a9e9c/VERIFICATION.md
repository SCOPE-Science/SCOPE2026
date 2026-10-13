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

`verify.py` is a standard-library exact-arithmetic replay of the endpoint certificate. It represents numbers as elements of \(\mathbb Q(\sqrt6)\), checks the radical identity for \(p_*\), checks positivity and normalization of all convex weights, reconstructs the sixteen Pauli-error probabilities, and verifies exact equality with the fifteen affine-support mixture.

For separability, the checker reconstructs each support's affine parity constraints. The CNOT Choi stabilizer eigenvalue bits are related to the output-Pauli label \(u=(x_1,z_1,x_2,z_2)\) by
\[
e=(z_2,\ x_1+x_2,\ z_1+z_2,\ x_1).
\]
Each affine constraint is converted to a product of \(G_0,G_1,G_2,G_3\); the checker then verifies pairwise symplectic commutation of the restrictions to the left subsystem of the asserted cut. The simultaneous-local-diagonalization argument in `RESULT.md` converts those checks into exact separability certificates.

The replay does not attempt to optimize over the full bi-entangling set and therefore does not certify that \(p_*\) is minimal. It certifies only the stated constructive endpoint and, together with the analytic local-noise composition argument, the interval \(p\ge p_*\).
