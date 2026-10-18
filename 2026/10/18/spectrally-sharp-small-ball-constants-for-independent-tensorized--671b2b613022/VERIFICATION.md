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

The standalone `verify.py` uses `scipy>=1.10` and reproduces 38 finite checks of origin densities, flat-spectrum constants, spectral imbalance, and direct small-ball integrals. Its actual completed execution printed `PASS: 38 scalar density, constant, and small-ball checks`, with two-probe rank-one asymptotic ratios 1.29470994, 1.21802548, and 1.17297716 at thresholds 1000, 10000, and 100000, respectively.

The rank-two exact Laplace density and the rank-one exact product-normal Bessel density independently support the normalizing constants; numerical checks are not a proof of the limit, nor of any statement for untested ranks. The analytic proof establishes all positive real moment orders using tail integration; finite samples cannot establish moment divergence.

Scope: independent real Gaussian factor pairs, fixed nonzero matrix, fixed positive integer number of probes, separable fixed residual, and asymptotically large threshold. Not covered: reused factors across an entire two-sided probing block; matrix-valued function approximation selected using the same sketch; non-Gaussian probes; finite-threshold sharp optimality or uniformity near singular-spectrum collapse.
