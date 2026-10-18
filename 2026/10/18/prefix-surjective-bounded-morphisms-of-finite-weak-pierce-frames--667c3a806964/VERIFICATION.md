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

# Verification and limits

Run `python verify_weakorder.py` to test the defining bounded-morphism equation by exhaustive function enumeration for selected source/target weak-order level sizes. It compares every applicable count with the formula and independently checks image-rank spectra and idempotence for small self-frames, ending with `VERIFY_OK`.

Run `python verify_algebra.py` to enumerate all upsets and test the equivalence between the bounded-morphism equation and preservation of Heyting implication by inverse-image maps for three small weak-order frames; each test ends with `ALGEBRA_OK`.

The exact infinite-parameter identities rely on the local upper-cone proof in RESULT.md. Finite exhaustive checks are supporting evidence only. No independent review or general-purpose formal proof certification has been performed.
