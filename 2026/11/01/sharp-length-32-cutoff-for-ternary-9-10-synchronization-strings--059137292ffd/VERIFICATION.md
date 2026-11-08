---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Alphabet relabeling to canonical restricted-growth digits 0,1,2 is bijective on symbol-permutation classes and preserves all LCS. Weakly admissible words (20LCS<=9L for every pair) are prefix closed. Appending a letter adds only new right-endpoint pair tests, so the recurrence tests every canonical word exactly once. I independently implemented a fresh dynamic-programming LCS exhaustive recurrence: length counts through n=33 match repository certificate for all 33 levels, with precisely 10 survivors at n=32 and 0 at n=33. I independently tested every pair of the explicit witness 01020120212012101201020120212012; strict minimum margin 9L-20LCS is 1. Inspected the actual 30-extension certificate and two source LCS implementations (DP and bit-parallel). The finite exhaustive classification plus prefix inheritance, not sampling, proves all n>=33 impossible. For epsilon<=.9 the same obstruction rules out unbounded ternary strings; it does not determine epsilon>.9.

## originality

PASS

Xu–Fu–Qiao–Tao construct infinite ternary synchronization strings for epsilon>226/227 in their 2026 arXiv first version; this is an existence result at much weaker quality. Camungol–Rampersad 2013/2018 analyze only equal-length adjacent factors and their 0.888 ternary lower similarity coefficient does not imply an all-unequal-length 32/33 boundary. Resultary and broad search found no exact matching table. Potential older unindexed exhaustive search is a remaining priority risk.

## value

PASS

A sharp, nontrivial exhaustive finite cutoff for the natural three-letter synchronization LCS condition yields an all-length obstruction, directly informing the open minimal ternary synchronization parameter. This is not merely a small arbitrary slice because every longer word inherits the forbidden 33-letter prefix; exact reproducibility and certificate are substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
