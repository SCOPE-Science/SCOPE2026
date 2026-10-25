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
# Exact verification

Run `python3 verify_triangle.py` with the Python 3 standard library. The script was run on the exact embedded source and passed its checks: 48 labeled mixed-state rational fixation recurrences, 48 mean-time recurrences, an independently assembled twelve-orbit transient-chain linear solve for both quantities, and six class/boundary comparisons. The complete finite algebra also appears as a six-row transition table and substitution argument in RESULT.md.

Each attempt samples uniformly one of six ordered focal/speaker pairs. For \(\Delta\eta\geq1\), only the threshold flags are needed. The uniform positive two-step absorption chance is the analytic justification for uniqueness, not an assumption made by the solver. The script checks finite linear identities, not arbitrary graph sizes or limiting stochastic behavior.

The public scientific status is self-reviewed; no independent audit has been performed.
