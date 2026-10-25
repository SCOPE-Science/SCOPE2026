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

# Verification of the four-run antisquare-factor theorem

The included `verify.py` constructs each word directly and forms the set of all distinct contiguous antisquare strings by testing complementary halves, independently of the closed formula. It checks the formula, universal four-run ceiling, and both directions of the equality classification for all 4096 quadruples in the box \(1\le a,b,c,d\le8\). A separate formula-based enumeration checks fixed-length maxima at each \(4\le n\le80\), with reported average ratios for selected lengths.

The expected output concludes with `VERIFY_OK`. The direct enumeration is finite and cannot establish the theorem for unbounded run lengths. The proof uses the explicit exhaustive run-type argument, equality-bound analysis, and integration of a piecewise-linear simplex function. The \(\(7/16\)\) coefficient is derived analytically, not estimated from a sample.

No independent external validation was performed.
