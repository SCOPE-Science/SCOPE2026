---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

On the naturally labelled cycle, all cyclic connected sets are nonempty cyclic intervals. Classical consecutive-integer proof shows every s not a power of 2 is a sum of at least two positive consecutive integers; for s<=2n this representation terminates at b<=(s+1)/2<=n, hence is a standard arc. Powers 2^k<=n are singleton arcs, so every value below P(n)=2^(1+floor log2 n) is represented. For n not a power of two, P(n)<2n and a wrapping arc of sum P(n) must use vertex n followed by prefix 1..j: it exists exactly when P(n)-n=j(j+1)/2. If n is a power of two, wrapping arc (n-1,n,1) has sum P(n)=2n. Thus mu(n)=P(n) precisely off those exceptional families. Each open dyadic block has exactly one exceptional n per positive triangular t<2^(m-1); endpoints add one; this gives the exact M-2+sum_m floor((sqrt(2^(m+2)-7)-1)/2), asymptotic (2+sqrt2)2^(M/2)+O(M), and E(X)=O(sqrt X). The previously published incompleteness theorem supplies that mu exists n>=8. Independently enumerated every cyclic interval for each n=8..512, verified exact first-gap criterion and 69 exceptions in that range.

## originality

PASS

Marotti–Needleman establish eventual incompleteness for natural cyclic labels; Sylvester identifies numbers representable as nonwrapping consecutive positive sums. The present additional wrap-around criterion and its exact dyadic exceptional census are not a direct statement of either. The first-gap invariant and density-one next-power law are compared by their actual implication content.

## value

PASS

The smallest missing connected-subset sum is the canonical arithmetic obstruction to sum-completeness of consecutively labelled cycles. Locating it for density one of all cycle sizes and exactly classifying rare exceptional orders with square-root scale and leading constant is a meaningful natural invariant, not an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
