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
# Numerical and analytical reproducibility

Execute `python signed_area_verify.py` using Python with NumPy, SciPy and mpmath. The script checks the Gaussian single-cycle covariance integral, the exact renewal-Laplace expression against its sharp small-frequency asymptotic, positivity and parameter boundaries of the stable constants, finite-horizon conditional-Gaussian characteristic functions for three distinct stable indices, and the signed-variance threshold. The executable check passed all 43 assertions. For the Cauchy example the finite-horizon characteristic-function approximation is visibly imperfect at the largest Fourier argument; the script explicitly tolerates finite-horizon error and does not claim a convergence-rate theorem.

Proof validation is analytic: the signed rewards are independent across *completed* renewal cycles but are not independent of their corresponding cycle durations. The deterministic renewal-speed limit permits the stable random-time-change argument despite this dependence. An incomplete final cycle must be controlled by tight backward age. For the variance, the renewal equation retains its final incomplete-cycle contribution, and the Tauberian step uses nondecreasing mean squared accumulated area, not the sign-changing sample area. Computations at finitely many parameter points are not an exhaustive proof of the theorem's parameter-wide limits. Independent external audit has not been performed.
