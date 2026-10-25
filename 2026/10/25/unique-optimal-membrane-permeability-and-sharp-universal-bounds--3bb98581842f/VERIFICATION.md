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

# Reproducibility and checked boundaries

The analytic derivation in RESULT.md establishes the theorem for the stated continuous parameters. For an independent computational reconstruction of the stationary *boundary-value equations*, run `python verify_membrane.py` with Python 3, NumPy and SciPy. No external data or file inputs are required.

The executable checks the interface boundary conditions by solving a four-unknown, piecewise-hyperbolic linear system on each side of a point reset. Its 110 randomly generated but deterministic point-source configurations compare the endpoint densities and flux against the closed form. Another 70 deterministic three-point mixtures test superposition. Ten contrasts are numerically optimized without using the critical-point root equation. Eighty contrast values check the optimizer's strict trend, while further computations check the weak- and strong-resetting limits, the first weak-rate correction and the sharp location envelope. This code was executed successfully.

The calculations use finite floating-point tolerances and finite test samples: they do not certify inequalities for infinitely many parameter choices. Those conclusions use the explicit strict concavity, hyperbolic identities and convexity proof. No conclusion about total reset entropy, nonsymmetric interface permeability, unknown-source reconstruction or independent external scientific audit is drawn.
