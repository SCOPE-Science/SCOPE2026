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

The complete analytical proof is in `RESULT.md`. The independent optimization diagnostic is `verify.py`, using NumPy and SciPy versions described in `requirements.txt`; run `python verify.py` to reproduce the 24 shape-scale checks. A convex-hull facet representation and linear programming determine the numerical optimum without imposing the claimed formula. The diagnostic is finite and uses numerical tolerances; it does not certify the universal theorem, replace the proof, or assess bibliographic uniqueness.
