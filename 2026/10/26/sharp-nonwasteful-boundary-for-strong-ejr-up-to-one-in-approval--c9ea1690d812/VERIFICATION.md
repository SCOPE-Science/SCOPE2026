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

# Reproducibility and verification

Run `python checker.py` using Python 3.10+ with only the standard library. The checker implements the original quantified conditions for ordinary EJR+ and strong EJR+ up-to-one with `fractions.Fraction`; it independently enumerates all affordable strict core objections and all weak Pareto improvements. The direct witness assertions and the replicated instances for factors 1 through 3 passed. A full exhaustive test of 12,746 profile/committee-size cases with up to three voters, four candidates, and one to three seats (with nonwastefulness required for one- and two-voter profiles) passed.

The exact general inequalities for arbitrary numbers of candidates, seats, and replication factors are proved in RESULT.md rather than inferred from finite tests. In particular, strict inequality at the strong payment cutoff matters and must not be relaxed to a non-strict comparison. No outside independent mathematical audit was conducted.
