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

The companion `verifier.py` is self-contained Python 3 code requiring no third-party packages. Invoke it with `python3 verifier.py` from the directory containing this package.

The checker uses exact rational arithmetic and a common-denominator Laurent polynomial representation. It verifies the initial conditional laws, normalization and negative-tail positivity for shifts from 1 through 8191, the polynomial identity for the stabilizing increment, the sharp density table for run lengths 1 through 12 and shifts by 0 through 4 binary places (60 exact identities), and 24 direct finite dyadic enumerations within an explicit boundary tolerance. Its printed `VERIFICATION_PASS` indicates these calculations completed.

The claim for arbitrary run length is established by the algebraic recurrence and nonnegative-power support in `RESULT.md`, not by checking all parameters. The finite-count comparisons are diagnostics, not infinite proofs. No independent audit was performed. Publication priority remains provisional.
