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

For all n≥4, θ>0, prescribed adjacent-arrow contraction gives q_n=1/2+θ(1−θ)/[2(θ+n−2)(θ+n−1)]. Ewens deletion conditioned on fixed B_i leaves Ewens(θ) on n−1 points and Pr(B_i)=θ/(θ+n−1). The expected descent count conditional on endpoint fixation is (n−2)q_(n−1); for interior it is (n−3)q_(n−1)+(n−1)/(θ+n−2). The covariance identity yields exact endpoint −θQ/(2H), interior −θ(θ−1)P/H, and total −θ²(n−1)[n²−4n+2+2θ(n−1)]/H; H,P,Q positive. Thus endpoints always negative, interiors flip sign at θ=1, fixed-θ n^-1 vs n^-2 scaling and total negative. Independently enumerated all permutations at n=4,5,6 for θ=1/2,1,3 with exact rational cycle weights and checked every fixed-position covariance. Infinite n, real θ follow symbolic formulas, not enumeration.

## originality

PASS

Best-of-knowledge PASS for exact Ewens θ-dependent labelled fixed-point covariance and interior sign reversal; the θ=1 uniform special case and unconditioned pair inversion marginals are explicitly prior art, not re-claimed.

## value

PASS

An exact sign reversal of a natural local-fixed-point/total-descents dependence at the canonical Ewens θ=1 boundary, with provably different endpoint/bulk orders and persistently negative total covariance, resolves a structural statistical question obscured by global fixed-point-count conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
