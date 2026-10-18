---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For uniform Catalan Dyck excursions of semilength n, P_n counts adjacent UD peaks and S_n is sum of 2n step-start heights (unscaled). Under first return UVDX, Q=S−n satisfies Q(W)=Q(V)+Q(X)+2|V|_U and P(W)=P(V)+P(X)+1_{V empty}; the generating system F=1+zF(F+t−1), G=z[G(2F+t−1)+2zF_zF] yields exact mixed peak-area coefficient via differentiation at t=1. Combining with Narayana E[P]=(n+1)/2 and Var(P)=(n²−1)/(4(2n−1)), derives Cov(P,S)=(n+1)/2−(n+1)4^(n−1)/binom(2n,n) (zero n=1, strictly negative n≥2); affine regression β=((2n−1)/(n−1))(2−4^n/binom(2n,n)) ~ −2√(πn). Independently enumerated 23713 excursions n1..10 and checked exact covariance rationally. Infinite statement rests on formal generating functions plus Stirling, not finite enumeration.

## originality

PASS

Blanco–Petersen 2012 analyze area jointly with a noncrossing-partition rank explicitly NOT identical to the number of peaks under their area-preserving bijection (their Remark 1.3). Classical Narayana and Carlitz–Riordan statistics are individual marginals. Mansour 2002 counts peak heights, not a displayed all-peak unscaled area covariance in material inspected. The exact cross covariance and sign may be obtainable from known joint peak-area q-Narayana generating functions; earlier broad Deutsch 1999 is incompletely inspected and remains high priority risk. Not claiming the general first-return mechanism as new.

## value

PASS

A precise negative correlation between path local complexity (peaks) and global geometry (area) across every nontrivial Catalan size, with a natural least-squares prediction slope scaling as √n, is a meaningful exact mixed-statistic invariant of uniform excursions; scope explicitly excludes nonlinear conditional distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
