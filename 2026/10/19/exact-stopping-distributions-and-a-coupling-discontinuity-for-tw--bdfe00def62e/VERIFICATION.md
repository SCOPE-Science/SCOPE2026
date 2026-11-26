---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run `python verify.py` under Python 3 with SymPy installed. The code checks 12,276 exact rational trajectories, four symbolic generating-function normalizations and mean identities, and 54 finite-law coefficient comparisons. It uses the signed-error iteration specified in `RESULT.md`: normalized singleton sketches, with zero quotients set to zero in the direction and line-search updates and idle draws counted. The zero-quotient rule on these updates is an explicit choice in this variant, not a rule attributed to the cited Algorithm 1. The mathematical proof, rather than the finite tests, establishes the result for admissible initial errors, all positive-definite two-by-two normal matrices, and all independent label probabilities in `(0,1)`.

These checks do not certify hardware precision or convergence to a prescribed tolerance.
