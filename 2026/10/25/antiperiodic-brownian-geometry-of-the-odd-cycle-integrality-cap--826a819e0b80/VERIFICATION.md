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

The self-contained `odd_cycle_verification.py` uses NumPy and a fixed random seed. Running it directly checked that all simplex vertices invert to valid integral maximum stable sets for odd sizes 5, 7, 11 and 19, that the cyclic inverse identities and determinants are numerically accurate, and that the unsigned Euler secant numbers through order eight match 5, 61 and 1385. Its Dirichlet sampling reports, for dimensions 5, 9, 31, 101 and 501, empirical cap squared radii and the Laplace diagnostic at one, alongside the proved finite means and limiting transform.

The analytical proof does not rely on numerical tests. The exact polytope description and its Jacobian, total-volume operator spectrum, independent exponential representation, functional CLT, and Gaussian covariance eigenvalues are verified in the accompanying proof. Only an ordinary self-review is available; no independent audit or independent mathematical validation has occurred.
