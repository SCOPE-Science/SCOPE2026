---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS: Structural induction on intuitionistic formulas uses the root implication clause plus classical evaluation at each maximal leaf; formulas depend only on (a,S). Atoms distinguish root colors, while negated classical minterms beta_t at the root distinguish presence/absence of each leaf color, proving injectivity. Each allowed pair is realized by repeat colors to fill k leaves, giving the binomial census. Theta_{n,k}, a finite disjunction of negations of minterms outside k-element sets, holds at all points of F_k but fails at a root with k+1 distinct leaf colors; duplication handles l>k. Independent enumeration of all persistent valuations for 1<=n,k<=3 exactly matched nine formula-count cases: n=2 gives 9,17,21 and n=3 gives 27,76,144. Infinite assertion rests on proof, not bounded enumeration.

## originality

PASS

PASS (best knowledge): The Almeida paper addresses uniform implication-depth and general colored-model mechanisms rather than an identified exact all-k fork type census; Hyttinen et al. work on more general layered Esakia spaces is materially different. The fork-specific elementary classification may have been stated in nonindexed intermediate-logic literature, and the closest primary paper was read only in abstract this run, so historical priority is qualified.

## value

PASS

PASS: The complete type spectrum and exact minimal-variable frame-distinction threshold are natural finite-model and intermediate-logic invariants; the explicit Theta formula certifies each strict visibility boundary. This is more informative than merely observing a finite-color upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
