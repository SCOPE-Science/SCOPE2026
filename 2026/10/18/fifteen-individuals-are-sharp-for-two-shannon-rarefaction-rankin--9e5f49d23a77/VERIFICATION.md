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

I reproduced the full finite classification with a different exact computation. For each census size and species abundance I enumerated all labelled subsets by binary masks, recording sample size m and intersection count j. For a profile let P(m) be the product of j^j over every subset of size m and every species with j>=2. The expected plug-in entropy is log(m)-log(P(m))/(m*binom(N,m)), so direct integer comparisons of the products give signs, and equality gives exactly zero. Choosing cuts among N-1 positions and accepting nondecreasing part lengths enumerates each unordered positive partition with at least two parts exactly once. Comparing unordered pairs within each part count and omitting zero signs before counting reversals gives no pair with two or more reversals for any N=2..14. At N=15 there are 175 profiles and 1708 eligible pairs, of which 1684 have no change, 23 have one and exactly one has two. The witness and its nine positive, four negative, and final positive signs match exactly. The frozen hypergeometric expression and its rational atanh-series remainder bound are also valid; the independent replay uses neither binomial weighting nor logarithm approximation for its comparisons.

## originality

PASS

The supported distinct claim is the first and unique two-reversal pair for equal-census, equal-richness expected sample plug-in Shannon entropy without replacement. The closest published comparators either use another statistic, use a different sampling index, or study an estimator without establishing this finite classification. No checked source established a duplicate or an implication to the bound result.

## value

PASS

Equal census and fixed richness control two confounders of a common diversity comparison. The exact smallest finite population and unique witness show when absolute sample depth alone can flip the expected Shannon ranking twice; that is a motivated sharp boundary, not an arbitrary size slice. The witness and full sign pattern are useful for testing ranking heuristics and implementations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
