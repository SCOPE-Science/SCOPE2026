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

Run `python3 verify.py` with the Python 3 standard library from this package directory. The test program makes 5,781 exact algebraic/sign and independent numerical consistency assertions. It compares the conditional-expectation and piecewise-polynomial covariance formulas at many rational parameter values, checks the complete predicted sign pattern away from its roots, tests exact six-point transition radii, and computes seeded independent Monte Carlo comparisons.

The exact rational checks use finite parameter grids, not symbolic quantification over all radii or graph sizes. Simulations are probabilistic corroboration and cannot prove the theorem. The infinite claim is established by the explicit conditional expectation and elementary polynomial inequalities in RESULT.md. No external audit has been performed.
