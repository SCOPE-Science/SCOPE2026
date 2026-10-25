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

# Computational checks and proof boundaries

Run `python3 verify.py` using Python 3 with only the standard library. It checks separately reconstructed polyhedron vertices and edges against the analytical face-incidence counts at nine positive parameters (1,500 generic orientations for each), checks four one-dimensional interface integrals by Simpson quadrature against their analytic values, evaluates the known cube limiting identity for the exact quadrilateral cone law, compares 550,000 Gaussian/Haar normals at two offsets with the predicted two-sided octagon loss and the exact quadrilateral probability, and checks three additional cube-side parameters using 70,000 random orientations apiece.

A successful complete run prints:

```
INDEPENDENT_POLYHEDRAL_EDGE_ENUMERATION_ALL_CHAMBERS_SAMPLED_OK
FOUR_SPHERICAL_INTERFACE_INTEGRALS_OK
HAAR_TWO_SIDED_OCTAGON_BREAKDOWN_AND_EXACT_QUADRILATERAL_LAW_OK 550000
EXACT_QUADRILATERAL_SOLID_ANGLE_AND_CUBE_ENDPOINT_OK
ALL_CUBOCTAHEDRAL_PHASE_TRANSITION_CHECKS_OK
```

The reconstruction is sampled, not an exhaustive enumeration of all real normal directions. The infinite statements rely on the symbolic face-incidence formulas, exact spherical solid-angle identity, analytic interface integration, and local error bounds in `RESULT.md`. Numerical Monte Carlo experiments cannot prove the error exponents, originality, or conditional assertions at measure-zero orientations. No independent mathematical audit was performed.
