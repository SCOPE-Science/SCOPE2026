---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For fixed-free n-mass identical spring system with n>=2, N=2n+1 odd and strictly positive ground and bond damping, T has simple eigenvectors phi_s(j)=2/sqrt(N)*sin(j(2s-1)pi/N). Ground coupling at p annihilates a mode exactly when N divides p(2s-1), and a bond coupling at b when N divides (2b-1)(2s-1). The latter follows via sine-difference cosine zeros and parity. Positivity of all damping coefficients implies the common kernel is exactly those modes with (N/g)|(2s-1), g=gcd(N,site labels,odd bond labels); there are (g-1)/2 modes with frequencies 2sqrt(k/m)sin(pi*t/(2g)), odd t<g. Invariant stable complement has negative real-part state-space spectrum by mechanical dissipation and absence of imaginary-axis modes, hence exponential convergence. The asymptotic local-kick energy is diagonal protected projection, yielding g/N except j multiple of g. Relative totient pairing gives phi(N)/2 stabilizing placements of each type. Independent examples n=4,7,10,13,19 checked all one-dashpot and selected mixed configurations, sine nulls and energy projectors; all-size theorem is analytic.

## originality

PASS

Best-of-knowledge original specific final mathematical result after explicitly excluding known foundational subclaims. All four equivalence/coverage/table/implication comparisons use stated primary reading, semantic search and uncertainty; no failure-of-search-as-proof assertion. The original claim is accepted without publication or unearned provenance.

## value

PASS

A sharp joint controllability/damping arithmetic invariant for two physically distinct types of viscous loss, with exact number of undamped modes and local energy retention independent of loss strengths. Mixed ground/bond duality provides a reusable vibration-design criterion, beyond classical single-site frequency locking.

The dated certificate retains the supplied scientific assessment, sources and limitations.
