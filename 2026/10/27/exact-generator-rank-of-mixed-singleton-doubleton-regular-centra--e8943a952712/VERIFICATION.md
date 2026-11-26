---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the mixed-block centralizer-rank theorem

Run `python3 verify.py` in this directory. Closure starts with the actual generators and appends generators on the right to enumerate nonempty words. For \(b=1,2\), an independent target set is obtained by enumerating arbitrary full maps of the point set and testing commutation with the prescribed idempotent. This also checks all two-generator candidates for \(b=1\) and all 2,628 pairs of nonunits adjoined to the nonidentity unit for \(b=2\). For \(b=3,4\), the check verifies the generators commute and compares the closure size against the counting formula, rather than testing every full point map.

The predicted printed generator counts are 3, 4, 5, 5 and the corresponding closure sizes are 6, 75, 1,372, 32,805. These checks are finite; the normal form, explicit construction, and lower bound in `RESULT.md` establish the general theorem.
