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

# Reproduction and proof checks

The source equations are \(\dot x_i=x_i[r(1-\sum_jx_j)-d-p_{i-1}x_{i-1}]\), with zero predator term for the first species. The proof checks the forward-invariant density simplex, the population logistic envelope, exact logarithmic-ratio cancellation, divergence of the first-species cumulative-population clock, and the inductive finite-integral-versus-divergent-integral dichotomy. This proves the result for every finite species count, not only the checked examples.

Run `python verify_hierarchy.py` with Python 3, NumPy, SciPy. The program tests the exact three-species terminal split, positive limiting mass, and the support-greedy selection rule for initial support patterns in chains of three, five, six and seven species. At the source package path the program returned `VERIFY_OK`.

The numerical integrations are finite-horizon diagnostic checks, not certificates of the claimed infinite-time limits. No external mathematical review or independent audit has been performed. The result does not claim a uniform decay rate across all positive initial configurations, and it does not cover unequal demographic rates or finite stochastic ecological populations.
