---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the fixed labelled alphabet and fixed-point-free involution, the t leftmost complete greedy arches of the half-word and the t rightmost mirrored arches leave exactly R followed by its complemented reversal. Every family of at least 2t+1 complete disjoint blocks can have its outside t blocks on each side replaced by those greedy arches, since the left endpoints of the remaining region can only move left and its right endpoints can only move right. A complete block in the centre exists exactly when the residual support meets every involution pair; two such disjoint blocks are impossible because each must cross the central cut. The greedy characterization follows, for example, by using the arch-terminal letters in order followed by a letter absent from the remainder to witness non-universality at the next length. The geometric series uses q! S(n−1,q−1) arches of length n, and for support size s uses s! S(n,s) words per support; the orbit-covering proper supports number binom(p,s−p)·2^(2p−s). This verifies the GF, including the empty word and the binary specialization. Every h-universal word has at least h occurrences of each symbol, so equality at physical length qh forces minimum-size permutation arches, and for odd h a final p-letter remainder with one letter per pair. Index at equality cannot exceed h.

## originality

PASS

Pass is for the full symmetry-constrained length/exact-index distribution and its equality-case multiplicities, not the general greedy arch theorem, palindrome doubling or Stirling identities. The inspected sources give close arch/remainder arguments but not the fixed-point-free folded-word count or a stronger counting theorem covering it. Conditional on the new orbit-covering refinement, the extremal formula is a consequence, not an unrelated second novelty claim.

## value

PASS

Fixed points of reverse-plus-relabel symmetry form a natural constrained word class. The formula gives the entire exact-index distribution uniformly, distinguishing even and odd exact indices by pair coverage, and supplies exact minimum-length witness counts. Those are useful counts for the constrained class, not just the general minimum-length bound or a small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
