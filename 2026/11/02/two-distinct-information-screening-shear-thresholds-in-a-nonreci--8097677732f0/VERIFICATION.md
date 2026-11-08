---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Dimensionless drift K=[[-1,g,-k],[0,-1,k],[k,-k,-1]] has cubic characteristic z^3+3z²+(3+2k²)z+(1+2k²-gk²). Routh–Hurwitz yields unique positive-definite stationary covariance for 0<=g<2+k^-2 (k>0). Six linear Lyapunov equations K C+C K^T+2I=0 give C13=gk[(2k²+3)g-(k²+2)]/F, F=(1+2k²-gk²)(8+4k²+gk²)>0; hence marginal X-Z independence iff g=m=(k²+2)/(2k²+3) for positive shear. Conditional Gaussian independence iff C13-C12C23/C22=0. Exact substitution gives positive-denominator gk times B(g,k)=k²g²-(5k^4+18k²+16)g+4(k²+2)², with B(4/5)>0,B(1)<0 and B(2+k^-2)<0. Thus exactly one physical positive root h(k) in (4/5,1); the other quadratic root is beyond stable range. Derivatives yield m decreasing and h decreasing via B_v<0 and B_g<0 along the smaller root. This proves 1/2<m<2/3<4/5<h<1. Independently solved the exact rational 6×6 Lyapunov system at k=1,g=3/5, obtaining C13=0,C12=2/7,C23=1/14,C22=15/14 and nonzero conditional covariance -2/105; source checker covers additional rational cases but finite checks do not certify all reals. Shear zero and instability boundary explicitly excluded.

## originality

PASS

Published primary results on the same subject and Resultary related findings were compared at the level of claimed mathematical implication; strongest already-covered components are credited and excluded from the novelty claim. The remaining specific classification appears new in actually inspected material, subject to listed source-access and indexing risks.

## value

PASS

The widely studied nonreciprocal stochastic trap has two structurally different zero-information screening transitions, one marginal and one conditional, with a universal gap for every positive hidden coupling. These thresholds distinguish unconditional independence from Gaussian conditional independence, a useful interpretation beyond the known stability boundary and generic stationary Lyapunov equation. The all-parameter ordering and monotonicity are substantive exact facts of this motivated model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
