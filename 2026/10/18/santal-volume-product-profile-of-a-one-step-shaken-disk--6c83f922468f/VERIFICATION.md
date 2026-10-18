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

The self-contained `checker.py` reproduces the elementary polar primitive against independently integrated improper integrals at six deformation parameters, tests first- and third-order Santaló-center drift and the quadratic Mahler deficit, and evaluates the flat-sided endpoint. Execute with Python 3 and `mpmath` installed using `python3 checker.py`.

The general correctness argument is mathematical: a polar angular integral, strict convexity in the center, the established shadow-system convexity-and-rigidity theorem, and a Taylor expansion. The checker performs finite precision spot tests only, and cannot independently certify uniqueness over a continuum or the completeness of the literature search. The checked domain is one vertical single-step deformation of the unit disk, not a random iteration.
