---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Differentiation of the individual translated profile gives g'(z)=-8z/Q(z)^(3/2), where Q=(z²+b²)(z²+b²+4); the central curvature changes sign exactly at the positive root of 5s⁴+2Ds²-b²(b²+4). For 0<t<s, putting x=s-t and w³=(s+t)/x makes the stationary equation Q(w³x)=w²Q(x). Dividing the expanded equation by w²-1 and writing y=w+1/w gives the frozen rational equation, bijectively for y>2. Both rational coefficients strictly decrease there, as follows from the stated derivative factorizations and the positive expansion in y-2. The endpoint values are the curvature numerator and -b²(b²+4). There are no off-center stationary points at or below threshold and exactly one on each side above it; the derivative beyond s and evenness finish the classification, including s=0. At the root r, Q'/Q=2/(3r), yielding a negative fourth derivative and positive s-derivative of the central curvature. The implicit function theorem in t² gives the stated coefficient and error term. The normalized threshold polynomial has opposite signs at 1/5 and 1/2 and gives both limiting ratios. The two equal-height maxima above threshold are isolated strict local maxima and both globally maximizing (not individually strictly higher than the other). A separate high-precision check on the original flux reproduced the b=1 benchmark and tested the opening at b=0.01, 1, and 100; it is not the universal argument.

## originality

PASS

The binary-source sum and observed double peaks are prior; the supported distinct contribution is the explicit symmetric threshold together with a global stationary-point count and quantitative onset. The closest inspected sources do not give that result. This is a bounded judgment, with a material unresolved comparison to Griest–Hu (1992).

## value

PASS

Equal impact parameters and equal flux isolate the baseline resolution question for a standard astronomical signal. The exact time-separation benchmark, exclusion of an intermediate mode regime and quantified peak opening are useful in distinguishing inherent profile geometry from cadence or noise limitations. The ideal result is not a detection guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
