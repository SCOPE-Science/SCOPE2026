---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For each received word y, form its exact set of source subsequences (insertions) or supersequences (deletions). A code C is list-two admissible exactly when the intersection with every received-word incidence set has size at most 2, equivalent to avoiding all three-codeword forbidden triples. The supplied source has a complete constant-popcount enumeration at the optimum k and next k+1 over every binary codebook at n=2..5; the second source implementation independently computes three-word common shortest supersequence / longest common subsequence rather than incidence masks. Crucially, downward closure turns absence at k+1 into impossibility of all larger codes. I independently implemented a third C++ forbidden-hypergraph enumerator and checked each of eight optima/next-level counts exactly, obtaining the stated labeled-optimum vectors. A separate independent group-action calculation of the 185 insertion optima yields 41 orbits size four, ten size two, and one singleton. For n=5 all 32 codewords, 128 insertion outputs, and 8 deletion outputs are covered; there is no infinite-length inference.

## originality

PASS

Compared equivalent mathematical formulations, stronger coverage, exact-data overlap, and logical prior implication using primary material and actual Resultary searches. No materially inspected theorem was found to imply the complete final claim; this is a best-of-knowledge, not an exhaustive novelty certificate. All unread relevant material and other risks are recorded.

## value

PASS

This is the first natural finite separation of equal-error-budget insertion and deletion list-two code capacities, together with a complete extremizer census rather than a lone witness. Exact small-blocklength examples are relevant test cases for emerging list-decoding conversion/capacity results; the 52 orbit types expose structure not captured by asymptotic rates. Its finite nature is deliberate and not a weakness by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
