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

The argument proves all dimensions analytically through a decomposition into two independent uniform coupon streams, exact finite-stage stochastic domination, Gumbel convergence and a dominated Fourier-inversion calculation.

Run `python3 verify.py` with Python 3 standard library. It independently compares the finite formula with exact first-step visited-state recursion for each \(1\leq a,b\leq10\) and checks the strict majority split and four example fractions. Observed output: `PASS: 314 independent exact-rational assertions`. This does not constitute an exhaustive proof for arbitrary parameters; the mathematics establishing every claimed range is in `RESULT.md`. The limiting tie constant follows from the geometric characteristic-function envelope and Plancherel, not from numerical extrapolation.

Historical priority is not independently certified. The accessible 2008 and 2022 primary full texts were compared; a relevant 1993 publisher paper was accessible through metadata only, which is identified as a residual overlap risk.
