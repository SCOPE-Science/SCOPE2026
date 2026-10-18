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

# Reproducibility and limits

Run `python3 checker.py` with Python 3.10+; it uses only the standard library. It computes truncation vertices, every pairwise difference, support values against the fourteen candidate inequalities, and the signed-permutation extreme points at seven exact rational truncation parameters. It verifies the special six-segment generating formula and the opposite-vertex criterion for representative exact diagonal hexagons. The expected last line is `ALL CHECKS PASS`.

These are finite algebraic tests, not a computer-assisted exhaustive proof over a continuum. The all-parameter identity follows from the coordinate and facet proofs in `RESULT.md`; the zonotope-only-if direction follows from the explicit diagonal facet geometry; the minimum width and equality normals follow from exact centered inball inequalities. An independent audit has not been performed.
