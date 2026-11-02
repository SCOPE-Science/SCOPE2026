---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Reconstructed the full domain 0<r<1, 0<epsilon<1, 0<p*<=1, pi(0)=1, pi(p*)=0, convex nonincreasing smooth pi with pi=0 after p* (or p*=1), and strict interior decrease. For f=-r-epsilon*pi-prime(P)(1-P)+pi(P), f-prime=(1+epsilon)pi-prime-epsilon(1-P)pi-double-prime<0, so exactly one P0. The source pi-prime-inverse((1-r)/epsilon) is undefined since its argument is positive while pi-prime<=0, and pi-prime need not be injective. Convexity yields pi(P)<=1-P/p*, so f<=h; h-prime=-1/p*-epsilon(1-P)pi-double-prime+epsilon*pi-prime<0, h(0)>0,h(p*)=-r, and therefore P0<=root(barP). Also pi-prime(P)>=pi-prime(0) yields h<=H(P)=1-P/p*-r-epsilon*pi-prime(0)(1-P), whose zero is U and whose slope -1/p*+epsilon*pi-prime(0)<0; hence barP<=min(p*,U). f(pi-inverse(r))=-epsilon*pi-prime(pi-inverse(r))*(1-pi-inverse(r))>0 provides strict lower bound. The admissible pi(P)=1-P, p*=1 gives exact P0=barP=U=1-r/(1+epsilon). Verified exact Git source-tree and independent algebra and 108 convex-family bisection parameter tests; tests illustrative, not an infinite proof.

## originality

PASS

Best-of-knowledge PASS for the combination of identifying a mathematically undefined upper endpoint in a published named convex equilibrium theorem and supplying a valid explicit initial-slope-only sharp-in-an-admissible-case replacement. IMPORTANT: the original primary proof ALREADY proves P0<=barP, and convexity makes the new U bound a short elementary consequence of the pre-existing h comparison, so the implicit-root result is COVERED and claimed novelty is strictly limited to diagnosing the failed final inversion and presenting a genuinely computable closed-form replacement. No independently published source-specific erratum or explicit U statement located in actual targeted searches. This is a qualified priority judgment, not an assertion the chord technique or all comparison bounds are new.

## value

PASS

This is a motivated theorem-level correction: the advertised upper endpoint of a published model equilibrium-localization theorem is not defined under its own hypotheses, despite the existence of the unique stable equilibrium. The replacement gives a computable closed-form bound from p* and the single endpoint derivative pi-prime(0), with an admissible exact equality case, enabling interpretation and safe use without inverting a derivative; barP remains a sharper valid implicit bound. Though the calculation is elementary and its comparison seed appears already in the source proof, correcting a formally false published bound with a demonstrably valid usable endpoint has a specific substantive purpose beyond a trivial normalization test. No claims about calibrated policy effects, nonconvex equilibria, or a new general vaccination theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
