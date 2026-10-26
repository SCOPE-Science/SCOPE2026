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

The proof is self-contained in `RESULT.md`. Run `python3 verify.py` to check both sides of the reflection identity, prime-power exceptional counts and mean, reciprocal Laurent-sector coefficients, and an explicit three-defect witness for each non-prime-power base in the verifier's finite range.

Additional direct checking before package assembly compared 12,760,901 reflected pairs over bases 2 through 22 and lengths at most 4 (skipping windows larger than 160000 integers), and checked non-prime-power witnesses for all such bases through 50. These finite checks cannot establish the stated universal quantifiers. No independent audit or external certification has been performed.
