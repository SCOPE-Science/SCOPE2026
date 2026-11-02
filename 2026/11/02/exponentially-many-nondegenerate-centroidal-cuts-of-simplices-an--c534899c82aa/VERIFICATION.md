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

# Verification record

The standalone `verify.py` was executed with Python 3, NumPy and SciPy. Its direct output was:

```text
ALL_DIMENSIONS_EXACT_BETA_TAIL_AND_HESSIAN_SIGNS_PASSED
INDEPENDENT_DIRICHLET_QUADRATURE_HESSIAN_PASSED
EXACT_SYMMETRIC_TRUNCATION_PROFILE_AND_SECTION_SEPARATION_PASSED
ALL_CHECKS_PASSED
```

The checker performs exact rational beta-binomial tail and truncation calculations for bounded test dimensions and independent Gaussian-Legendre quadrature of both transverse Hessian-sign blocks for one representative dimension and partition. It is not an exhaustive computational certificate of the all-dimensional theorem. That universal conclusion follows from symmetry, exact beta aggregation, conditional Dirichlet moments, derivative calculations and cap separation in the analytic proof. In particular, the two sign blocks have strictly nonzero coefficients whenever their dimensions are positive.

Scientific limits: Only explicitly constructed partition cuts are classified; there may be additional centroidal cuts for higher-dimensional simplices. No independent audit or third-party certification has occurred.
