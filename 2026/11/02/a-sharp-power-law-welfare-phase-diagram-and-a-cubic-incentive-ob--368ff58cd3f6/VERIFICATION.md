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

# Reproducibility

Run `python3 verify.py` in the same directory as this file and `RESULT.md`. The deterministic verifier checks exactly 144 line configurations attaining the predicted bound (population sizes 3–20 and eight tested exponents), 18,000 seeded random profiles against the predicted upper bound, finite examples for \(q\le1\), and an exact rational successful deviation at exponent four. The observed output is:

```
VERIFY_OK sharp_constructed=144 random_profiles=18000 power4_manipulation_before=1/3 after=154668497/466849700 phase_q1_and_subcritical=checked
```

The root comparisons use floating-point arithmetic; the explicit profitable deviation at exponent four is exact rational arithmetic. Finite testing cannot prove the sharp bound for arbitrary real exponents or metric profiles, nor a universal incentive violation for all \(q>3\). Those conclusions rely on the proof and one-sided derivative in `RESULT.md`. The previously known exponents one and two remain prior results; independent audit is not performed.
