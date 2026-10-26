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

# Verification record

Run `python3 verify_coupon_comparison.py` using standard-library Python 3 in the directory of the accompanying files.

The executed test printed:

```
PASS: 1736 exact occupancy/coupling assertions; 1011 exact expected-time and drift assertions; total 2747.
```

The code independently enumerates the discovered-label set distributions under four deterministic eviction policies (including ones depending on the current coverage and time) for populations from three through six labels, then compares those laws with coupon collection on the initially missing labels. It uses exact `fractions.Fraction` and checks all admissible packet sizes. It separately computes independent-packet expected completion times by an exact absorbing-state recurrence and by inclusion–exclusion for populations from two through sixteen labels, validates the strict classification, and tests the superharmonic drift inequality at every relevant finite state.

Finite computations do not prove claims for unrestricted sizes or all possible policies. The proof uses a conditional transition-kernel identity and a strict potential drift calculation for those universal conclusions. No external independent audit was performed.
