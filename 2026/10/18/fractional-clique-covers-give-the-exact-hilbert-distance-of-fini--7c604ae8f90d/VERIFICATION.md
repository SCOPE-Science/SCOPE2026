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

The proof uses normalization of quadratic comparisons, averaging over coordinate sign changes, and finite LP strong duality. These are analytic and algebraic arguments valid in all finite dimensions, not extrapolations from enumeration.

The included `checker.py` runs using Python 3 standard-library modules only. Running `python3 checker.py` enumerates all 64 labeled simple graphs on four vertices and compares exact Fraction-valued LP optima for each primal and dual. It also tests seven explicitly matched primal/dual feasible witnesses, including odd holes and an odd antihole. Every check passed in the packaged source directory.

The perfectness characterization assumes the published strong perfect graph theorem; that theorem is not reproved or independently verified by the finite script. The code does not claim to certify every finite graph, every family, or absence of a prior equivalent theorem. Independent scientific audit has not been performed.
