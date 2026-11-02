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

# Reproducible verification and proof limits

The accompanying standalone Python 3 program `check_unicyclic.py` requires only the standard library. From the directory containing it, execute `python3 check_unicyclic.py`. It enumerates every simple graph with the same number of edges and vertices for \(3\le n\le7\), discards disconnected graphs, and checks the full exact bivariate table of unique-cycle length and leaf count against the derived inclusion-exclusion formula. It also checks the conditional means, strict finite regression, exact first and mixed moments, and finite numerical signs and convergence trends for selected larger sizes. The exhaustive totals are 1, 15, 222, 3660 and 68295.

Finite exact and numerical computations do not prove the statements for arbitrary graph orders. The general proof is in `RESULT.md`: the rooted-forest matrix-tree determinant and deletion bijection are exact for arbitrary \(n\); strictly increasing conditional means establish the covariance sign; a truncated-Poisson limit, vacancy martingale central limit theorem, and uniform-integrability argument establish the asymptotic joint law and covariance coefficient. The proof treats the pure-cycle and triangular boundary cases separately.

Only the uniform labeled simple connected unicyclic model is covered. A full stochastic ordering of leaf-count distributions at different cycle lengths has not been established. Independent external validation and independent audit have not been performed.
