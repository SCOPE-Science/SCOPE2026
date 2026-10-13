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

The algebraic proof is contained in `RESULT.md`.

`artifacts/verify_armijo_scalar.py` checks the Armijo equivalence, geometric accepted-step band, contraction envelope, and minimax formula over representative and dense parameter grids. The grid is supporting evidence only; the quantified result follows from the analytic proof.
