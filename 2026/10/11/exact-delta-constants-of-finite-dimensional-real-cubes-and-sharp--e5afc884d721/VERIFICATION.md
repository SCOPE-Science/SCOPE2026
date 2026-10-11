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

# Verification record

The theorem rests on the analytic finite-dimensional convex-hull reduction, the negative-face capacity lemma, the explicit convex witnesses, the strict positive separating-functional gap, and the dimension-dependent capacity bound. These steps are displayed in `RESULT.md` and are valid for all real dimensions \(n\ge1\) and all \(x\in B_{\ell_\infty^n}\).

Reproduce the exact-rational checks with `python3 verify_cube_delta.py`. The program uses only the Python standard library. Its executed output was:

`VERIFY_OK exact_rational_checks=31294 constructive=14941 separating=16353 dimensions=1..12`

The checker samples rational cube points and radii, constructs exact barycentric representations whenever the signed far-cap criterion holds, constructs explicit separating linear functionals when the opposite-cap budget fails above the coordinate-escape floor, and tests uniform-coordinate thresholds and global sphere extremizers. These tests were supplemented by 1,960 independent finite-vertex convex-hull feasibility comparisons using linear programming. Those exploratory LP checks have floating-point tolerances and are not asserted to be exact certificates. Neither test family replaces the quantified analytic argument. Boundary cases include \(n=1\), \(n=2\), \(n=3\), full vertices, zero coordinates, and opposite-cap endpoint radii.

No independent audit was performed, and no external mathematical validation is claimed. The scientific limitation is finite-dimensional real sup-norm cubes only; bibliographic coverage may be incomplete.
