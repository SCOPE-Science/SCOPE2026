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

# Reproduction and limits

Run `python3 verify.py` with the standard Python 3 library. The program computes direct majority success using an independent discrete-convolution dynamic program. Delegated majority success is computed with a copied, weight-two proxy vote and the background distribution; it then compares their exact rational difference with the closed form derived in `RESULT.md`.

The program checks 4,800 seeded rational parameter settings, 2,916 fully enumerated profiles on a specified three-point grid, and both phase-reversal examples for electorate sizes three through seventeen. The algebraic proof, not finite sampling, establishes the formula for all positive integers and the sign-change bound for all odd population sizes. In particular, the computation does not establish uniqueness in the literature or generalization beyond the assumptions.
