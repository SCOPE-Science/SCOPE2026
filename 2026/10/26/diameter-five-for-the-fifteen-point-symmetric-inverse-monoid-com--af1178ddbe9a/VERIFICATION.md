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

# Reproducibility

Run `python3 verify.py` with Python 3. The certificate checks the four ordered pairs of exponents (3,3), (3,5), (5,3), (5,5). For each pair, transitivity is explicitly tested, and for all fifteen possible images of a basepoint the equivariant map equations for two permutations and inverses are propagated throughout the orbit. Only the identity permutation survives each row. The verifier independently checks all 196 pairs of nonidentity powers and all five edges of the exhibited path of six noncentral partial bijections. It ends with `VERIFY_OK_INVERSE_MONOID_15_DIAMETER_5` on success.

The calculation is complete for the finite certificate, not experimental evidence of a uniform result in arbitrary degree. The group-theoretic reduction of all powers to the four cases and the published five-step upper bound are given in `RESULT.md`.
