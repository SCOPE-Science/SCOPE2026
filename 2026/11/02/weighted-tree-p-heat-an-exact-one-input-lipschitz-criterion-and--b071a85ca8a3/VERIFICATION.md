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

# Reproducible verification

Run `python3 verify_tree_p_heat.py` with the Python 3 standard library. It independently enumerates edge-sign boundary configurations on six example trees for three integral exponents, computes star feasibility fractions exactly, and evaluates two-input Jacobian witnesses on a unit three-vertex path for six non-Hilbert exponents.

Observed output summary:

```text
BOUNDARY_EXACT_OK cases= 18 signed_faces= 678
STAR_MASS_THRESHOLD_EXACT_OK q=3,4,5
TWO_INPUT_WITNESS_OK p= 1.2 d_dt_first_gradient= 0.3999997
TWO_INPUT_WITNESS_OK p= 1.5 d_dt_first_gradient= 0.9999995
TWO_INPUT_WITNESS_OK p= 2.5 d_dt_first_gradient= 2.9999994
TWO_INPUT_WITNESS_OK p= 3 d_dt_first_gradient= 3.999999
TWO_INPUT_WITNESS_OK p= 4 d_dt_first_gradient= 6.0
TWO_INPUT_WITNESS_OK p= 5 d_dt_first_gradient= 8.0000031
ALL_TREE_P_HEAT_LIPSCHITZ_CHECKS_OK
```

Finite exact arithmetic applies to the boundary tests with integral exponents and the mass-threshold fractions; the nonintegral-exponent Jacobian witness is numerical. The universal theorem is established by analytical coordinate, invariance and Perron arguments in `RESULT.md`. The verification is not independent auditing or formal certification.
