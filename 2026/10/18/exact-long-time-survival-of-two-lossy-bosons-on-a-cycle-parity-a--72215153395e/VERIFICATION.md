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

# Finite-matrix verification and its scope

The standalone Python 3 program `verify.py` requires NumPy and SciPy; it constructs the two-boson Hamiltonian directly from bosonic creation/annihilation occupancy factors, not from a reduced momentum expression. It separately constructs the projector onto doubly occupied states, diagonalizes the Hermitian hopping matrix, and finds the kernels of the loss projector within **each distinct eigenspace**. This procedure yields the full dark projector without directly assuming the parity formula.

Executing `python verify.py` with the accompanying dependencies performs 360 independent localized two-boson basis-vector survival checks and ten dark-dimension comparisons, for every ring length from 3 through 12. The run succeeded in the stated environment. By construction, this finite numerical confirmation is not an infinite-size proof, and the tolerance in the script accommodates floating-point eigenspace decomposition. The analytical momentum-sector proof in `RESULT.md` covers all \(n\ge3\).

No independent scientific audit or certification is represented here.
