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

The exact-arithmetic checker `verify.py` ran and reported `PASS: 190 exact integer/rational assertions`. It compared the independent inclusion-exclusion double sum to a Markov state-count recurrence for all \(1\le a,b\le8\); checked the central-binomial closed form for \(1\le b\le17\); and checked balanced endpoint/coupon-tie identities, inequality strictness, and specified exact small values.

The asymptotic logistic limit and balanced \(1/(8m)\) correction are proved analytically in `RESULT.md`. The program is finite and is not an exhaustive proof of any infinite claim. No external or independent audit has been conducted.
