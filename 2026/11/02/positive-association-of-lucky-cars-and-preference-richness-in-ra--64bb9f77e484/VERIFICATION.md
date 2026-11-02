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

The included `verify.py` can be run using `python3 verify.py` without external packages. It checks full bivariate tables via an independently specified circular recursion versus direct linear parking enumeration for each size from one to seven, accounting for 280,392 successful parking functions. It verifies local and aggregate moments, checks every realizable lucky-bit pattern's exact conditional preference-richness law and single-bit monotonicity, and evaluates selected increasing transformations and large-size asymptotic comparisons. The executed run returned `PASS: 3048 assertions; enumerated 280392 parking functions; correlation limit 0.6308785600416854`.

All enumerated equalities use Python integers or `fractions.Fraction`; finite large-size coefficient checks use floating-point arithmetic. The general association and asymptotic results are established by the proof in `RESULT.md`, not by finite enumeration. Independent audit and independent validation remain unperformed.
