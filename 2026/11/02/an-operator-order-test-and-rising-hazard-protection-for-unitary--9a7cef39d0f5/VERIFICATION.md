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

## Reproduction

Install NumPy as specified in `requirements.txt`, then execute `python verify.py` in the same directory as the program. The script prints a passing assertion count and exits with an error if any check fails. A recorded execution passed 13,298 finite assertions.

## Actual checks

The program independently enumerated reset/no-reset histories for short horizons; compared the resulting state channels with their renewal sums; verified trace-preserving normalization and intervening-map compositions; checked positive semidefiniteness against Choi eigenvalues in dimensions two, three, and four; exercised arbitrary and nondecreasing hazards with random unitaries and pure/mixed resets; reproduced the exact two-step negative eigenvalue for several decreasing hazards; and checked the increasing age-hazard ramp through 100 discrete times. Source code uses a fixed random seed for reproducibility.

## Limits

The all-time, any-finite-dimension claim is analytic and cannot be established by sampling or finitely many Choi matrices. The strict obstruction follows from an exact symbolic eigenvalue, not from a numerical negative-value search. The computations assume double-precision complex arithmetic and apply explicit tolerances. Independent audit has not been performed.
