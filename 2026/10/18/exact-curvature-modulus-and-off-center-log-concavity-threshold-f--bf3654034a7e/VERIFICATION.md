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
# Verification of the exact curvature classification

The probability distribution is defined by three normalized Gaussian density components with weights summing to one. The analytic argument reduces the optimal curvature to a maximization of \(R_c(z)=(1+cz)/(c+z)^2\) for \(z\ge1\). The two displayed nonnegative algebraic certificates in `RESULT.md` prove this maximization for **every** \(c>0\) and all \(z\ge1\), including \(c=2\). The log-concavity thresholds then follow from a complete case distinction on normalized separation and the exact attained modulus.

The separate direct-formula comparison in `verify.py` evaluates the Gaussian mixture density, its first and second derivatives, and \(U''=(f'/f)^2-f''/f\) directly; it checks this against the hyperbolic formula at representative parameters and observations. Other tests check the exact rational factorizations and the strict-unimodality example's curvature constants. Run the script with `python3 verify.py` using the Python standard library. No Monte Carlo, search grid, or floating-point test constitutes a proof of the continuum statement.

At critical points \(\kappa=0\), the classification claims log-concavity but not strict positive strong convexity. The limit as the central weight approaches one is distinguished from the excluded single-Gaussian endpoint. Unequal-variance and asymmetric Gaussian mixtures are outside scope. Independent external validation has not been performed.
