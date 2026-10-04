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
The bundled verifier reconstructs the Hamiltonian for the six-state controlled model at a strictly positive interior test point.

Checks performed:
- Centered finite differences of all six state coordinates agree with the analytic Hamiltonian gradients underlying the corrected costates.
- Centered finite differences of all three controls agree with the stated stationarity derivatives.
- The recovered-state derivative contains the common incidence term induced by the state dependence of \(N\).
- With transmission suppressed, the susceptible quarantine derivative depends on the quarantined adjoint coordinate, isolating the printed coupling error independently of the incidence calculation.

The verification is local algebraic replay of the necessary conditions, not a full optimal-control trajectory recomputation. No independent audit has been performed.
