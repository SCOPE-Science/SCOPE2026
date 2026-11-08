---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Uniform positive color-run compositions yield E[X]=(a/p)1, Cov(X)=a(a-p)(pI-J)/(p^2(p+1)), analogously for b and q. Writing inversion U=X^T M Y gives a bilinear variance depending on incidence statistics t,h,j. Even 2r run start orientations mix means ab(r±1)/(2r), adding between-orientation variance, while odd 2r+1 run orientations have equal means and probabilities (a-r)/(a+b-2r),(b-r)/(a+b-2r). Formula (1) and exact positive-numerator difference identities (2)–(5) establish both within-parity decreases and strict odd troughs, with feasibility boundaries a,b>=1. Reversal gives E[U|R]=ab/2. Independent exact Fraction enumeration checked 400 conditional strata for a,b<=8; infinite proof is the displayed symbolic identities and positive-coefficient polynomials.

## originality

PASS

Classical unconditional Wilcoxon variance and fixed-weight run-count distributions are established. The fully conditioned, exact all-composition variance sawtooth and strict ordering identities were not found directly in the relevant inspected primary sources; originality is qualified by possible implicit derivatives of historical joint distributions.

## value

PASS

Wilcoxon inversion rank statistic and Wald–Wolfowitz run count are natural joint statistics under a fixed-composition permutation null. Conditional variance has strict nonmonotone sawtooth despite zero covariance, giving a meaningful exact second-order dependence classification and potential stratified finite-sample methodology without asserting power claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
