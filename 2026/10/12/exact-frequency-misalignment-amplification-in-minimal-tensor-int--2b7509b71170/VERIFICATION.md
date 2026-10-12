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

Execute `python3 verify.py` with a current standard-library Python interpreter. The program reconstructs the two-point real inverse-DFT representation, independently computes selected-sensor tubal inverses frequency by frequency, and checks the expected physical Frobenius energy against the stated sharp coefficients. The comparisons use rational arithmetic on rational unit-vector witnesses and additional 3,500 seeded rational pairs. The exact algebraic proof, including strict positivity, nonzero residual qualification and the anti-aligned limit, establishes the universal statement. No unverified generalization to higher-rank tensors or complex sketches is included.

Independent audit: not performed.
