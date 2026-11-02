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

# Verification

The exact graph-level infected-count recursion and a separate uniform gate-rank conditioned recursion use rational arithmetic to calculate the mean flooding time on the two-clique, single-bridge network. They agree for every \(2\le n\le8\) and each bridge rate in \(\{1/2,1,3/2,3\}\). The gate-source specialization and lower bound obtained by retaining only the delayed second-clique completion are checked for the same parameter pairs. Total exact checks: \(84\).

Two further Laplace/moment product comparisons at each of \(n=100,1000,10000\) and \(s=\pm1/4\) confirm convergence toward the derived gamma transforms, totaling \(12\) additional numerical checks. Execute `python checker.py` to reproduce `CHECKS_PASS 96`.

The independence of the uniform infection order and the exponential holding times, the two-Gumbel convergence, the gate-rank Gumbel–logistic convergence, and uniform moment control are proved analytically in `RESULT.md`. No finite checker run is treated as an infinite proof. Source comparisons are limited to the identified papers and indexed searches. Independent audit and historical-priority certification have not been performed.
