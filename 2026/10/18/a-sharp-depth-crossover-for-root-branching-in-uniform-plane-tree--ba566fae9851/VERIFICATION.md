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

# Verification and limits

The proof rests on explicit generating functions and exact coefficient extraction, not computer enumeration. The included `verify.py` independently enumerates all 82,499 plane trees with 2 to 12 vertices and checks 45,024 assertions, including exact rational covariance evaluations and zero/sign boundaries through order 300. Run `python3 verify.py`; expected output: `VERIFY_OK trees 82499 assertions 45024`. This checks a finite range only. The asymptotic statement follows from a separate logarithmic product expansion for the Catalan coefficient ratio. No external or independent scientific audit was conducted.
