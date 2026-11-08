---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Conditional on R=r the r positive one-run lengths form a uniform composition of a because the number of placements of b zeros is C(b+1,r), independent of the lengths. Counting singleton parts yields C(r,s)C(a−r−1,r−s−1)/C(a−1,r−1) for r<a and a point mass at r=a. The explicit adjacent row likelihood ratio (r+1)(d−u)(d−u−1)/[(u+1)u(d−1)] increases with s, and feasible supports shift right; this verifies all joint TP2 minors including zero entries. Marked-composition expectation r(r−1)/(a−1), factorial moments E[(R)_t]=(a)_t(b+1)_t/(a+b)_t for t<=3 and Vandermonde produce covariance 2ab²(a−1)(b+1)/[(a+b)²(a+b−1)(a+b−2)]. Independent enumeration checked exact joint counts for fixed-content words through small a,b, 3,738 exact minors and 35 exact covariance cases; formulas handle degenerate boundaries explicitly.

## originality

PASS

The fixed-composition distribution of R (known since classical runs tests), conditional composition counting and marked singleton-part counts are acknowledged. The strictly likelihood-ratio ordered two-statistic family and its all-content TP2 proof are not implied by the inspected scalar run-count formula.

## value

PASS

Run tests in fixed-composition strings naturally condition on total one-run count. The result provides full monotone dependence of singleton-run abundance, stronger than its mean trend and a precise positive covariance across all admissible compositions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
