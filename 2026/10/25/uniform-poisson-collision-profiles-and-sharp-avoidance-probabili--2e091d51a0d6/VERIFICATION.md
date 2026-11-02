---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Under Stam sample K with mass k^n/(e B_n k!), independent uniform K-box labels at vertices, equality constraints for forest edge subsets of size j have conditional probability K^-j because an acyclic edge subset has |V|−components=j. Thus conditional indicators are jointly independent Bernoulli(1/K) and X|K~Bin(e,1/K), including all forest shapes; cyclic graphs fail this factorization. Exact factorial moments (e)_j B_(n−j)/B_n and inclusion-exclusion follow by edge contraction. Consecutive k^n/k! weight ratios are monotonically decreasing; mode at t=n/W(n)+O(1), and moderate deviation |K−t|>n^(3/4)/W(n) is O(n exp(−c√n)), sufficiently small relative to min main probability exp(−W(n))=W(n)/n. Inside event K=t(1+O(n^-1/4)), uniform e<=n−1 yields |e/K−e W/n|=O(W n^-1/4), e/K²=O(W²/n); Le Cam and Poisson coupling give TV o(1), while e log(1−1/K)=−e W/n+o(1) gives relative avoidance. Independent exhaustive enumeration of set partitions n=3..6 and all path edge counts matched exact Bell-transform law, not used for limit proof.

## originality

PASS

Best-of-knowledge PASS for uniform moving-parameter total-variation bound and uniform relative rare-event avoidance law; conditional Stam Bernoulli factorization, finite Bell-transform counts, and asymptotic normal level statistics are known and credited. Inspected theorem statements do not yield a uniform relative estimate for probabilities ~W(n)/n.

## value

PASS

Forest edge constraints factor exactly after conditioning, yielding a natural sharp boundary from cycles. A uniform relative approximation for an event of probability as small as W(n)/n on spanning trees is mathematically stronger than the known central limit and total-variation statements, and directly supplies a quantitative first-order constraint probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
