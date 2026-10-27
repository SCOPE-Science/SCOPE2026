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
# Reproduction

Run `python3 verify.py` in a standard Python 3 environment. It enumerates every idempotent map on sets of sizes one through five, every ordered commuting pair of them, and every triple of ranks, and compares against an independently evaluated integer-polynomial fiber recurrence. It also tests the sharp support inequalities and checks the standard single-idempotent rank formula. Observed total pair counts are 1, 7, 58, 601, and 7616, respectively. The final line is `VERIFY_OK_COMMUTING_IDEMPOTENT_TRIRANK`.

These are exhaustive checks only for the five finite sizes indicated. The general formal identity and support characterization follow from the mathematical argument, not from finite sampling. No separate independent mathematical audit is claimed.
