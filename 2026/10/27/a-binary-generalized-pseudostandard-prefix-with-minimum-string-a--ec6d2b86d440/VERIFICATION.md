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

# Finite verification

Execute `python3 verify.py` with the Python 3 standard library. The verifier constructs the length-182 word from its eight closure steps and checks all intermediate lengths and pseudopalindromic invariants. It exhaustively checks all 12608 distinct nonempty factors against the six indicated positions. For the lower bound, it recomputes all occurrences and incidence types of twelve particular factors, confirms the twelve listed inclusion-maximal incidence masks, and explicitly tests each of the 792 five-mask combinations.

Expected successful output: `PSEUDOSTANDARD_ATTRACTOR_6_PASS length=182 distinct_factors=12608 obstructions=12 maximal_incidence=12 five_type_cases=792`.

The claim is only about this finite pseudopalindromic prefix. No assertion about a minimum possible witness length, all directives, infinite unboundedness, or independent validation has been checked.
