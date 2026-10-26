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

Reproduce the finite checks with `python verify.py`. The script tests all increment sequences for cycle sizes \(4,6,8,10,12\); each exact histogram equals the independent integer path-matrix trace computation. It also checks total counts and the sum of image sizes. The run printed `VERIFY_OK` without exceptions.

The proof of the all-size claims does **not** rest on finite enumeration. Every graph endomorphism is coded by a closed nearest-neighbor walk. Its noninvertible image size equals its span plus one. Closed-walk trace differences count each possible span, and a first-maximum reflection bijection gives the precise binomial tail probabilities. The classical sum of those tails gives the exact mean. The 2009 primary paper on congruences of paths and cycles was unavailable in full text; overlap cannot be excluded absolutely. Independent audit and independent validation have not been performed.
