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

With one jumble and max target length four, J4(00110) contains precisely the 10 four-letter targets allowed by 3 zeros and 2 ones. Positive 0001 and 0011 membership and absent 0000 and 0111 force any globally equivalent source to have exactly three zeros and two ones, regardless of initial length. Exhausting ten anagrams yields the class {00110,01001,01010,01100,10010}; five other words have five distinct missing-target patterns and are singleton classes. All ten have the same shorter-layer profile; I independently recomputed J_t for all 10 sources and t=0..4 and obtained six classes, with no infinite inference from finite search.

## originality

PASS

CRITICAL PRIORITY QUALIFICATION: Fleischmann–Huch–Kim–Koß–Wiards, Jumbled Simon’s Equivalence and Embeddings (arXiv:2610.17910, October 13, 2026), Example 12 ALREADY exhibits a finite intermediate-size equivalence class [acbab]_(3,1), therefore the general 2025 open *existence* question was already answered before this November 2 finding. Consequently do NOT award this result priority for solving the broad existence question. However that example uses a ternary alphabet and different (k,ell), and neither its stated construction nor the original paper implies the exact five-element BINARY (4,1) class or the complete six-class partition of binary (3,2) Parikh words. On bounded reading, originality PASS only for that strictly narrower explicit binary classification, not the already-covered general existence theorem.

## value

PASS

Beyond the already answered general existence question, the binary alphabet restriction and complete partition of the natural smallest nontrivial 3:2 Parikh family provide a concrete exact word-combinatorics invariant: all ten words partition into a 5-class plus five singletons under the precisely specified relation. The binary witness demonstrates intermediate classes without a third letter, unlike the earlier ternary example, making the exact classification independently useful; no claim of minimal word length across all binary words is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
