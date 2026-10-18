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

The exact proof reduces the 31 rational line restrictions to 3 coordinate lines, 12 two-coordinate lines, and 16 three-coordinate lines, then evaluates one binary-quartic discriminant for the latter. The explicit discriminant matrix checks every normalized diagonal coefficient triple. The rational-point spectra follow by counting coordinate supports and quadratic characters.

`check_formula.py` independently implements the closed discriminant, normalized-case enumeration, and support-count calculations. `scan_lines.py` exhaustively constructs all rational projective lines and computes geometric smoothness by homogeneous Sylvester resultants rather than the closed discriminant. It directly checks the full section and surface point counts. Both require Python 3 and the standard library only.

Reproduced results appear in `formula_output.json` and `scan_output.json`. These computations cover the stated finite family exactly; they do not test general quartics or replace independent mathematical audit. The rational points of both model surfaces and every rational smooth member are counted with the full weighted-projective double-cover fibers, not as points of the branch quartic.
