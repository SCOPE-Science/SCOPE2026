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

The proof is analytic for every admissible population endpoint \(M\), sample size \(n\), and range \(r\).

`checker.py` independently enumerates all subsets for consecutive integer populations with endpoint \(M\le17\). For every sample size and every observed range stratum, it computes the unbiased sample variance using exact rational arithmetic and checks the conditional average against the closed formula.

The finite enumeration is a consistency test only. No bounded computation is used to justify the universal quantifiers.
