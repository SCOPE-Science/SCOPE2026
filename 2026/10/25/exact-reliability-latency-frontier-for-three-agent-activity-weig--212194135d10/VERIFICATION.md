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

# Verification

Run `python3 verify.py` with a standard Python interpreter. It imports only standard-library modules and prints `PASS 988640 exact-rational assertions`. The script enumerates initial rational opinions, confidence bounds, edge words, node weights and waiting-time identities using exact rational arithmetic; no floating approximations are used in the assertions. It verifies the stated configuration \((0,2/5,1)\), the strict tolerance \(1/10\), and the three-switch requirement. The infinite-parameter correctness proof is in RESULT.md; finite enumeration does not establish completeness for continuous opinions, probabilities or confidence radii. Independently check the algebraic Cauchy–Schwarz equality condition for the sharp positive-weight optimum; the checker is not an independent scientific audit.
