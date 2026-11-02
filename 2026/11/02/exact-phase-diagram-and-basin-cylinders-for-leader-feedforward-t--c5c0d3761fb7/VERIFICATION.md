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

The claimed network ODE, scalar root equation, equilibrium count, hyperbolic index formula, all basin sets, and perturbation conclusion are established by the analytic steps in RESULT.md. The accompanying executable checker draws deterministic random row-stochastic feedforward instances, enumerates all recursively generated equilibria, checks equation residuals and Jacobian indices, and numerically integrates initial-value problems. It prints `VERIFY_OK` with counts. Numerical checks are finite corroboration only; no certified enclosure of all real-network behavior is claimed. The perturbation argument is analytic, and does not imply basin-cylinder preservation. The motivating manuscript's complete text was inaccessible; originality therefore carries an explicit source-priority risk.
