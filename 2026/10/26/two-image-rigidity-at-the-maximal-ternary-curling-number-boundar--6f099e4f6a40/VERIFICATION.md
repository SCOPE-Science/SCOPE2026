---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every overlap-free source prefix is cubefree, hence its curling digit is 2 precisely for a square suffix and 1 otherwise. Prefix heredity makes the terminal-overlap recursion exhaustive. Independently compiled and ran a standalone C++17 implementation of the complete first-symbol-normalized ternary search: exactly 1680 valid length-83 prefixes, 2016 length-84, zero length-85; at 84 exactly two transform images with normalized fibers 1344 and 672. Grouping normalized length-84 words yields 672 distinct parents, each with three terminal extensions. Multiplication by three first-letter choices gives 5040 length-83 words, 6048 length-84, fibers 4032/2016; the 2016 terminal words use all three source letters, so the S3 orbit counts are 1008 total, 672/336 by fiber. Direct finite recursion, not simulation, proves the full finite statement. The source normal-form T and final equal-last-pair digit test are consistent with the terminal recurrence.

## originality

PASS

Best-of-knowledge PASS with material limitation: maximum length 84 and total 6048 were explicitly published by Caveney–Dong–Shallit (2026) and are NOT novel. The purported contribution is the two-image complete fiber split and length-83 all-or-none extension rigidity, not stated in accessible abstract; source-package description cites Theorem 7 for total count. Attempts to retrieve full preprint via arXiv HTML/PDF were blocked, so an appendix could already include these exact finer counts. No contrary evidence uncovered; high priority risk retained.

## value

PASS

The exact two-image collapse and all-or-none one-step branching describe meaningful internal structure at a previously known extremal finite boundary: a natural complete fiber classification, not mere repetition of the known 6048 total.

The dated certificate retains the supplied scientific assessment, sources and limitations.
