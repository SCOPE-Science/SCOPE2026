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

# Reproducibility and verification

Run `python3 verification_check.py` with a standard Python 3 installation; no nonstandard packages or input data are needed. The checker uses finite differences to diagnose strict radial concavity, the exact no-reset survival functions, sharp fixed-mean chord/Jensen inequalities, the Poisson mean expression, and composite Simpson quadrature for deterministic reset intervals.

Actual local execution output:

```
line: Poisson point=4.67077427047, endpoints=3.0269152273; periodic-clock point=3.39837801428, endpoints=2.54866173411
sphere: Poisson point=21.1671682968, endpoints=9.72458187132; periodic-clock point=17.5634865109, endpoints=9.21599294246
PASS: 332 finite assertions
```

The analytic proof supplies the global result: exact one-cycle Brownian survival; strict radial concavity for every positive elapsed time; convex-order comparison; a common-quantile coupling of the one-cycle first-passage laws; synchronous renewal-cycle induction; and positive chance of success in every fresh search cycle. The finite numerical checks only corroborate selected formulas. No simulation or numerical quadrature is used to assert all-clock stochastic order, uniqueness or almost-sure completion.

Verification boundaries: the one-dimensional target and exterior three-dimensional spherical target, generator \(D\Delta\), fixed initial position, independently sampled reset radii on a bounded interval separated from the target, strictly positive finite iid renewal intervals, and instantaneous full spatial relocations. Full-law inequalities need no mean waiting time; finite mean time formulas require finite mean reset intervals. Numerical inequalities at very short times can be obscured by floating-point cancellation and are therefore not used in the proof. Independent scientific validation has not been performed.
