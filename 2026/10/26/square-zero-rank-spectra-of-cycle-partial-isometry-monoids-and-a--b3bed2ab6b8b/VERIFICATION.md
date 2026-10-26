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

# Reproduction and scope

Run `python3 cycle_square_zero_checker.py` with Python 3.10 or later. The script uses only the standard library. It independently enumerates all partial injections between disjoint domain and image subsets of a cycle for each \(3\le n\le12\), checks the cycle geodesic distance for every pair of domain vertices, and compares every rank coefficient against the separately implemented divisor-polynomial formula. The tests inspect \(4{,}447{,}144\) candidate partial injections and print `ALL_CYCLE_SQUARE_ZERO_CHECKS_PASSED 4447144` on success.

The separate larger-size calculations at \(n=81,82,121,122\) compare finite values with the leading parity-dependent asymptotics and scaled moments. These are numerical spot checks, not a proof of convergence. The infinite statements are proved in `RESULT.md` by orbit decompositions, Lucas-number exponential bounds, and a binomial central limit theorem. No independent mathematical assessment has been performed.
