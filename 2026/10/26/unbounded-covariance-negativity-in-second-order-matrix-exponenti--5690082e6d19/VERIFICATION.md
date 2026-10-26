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

# Reproducibility and proof boundaries

Run `python3 verify.py` with Python 3 and no additional packages. The program reconstructs the source-specialized formulas from \(f(x)\) and \(g(x)\), checks the exact Gram-covariance formula against Simpson quadrature, checks the METD1 determinant identity on several pairs, validates the METD2 off-diagonal formula and a finite negative-determinant witness, evaluates the exact rational inequality, and compares stiff-limit eigenvalue ratios with the proved value. The checked package passed **55** assertions.

No finite suite establishes the assertion for every decay-rate pair or the limit as the stiffness diverges. The full proof is in `RESULT.md`: integral representations establish strict positivity of \(f,g\), the Gram argument establishes true-covariance positivity, entrywise specialization identifies the numerical outputs, and continuity of eigenvalues establishes the asymptotic law. The precise input is two-dimensional, real symmetric strictly dissipative dynamics with rank-one positive semidefinite forcing, unit step, and zero initial covariance. The exact eigenvalue asymptotic belongs to the symmetrized numerical matrix, not to its non-symmetric raw output. Independent scientific audit has not been performed.
