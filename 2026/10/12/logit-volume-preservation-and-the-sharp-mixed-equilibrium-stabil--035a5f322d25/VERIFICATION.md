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

The theorem was reconstructed from the source's affine marginal-incentive model and checked symbolically at the level of general formulas.

The packaged script `artifacts/verify.py` was run from the packaged path. It returned `VERIFY_OK`. The script checks exact rational instances of the weighted-cycle identity \(J^N=(\prod_i a_i)I\), checks the closed positive-real-root counts across multiple dimensions, and checks exact cancellation of the two-player conserved-quantity derivative.

The finite script checks are regression tests only. The general proof is the analytic argument in `RESULT.md`: zero divergence after the logit transform, the weighted-shift identity, exact root geometry, strict-pure-equilibrium linearization, and the explicit first integral in the exceptional two-player case.

Limits: no claim is made for non-robust games, discrete-time updates, stochastic perturbations, or global higher-dimensional attractor classification.
