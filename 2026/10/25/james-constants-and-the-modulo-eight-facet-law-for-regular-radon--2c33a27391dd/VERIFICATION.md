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

Run `python3 james_polygon_check.py` with a Python 3 standard-library interpreter. The program calculates the Minkowski functional directly as the maximum of all polygon facet functionals, independently of the simplified trigonometric formula. It compares the two evaluations for fourteen admissible orders from 6 through 98, verifies the vertex and vertical-edge unit directions and their chord symmetry, and computes 448 sampled local James values by bisection for isosceles partners. It also checks the hexagon value \(3/2\) and the previously known decagon value \((3\sqrt5-1)/4\).

The completed run printed `CHECK_OK: 14 polygon orders, 448 sampled local James values; exact special-value checks passed.` These floating-point checks are finite corroboration, not an exhaustive global search or a proof of the entire family. The actual argument uses the planar-polyhedral vertex-reduction theorem and the exact nearest-facet calculation recorded in RESULT.md.

No independent mathematical audit has been performed. Bibliographic originality remains subject to the full text of Mizuguchi's 2020 paper and any unindexed older calculations.
