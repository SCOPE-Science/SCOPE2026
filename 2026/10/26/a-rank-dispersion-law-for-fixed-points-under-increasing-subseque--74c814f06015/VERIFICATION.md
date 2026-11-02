---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Uniform permutation, n>=2, 2<=k<=n, nonconsecutive increasing position-subsequences. For a fixed point at i, a k-subset avoiding i retains probability 1/k!, while a subset with rank r at i contributes K_{i,r}^2/(n-1)_(k-1) after conditioning. Vandermonde gives q_{i,r}=K/B with sum_r q=1; subtract B/k! and multiply by P(pi(i)=i)=1/n to obtain the exact nonnegative sum of squares. Strict log-concavity excludes uniform q for k>=3; k=2 is zero only at the median position when n is odd. Summation gives the global covariance, and division by E Z=binom(n,k)/k! gives size-biased E F. Fixed-k beta-integral and central binomial convolution prove the displayed asymptotic. Independently enumerated all permutations n=2..7, 112 exact labeled (n,k,i) comparisons, with all zero cases; checked all seven source-tree entries and independently reconstructed the complete 7-blob tree SHA. The exhaustive check is not the proof for arbitrary n.

## originality

PASS

Qualified best-of-knowledge novelty is the exact local fixed-point / increasing-subsequence cross-moment, nonnegative hypergeometric rank-dispersion decomposition, unique local cancellation and explicit fixed-k asymptotics, not the size-biased measure or standard permutation first/second moments.

## value

PASS

The local covariance nonnegativity and exact exceptional median cancellation describe how a canonical size-bias changes another natural permutation statistic. The complete arbitrary-n identity and fixed-k leading constant are independent useful cross-dependence invariants; a researcher studying permutation change of measure can use the precise formula, not merely a generic second-moment bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
