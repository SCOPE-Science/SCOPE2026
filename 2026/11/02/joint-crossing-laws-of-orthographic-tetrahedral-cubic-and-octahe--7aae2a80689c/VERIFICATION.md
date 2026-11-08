---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For generic U the tetrahedral K4 projection has one proper disjoint-edge intersection exactly for a two-positive/two-negative affine dependence, equivalent to max |u_i| > sum of other |u|; otherwise none. The projected octahedral graph has four generic determinant-sign chambers with proper crossing counts 2,2,2,6 and cube has six such chambers each with 2 crossings; all parallelotopes reduce affinely to cube. These exhaustive open chambers and determinant sign invariance, not random samples, establish the pointwise coupling N_C=2 and N_O=6-4 N_T. Integrating 24 congruent spherical triangles yields p=(12/pi) arctan(3-2sqrt(2)). Independent vector-projection intersection calculation tested 5000 Gaussian sphere directions with counts 3334 for (1,2,2) and 1666 for (0,2,6), and no pointwise mismatches. Actual verify_wireframe.py symbolic determinant/chamber certificate was read; finite sampling alone is not an all-directions proof.

## originality

PASS

Best-of-knowledge PASS for the joint fixed-direction full-wireframe crossing relation and affine parallelotope two-crossing rigidity. Inspected geometric-drawing prior concerns maximizing crossings over all abstract graph drawings, while projection shadow counts concern visible silhouettes. A directly relevant 2009 cube-graph paper was accessible only by abstract, so its possible coverage is retained as risk.

## value

PASS

An exact coupling of crossing statistics of three canonical regular solids under the same Haar orientation, including an affine-rigidity statement for every parallelotope, is a natural discrete geometric invariant with potential use in geometric graph drawing and random projections; it is not a routine renaming of maximum graph crossing number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
