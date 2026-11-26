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

Under the i.i.d. atomless assumption the ranks form a uniform permutation. For i<j the prefixes and suffixes used by the flags are disjoint. For i=j the joint probability is the beta integral, and the truncated pivot is strictly stochastically smaller than uniform if i>1, giving strict negative covariance if also i<n. The endpoint flags A_1 and B_n are constants. For i>j, after conditioning on A_i, the pivot M has Beta(1,i) law, and the j-through-(i-1) maximum is M+(1-M)Z with independent Z~Beta(i-j,1). Its argmax is uniform in that block and the n-i subsequent draws are independent. Thus the conditional probability of B_j is at least 1/(n-j), strictly above 1/(n-j+1), even when i=n; expansion and beta moments give exactly the displayed factorial sum. For the shifted matrix, deleting row k and column j in a leading k-minor leaves a block triangular minor with factors D_(j-1) and the superdiagonal h_(t,t+1), j<=t<k. Their signs cancel the cofactor sign, so every term in the last-row recurrence is positive, including the 1x1 case. This proves sign-nonsingularity, not just nonsingularity of one numerical matrix.

## originality

PASS

The supported addition is the complete position-indexed law for opposite scans of the same permutation, with the forced invertibility of its nonconstant cross-covariance pattern. The nearest prior generating function marks the correct two counts but cannot separate positional entries or certify the sign pattern; the nearest indexed catalogue finding uses a different pair of permutation statistics. The Hessenberg argument is standard and is not itself credited as new.

## value

PASS

These are two classical and naturally paired record processes. Position indexing exposes a directional pattern of exact independence, negative shared-pivot dependence and positive separated-pivot overlap that joint counts suppress. The sign pattern rules out any nonzero linear contrast invisible to all reverse records and gives robustness without estimating determinant magnitudes. This is a useful finite-size dependence law, not just a single enumerated determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
