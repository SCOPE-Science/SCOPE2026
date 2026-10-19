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

Run `python3 checker.py` with standard-library Python 3. The program exhaustively generates nonisomorphic trees through ten vertices via leaf extension and complete canonical center encoding, enumerates all edge-support sets and exact maximum matching sizes, reports one duplicate profile at ten and none below, and independently checks both witnesses via rooted polynomial recursion. `ALL_EXACT_CHECKS_PASSED` indicates all assertions passed. The enumeration does not extend past ten; the character-theoretic conclusion for all odd prime powers follows mathematically from the pre-existing rank formula.
