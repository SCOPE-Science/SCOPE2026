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

# Verification details

Run `python checker.py` (Python 3.10 or later, standard library only) from this directory. The checker enumerates every order-reversing weak negation with double-negation inflation on each finite chain of length 2 through 11. For each it reconstructs multiplication and the finite residuated implication; verifies commutativity, associativity, residuation, and negation; evaluates the original Nelson axiom for every ordered pair; compares the direct Nelson-axiom test against the strictness criterion; and counts both canonical recovery operators and the mismatch spectrum. The observed verdict was `ALL_CHECKS_OK`.

The count through 11 elements is exhaustive *only for that finite range*. The proof for arbitrary sizes is the structural bijection and the recurrence in `RESULT.md`. The geometric limit follows from Binet's formula. Literature priority is qualified by inaccessible historical full text; no independent audit has been performed.
