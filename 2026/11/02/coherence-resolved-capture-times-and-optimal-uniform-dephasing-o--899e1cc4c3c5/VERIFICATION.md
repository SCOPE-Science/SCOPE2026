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

# Reproduction and scope of checks

Execute `python check_star.py` with NumPy and SciPy. This constructs the full density-matrix generator and solves a linear first-moment equation independently of the reduced proof, on \(180\) combinations of star sizes, rates, coherent bright and dark states, localized states, and random pure/mixed states. Maximum observed relative error: \(5.330\times10^{-15}\). Maximum entrywise residual in the explicit adjoint Poisson equation: \(1.421\times10^{-14}\). The program also checks positivity and tests analytic dephasing minimizers.

The algebraic proof covers every integer \(n\ge2\), positive \(J\), \(\kappa\), \(\gamma\), nonnegative \(\delta\), and arbitrary trace-one leaf density matrix. A finite floating-point simulation is not a proof for all sizes. Exact zero leaf dephasing requires the separately analyzed invariant-subspace limit. Historical originality remains provisional; independent audit is not performed.
