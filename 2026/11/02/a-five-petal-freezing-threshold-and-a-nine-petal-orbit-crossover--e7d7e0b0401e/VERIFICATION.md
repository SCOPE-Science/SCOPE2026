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
# Reproducibility

Run `python3 verify_fca5_friend.py` using Python 3 and no third-party packages. It enumerates the finite 163835-state hub/occupied-petal-pair factor (plus the 5 unreachable empty-support states, which are excluded from the claim), determines every recurrent period, checks monodromy of ordered pairs along six-cycles, counts weighted supports using inclusion–exclusion, and verifies the sharp maximum first-periodic-entry times. It independently checks 81375 fully labelled configurations for one, two and three petals using explicit local neighborhood rules. The recorded stdout is included as `verify_fca5_friend.out`. No finite experiment is treated as proof for unbounded petal count: exact factorization and counting furnish that step.
