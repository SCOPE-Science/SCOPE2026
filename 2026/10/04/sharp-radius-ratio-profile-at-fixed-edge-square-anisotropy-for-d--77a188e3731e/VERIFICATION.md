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

The analytic proof in `RESULT.md` establishes the infinite statement. The bundled `verify_profile.py` is a deterministic replay aid.

Running `python verify_profile.py` returned:

```text
VERIFY_OK
seed 210031
checks 157750
max_radius_formula_relative_error 4.441e-16
max_edge_anisotropy_error 9.992e-16
max_parametrization_error 4.829e-16
max_endpoint_error 1.214e-14
max_profile_violation 0.000e+00
```

The script checks the inradius independently through volume/surface area, checks the edge-based and coordinate-based definitions of anisotropy, checks the closed trigonometric formula, and checks both equality branches. Random finite checks do not certify the universal quantifiers; those follow from the symbolic derivation in the proof.
