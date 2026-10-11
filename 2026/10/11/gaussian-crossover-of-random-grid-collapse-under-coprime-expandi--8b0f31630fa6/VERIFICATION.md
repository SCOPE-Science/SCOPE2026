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

# Verification of exact random-grid Cramér cutoff

The included `verify.py` is a standalone standard-library script. Running `python verify.py` must print `CHECK_OK` after comparing all map-selection words through length six on the first three grids with an **independent exact rational integration** of the centered circle Cramér discrepancy. The tests also exhaust finite Bernoulli collapse probabilities through length nine and compare selected large-grid binomial sums with the limiting normal CDF.

The proof in `RESULT.md` supplies the infinite-range steps: exact cyclic subgroup arithmetic, a rational sawtooth integral for the discrepancy, the triangular-array central limit theorem with joint count dependence, convergence of the collapse CDF, and the geometric waiting-time central limit theorem at fixed unequal switching probabilities. The checker is only a diagnostic for finite cases; it does not verify the general analytic theorems, completeness of prior research, or independent correctness.
