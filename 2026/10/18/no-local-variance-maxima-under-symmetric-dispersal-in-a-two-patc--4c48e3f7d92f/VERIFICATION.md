---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

H(d)=[[a+d,-d],[-d,b+d]] is symmetric positive definite for a,b>0,d>=0. Solving HΣ+ΣH=Q yields the stated rational V1(d) with denominator 2(a+b+2d)[ab+(a+b)d]. Independently derived this solution and verified symbolically the exact quadratic derivative numerator Ad²+Bd+C. The two distinct negative poles of this rational function imply a nonconstant derivative has at most one positive zero. Positive semidefiniteness c²<=qr implies C>=0 forces A>=0 and the boundary B signs; hence there are no local maxima and a patch with minimum has C<0<A. Trace derivative −(1/2)tr(Q H^-1 L H^-1)<=0 prevents minima of both patches. Independent noise gives sharp r/q>(a²+4ab+5b²)/(a²+4ab+b²), and an independent exact computation checked the witness a=b=q=1,r=4 with min d=(sqrt15−1)/7 and regional total variance fixed at 5/2. The full parameter theorem depends on the analytic PSD argument, not a bounded grid.

## originality

PASS

Prior broad ecological metapopulation literature addresses homogenous synchrony, nonlinear multiplicative-noise extinction and persistence, not an explicit classification of stationary local variances for asymmetric stable two-patch additive OU with arbitrary PSD noise covariance. The elementary Lyapunov equation itself is routine; the strongest candidate contribution is the global shape restriction, impossibility of simultaneous minima, and sharp threshold. Full Lande–Engen–Sæther 1999 primary paper remains inaccessible; we record it as genuine priority risk rather than saying the whole paper excludes the theorem.

## value

PASS

This theorem identifies a qualitative restriction and a sharp parameter boundary for a natural local ecological fluctuation statistic: dispersal can reduce and later increase a patch’s risk even when regional aggregate variance is constant, but cannot create a local maximum. Correlation is allowed throughout the PSD cone including singular noise. This is a motivated model-level structural theorem, not an arbitrary algebraic fit; it does not assert nonlinear persistence or extinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
