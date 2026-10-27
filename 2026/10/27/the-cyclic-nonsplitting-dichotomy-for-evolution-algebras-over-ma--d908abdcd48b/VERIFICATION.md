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

Run `python3 verify.py` from the package directory. The checker models nonzero elements of the smallest nonprime field using exponents of a fixed primitive cube root of unity, explicitly solves the monomial-isomorphism constraints for every cycle shift, and independently checks the predicted class and group order for all coefficient vectors of dimensions one through seven. It additionally counts idempotents by enumerating all four-element coordinate assignments in dimensions one through five, and checks that the twisted automorphism group has an element of the predicted full order in dimensions two, four, six, eight, ten, twelve, eighteen, and twenty-four. The recorded replay result is `VERIFY_OK`.

The computation does not certify any unbounded assertion; the symbolic recurrence and explicit generators in the proof establish the statement for all positive dimensions. No external independent audit was performed.
