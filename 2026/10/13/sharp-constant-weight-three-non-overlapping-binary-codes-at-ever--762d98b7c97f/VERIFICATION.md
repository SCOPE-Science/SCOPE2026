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

The all-length claim follows from the direct four-part proof in `RESULT.md`. `verify.py` implements independent exhaustive prefix-suffix comparisons over all ordered pairs in the constructed code for each length from 4 through 40. It verifies each word has weight three, the claimed cardinality, and a distinct primitive rotation class. For lengths 4 through 25 it also enumerates all three-one words independently, extracts primitive rotation classes, and checks the code hits every class exactly once.

Run `python3 verify.py` with the Python 3 standard library. The final expected line is `VERIFY_OK`, with the checked size data preceding it. `TABLE.csv` contains that complete output in a machine-readable tabular form (without the final status line). The same checks were executed against the embedded source contents before acceptance.

This is a finite, reproducibility-oriented supplement. It neither certifies novelty nor asserts coverage of all lengths by enumeration. Full mathematical coverage is provided by the non-overlap case split, necklace bound and closed-form count.
