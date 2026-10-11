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

# Verification of the inverse-power two-cycle classification

Run `python3 checker.py` from the extracted directory using Python 3 with no third-party dependencies. The packaged run reported `PASS: 1804 exact-rational/float finite diagnostics.`

The checker constructs positive two-cycles from 253 rational ratios for each integer exponent from 2 through 8, verifies the cycle identities and threshold using exact fractions, and checks the derivative multiplier when the exponent is 2. It then checks 28 floating-point instances of the closed-form quadratic-inverse cycle and 5 finite grids of the hyperbolic-sine ratio.

These experiments verify sample identities, not uniqueness or existence for the continuum. The mathematical proof derives necessity from the cycle equations, proves strict hyperbolic-sine monotonicity, and obtains the quadratic-inverse multiplier by exact algebra. At the neutral multiplier \(-1\) no nonlinear stability classification has been attempted. No independent audit has been performed.
