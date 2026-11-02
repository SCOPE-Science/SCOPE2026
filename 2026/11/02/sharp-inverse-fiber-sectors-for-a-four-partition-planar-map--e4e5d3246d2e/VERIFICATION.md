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

# Mathematical verification

The analytical proof uses four nonsingular quadrant cones, the exact ordering of their image rays, direct elimination for the invertible case, and geometry of angular sectors. Run `python3 verify.py` in this extracted directory. The checker uses exact rational arithmetic, recomputes direct quadrant inverses, and tests the regular and boundary formulas on stated finite grids. Exact finite computations detect algebraic errors but are not proofs for all real parameters. Singular parameter lines, forward stability and independent certification are not covered.
