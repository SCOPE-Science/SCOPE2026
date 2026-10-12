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

The finite exact calculation in `verify.py` constructs a 16-state cyclic transfer matrix over the integer polynomial ring. Newton's identities verify its full characteristic determinant, and a separate vertex-subset algorithm tests the intended open-neighborhood property for every subset at cycle lengths 3 through 8. It checks exact maximum degrees and coefficients through length 60, compares with the independently derived cyclic-gap binomial formula, and counts exact covers by maximum packings through length 8. No random choices or proprietary dependencies are used. Finite length checks alone are not a proof of the infinite result; that implication comes from the cyclic-group isomorphism, exact gap enumeration, symbolic determinant, trace identity and formal coefficient extraction proved in `RESULT.md`.
