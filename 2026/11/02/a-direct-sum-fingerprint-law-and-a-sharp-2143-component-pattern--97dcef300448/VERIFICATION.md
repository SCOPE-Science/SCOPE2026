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

Run `python3 verify.py` with the standard library. The checker evaluates all claimed finite-size signs through order 39 using exact `Fraction` arithmetic. It independently enumerates every permutation of lengths up to seven for every ordinary pattern of lengths two through four and compares the resulting true covariance with the formula. The proof itself supplies the separate analytic bound for \(n\ge40\); enumerating a finite range does not establish that bound. No independent audit is claimed.
