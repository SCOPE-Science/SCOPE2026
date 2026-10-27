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

The proof is self-contained in `RESULT.md`. Its nonstandard critical point is that every factor of at least five symbols has a unique source-block phase; this follows by checking all four possible adjacent image-block pairs and the distinctness of each nonempty image prefix and suffix.

Run `python3 checker.py` in a directory containing the two delivered files `checker.py` and `checker_output.txt`. The checker recomputes all eight forbidden crossing windows, the suffix-array-derived minimal-unique intervals for iterates two through nine, and full independent factor-multiset checks for iterates two through five. Its output matches the delivered `checker_output.txt` exactly.

Only the finite checks are computational. They do not claim to verify all iterates. The general theorem follows from induction and the endpoint-minimality argument in `RESULT.md`. Independent scientific audit has not been performed.
