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

Run `python3 verify.py` with Python 3. The script constructs all initial binary words for each ring length from 3 through 16, evaluates the actual exceptional-site update, identifies every eventual cycle, verifies that the only possible periods are one and two, and confirms that both states of every genuine two-cycle differ solely at the exceptional site. It separately counts run-length compositions and matches the closed coefficient formulas. The printed success line is `CONTRARIAN_VERIFY_OK`.

The infinite assertions follow from the frozen-pair and run-composition proof, not from finite enumeration. No independent audit has been performed. Extinction-time distributions, multiple defects, alternate update rules and unindexed historical sources are not resolved.
