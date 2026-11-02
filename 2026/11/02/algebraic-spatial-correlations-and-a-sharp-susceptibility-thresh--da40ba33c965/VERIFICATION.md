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

# Verification and reproducibility

The proof is given in `RESULT.md`. The accompanying `verification.py` checks deterministic numerical consequences, not infinite asymptotic truth. It requires Python 3.10 or later, NumPy and SciPy (specified in `requirements.txt`). After extracting these files into one directory, run `python verification.py`.

In the assessed package execution, the checker completed **71 assertions**, with no failures or integration warnings when warnings were promoted to errors. It compared the exact Mellin/Beta first-passage negative moments against independent endpoint-weighted numerical integration; checked the equilibrium renewal-age law against direct normalization; compared multiple stationary spatial covariances from scaled-Bessel first-passage densities with their explicit large-distance constants and Gamma-ratio upper bounds; and replayed the exact inverse-first-passage moment identity for integer order.

Finite-distance quadrature cannot certify an infinite-distance limit, an untested parameter value, or scientific novelty. The proof of universal asymptotics uses the exact Laplace/Mellin calculation, an explicit Poisson jump-count bound, and covariance summation. Independent mathematical and publication-priority audits have not been performed.
