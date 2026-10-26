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

# Verification and reproducibility

A proof is included in `RESULT.md` and an independent finite diagnostic in `verify.py`, using only Python standard-library exact rational arithmetic. The diagnostic enumerates all matchings of up to ten labeled half-edges for all weak degree compositions into two, three, or four groups, then checks the regular specialization and the four-half-edge exception. The executable returns `PASS: 2223 exact moment/formula/sign assertions` on the supplied package.

The general theorem does not depend on numerical evaluation. Its key identity is the probability that any three specified disjoint matching pairs occur, \(1/((q-1)(q-3)(q-5))\); multiplying by compatible loop and parallel-edge witnesses determines the exact mixed moment. Degenerate four-half-edge regular configurations are handled separately. Exhaustive tests are finite and do not certify unbounded quantifiers or historical novelty. Independent audit has not been performed.
