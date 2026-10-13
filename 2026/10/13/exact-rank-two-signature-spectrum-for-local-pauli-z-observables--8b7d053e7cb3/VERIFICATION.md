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

The claim is proved analytically in `RESULT.md`. The critical identity is the exterior-square determinant formula applied to each local Pauli operator. In the computational wedge basis this gives the exact sum identity with Hamming distance, from which the universal upper bound follows without enumeration.

Sharpness is constructive: a product of arbitrary one-qubit states on the first \(n-2\) qubits with the two-dimensional Bell subspace on the final two qubits yields all compression vectors \( (t_1,\ldots,t_{n-2},0,0)\) with \(t_i\in[-1,1]\). Their norms fill the claimed interval.

Limits: this verifies the radial spectrum and quadratic bound only. It does not verify or claim a complete vector-range classification for \(n\ge4\).
