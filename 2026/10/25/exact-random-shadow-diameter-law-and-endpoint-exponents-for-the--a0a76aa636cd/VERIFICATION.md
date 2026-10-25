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

# Reproduction and verification limits

The proof's critical identities can be checked independently by projecting all six vertex pairs of the explicit unit-edge tetrahedron. The standard-library script `verify_tetra_projection_diameter.py` checks 30,000 random directions, compares five CDF values with numerical spherical-chamber quadrature, confirms the extremizing normal, and checks convergence to both endpoint coefficients. Run with `python3 verify_tetra_projection_diameter.py`.

The run reported `DIRECT_SIX_EDGE_PROJECTION_AGREEMENT_OK 30000`, five `NUMERICAL_CDF_AGREEMENT_OK` lines, `BOTH_SHARP_ENDPOINT_ASYMPTOTICS_OK`, `EXACT_MINIMIZING_DIRECTION_AND_SUPPORT_OK`, and `ALL_RANDOM_TETRAHEDRON_SHADOW_DIAMETER_CHECKS_OK`.

The universal assertion uses the six-edge identity, chamber geometry and Taylor estimates in `RESULT.md`. Finite experiments cannot establish the theorem, strict global support claims, asymptotic constants, or historical novelty. Independent audit is not performed.
