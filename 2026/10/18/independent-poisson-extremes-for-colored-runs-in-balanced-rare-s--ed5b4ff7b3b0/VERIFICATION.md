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

# Verification of the conditional run-extremes theorem

The standalone file `verify.py` is executable with Python 3 and the standard library. On the delivered code, `python verify.py` completes successfully and reports **285 finite exact/analytic comparison assertions**.

Checks performed: enumerate every balanced binary word of even lengths 2 through 14; compare capped maximum-run counts for each attainable switch count against independently computed pairs of positive compositions; compare exact odds-weighted probabilities at three rational parameter values; and check the finite uniform Bessel estimate at sizes 40, 100 and 400 using an independent positive-series implementation. The exact checks use integer and rational arithmetic, while only the Bessel diagnostics use floating point with a displayed numerical tolerance.

This finite program verifies combinatorial ingredients and a finite approximation inequality at tested instances. The proof in `RESULT.md`, not the test output, establishes concentration, conditional coupling and weak convergence for all asymptotic sequences in the stated range. No external validation or independent audit is claimed.
