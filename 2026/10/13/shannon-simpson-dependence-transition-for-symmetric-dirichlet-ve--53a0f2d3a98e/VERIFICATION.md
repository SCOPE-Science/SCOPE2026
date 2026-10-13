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

# Verification of symmetric Dirichlet Shannon–Simpson dependence

The mathematical argument is in `RESULT.md`. An ordinary reproducibility checker is supplied in `verify.py`; execute `python verify.py` using Python 3 with NumPy, SciPy and SymPy installed.

The checker separately reconstructs the mixed moment \(\mathbb E[HQ]\) via differentiated Dirichlet exponents, the entropy variance via second derivatives, and the Simpson variance via fourth moments. Symbolic subtraction of the claimed formulas simplifies identically to zero. It also simulates twelve Dirichlet laws (four dimensions and three positive shape values), each using 300,000 seeded draws, and compares sampled covariance with exact covariance within six conservative estimated standard errors. Finally, it checks high-dimensional correlation convergence for five fixed positive shapes and the small-shape limit for four fixed dimensions. All checks completed successfully.

**Limits of these checks:** Numerical simulation and finite parameter checks do not prove a statement for infinitely many dimensions or all real shapes. The monotonicity assertion rests on the positive integral for the trigamma combination, not numerical differentiation. The Gaussian limit rests on the iid-gamma multivariate central limit theorem and delta method. Historical priority and independent mathematical validation remain unresolved.
