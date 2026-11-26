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

For S=2X−1 and T=2Y−1, condition on how many of a,b occupy i,j. With none the sign S is balanced by swapping the values at i,j without altering T; with both, ST=1 for two ordered placements. In the exactly-one case, e.g. π(i)=a, the free value at j and the free position of b range independently over n−2 options apiece: each pair of choices has (n−3)! completions. Their signed biases are (2a−n)/(n−2) and (2i−n)/(n−2). In the four cases the signed products sum to (h_a−h_b)(t_i−t_j), where h_b=(2b−n−2)/(n−2) and t_j=(2j−n−2)/(n−2); each case has mass (n−2)/[n(n−1)]. Dividing the resulting E[ST] by 4 gives the frozen formula with positive coefficients on the independent constant and shifted-gap vectors. The displacement identity follows by summing j−i over inverted pairs: the contribution at r is r times (# earlier larger minus # later smaller) = r(r−π(r)). Invariance of I and D under inversion gives two shared modes. Within each family the incidence Gram formula is positive definite: disjoint pairs have zero covariance and shared endpoints give the signed 1/12 from the six three-point orders, with diagonal 1/4. Orthogonal projection between the spans therefore has rank two, fixes both independent common modes, and maps their orthogonal complement to zero. This verifies the intersection, residual orthogonality and the two unit canonical correlations. For n=2 the lone comparisons agree pointwise and have variance 1/4.

## originality

PASS

The supported distinction is the full index-resolved mixed kernel and the exact common linear subspace/projection. Earlier within-family covariance, aggregate adjacent-descent distributions, and scalar Kendall–displacement correlations are materially related but do not supply them. Classical inversion invariance, within-family incidence covariance and weighted-inversion identities are not credited as new.

## value

PASS

The exact projection solves a natural joint-dependence question about the complete forward and inverse comparison families, not only an aggregate covariance. It identifies which two interpretable rank statistics account for all shared second-order information and shows that every other pair of residual linear modes is uncorrelated, while the indexed kernel also gives exact covariance for arbitrary weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
