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

# Computational checks and limits

Run `python verify.py` with a standard Python 3 interpreter. The script enumerates all loop-free directed relations on \(n=1,2,3,4\) labelled vertices, testing frame weak connectedness directly and, separately, the truth of the associated two-variable modal formula for every possible valuation and world.

Expected valid counts are 1/1, 4/4, 52/64, 1907/4096. Their edge-count polynomial coefficients are printed during execution. The independently checked implication is an exact statement for these four finite sizes; it does not establish the arbitrary-size or asymptotic claims, which have analytic proofs in RESULT.md.

The limits use (i) elementary binomial-to-Poisson convergence for independent rare outdegree rows and missing dyads and (ii) quantitative expectation/variance bounds for intermediate densities. No simulated data is used to prove infinite limits.
