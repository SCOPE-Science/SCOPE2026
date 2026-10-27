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

# Reproduction and checks

Run `python3 verify_periodic_square_avoidance.py` using Python 3 without external libraries. The program builds exactly 30 admissible states and 42 transitions; obtains the full integer characteristic polynomial by both Newton trace identities and Faddeev--LeVerrier; checks the factorization; enumerates all ternary words for lengths 1 through 11 and necklace representatives for 1 through 9; verifies direct traces through 30; and validates four common-state closed walks at lengths 4, 6, 11, and 13.

Successful output begins `TERNARY_PERIODIC_SHORT_SQUARE_PASS`. These numerical checks supplement, but do not replace, the graph-bijection proof, exact determinant identity, and additive-semigroup proof for all admissible periods. No external or independent mathematical audit has been performed.
