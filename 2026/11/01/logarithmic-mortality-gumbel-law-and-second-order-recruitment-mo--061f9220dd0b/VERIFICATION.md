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

The derivation uses the exact Poisson recruitment survival identity and an endpoint Laplace expansion after a reciprocal-time change of variable. The leading asymptotic assertions are analytical and are not inferred from finite numerical samples.

Execute `python verify.py` with Python 3, NumPy and SciPy. It checks dimensionless survival kernels by independent quadrature and a complementary-error-function formula, the convergence of centered distribution functions at several positive mortality coefficients and three evaluation points, and the exact mean integral by two equivalent survival representations. The executable reports its count and fails if any prescribed tolerance is exceeded.

The checks use finite parameter values and floating-point quadrature. They cannot replace a proof of uniform asymptotics or independently establish publication priority. Very large ratios are treated through logarithmic parameterization to avoid overflow; verified asymptotic agreement is approximate at finite ratios. No independent external audit has been performed.
