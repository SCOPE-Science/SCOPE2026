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

# Verification notes

The companion `verify.py` implements the local Rule-54 output function and the four-by-four Boolean predecessor matrices from the truth table, independently constructs the forbidden-pattern suffix automaton, and checks all returning length-at-least-two cycles by exhaustive closure in the finite relation product state. It reports visited-state counts (in the canonical 13-state order) of `144, 131, 132, 119, 103, 112, 84, 67, 67, 65, 119, 112, 67`. No fixed path-length cutoff enters the mathematical certificate; equal triples are merged only when their exact automaton state, Boolean product and capped length match.

The verifier calculates 13 exact transfer traces, uses Newton identities to recover all 13 coefficients of the characteristic determinant, and confirms `1, -2, 1, -1, -1, 1, -1` followed by seven zeros. It independently enumerates the Rule-54 image and cyclic forbidden avoidance for all ring sizes 1 through 16 and confirms the unique length-one exception. Expected final line: `VERIFY_OK`.

The direct enumeration is finite corroboration; the all-length conclusions are supplied by the finite relation closure and exact matrix identity. No independent audit or external theorem prover is claimed.
