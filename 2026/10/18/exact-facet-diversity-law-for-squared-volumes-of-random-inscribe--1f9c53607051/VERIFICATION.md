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

# Reproducibility checks and limits

The normalized volume of a sampled simplex is the absolute determinant of its barycentric row matrix. The proof checks the facet Dirichlet second-moment matrix, the weighted rank-two determinant identity, its squarefree coefficient, and the sharp Cauchy–Schwarz equality condition. These establish the assertions in all integer dimensions at least two.

The supplied standalone `checker.py` uses exact rational arithmetic and two independently enumerated determinant permutations. It verifies the predictions at dimensions one through four for three distinct facet-probability choices per dimension, including zero-probability facet labels; the dimension-one cases are auxiliary tests outside the theorem's stated dimensional scope. Monte Carlo tests sample new Dirichlet barycentric rows in dimensions two, three and four and check the formulas with measured standard errors. These finite checks alone do not establish the all-dimensional theorem.

The unrestricted iid second-moment/covariance determinant identity was already known (Rademacher, 2010), and the novelty comparison concerns only the explicit facet laws and the optimal stratified-versus-iid design. Primary-literature and mathematical-record searches did not identify a dominating equivalent, but search absence is not a proof of uniqueness. No independent mathematical audit has been conducted.
