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

# Reproducibility and limits

The source and target are specified completely in `RESULT.md`. Run `python3 verify.py` in the same directory as `collapse_certificate.txt`, using Python 3. No third-party packages or external data are required.

The checker independently generates the entire finite map set via (i) the ideals/components parameterization and (ii) recursive assignments in a linear extension; both produce exactly 2836 identical order-preserving functions. The exact ideal distribution contains 430 ideals. Every one of the 2824 certificate lines is verified as a legal up- or down-beat deletion against the *current* surviving pointwise poset, not an out-of-date original order. The final twelve functions are checked against the four constants and all eight coordinate projection/automorphism maps, and every induced terminal comparability is checked. The certificate contains 2668 up-beat and 156 down-beat deletions.

Expected success output:

`VERIFY_OK maps=2836 ideals=430 two_enumerations=true beat_deletions=2824 core=4_point_circle_plus_8_isolates nonzero_maps=8`

The checker and certificate together establish the exhaustive finite reduction; the mathematical conclusion uses Stong's beat-point strong deformation-retract theorem. They do not prove anything about infinite parameter families or replacement of the finite function space by a geometric realization mapping space. Independent audit has not been performed.
