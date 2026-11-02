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

# Verification evidence and bounds

Run `python checker.py` with ordinary Python 3 from the extracted package. Its successful terminal marker is `ALL_CHECKS_OK`. It checks complete enumeration through four vertices using a separate domain/range-bijection search and a canonical path/necklace decomposition; integer generating-function coefficients through size 100; the exact coefficient-marking identity for one specified singleton component; and joint marked-component polynomial relations for distinct sizes 1 and 2. The uniform-unlabelled enumeration is independently cross-checked against exhaustive labelled constructions reduced by isomorphism.

The full theorem's analytic saddle-point expansions, Hanf locality, and unbounded quantifiers have **not** been exhaustively verified by finite code. The proof in RESULT.md identifies the noncomputational premises and arguments. An inaccessible older paper may have stronger prior coverage, so no historical priority certification is claimed. Independent audit: not performed.
