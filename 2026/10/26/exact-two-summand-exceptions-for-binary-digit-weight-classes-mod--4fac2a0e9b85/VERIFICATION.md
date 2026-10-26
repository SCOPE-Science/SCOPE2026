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

Run `python3 certify_mod3_sums.py`. No external libraries or data files are required. The program separately constructs the 18-state nondeterministic binary-addition automaton, and the reference regular-language NFAs (43, 30, 11 states for the three residues). It performs exhaustive BFS of the product of their subset automata with the target digit-weight tracker and tests equivalence on all legal finite binary strings. The counts of all reachable comparison states are 108, 108, 107. The one-digit representation of zero is tested separately. Every mismatching state terminates the checker through an assertion.

Independently, it enumerates all integers from 0 through 10,000 and tests two-summand existence using literal pair enumeration against the predicted exception families. That finite range is a cross-check only, not the source of the infinite conclusion. The finite-state exhaustive calculation, together with the transition/acceptance proof in RESULT.md, supplies the infinite verification; its trust assumptions are correctness of Python integer/bit operations and the stated small automata implementation. No separate external mathematical audit has occurred.
