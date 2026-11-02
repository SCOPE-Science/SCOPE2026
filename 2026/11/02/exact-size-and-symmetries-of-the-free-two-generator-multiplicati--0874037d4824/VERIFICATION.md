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

The supplied `verify.py` is a self-contained Python 3 program without third-party packages or network dependencies. Running `python3 verify.py` reconstructs the six-element free band, the 4095-element nonzero polynomial semiring, the least congruence imposing multiplicative idempotence, its 94 quotient elements and its two ordered generating pairs.

The code checks the six-word band multiplication for associativity and idempotence, the saturation invariant for all 4095 representatives and each of ten generating congruence contexts, every semiring axiom on all triples of the 94 quotient elements, and generation by all 8836 ordered pairs.

Observed output included `BAND_SIZE=6 FORMAL_POLYNOMIALS=4095`, `CONGRUENCE_MERGES= 4001 CONGRUENCE_CLASSES= 94 PROCESSED_PAIRS= 44105`, `GENERATING_ORDERED_PAIRS= 2 AUTOMORPHISM_GROUP_ORDER=2`, and `VERIFY_OK`.

The finite algorithm proves the exact free-algebra result only because the proof establishes that the finite polynomial semiring surjects universally and that the saturated relation is precisely the defining congruence. The program alone would not prove the result without those reductions. Full independent mathematical audit and exhaustive older-monograph priority comparison have not been performed.
