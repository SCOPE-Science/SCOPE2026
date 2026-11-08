---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For each simplex the barycentric facet-threshold description of a translate yields exact overlap (1-sum(a_j)_+)^d and the constrained excluding-translate infimum max(0,1-t,min lambda_j). Factorization across products proves the all-point formula with theta=min(t,1). At each centroid, the controlling mass is max_i theta^(N-d_i)min(theta,d_i/(d_i+1))^d_i. For t beyond max T_d, b(d)=d log(d/(d+1)) has strictly positive second derivative 1/[d(d+1)^2], so its affine-tilted dimension envelope is controlled exclusively by smallest and largest factor dimensions. The unique crossing produces the stated three active branches and plateau; factorwise inequalities give the entire median set. Independently checked the triangular-prism values T_2=2/3, t_*=8/9 and the middle term 4t/9, plus exact rational overlap identities at representative boundaries. The proof applies to all positive factor dimensions and all ambient points; finite samples alone would not.

## originality

PASS

The general convex-body erosion identity and single-simplex depth formula do not by themselves state the coupled extreme-dimension envelope or exact median geometry of genuine products of unequal-dimensional simplices. The proof supplies nontrivial product minimax and convex-dimension reduction. Compared mathematical implications, not titles. Current result survives on best available primary abstract statements, direct original proof, existing result summaries and explicit residual priority risks; this is not a guaranteed novelty certificate.

## value

PASS

The exact phase law and median-set dimension transitions are a meaningful explicit benchmark for multivariate translate depth of nonsmooth products. In the simplest triangular prism the median shape changes segment -> point -> triangle at isolated scale 8/9; this is not a trivial reformulation of single-simplex centrality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
