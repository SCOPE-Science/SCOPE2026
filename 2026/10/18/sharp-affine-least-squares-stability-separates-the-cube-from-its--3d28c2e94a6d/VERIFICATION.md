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

The companion `check.py` runs using Python 3.10 or later. Its exact-rational component requires only standard-library modules (`fractions`, `math`). Optional SciPy quadrature independently checks the two one-dimensional integral reductions. In the reviewed execution, all 365 assertions passed.

The exact comparison for dimensions three through twelve is exhaustive, using symbolic rational fractions from the displayed formulas. Infinite-dimensional extrapolation is not made from those tests: for dimensions at least thirteen the analytical lower and upper bounds give strict separation. The central-limit and uniform-integrability proofs give the asymptotic constants. The correctness of the analytical derivations and the asserted originality have received the stated self-review; independent audit has not been performed.
