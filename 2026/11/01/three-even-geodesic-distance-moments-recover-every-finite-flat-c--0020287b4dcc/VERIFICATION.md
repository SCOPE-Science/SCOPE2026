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

# Reproduction and mathematical checks

Run `python verify.py` with Python, SymPy, and SciPy. The script verifies exact symbolic moment expansions, the sharp two-to-one fold, the exact nonvanishing separation of the sixth moments for twin parameters, the nonzero derivative at the fold, and two-dimensional independent quadrature for five positive cylinder parameter pairs. These numerical trials do not establish the theorem by themselves; the complete proof is in `RESULT.md`.

The metric is the shortest path constrained to the lateral cylinder. The uniform measure is two-dimensional surface measure, not volume measure of the filled Euclidean cylinder. A boundary zero-height or zero-circumference limit is excluded. Earlier equivalent formulas under alternate terminology have not been exhaustively ruled out, and independent mathematical audit has not occurred.
