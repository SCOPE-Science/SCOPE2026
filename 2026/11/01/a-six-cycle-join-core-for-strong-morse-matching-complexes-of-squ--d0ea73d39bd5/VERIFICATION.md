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

# Verification instructions and boundaries

Run `python3 verify.py` with Python 3.9 or later and no external packages. All labels, expected local configurations, face counts and free-face checks are implemented in the standalone script. The script enumerates every total ordering for one, two and three square bouquets, rather than sampling them. It compares each result with the symbolic local model, checks mod-two chain ranks, and verifies full free-face certificates reducing the two- and three-square cases to joins of six-cycles. A successful execution ends with `ALL_VERIFY_OK`.

Verified outputs include 12, 72 and 378 maximal faces, and counts of 64 and 768 valid elementary collapse pairs for the last two cases. The full parameter theorem is established by the order classification and join-collapse argument in `RESULT.md`, not by treating finite enumeration as proof at untested sizes. No independent mathematical review has been performed.
