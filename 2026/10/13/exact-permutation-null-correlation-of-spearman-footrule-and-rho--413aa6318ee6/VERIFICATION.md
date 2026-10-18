---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For arbitrary arrays A,B the random permutation linear statistics X_A=sum_i a_(i,Pi(i)) satisfy Cov(X_A,X_B)=(n-1)^-1 sum_ij a^circle_ij b^circle_ij by direct same-index/different-index sampling and double centering. Take A=(i-j)^2 and B=|i-j|, use row/column sums and cubic distance sums to obtain Cov(F,D)=n(n+1)(n^2+1)/30; analogous centered-square calculation gives Var(F)=(n+1)(2n^2+7)/45 and Var(D)=n^2(n-1)(n+1)^2/36. Applying the affine transformation R=1-6D/[n(n^2-1)] yields exact covariance/correlation and the nonzero limit. Independently enumerated EVERY n! permutation for n=2..7 and recomputed exact mixed moments with fractions. This bounded enumeration does not prove all n, which follows from the centering identity and polynomial sums.

## originality

PASS

Jiang arXiv:1110.0807 defines exactly the footrule p=1 and squared-displacement p=2 metrics and discusses computability of their correlations, but its inspected Sections 4-5 do not display this pair-specific finite polynomial or limiting -3/sqrt(10). Diaconis--Graham supplies foundational F marginal distribution/variance and other permutation-metric comparisons without the mixed F/R formula. Berry--Mielke is plausibly directly relevant but only abstract accessible; authorized institutional full-text retrieval returned vpn_disconnected; this is an explicit material originality risk, not evidence of coverage. Closest Resultary Spearman rho--Gini boundary concerns different measures.

## value

PASS

Footrule and rho are two canonical rank-disagreement summaries with no ties; the exact finite-sample null correlation quantifies how much duplicate information they encode, and its strong asymptotic anticorrelation persists rather than vanishing. The natural all-n mixed invariant is independently useful as a null calibration benchmark, even though double-centering is the standard proof method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
