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

# Verification notes

- Reconstruction: the operator-distance calculation reduces to minimizing spectral width of a Hermitian pencil and matching top/bottom pure-state expectation vectors via Toeplitz–Hausdorff convexity.
- Boundary checks: one or zero measured operators follow by dropping coordinates; the zero-width case puts the target in the observed span. At scaling zero, the Pauli shell becomes the sphere of radius equal to the top-block mass. At scaling one, the full interval bound is attained by orthogonal block states.
- Independent identities: the two qubit blocks of each residual have eigenvalues centered at the scalar residual and displaced by the Euclidean Pauli coefficient norm; this gives distance exactly one.
- Run `python CHECK.py` to reproduce exact rational shell tests and floating explicit Pauli-vector witnesses. Finite checks provide consistency only; the proof establishes the continuum of parameters and arbitrary finite dimension.
- No externally performed independent audit or proof certification is asserted.
