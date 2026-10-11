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

# Verification details

Run `python verify.py` with SymPy installed. Its exact rational-polynomial simplifications verify the first integral, invariant-leaf equation, dissipation formula, orientation of the \(y=-1\) boundary, the Dulac divergence, and the Hamiltonian linearization. The optional SciPy quadrature records sample periodic-orbit times at finite energies. No finite set of samples certifies the infinite-energy limit; that limit follows from the turning-point estimates in the proof. The same is true of LaSalle convergence, finite-time escape and the invariant-measure classification, which are proved analytically.

All claims concern the exact vector field and the explicitly stated parameter and state-space regions. An independent scientific audit has not been performed.
