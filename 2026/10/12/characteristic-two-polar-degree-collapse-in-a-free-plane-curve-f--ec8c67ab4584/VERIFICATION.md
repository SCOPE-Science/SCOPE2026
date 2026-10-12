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

The proof gives universal polynomial identities and a complete local base-scheme description for odd integers \(m\ge3\) over algebraically closed fields of characteristic two. Bézout computes the *total* generic field-extension degree, including inseparable multiplicity. No finite sample is invoked to prove the universal result.

The accompanying `verify.py` uses standard-library finite-field arithmetic. It directly enumerates the gradient base locus over splitting fields for \(m=3,5,7\) and checks the characteristic-two cancellation on every field point; for each case it confirms exactly \(m^2+3\) geometric base points. It also checks the local-length and characteristic-zero arithmetic formulas. Run `python verify.py`; expected final line: `VERIFY_OK: characteristic-two exact identities, polar base supports, and degree formulas`.

The checker does not independently certify the general irreducibility proof, infinite degree formula or bibliography. Independent audit: not performed.
