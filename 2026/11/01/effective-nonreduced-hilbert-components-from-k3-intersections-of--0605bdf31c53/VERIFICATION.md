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

Run `python3 artifacts/verify_target.py` after extracting the two embedded paths into the same directory tree. The program verifies the integer intersection form, divisor identities for all tested \(m\), the numerical component and tangent dimensions, and the restriction basis on the projective line; it must print `VERIFY_OK`.

The all-\(m\) cohomological arguments are mathematical proofs from Kawamata--Viehweg vanishing, Kodaira vanishing, Serre duality and the exact sequence restricting quadrics to a line. The verification script checks their algebraic divisor input identities; it is not a computational substitute for any of these theorems. The obstruction comparison uses Nasu [1, Lemmas 2.11--2.12, 4.3, 4.6 and Proposition 4.7] under the newly verified effective hypotheses. Only self-review has been performed; independent audit has not.
