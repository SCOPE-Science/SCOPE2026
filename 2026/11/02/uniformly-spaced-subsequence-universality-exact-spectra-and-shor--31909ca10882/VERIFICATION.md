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

Use `python3 verify.py` from a directory containing the extracted source file; it needs only the Python 3 standard library. The test constructs all binary, ternary, and four-symbol host strings in eight finite parameter ranges, uses a literal greedy-embedding oracle for all target patterns, and independently predicts coefficients using inclusion–exclusion for the alphabet-avoiding remainder and the minimal-all-letter arch counts.

Actual execution result: `VERIFY_OK independent_literal_hosts=127594 alphabets=2..4 spacing=1..4 exact_bivariate_coefficients=TRUE shortest_hosts=TRUE`. The printed per-family results are in the program output. The executable source is embedded alongside this document and was run directly from its packaged source path.

The verification checks finite coefficients only. The claimed all-parameter conclusion rests on the fully specified combinatorial bijection and generating-function proof in `RESULT.md`, not on any finite search. No independent audit has been performed.
