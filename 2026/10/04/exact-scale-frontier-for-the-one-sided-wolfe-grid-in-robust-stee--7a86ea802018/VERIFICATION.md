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

The proof uses the scalar specialization of the published auxiliary direction problem and Wolfe conditions. No numerical approximation is needed for the theorem.

`artifacts/verify_wolfe_grid.py` checks the exact interval conditions on a rational parameter lattice, confirms the if-and-only-if one-sided-grid frontier, and verifies the explicit counterexample.

The finite replay is supporting evidence only. The quantified result follows from the algebra in `RESULT.md`.
