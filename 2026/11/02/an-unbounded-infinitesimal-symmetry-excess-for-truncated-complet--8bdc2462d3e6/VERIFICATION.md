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

# Finite checks and their limits

Run `python3 verify.py` in the directory containing this package. The verification program independently enumerates all candidate images of the two generators over the indicated small finite fields, checks the multiplication identities of the quotient algebra and the invertible first-order linear part, and tests the dimension count of derivations.

Observed complete results: over F2, n=3: 64 automorphisms; over F2, n=4: 2048 automorphisms; over F4, n=3: 36864 automorphisms. Binary derivation counts are n=3: 1024 and n=4: 65536. The program emits `ASYMMETRIC_TRUNCATION_OK`.

Finite enumerations do not prove the theorem for every n or every field. The global arguments are the characteristic-two squaring rule, binomial expansion modulo x squared and y to the nth power, Nakayama for a finite local algebra, and tangent-space identification with derivations. No independent audit has been performed.
