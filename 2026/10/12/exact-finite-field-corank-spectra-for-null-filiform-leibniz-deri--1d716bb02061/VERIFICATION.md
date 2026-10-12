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

Execute `python3 verify.py` with Python 3 and no third-party dependencies. The script constructs finite fields from irreducible polynomial models; it tests complete rank distributions over six field sizes and 29 parameter instances, totaling 25,695 fully enumerated derivations. It also checks the individual characteristic-resonance test in 96,988 nonzero-leading cases. Expected final output includes `VERIFY_OK`.

The script's finite enumerations and representative checks of the Leibniz derivation identity are not proofs for arbitrary dimension or field size. The general argument in RESULT.md uses a full derivation parametrization, truncated-polynomial gauge reduction, the characteristic-p operator-power identity, and an exact independent-condition count. The source of the derivation normal form is credited; finite-characteristic validity is separately proved in RESULT.md.
