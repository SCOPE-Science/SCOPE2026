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

# Verification of the layered-order bounded-morphism census

The executable `artifacts/verify.py` separately implements finite source and target orders, reflexive order comparison, surjectivity, the homomorphism condition, and the backward lifting condition. Its `predicted` function implements the independent Stirling-number product. Exhaustive comparisons cover 181 source/target pairs with all source level sizes between 1 and 3, all target level sizes between 2 and 3, source totals at most 6, target totals at most 5, and up to three/four levels as selected by the script's exact loops. No errors were observed.

Illustrations confirmed include \((2,2)\to(2,2)\) giving 4 maps; \((3,2)\to(2,2)\) giving 12 maps; \((3,3)\to(2,3)\) giving 36 maps; and unequal-height zero cases. The separate singleton-target test \((2,1,1)\to(2,1)\) gives 2 onto bounded morphisms, validating the stated boundary phenomenon. See `artifacts/verification_output.txt` for the direct output. Execute `python3 artifacts/verify.py` using Python 3's standard library; no external dependencies.

The verifier enumerates finitely many small cases only. It does not constitute an infinite proof or a historical novelty certificate. The all-size argument is contained in the two lemmas in `RESULT.md`. No independent audit has been performed.
