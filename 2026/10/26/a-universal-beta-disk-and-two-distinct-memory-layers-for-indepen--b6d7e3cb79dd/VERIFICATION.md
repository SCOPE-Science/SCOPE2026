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

# Mathematical verification

The standalone `checker.py` uses Python's standard library. Run `python checker.py` in a directory containing the extracted result files. In the reviewed package it printed `PASS 613 deterministic checks` and then `PASS 640 total deterministic checks including time-covariance limits`.

The checks cover angular stationary-density normalization and Fourier harmonics, radial Beta moment and derivative quadrature, exact rational stationary generator equations (position, position/orientation products, quadratic observables), the quantitative limit bound on second moments, parameter recovery identities, and limiting two-time correlations reconstructed from an exact finite-stiffness covariance formula. These checks do not replace the infinite-dimensional stochastic-process and limiting-time arguments in the proof.

The two-time finite-stiffness derivation can be independently reproduced from the orientation conditional mean and a linear first-moment equation between resets, with position reset contributing its own linear loss term. The exponential kernel at coincident relaxation rates is interpreted continuously.

No independent validation or external audit has been undertaken.
