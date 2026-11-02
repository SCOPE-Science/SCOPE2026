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

# Verification scope

The standalone `verify.py` uses two routes: direct distinct-factor enumeration and exhaustive palindrome-split testing, compared with the closed-form four-run and three-run counts. It also enumerates positive run-length compositions for fixed total length and checks exact extremal values and explicit witnesses.

The checker returned `VERIFY_OK` with `definition_comparisons 2500` and `parameter_comparisons 1215415`. It checked lengths 4–16 by the definitions for four runs, lengths 3–17 for three runs, all four-run parameter compositions at lengths 8–75, and witnesses through length 299.

The finite checks do not establish the result for arbitrary length. The inequalities in `RESULT.md` constitute the mathematical proof for all lengths in scope. Bibliographic coverage and historical priority are not independently certified.
