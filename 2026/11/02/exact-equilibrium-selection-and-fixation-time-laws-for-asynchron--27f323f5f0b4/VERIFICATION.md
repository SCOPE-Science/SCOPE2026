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

# Verification and scope

The theorem is proved by a uniform first-update permutation, a two-group exponential-maximum identity and memorylessness of independent Poisson clocks. The exact computation is an internal arithmetic check and does not certify uniqueness of the research result.

Run `python3 verify.py` with Python 3 and only standard-library dependencies. The program checks all \(1936\) initial producer-count states with \(1\le a,b\le8\), using direct rational first-step recurrences independently of the closed-form harmonic and hypergeometric-suffix expression. It also tests both winning probabilities and total suffix probability. Successful execution prints `PASS: 1936 exact rational states, two independent recurrences; suffix mass checked`.

The script does not enumerate every large-network action path or constitute an infinite proof. No stochastic simulation, external verification, or independent audit is claimed.
