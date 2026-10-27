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

# Verification record

The proof is deductive and applies to all admissible integers. `verify.py` is a standard-library Python 3 script that enumerates actual subset-power-automaton transitions, compares the complete reachable image collection to the residue-class condition, verifies every rank coefficient, and separately counts successful contraction-macro orderings by exhaustive recursion. The checker was executed successfully and its recorded stdout is in `check_output.txt`. The 77 parameter pairs include boundary regimes beyond the theorem, which provide additional consistency tests. The largest exhaustively traversed automaton has 12 states; these finite checks alone are not an infinite proof.

The verified theorem is confined to noncoprime displacement and two explicitly defined letter transformations. No independent audit has been performed. Historical equivalence in inaccessible or unindexed literature cannot be excluded by computational verification.
