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

# Reproducibility and scientific checks

Run `python checker.py` (NumPy required) next to this file. The checker uses a tilted Poisson-time embedded chain: between resets, the Brownian displacement at an independent exponential time has a two-sided exponential law; integration over site Voronoi intervals gives a finite-dimensional tilted transition generator. This is independent of the harmonic-coordinate method in the proof. Its first two eigenvalue derivatives recover the physical drift and asymptotic diffusivity.

Actual result: `PASS: 235 finite checks. Independent tilted-reset-chain and closed form agree.` Tests include six arbitrary/regular positive-gap configurations, exact destination-weight comparisons, row stochasticity, small-rate cubic-gap slopes, fixed-rate disorder reversal, large-rate asymptotics, and 100 seeded Cauchy/normalization comparisons.

The main analytic certificate is the derivation in `RESULT.md`: normalized invariant density, distributional forward equation, a C1 piecewise-sinh corrector solving the generator equation, exact bracket integration, ergodic martingale CLT, Taylor expansion and exponential asymptotics. Finite numerical tests do not prove the limiting theorem, strict general inequalities or publication originality.

There is no independent mathematical audit, no exhaustive bibliographic certification and no assertion about arbitrary clocks or nonperiodic environments.
