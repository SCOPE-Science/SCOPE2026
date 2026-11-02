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

The finite checker `checks/check_covariance.py` uses only Python standard-library integer arithmetic and `fractions.Fraction`. Run: `python3 checks/check_covariance.py` from the research package root. The program exhaustively enumerates words for \(2\le a\le7\), \(2\le b\le6\), checks all eligible pairs of distinct positive run lengths, verifies the \(t\)-polynomial identities on \(10\le t\le140\), and compares exact signs against the limiting sign polynomial off critical values. Passing finite tests does not certify the universal limits; their proof uses explicit falling-factorial expansion. Historical-priority validation and independent audit are outstanding.
