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

# Verification details

The standalone script `check_edge_crossover.py` has no third-party dependencies. Running `python3 check_edge_crossover.py` from its containing directory successfully executed:

- Full five-component map versus scalar fifth iterate at exact rational parameters and edge states: `FIVE_STEP_RETURN_EXACT_RATIONAL_OK`.
- Both singular endpoint power laws using exact fractions: `SINGULAR_EXACT_POWERS_OK`.
- High-precision moving-time scaling and transition log-error estimates for growing return horizons: `MOVING_TIME_CROSSOVER_AND_BOUND_OK`.

The infinite quantifiers are proved in `RESULT.md` by the explicit logarithmic defect bound, which vanishes at the prescribed changing-parameter observation times, and by induction over each fixed downstream offset. Numerical testing is supplementary; no finite test is asserted to establish convergence for every horizon, initial state or parameter.

A later journal version was identifiable by DOI, but the arXiv preprint was the full primary text inspected. The proof is restricted to the specified invariant edge and does not classify dynamics in the interior of the simplex.
