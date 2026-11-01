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

# Reproducibility and proof limits

Run `python3 artifacts/verify_cube_section_inradius.py` from the extracted package root (Python 3, standard library only). The check constructs literal intersections of planes with the twelve edges of the 3-cube and calculates origin-to-facet distances directly, without using the normal-coordinate inradius formula in the polygon stage. It also independently integrates the two-coordinate Dirichlet density, checks that random radii lie in the deterministic support, and compares the high-dimensional cubic-scale mean and median with the analytic limit. The actual execution returned `CUBE_SECTION_INRADIUS_CHECKS_OK`, with 400 3D polygon instances, 6 quadratures, 36,000 random finite-dimensional radii, and 5,000 dimension-800 asymptotic samples.

A supplementary separately constructed local check optimized the center and radius jointly using a linear-program formulation in 300 random instances across dimensions 2, 3, 4, 5, 8, and 15 and matched the formula. This supplementary check is not required to run the standalone program and is not a formal or third-party audit.

For the universal assertion, read the proof of the projected coordinate-functional norm, equality of centered and freely centered best radii, the two center equations, the Dirichlet survival integral, both boundary expansions, and the Gaussian minimum plus uniformly integrable tail. Neither simulation nor a finite-dimensional check proves the assertions for arbitrary dimension or asymptotic moment convergence. The theorem does not establish first-publication priority beyond the inspected sources.
