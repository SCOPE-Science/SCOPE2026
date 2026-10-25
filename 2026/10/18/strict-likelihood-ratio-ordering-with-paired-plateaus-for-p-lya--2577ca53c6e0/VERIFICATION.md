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

Conditional on K=k ones in an exchangeable n-letter binary word, each arrangement has equal probability. Positive run-block compositions yield N(2s)=2 binom(k-1,s-1)binom(n-k-1,s-1), N(2s+1)=(n-2s)/s times the same product; hence the universal even-to-odd ratio (n-2s)/(2s) after mixing any exchangeable law. Folding B=min(K,n-K) gives a TP2 kernel in B versus total runs R, with nested supports, from monotonic neighboring-count ratios. The symmetric beta-binomial folded masses wα(B) are strictly TP2 across α since (α+b)/(α+n-b-1) rises with α for b<h. The two-by-two mixed determinant factors into sums of nonnegative products, and boundary-support witnesses force strictness at precisely r odd, whereas the universal run-pair identity forces equality at r even. Every r≤n has positive Pólya mass for n≥2 and α>0; n=1 is excluded. Independently enumerated every binary word at n=2..9 with exact rational α=1/2 and 3/2 and verified every strict/equal adjacent determinant, separately from source checker. Infinite-parameter theorem follows from TP2 algebra, not finite α sampling.

## originality

PASS

Exact Pólya urn run-count laws and joint multicolor run-statistic distributions are prior, including Eryilmaz Theorem 1. However, a distribution identity indexed by α does not automatically certify all-concentration likelihood-ratio sign monotonicity or exact alternating adjacent equality. The present theorem proves an additional uniform parameter-order property by a TP2 decomposition and identifies universal plateaus for exchangeable binary words. Strong historical risk remains that traditional run-distribution literature implicitly simplifies to this ordering.

## value

PASS

Likelihood-ratio order is substantially stronger than a monotone expected number of runs and is informative for reinforced-sequence inference and run-based testing. The sharp pattern of equality plateaus versus strict transitions explains exactly which thresholds discriminate changes in concentration. The universal exchangeable identity is a natural combinatorial structural lemma, not a renamed binomial identity only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
