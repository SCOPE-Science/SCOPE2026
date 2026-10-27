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

# Verification of the mixed-block centralizer-rank theorem

Use `python verify.py` with an ordinary Python 3 interpreter. The program separately constructs all full maps commuting with the prescribed idempotent (rather than using the normal-form proof), computes multiplication closures, and reports complete checks for \(b=1,2,3,4\). It also exhaustively tests the \(2628\) proposed three-element subsets with one unit for the degree-two mixed case.

Successful replay prints `VERIFY_OK_MIXED_REGULAR_CENTRALIZER_RANK`. The finite checks have no force as an infinite proof. The constructive argument in RESULT.md handles all \(b\ge1\). Historical uniqueness and independent audit have not been established.
