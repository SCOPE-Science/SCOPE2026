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

# Reproduction of the integral homotopy calculation

Execute `python verify_paley23.py` with Python 3.9 or later. No external packages, local data files, or downloads are required.

The verifier rebuilds the 23 facets from the nonzero quadratic residues modulo 23. It checks the 42,297 distinct nonempty faces, an exactly reproducible sequence of 19,184 elementary simplicial collapses, the remaining 3,929-face subcomplex, and the complete acyclic matching of that subcomplex. It checks the 212-by-4 integral Morse boundary via signed gradient reductions, proves the upper bound on its rank by an exact column relation, and proves the lower bound and primitive image by a specified determinant of absolute value one. The standard CW-attachment argument in RESULT.md then yields the integral homotopy classification.

The checker is exhaustive for the specified finite complex but is not a theorem covering different tournaments or field orders. Independent external validation has not been performed.
