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

# Verification and boundaries

The theorem is established in `RESULT.md` by exact quotient geometry, an explicit two-center torus-covering identity, the cup-product obstruction, and exact elementary Voronoi radii. No finite experiment is treated as a proof for all sources.

The standalone `tetra_radius_verify.py` was executed using Python, NumPy, and SciPy. It generated a periodic triangular supercell, computed Voronoi vertices of two shifted copies of the lattice, and tested the following claims: vertex eccentricity \(2/\sqrt3\) (computed \(1.1547005383792515\)); three nonzero order-two shift classes with eccentricity \(1\); and 250 pseudorandom generic shift classes satisfying the analytic bounds. The generic sample minimum was \(1.000031628761\), maximum \(1.149742494086\). Re-running with the included fixed random seed should reproduce the indicated checks to floating-point tolerance.

The implemented finite Voronoi calculation avoids randomized perturbations; numerical checks are corroborative and are not a universal certificate. The analytic argument does not use SciPy.

The exact result is silent on uniqueness of the six known edge-midpoint minimizers, uniqueness of vertex maximizers, general polyhedral metrics, and any independent historical originality certification.
