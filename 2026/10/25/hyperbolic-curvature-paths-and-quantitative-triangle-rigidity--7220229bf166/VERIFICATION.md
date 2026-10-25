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

# Reproduction and limitations

Run `python verify.py` using a standard installation of Python 3; no extra packages or external files are required. The code independently computes polygon area and area centroid by shoelace integration, computes boundary and exterior-angle centroids, and then independently integrates the disjoint original polygon, outward edge rectangles and circular vertex sectors to obtain exact geometric moment expressions numerically. It compares those moments to the rational parallel-body centroid formula at 875 polygon/offset settings and independently checks a differential determinant identity. Randomized polygon examples are reproducible because their pseudorandom seed is fixed. It also tests 278 scalene triangles having separated angles and eight isosceles triangle paths. A successful run prints `PASS`.

These finite checks cannot prove the theorem for every convex body or every triangle. The proof requires the analytic partition argument, continuity under convex polygon approximation, the conic discriminant, and strict concavity of sine with its divided-difference integral. Those steps appear in `RESULT.md`. Arithmetic tolerances are used only in numerical regression tests; the mathematical statements contain no floating-point assumptions. The bound's global sharpness is not claimed. No independent audit or external publication-priority validation has been performed.
