---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

A finite word is rich iff each prefix has a unique-occurrence palindromic suffix; for any new extension this is precisely its longest palindromic suffix and all earlier suffix occurrences can be searched exactly. Since the preceding prefix is abelian-cube-free, every newly introduced forbidden cube must end at the new final character, detectable by comparing the three consecutive Parikh vectors for each length. Restricted-growth normalization provides exactly one sequence per S3 alphabet orbit, including 1-/2-symbol words. Independent newly written compiled C++ code implemented this exhaustive recurrence (separately from packaged verify.c) and gave exactly four canonical 180-words with their complete strings matching RESULT.md, zero canonical 181-words. Each uses three symbols => 24 actual words; direct reversal re-canonicalization pairs 1↔3 and 2↔4. No infinite-family inference.

## originality

PASS

Andrade–Mol published the same natural extremal length 180 and avoidance definition; inspected complete main paper does not state four canonical equality cases or the two reversal-orbit classes. The cited undergraduate thesis was inaccessible and may contain enumeration details; best-of-knowledge positive with significant priority uncertainty.

## value

PASS

Precisely classifying all extremizers of a sharp, independently motivated rich-word power-avoidance problem is a complete finite structural answer; distinguishes the 180 extremal witnesses and their reversal behavior beyond the formerly published maximum length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
