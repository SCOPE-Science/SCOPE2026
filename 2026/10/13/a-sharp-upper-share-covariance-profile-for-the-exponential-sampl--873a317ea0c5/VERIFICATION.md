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

# Reproduction and limits

Invoke `python3 verify.py` in the directory containing the standalone script. No third-party modules or data files are required.

The script evaluates independent exact covariance formulas for every integer sample size between 2 and 150 and every admissible top-share rank, totaling 11,324 exact-rational comparisons. It checks the finite-difference formula and complete maximizing set and evaluates the limiting optimizer in increasingly large sample sizes. It additionally generates 40,000 independent exponential samples for each of five sample-size/rank pairs using a fixed random seed, tests the two independent ways of calculating each statistic for each raw sample, and compares empirical covariances with analytic values within declared Monte Carlo tolerances. It ends with `VERIFY_OK` only when each assertion holds.

These finite and probabilistic checks are not an infinite-size proof, and approximate Monte Carlo agreement does not establish historical novelty. The exact all-size proof is the Dirichlet linear-functional calculation and sign-change analysis in `RESULT.md`. No external or independent audit was performed.
