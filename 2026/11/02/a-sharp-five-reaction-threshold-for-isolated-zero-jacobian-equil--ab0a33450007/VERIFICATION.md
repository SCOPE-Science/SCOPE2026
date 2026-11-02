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

# Verification and limits

Run `python3 verify.py` with SymPy. The checker performs exact rational/symbolic calculations for every one of the fifteen missing-monomial pairs, the rank-three property of every four-support evaluation matrix, the factorizations, the original five-channel reaction expansion, its zero Jacobian and its unique equilibrium. All tests passed in the packaged implementation.

The algebraic proof in RESULT.md establishes the universal case beyond finite numerical samples. The checker enumerates all fifteen *structural support cases* rather than attempting to enumerate all choices of rate constants, product complexes or real coefficients. It does not supply independent external certification, verify all unrelated historical literature, or make claims about the stability of the sharpness witness.
