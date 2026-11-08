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

# Verification record

Run `python3 checker.py` using a standard Python installation (3.9+). The program deterministically constructs every occupancy state for 1–4 walkers, generates the killed-chain transition matrix, and performs exact rational Gauss–Jordan elimination for the first two integrated survival moments. It asserts the exact fractions for means and zero-rate derivatives.

A second exact computation uses ordered tuple states of sizes 4, 16 and 64 for one, two and three walkers respectively. This independently checks the occupancy-count reduction and its rates. At reset rate \(r=1/1000\), an independent exact inversion of the resetting generator verifies a decrease for three walkers and an increase for four walkers. The four-walker certificate uses all 35 count states and the explicit transition construction; an independent full 256-state exact inverse was not run. The full finite-state equations, rather than a partial search, prove the rational claims.

The restart derivative identity is analytic and follows from the renewal equation under exponential tails. Strict signs imply a nonempty interval of small positive reset rates on each side of the sign change. No claim is made of the globally optimal reset rate, or of behavior for five or more walkers.

All numerical fractions in the result are produced by deterministic rational arithmetic, not fitting, Monte Carlo, or approximate spectral evaluation.
