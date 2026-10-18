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

# Verification of the short-arm spider theorem

Execute `python verify.py` with Python 3.9 or newer. `verification_output.txt` records the actual successful execution from the included program. The verifier builds every graph independently from the arm lengths, using vertex zero as hub, and checks the defining private-neighbor condition by adjacency bitmasks.

For all 24 profiles with at least three arms and graph order at most 17 in the checked parameter box, the verifier evaluates 761,216 vertex subsets, computes the actual minimum cardinality and the *entire family* of minimizing masks, and compares this family to the theorem's constructive classification. It also verifies all 66,549 configurations generated across 78 additional profiles, including trees with many short arms and up to nine long arms.

The proof is not a computer-assisted induction. Infinite-range correctness follows from the two local arm-state lemmas and the sharp cardinality bounds in RESULT.md. Exhaustive small instances and larger constructive instances detect implementation and boundary errors, but alone cannot establish the theorem for all parameters. Independent scientific audit is not yet performed.
