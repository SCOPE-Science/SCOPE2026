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

# Verification of the switched coordination Floquet law

## Analytical verification

The proof is self-contained in `RESULT.md`: logit return-map differentiation verifies uniqueness and instability; exact selection-weighted residence identities yield the differential variance formula; the strict support inequality verifies monotonicity; phase residence-time divergence and Cesàro averaging give the slow-period limit. No computer-assisted infinite-domain certification is asserted.

## Executable check

Install `scipy >= 1.10` and run `python check_floquet.py` with Python 3.10 or newer. This integrates the original scalar differential equation over both switching intervals, accumulates a separate original-coordinate variational exponent, solves the return-map fixed-point equation, and checks the quantitative formulas over 31 finite parameter/period cases. It includes centered-difference numerical checks of the variance derivative and a fast-period expansion check. A passing numerical test is not a proof for all real parameter values or all switching periods. The code does not attempt to verify independent bibliographic novelty.

## Scope and limitations

The comparison is for fixed payoff and duty parameters as cycle duration varies, in a scalar nonstochastic coordination game with exogenous periodic switching. No inference is made about global convergence of the original two-population model, feedback-controlled schedules or stochastic stability. Independent review is not yet performed.
