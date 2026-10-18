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

The analytic proof uses the exact stationary Gaussian-mixture representation in arXiv:2312.02570v1, Gaussian Mills asymptotics for the normalized maximum, and Gaussian hazard bounds for dominated convergence at both trap-variance endpoints. No infinite statement is inferred from finite computations.

Run `python verify.py` with Python 3, NumPy and SciPy installed. The program evaluates the full finite-particle CDF integral by endpoint-resolved numerical quadrature, both asymptotic crossover integrals, and the two literal-edge asymptotic formulas for three parameter sets and three logarithmic particle counts. It also integrates the stationary mixing density directly. Actual execution returned `All 123 normalization, positivity, and large-N edge checks passed.` Numerical quadrature is approximate and its error thresholds are only diagnostics; its finite checks do not constitute an exhaustive proof.

The test uses \(\log N=120,400,1200\) as numerical asymptotic parameters and handles astronomical \(N\) through logarithmic normal-tail evaluations, without enumerating particles. Only positive switching and diffusion parameters and two strictly unequal positive trap stiffnesses are covered. Source priority beyond the inspected literature is not independently established.
