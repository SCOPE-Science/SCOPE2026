---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof in `RESULT.md` gives all Ky Fan inequalities on the completely positive negative-coefficient branch in dimension at least three. It uses an exact Schmidt block decomposition, a positive Gram identity, and matching upper- and lower-end spectral partial-sum bounds before extending to mixed states by convexity.

The unchanged ancillary verifier `verify.py` requires NumPy and can be run with `python3 verify.py`. Its finite Gram and pure-input spectrum checks include regimes outside the finding; the tests for physical parameters above one at local dimension at least three are relevant here. The proof, not the finite samples or floating-point checks, establishes the universal quantifiers. The theorem does not treat unequal channels or three or more uses.
