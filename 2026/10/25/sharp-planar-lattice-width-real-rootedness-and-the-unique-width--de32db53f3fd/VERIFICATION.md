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

# Reproducibility

Execute `python3 verify_planar_width_roots.py` from the extracted file directory. An actual run returned:

`PLANAR_WIDTH_ROOTS_OK det7=5 det9=3 low_discriminant_pairs=5`

The script uses only the Python standard library. Its independent integer-lattice enumeration checks four dilations of each of the five determinant-seven and three determinant-nine primitive Hermite triangles, and its finite primitive-direction search verifies their exact widths. The direction search bound is sufficient for these finite small certificates because any width below the obvious vertical span bounds both projected vertex coordinates, producing finite bounds on both integer direction components. The analytic proof of the theorem is in `RESULT.md`; universal statements are not inferred from finite tests. The published planar flatness and isominwidth inequalities are used, not independently certified here.

Independent audit has not been performed. Historical priority remains uncertain.
