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

# Verification record

The package includes the complete `check.py` source. It verifies the exact symbolic coefficients of the first three squared-distance moments by rational Dirichlet integration, six exact rational reconstruction examples, the two-moment counterexample, and 420000 independent simulated point-pairs for numerical corroboration. Run with `python3 check.py`; expected terminal success message: `TRIANGLE_PAIR_DISTANCE_MOMENTS_OK exact_polynomial_orders=3 rational_cases=6 monte_carlo_samples=420000`.

The infinite theorem rests on the displayed rational moment identity and the polynomial inverse, not on finite simulation. An external mathematical audit has not been performed. Historical priority may require additional checks beyond the inspected literature.
