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

Run the included `check_hypersimplex.py` with Python 3, NumPy and SciPy. It tests the exact support-function formula directly against enumerated zero-one hypersimplex vertices for dimensions four through eight and all nontrivial ranks (250 comparisons). It also verifies six Gaussian covariance integrals by quadrature, locates the unique positive zero of the analytic covariance with a root bracket, and reproduces covariance signs on either side of the rank-fraction boundary by 20,000 fixed-seed random directions in dimension 768.

Analytical verification is in `RESULT.md`: the order-statistic support identity, quantitative DKW threshold replacement, joint Gaussian/radial delta method, exact covariance-convergence identity, Gaussian integration, and uniqueness argument for the covariance zero. The simulation is stochastic evidence, not an infinite proof. Neither numerical root finding nor a finite empirical covariance is used to infer uniqueness or asymptotic convergence.

The proof covers only fixed positive proportional ranks in the canonical hypersimplex realization. Independent mathematical validation remains not performed.
