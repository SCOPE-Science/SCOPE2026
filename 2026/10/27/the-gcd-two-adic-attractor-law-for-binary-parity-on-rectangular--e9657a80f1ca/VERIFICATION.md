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

The update was coded directly using the four modular-neighbour indices, not by manipulating the Laurent factorization. The verifier generated binary matrix powers, checked predicted stable rank at the asserted sharp time and at the next update, confirmed nonstability one update before the asserted time, and independently checked the maximum-depth rank decrement for nontrivial gcd cases. It covered all 144 ordered pairs of torus circumferences between 3 and 14 inclusive. It additionally mapped every state for the 3-by-3, 3-by-4, 4-by-3 and 4-by-4 tori through the stated maximum time and independently counted the distinct recurrent images (74,240 starting configurations). A separate exhaustive depth census for all 512 states of the 3-by-3 torus gave 16 initially recurrent and 496 transient states; on the 3-by-6 torus it gave the populations 256, 16,128, 245,760 at depths 0, 1, 2 respectively, matching the exact 15/16 peak fraction.

Use `python3 VERIFIER.py` in the directory containing the two embedded files. Successful output ends in `VERIFY_OK`; the accompanying `verification.log` gives the specific completed-run output. These finite tests corroborate the proof and are not an infinite certificate. The proof of the all-size claim is the local-algebra argument in `RESULT.md`. No outside audit or certification has been performed.
