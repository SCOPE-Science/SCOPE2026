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

Run `python3 verify.py` with Python 3.10 or later, using only standard-library modules. The executable verifies the synthetic model's exact fractional loop coefficients, the quadratic branch identities, the claimed optimizer, the exact two-sided threshold polynomial, and the endpoint inequalities. A seeded randomized finite stress test compares the stated global optimizer with grids of admissible positive coefficient triples; this is computational evidence only.

The infinite universal assertion is established analytically in RESULT.md by the explicit characteristic quadratic, positivity of the root discriminant, implicit differentiation, uniqueness of critical points, and endpoint monotonicity. No computer enumeration is used as an infinite proof. The result does not address nonautonomous seasonality, nonlinear stability, or fitted real-world interventions. Independent audit is not performed.
