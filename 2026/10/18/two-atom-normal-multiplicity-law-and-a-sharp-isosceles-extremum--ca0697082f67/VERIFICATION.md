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

The standalone `verify_triangle_normals.py` is self-contained and requires Python 3 standard library only. Run `python3 verify_triangle_normals.py`; the expected output is `TRIANGLE_NORMALS_EXACT_OK checks=2715`.

Exact rational checks compare a direct face-by-face normal-base enumeration with the analytically predicted four-or-six count on interior barycentric grids for six rational triangles. The program additionally checks the exact opposite-side interval identity in the obtuse cases and the squared-gap sharp inequality for rational leg ratios and angle-cosine parameters. Its assertion count is 2,715. The analytical proof in `RESULT.md`, rather than finite tests, establishes the theorem for real triangles and parameters.

No external or independent audit has been performed. Inaccessible historical full texts prevent definitive priority certification.
