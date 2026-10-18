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

The general conditional-matching argument and the integer Pell reduction are given in RESULT.md. The attached standalone `verify.py` enumerates all \( (2n-1)!! \) matchings for \(2\le n\le7\), determines all crossings and cyclic chord-length classes, and checks exact covariances, their zero condition, the conservation sum, and four independent Pell iterations. It reports 111 exact assertions passed under Python 3 using only the standard library. Finite enumeration is complete for the enumerated sizes, but is not a proof for infinitely many sizes. No independent audit or external verification is asserted.
