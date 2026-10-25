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

# Reproducibility and verification

The file `bipyramid_checker.py` uses only the Python standard library. Execute `python bipyramid_checker.py` from the directory containing this file. The script reconstructs triangle planes and outward unit normals directly from all vertex coordinates and the exact centroid formula. It then classifies each face by the strict barycentric position of the centroid's perpendicular projection, each edge by the perpendicular-foot parameter and the positivity of both adjacent normal-cone coefficients, and each vertex by strict dot-product inequalities on its adjacent edges.

The program exercised \(56\) noncritical parameter cases in all three open regimes for seven polygon orders \(n=3,4,5,6,8,11,20\). Every reconstructed signature matched the exact stated phase formula, and every case satisfied \(S-H+U=2\). Sample printed signatures for \(n=3\) are \((6,9,5)\), \((3,6,5)\), and \((3,3,2)\); for \(n=4\), they are \((8,12,6)\), \((4,8,6)\), and \((4,4,2)\).

These finite floating-point checks do not prove the theorem for arbitrarily large polygon order, real heights, or exact transition parameters; the proof uses closed-form centroid, plane, cone and edge-foot inequalities. The script deliberately tests strictly noncritical samples and does not purport to certify degeneracy at a floating-point equality. No independent audit is asserted.
