---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Rebuilt all 2^9 words, filtered exactly 148 bifix-free vertices, tested 3080 mutually compatible graph edges, and independently enumerated all 1152 size-14 cliques by increasing-index bitset intersection (491170 search nodes). A separate target-15 clique search exhausted 255710 nodes and excluded any size-15 clique. Exhaustive Hamming comparisons gave histogram 1148 of d=1 and four of d=2. Complement and reversal close the four into one four-member orbit. These enumerations exhaust this finite nine-bit domain rather than extrapolating to larger lengths.

## originality

PASS

Chee et al give the size-14 maximum, while Stanovnik, Moškon and Mraz compute optimum-code solutions and the number 1152. Their full 2024 open-access paper does not state the additional Hamming-distance histogram or four-element complement/reversal orbit; the codebook data can make it computationally derivable but the exact noise-distance constraint was not implied by the displayed scalar optimum.

## value

PASS

The minimum Hamming separation of a maximally large self-synchronizing code is a direct measure of substitution robustness. Showing d<=2 throughout the cardinality-maximal layer (and only four d=2 designs) is a meaningful sharp design tradeoff; it does not claim single-error correction or an all-length theorem. This is a complete natural optimum-layer classification, not merely a repeat of its known size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
