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

# Reproducible checks

Use Python 3 standard library. Run `python3 verify_rank_types.py` and `python3 verify_intervals.py` in the same directory as the supplied programs. Compare stdout with `rank_output.txt` and `intervals_output.txt`, respectively.

The first checker computes the complete three-pebble, finite-rank type recurrence in the pure ternary cyclic-order signature (with equality) for circle sizes \(3\) through \(40\), including all partial assignments of the three variables up to orientation-preserving rotation. It does not assume the claimed classification when building the colors. The resulting class partition agrees with the formulas for ranks \(0\) through \(6\).

The second checker independently calculates the recursive interval threshold formulas' truth values, the split-profile stabilization at the inductive cap, and the existence of the two-arc lower-bound witness pairs. Its output lists the exact check counts and tested ranks.

These programs verify the stated finite calculations, not infinitely many finite structures or a formal proof checker of the theorem. The theoretical unrestricted-rank and unrestricted-size conclusions depend on the explicit combinatorial induction in `RESULT.md`. The calculations and literature comparison have not been independently audited.
