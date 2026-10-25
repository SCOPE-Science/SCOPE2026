---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Kim Definition 3.19 fixes ||f||_{E^p}=||f||_infty+||Z||_p+||H||_p. A level-m elementary tent has maximum 2^{-m/2-1}, one Z_m=2^{-m/2}, and H_j=2^{-m/2} exactly for 0<=j<=m, producing norm 2^{-m/2}[(m+1)^{1/p}+3/2]. The half-tail estimate (Kim Proposition 3.24) and monotonicity yield ||f-Pi_N f||_infty<=1/[2(N+1)^{1/p}] on the unit ball. Interpolating at 2^N+1 nodes gives that sampling upper bound. For any deterministic adaptive algorithm given at most n exact queries, its all-zero transcript visits at most n interiors of 2^m>n dyadic cells; a unit tent and its negative supported in an unvisited cell produce identical transcripts and have unavoidable supremum error at least their amplitude. The two levels m=ceil(log2(n+1)) and M=floor(log2(n-1)) differ from log2(n) by O(1), squeezing the exact coefficient 1/2. Uniform convergence of finite-rank interpolants proves compact inclusion. The independent finite identity checks are only corroborative.

## originality

PASS

The specified energy norm, truncation and half-tail upper bound are explicitly Kim’s prior work. The new assessment is the matching zero-transcript lower bound uniformly over nonlinear adaptive deterministic samplers and the resulting exact leading information radius. The two potentially broader sampling papers work with different smoothness balls and/or Lq losses; similarity of sampling vocabulary alone gives no implication.

## value

PASS

The E^p norm was introduced for pathwise integration but its attainable recovery rate from exact observations was not previously quantified at the information-theoretic level. A sharp lower bound against all adaptive nonlinear deterministic algorithms and exact 1/2 coefficient turns a qualitative tail upper bound into a complete optimal recovery theorem. The adversary is simple but its exact norm calculation, matching of dyadic scales and robustness to adaptivity establish a motivated missing boundary fact rather than a restated textbook interpolation inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
