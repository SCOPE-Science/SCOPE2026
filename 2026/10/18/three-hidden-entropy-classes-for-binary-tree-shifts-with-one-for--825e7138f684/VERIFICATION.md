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

# Reproduction checks and limits

Run `python3 verify.py` with Python 3 standard libraries. The checker enumerates all admissible labeled complete binary trees of heights one through four for the three forbidden-star representatives. It checks every forbidden word at height three under global bit complement and child exchange, and independently verifies the recurrence against enumeration. It checks representative recurrence inequalities through height eight and performs exact-fraction interval invariance and ordering checks. A 75-decimal-digit calculation evaluates the convergent entropy sums and the fixed-point prefactors, with an analytical omitted-series tail smaller than \((\log2)2^{-50}\) after retaining terms \(j<50\).

Executed outcome: `VERIFY_OK: 54 exact finite-enumeration, symmetry, interval, and high-precision assertions`.

The exact finite computations do not establish infinite-height results by themselves. Those follow from the recursion, strict interval contractions and the convergence estimates proved in `RESULT.md`. The numerical decimal computations are not formally interval-rounded and do not certify any unproved arithmetic property. Independent auditing is not performed.
