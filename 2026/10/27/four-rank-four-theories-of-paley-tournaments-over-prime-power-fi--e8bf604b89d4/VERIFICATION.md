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

Run `python3 verify_paley_tournaments.py` and compare with `verification_output.txt`. The source file is entirely standalone and uses only Python 3 standard-library functionality.

The script reconstructs Paley tournaments over prime fields of orders \(3,7,11,19,23,31,43\) and over the proper prime-power field \(\mathbf F_{27}\). It verifies their tournament axioms, checks two-extension at orders 3, 7 and 11, checks all triple-extension patterns for each, and independently checks each pattern through neighborhood bitsets at orders at most 27. The exhaustive checks examine \(969\) triples at order 19 and \(1771\) at order 23. An exact nested atomic-type recurrence computes complete rank-four theories for eight tested orders, confirming four classes. The code also tests the rank-three stabilization criterion, the transitive-configuration and common-dominator formulas, four-vertex tournament isomorphism types, the existential-fragment contrast, and the initial numerical character inequality.

The analytic character-sum bound \(|\sum\chi((z-a)(z-b)(z-c))|\le2\sqrt q\) is an invoked standard theorem, not independently certified by a finite computation. The proof's reduction from three-extension to the four-move game is mathematical and all-field, not an inference from the tested values. No separate expert or external audit was performed.
