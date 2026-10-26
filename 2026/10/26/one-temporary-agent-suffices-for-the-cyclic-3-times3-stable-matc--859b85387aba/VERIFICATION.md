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

The standalone checker `verification/check_history.py` was executed with the Python standard library. It enumerates all matchings for the specified finite market, filters for individual rationality and absence of blocking pairs, verifies that the full market has exactly three stable matchings, verifies the unique stable matching of each five-agent submarket, checks the final-entry outcome for each missing terminal agent, and replays the one-temporary-woman history.

The checker output was:

`PASS: exactly three stable matchings; all six five-agent submarkets have unique stable matchings; every terminal-agent final-entry transition misses the middle matching; one temporary woman realizes it; the minimum temporary-agent count is exactly 1.`

`Temporary-entry proposal chain: 6:0:accept -> 5:0:reject -> 5:1:accept -> 3:1:reject -> 3:2:accept -> 4:2:reject -> 4:0:accept -> 6:0:reject`

The infinite-history exclusion is proved separately in `RESULT.md`: every terminal-agent history's first full-market occurrence of the middle matching would have to arise from one of the six tabulated final-entry transitions, none of which yields that matching. The checker does not claim a general result for larger markets. Independent audit and independent validation have not been performed.
