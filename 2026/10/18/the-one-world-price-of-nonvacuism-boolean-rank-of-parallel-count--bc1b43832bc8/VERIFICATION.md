---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed the proof in RESULT.md §§1–4 against Huang–Wen Definitions 3.1–3.5 and 4.1. Identity forces every selected witness for each contradictory antecedent into the anti-logical domain. Its rectangle consists of the rows selecting it and columns it falsifies, so rectangles cover exactly the ones of B=1−T. In SCP1 a zero row needs a selected world with empty falsification set; that world's rectangle can be deleted without affecting rank, and one such world serves every zero row. To realize the bounds, use the factors for the prescribed selections, set all q_j true at the lone normal world, and make every whole formula at each anti-world true except the designated false q_j. Define all other selections by formula complexity: a normal truth selects the normal world, a normal falsity selects nothing in SCP or a fixed anti-world in SCP1. Evaluation of a conditional consults only the previously assigned selection of its strictly smaller antecedent. All normal falsities are true at the fixed anti-world, and the singleton accessibility relations ensure the diamond restrictions apply exactly to normal truths. No fixed anti-world is needed for SCP at rank zero; SCP1 has at least one even for B=0. An embedded identity attains the SCP maximum; a zero row plus min(r−1,s) distinct unit rows attains the SCP1 maximum, including r=1. The supplied check.py is finite corroboration by inspection, not a replay or a proof of the global semantic extension.

## originality

PASS

The Boolean factorization/cover invariant and the nonempty-selection axiom themselves are old. The supported distinction is the exact global semantic realization and minimum budget for arbitrary simultaneous truth tables in both systems. Neither the inspected semantics nor the relevant Boolean-rank or analogous witness-budget result states or supplies that full construction and optimum. This is a bounded comparison, not a priority guarantee.

## value

PASS

The one-normal-world restriction isolates the cost of the anti-logical region. The exact resource calibration both constructs minimum models for arbitrary prescribed counterpossible behavior and shows precisely when replacing vacuous selections by globally nonempty ones incurs a cost. This is a model-size result rather than a new matrix invariant, and need not extend to models requiring extensional antecedents or constrained anti-logical truth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
