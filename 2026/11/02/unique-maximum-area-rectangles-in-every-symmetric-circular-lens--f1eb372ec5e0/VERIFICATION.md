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
# Reproducible checks and scope

The analytic statement and proof appear in `RESULT.md`. Execute `python3 verify_lens.py` using Python 3 and its standard library. The program prints `ALL_CHECKS_PASSED` when the following checks succeed: equality of the optimizer with its stationary quadratic; admissibility of the optimal rectangle at each tested parameter; the aspect-ratio inverse; strict rectangle-versus-square improvement for positive separation; a deterministic finite family of independently scaled feasible rotated rectangles whose areas never exceed the predicted maximum; and near-coincident and nearly tangent asymptotic coefficients. The candidate was run from the standalone file and produced `ALL_CHECKS_PASSED`.

These finite evaluations are consistency tests, **not** an exhaustive search over uncountably many rectangles and **not** proof of the theorem. The continuum argument uses a necessary-and-sufficient containment inequality, orientation minimization, a unique one-variable stationary point, and an averaging identity to eliminate possible translated ties. The checks do not establish historical priority, handle unequal disks, or constitute independent mathematical validation.
