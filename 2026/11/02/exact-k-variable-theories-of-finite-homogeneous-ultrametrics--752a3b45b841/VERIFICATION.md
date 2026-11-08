---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Fixed h>=1 and named distance levels R_i on leaves of uniform rooted prefix tree with b_i>=2. For differing truncated branch values min(b_i,k), the existential sentence requiring t=b_i+1<=k leaves pairwise at R_i distinguishes precisely a smaller branching level; t points at common level-i parent must occupy distinct i children. If all min(b_i,k) agree, each partial distance-preserving correspondence of fewer than k pebbled leaves extends after any Spoiler move: occupied child prefixes map identically and a new unused child exists on both sides whenever needed because occupied child count<k, with exact agreement if b_i<k. This gives Duplicator every finite k-pebble game, hence unrestricted rank FO^k equivalence. There are (k-1)^h truncation vectors; sharp maximum smallest representative k^h, minimal separating variable width min_i:bi!=ci (min(bi,ci)+1). Counting C² annulus sizes N_i=(b_i-1) product_{j>i} b_j, recovered bottom-up. Independent enumeration tested the full two-way extension signature property for 12,784 compatible partial isometries across four (b,c,k) pairs with differing underlying tree sizes; all passed.

## originality

PASS

Qualified best-of-knowledge originality: compare exact statement and model rather than terminology. Known foundational tools, marginal/special cases and directly overlapping results are credited. No actually inspected stronger result is shown to imply the complete final claim. Unavailable or only partially inspected plausible primary work is identified in residual risks; failed searches are not treated as proof of novelty.

## value

PASS

This is an all-height, all-variable-width classification of the expressive power of ordinary bounded-variable logic on a natural homogeneous hierarchical metric family. Sharp k^h representatives, number of complete FO^k theories and the C² contrast show a structural logical threshold that can guide finite model classification. It is not merely a numerical parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
