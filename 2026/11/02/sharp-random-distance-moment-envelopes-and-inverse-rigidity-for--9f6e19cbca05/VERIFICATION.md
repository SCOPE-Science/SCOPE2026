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

# Verification of the random-distance moment theorem

The accompanying self-contained `verify.py` was executed with Python 3 and returned:

`VERIFY_OK exact_moment_profiles=1651 independent_quadratures=12 simulation_draws=180000`

It implements the exact finite-sum moment integral using rational arithmetic, independently approximates the survival integral, samples wrapped coordinate differences directly from pairs of Haar-uniform torus points, and checks the two sharp configurations. Its cases span dimensions 2 through 7 and multiple nonuniform ratios, including repeated lengths.

The full theorem is not inferred from those cases. Its proof is the CDF identity, monotonicity of two rescaled quantile functions, the integral tilt comparison, and a limiting argument. Exact-population hypotheses and all strict/equality boundary cases are in the main mathematical statement.

No external or independent audit has been performed. The literature comparison establishes only best-knowledge historical priority, not a certification of novelty.
