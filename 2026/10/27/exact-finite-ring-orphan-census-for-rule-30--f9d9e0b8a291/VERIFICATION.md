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

# Finite-ring Rule-30 exact verification

Run `python3 verify.py` with Python 3 using only its standard library. The verifier independently constructs the two four-by-four Boolean de Bruijn matrices and the complete reachable 41-element relation monoid. Its breadth-first relation indexing is deterministic. It asserts the number of accepted diagonal relations is 30, checks every monoid transition, obtains all integer output-orphan counts from integer path counts, and checks that each of the 41 consecutive sixth-order recurrence errors starting at index 1 vanishes.

By Cayley–Hamilton for the explicitly constructed 41-by-41 integer transition matrix, 41 initial error zeros imply every later zero. That argument, stated in RESULT.md, is the essential infinite-length step. The verifier also independently brute-force enumerates all binary configurations on rings of lengths 1 through 13 and verifies the cubic power-sum formula to length 70. Expected exact output:

`VERIFY_OK monoid_states=41 recurrence_initial_shifts=41 direct_rings=1..13 power_sum_cases=70 image_sizes_n8_n12_n16=223,3816,63199`

Only finite-ring one-step images are addressed. This code and proof have not undergone independent external audit. The original finite-width thesis title noted in the reference list could not be inspected in full, so historical priority beyond inspected works remains open.
