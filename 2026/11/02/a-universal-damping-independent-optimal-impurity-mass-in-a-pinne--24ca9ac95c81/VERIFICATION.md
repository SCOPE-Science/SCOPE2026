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

For a pinned harmonic 3-site chain with masses (1,u,1), w,k,gamma>0, equal endpoint momentum damping and TL>TR>=0, the six-dimensional linear drift is Hurwitz by energy dissipation and observability from endpoints. Its 21-variable stationary Lyapunov system yields j=DeltaT*gamma*k^2*(gamma^2*u*(k+w)+k^2)/(2D(u)) with positive D; the reconstructed D quadratic discriminant is -k^2*(k+w)^2*(7k^2+24kw+8w^2). Direct rational differentiation factors j' as a strictly negative factor times [(k+w)^2*u-(k^2+3kw+w^2)], with all remaining factors positive. This proves a unique global maximum u*=1+kw/(k+w)^2 in (1,5/4], independent of gamma and DeltaT. Independently assembled 6x6 Lyapunov equations numerically for three distinct spring/pinning/friction parameter sets, checking formula and current maxima including unit case u*=1.25, j=1/7. Supplied symbolic checker was inspected, and its reported exact solve alone was not treated as independent evidence.

## originality

PASS

Best-of-knowledge originality for the precise final mathematical claim; generic tools and starting formulae are acknowledged as prior. General exact covariance/Lyapunov formulas and alternating mass chains can potentially specialize to the trimer; the closest 2010 text is inaccessible and therefore remains a material unresolved historical priority risk, not evidence for noncoverage.

## value

PASS

The central mass is a natural design parameter of the smallest harmonic bridge having an interior impurity. The sharp global all-friction optimizer and universal bound 5/4 are precise structural identities, not a parameter fit; equal-mass conductor is strictly suboptimal though the gain can be modest. It does not generalize to extended chains or different friction conventions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
