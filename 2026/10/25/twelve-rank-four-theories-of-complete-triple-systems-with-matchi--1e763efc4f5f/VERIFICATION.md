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

# Verification

The accompanying `verify.py` uses only the Python 3 standard library and runs the exact rank-four recursive one-point-extension invariant on all nineteen canonical matching-defect structures with singleton and doubleton part counts capped at four. It has a direct all-vertex implementation and a separate stabilizer-orbit-representative implementation. Both yield precisely the same partition, independently of object enumeration order.

The rank-zero atomic base enumerates every equality pair and every ternary edge triple on the selected tuple; all edge atoms with repeated entries are false. The one-point extension set is complete for quantifier-rank recursion by induction. The proof of the infinite cap is written in RESULT.md and must be used with the finite computation; testing large examples alone would not justify the claim.

The run output is reproduced in `verify.log` and ends in `VERIFY_OK`. It establishes class count 12, smallest sizes 3,4,4,5,5,6,6,7,7,8,8,9, and sharp uniform bound 9. No independent scientific audit has been performed.
