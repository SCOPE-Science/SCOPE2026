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

The proof is analytic and self-contained in `RESULT.md`. In particular, the generator eigenfunction and exact pointwise flip-rate identity imply the explicit martingale bracket; finite simulation is not the basis for the theorem.

`check_entropy_work.py` runs reproducible fixed-seed exact-event simulations, with a Brownian Ornstein–Uhlenbeck conditional transition on each orientation-held interval. The stationary orientation state is sampled at the outset, but the simulated initial position is zero rather than stationary; this affects finite-time statistics only through an order-one transient. Program thresholds allow finite-sample noise; they cannot certify asymptotic normality or an exact equality for arbitrary parameters. It also evaluates the analytic derivative and its zero-count in six switching-ratio cases (including both boundary ratios).

Direct symbolic identities used in the proof are \(QV=-\Gamma V\), \(V^2=s^2+hV\), \(L A=-(\kappa+\Gamma)A\), and \(q_v(v'-v)^2=2\Gamma s^2+\Gamma h v\). Limits and critical-point uniqueness follow from a strictly decreasing rational function on the unit interval. The two-state stationary process has finite moments of every order under strictly positive confinement and diffusion.

All verification here is self-review. No independent audit has been performed.
