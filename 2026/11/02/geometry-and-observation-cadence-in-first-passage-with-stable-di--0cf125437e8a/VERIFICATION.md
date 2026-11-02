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

# Verification notes

Run `python verify.py` from the extracted package directory; dependencies: Python 3.10+ and SciPy. The numerical integration of Gamma-weighted error functions is independent of the closed-form Cauchy expression. The program also checks two different passive-wedge normalizations, long-time coefficients and the combinatorial sampled-sensing lower bound. Its printed check count and pass result were obtained from this package's actual `verify.py` file.

The Dirichlet eigenfunction expansion and stable negative-moment identity prove the all-angle/all-index statements; finite testing alone would not establish them. Numerical asymptotic checks have finite horizons and no unbounded-tail certification. The observed round-off and quadrature tolerance are included directly in the script. Mathematical and literature independence has not been externally assessed.
