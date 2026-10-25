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

# Verification of the rounded-polygon short-chord law

The accompanying checker calculates an invariant-line short-chord probability by direct high-resolution polygonal rounding, independent cross-section intersections, bisection of line depths, and angular integration. It compares numerical results with the formula for a square, a rectangle of equal perimeter and side count but different angles/aspect, and an equilateral triangle of matched perimeter and different side count. It also numerically verifies the \(-1/30\) coefficient of \(\Psi(s)/s^3\). The checker requires NumPy, SciPy and Shapely and runs with `python verify_rounded_chords.py`.

The program's spatial discretization and quadrature prevent treating the numerical agreement as an exact proof. The analytical argument is written in `RESULT.md`, including all hypotheses, branch restrictions and small-\(s\) expansion steps. The negative originality finding in a limited search is not a mathematical novelty certificate.
