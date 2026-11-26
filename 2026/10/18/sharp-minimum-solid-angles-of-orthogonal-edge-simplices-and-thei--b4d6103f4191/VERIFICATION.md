---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The sharp equivalent follows analytically from the rectangular-simplex cone comparison, Gaussian integral, strong law for exponential first and second moments, bounded convergence and Stirling's formula. The finite-dimensional angle formulas have known equivalent forms; they are not claimed as new. The scope is a simplex with one orthogonal vertex and angles measured as fractions of the full unit sphere.

The unchanged `right_simplex_checker.py` uses Python 3, NumPy, SciPy and SymPy. Its finite checks compare quadrature to exact angle formulas in dimensions two and three, check symbolic Dirichlet moment algebra, and sample the dimension-dependent expectation factor. The finite runs do not establish convergence or a sharp prefactor. The source package recorded expectation estimates of approximately 0.4417854, 0.3872053, 0.3728229 and 0.3690013 for dimensions 16, 64, 256 and 1024, respectively, against the limiting value 0.3678794.
