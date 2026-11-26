---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A two-letter projection preserving one unequal position commutes with rotation, and its separating DFA lifts to the full alphabet. Binary witnesses also give lower bounds on a larger alphabet, since other letters are never read. The inverse shift yields the same unordered pairs. For a one-symbol shift, either a last-bit recorder works or a reset and swap record the parity of trailing equal bits, whose lengths differ by one. For a two-symbol constant prefix, a reset and a 3-cycle distinguish trailing run lengths differing by two. For a mixed prefix, independent saturation from the two written triples reproduced all 12 transformations, their transitions and commuting indices 0, 4 and 10. The closed product with the recognizer for (01)* certifies the full word language, not just a finite length cutoff. Noncommuting actions differ on a selectable initial state and thus admit a distinguishing accepting set. For sharpness at n≥4, the pair 0^(n−2)10 and 0^(n−4)1000 has the same Parikh vector and ends in 0. A constant on 0 makes their actions identical; two permutation actions commute; and with a constant on 1 the trailing counts 1 and 3 act identically under any two-point permutation. This exhausts all two-state transitions. The frozen verifier and recorded output were inspected, not executed. Independent construction checks covered 8,166 one-step and 8,154 two-step distinct binary rotations for lengths 2–12, and checked all 16 two-state transition-map pairs on the lower family for 4≤n≤24. The exact theorems are about maxima, not equality of every individual separation number.

## originality

PASS

Earlier inspected conjugate-separation results bound these shifts by three and five states and give a four-letter lower witness, but do not settle the exact sharp all-length profile. The material later binary census is acknowledged as equivalent coverage of shift two through alphabet projection, not discounted as just another parametrization. No evidence was found that this coverage predates the frozen result; no claim of discovery priority is made.

## value

PASS

Nearest shifts are natural cases of the extremal conjugate-separation problem, whose prior bounds are not sharp there. The all-length three-state upper construction with a finite transition closure, paired with an all-length obstruction to two states, improves the upper bound of five and resolves the exact worst-case constant. The finite graph is useful because it certifies arbitrarily long inputs, not because of the number of small cases counted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
