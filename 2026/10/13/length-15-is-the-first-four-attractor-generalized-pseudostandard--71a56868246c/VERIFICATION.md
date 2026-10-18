---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Every iterated shortest R/E closure of a word after appending one bit strictly increases length. Therefore the directed closure graph truncated at length 15 is finite and its breadth-first traversal over all four (bit, antimorphism) choices, with word deduplication, is complete. For each reachable word, union-of-factor-occurrence position masks give an exact hitting-set characterization of minimum string attractor; direct per-occurrence checking is an independent second test. Independent regeneration recovered exactly 2,4,4,8,6,12,10,18,12,24,16,34,18,40,28 distinct words at lengths 1..15 and their complete attractor histograms; no gamma=4 below 15 and exactly the two complementary length-15 words have gamma=4. Their displayed (0,4,7,11) set hits every factor, while all 455 triples fail. Direct closures reconstruct both four-step directives.

## originality

PASS

The closest primary literature and published-result searches were compared for statement implication and actual mathematical object, not just titles. The 2024 conjecture upper bound gamma<=4 does not imply existence at length15 or absence at length<15. Thue–Morse size4 at length16 does not imply minimality over mixed directives, and the size5 length36 example concerns a different boundary. Search terms included pseudopalindromic prefixes, mixed palindrome/antipalindrome closure, generalized pseudostandard and exact complementary binary words. These describe the same class, unlike all unrestricted binary words. Residual risks are retained; inaccessible full text alone is not equated to scientific failure.

## value

PASS

Determines the exact first attainment of a natural, previously conjectured upper threshold in binary generalized pseudostandard prefixes and completely classifies the first equality layer. A sharp onset at length 15 rather than the known length-16 Thue–Morse family is mathematically motivated and independent of any unfinished higher-length census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
