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

# Reproducibility and scope

Run `python3 verify.py` with a standard Python 3 interpreter; there are no external dependencies. The program independently concatenates planar perfect matchings by union--find, tests rank and idempotence, independently constructs the commuting adjacency matrix, enumerates every clique by depth-first search, and checks the claimed recurrence, pair counts and maximum sizes. For \(2\le n\le8\), it enumerates all Catalan-many noncrossing perfect matchings and verifies exhaustion of the rank-\(n-2\) stratum. For every \(2\le n\le12\), it checks all \((n-1)^2\) corank-two diagrams and all ordered pairs of idempotents, together with the full clique polynomial. Completion marker: `VERIFY_OK_JONES_CORANK_TWO`. These tests are finite, not a substitute for the all-\(n\) argument. No independent audit has been performed.
