---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The balanced three-periodic normal measure (facet lengths delta(1-t) every third direction, delta(1+t/2) otherwise) yields unique centered Minkowski polygon for N=3m>=9. Facet-support recurrence ell_j=(r_{j-1}+r_{j+1}-2cos(delta) r_j)/sin(delta) with r_j=A-L tau_j gives support values a=A+Lt,b=A-Lt/2. Adjacent line intersection has squared radius (x^2+y^2-2cos(delta)xy)/sin^2(delta), so inradius is b and circumradius is mixed (a,b). Consequently dH(K,B)=max{1-b,R-1}. The exact quadratic R^2-(2-b)^2=C0+C1t+C2t² has C0<0,C2>0 and is positive at t=1 by a strict arctan inequality, giving exactly one crossover t_N in (0,1). Analytic series yield 1-t_N=3pi²/(5N²)+O(N^-4) and uniform dH=pi²(1+2t)/(3N²)+O(N^-4). Matching one-step transport plan and geodesic distance-to-deficit potential give W1=2pi t/(3N). Independent symbolic Taylor and quadratic-identity calculations corroborate finite identities, not infinite quantifiers.

## originality

PASS

The primary 2026 inverse Minkowski reconstruction theorem gives a general transport upper bound and the equal-weight grid instance t=0, but not an exact three-periodic facet-versus-vertex switch and N^-2-thin threshold. The published equal-area/equiangular polygon result is for period-two lengths and an area deficit, and a sharp Cauchy quadrature result optimizes a distinct zonogon brightness statistic. General inverse support recurrence permits calculation but does not state the sharp phase theorem without the additional derivation.

## value

PASS

The balanced three-periodic family is a natural discretized surface-area measure for inverse Minkowski reconstruction. This exact all-t phase classification shows where farthest vertices supersede nearest facets; the threshold has a quantitatively sharp N^-2 boundary layer. Uniform N^-2 Hausdorff approximation while W1 is N^-1 for fixed positive t exposes a concrete limitation of generic transport stability bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
