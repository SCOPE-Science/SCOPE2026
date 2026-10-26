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

Run `python VERIFY_picard2_bitangent.py` under Python 3 with SymPy. The exact arithmetic verifier prints `VERIFY_OK: both dual charts, exact square-contact equations, elimination, seven-step local algebra` when all assertions succeed. It independently reconstructs the quartic restriction and its odd coefficients and checks the complementary charts. Its finite computations verify the nonstandard polynomial identities. The argument that the quotient is finite flat and the classification of the geometric fibres rests on the monic-polynomial and separable-cubic proofs in RESULT.md, rather than on sampled parameter values.

The scope is the square-contact closed scheme attached to the indicated smooth characteristic-two Picard quartic family; no statement is made about the moduli space of theta characteristics, mixed-characteristic limits, or independent scientific verification.
