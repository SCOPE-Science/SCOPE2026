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

Run `python3 verify.py` in a directory containing the included standalone verifier. It uses only Python's standard library and checks 250 positive window lengths against 19 initial windows, several exact summation identities, and the stride-two gcd. A successful run prints a `PASS` message.

The mathematical claim for all window lengths and all starting positions is proved in RESULT.md; finite checks do not constitute an exhaustive infinite proof. No external independent audit has been performed. The scientific review is self-review only.
