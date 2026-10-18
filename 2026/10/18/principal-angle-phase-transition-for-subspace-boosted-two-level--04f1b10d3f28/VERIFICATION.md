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

The formula follows algebraically from principal-angle two-by-two blocks, monotonicity of characteristic roots at fixed determinant, and minimization of the normalized trace. There are no external theorem-prover certificates and no claim of independent audit.

Run `python verify.py` using Python 3 and the Numpy dependency recorded in `requirements.txt`. This reconstructs symmetric inverse-preconditioner products and compares their extreme eigenvalues with the claimed analytic roots for 50 multi-angle cases and 300 scalar boost values. It checks the computed optimal gain against the tested alternatives and separately checks four high-contrast critical-window examples. The numerical program is only a reproducibility and transcription check, not a proof for arbitrary dimensions or all angles.

Scientific limits: exact two-level SPD spectrum, equal-dimensional target/candidate spaces, scalar boost \(\gamma\ge1\); no theorem for nonuniform eigenvalue clusters, nonlinear solvers, or full CG convergence trajectories.
