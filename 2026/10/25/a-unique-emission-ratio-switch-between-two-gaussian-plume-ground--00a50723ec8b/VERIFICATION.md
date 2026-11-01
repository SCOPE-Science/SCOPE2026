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

PASS. With r=(H2/H1)^2>1 and q=Q2/Q1>0, substitution t=H1^2/(2k_z^2 x^2) turns the two-source centerline concentration into a positive parameter-independent multiple of F(t)=t(e^{-t}+q e^{-rt}); x>0 reverses the t ordering. F prime is positive on (0,1/r], negative on [1,infinity), and inside (1/r,1) has the sign of q-h_r(t), where h_r=e^{(r-1)t}(1-t)/(rt-1). Differentiating log h_r gives the quadratic whose fold discriminant changes at r_c=3+2sqrt2, with turning locations t_±=(r+1±sqrt((r-3)^2-8))/(2r). The two-maximum interval is exactly q_-<q<q_+. For two smooth maxima, the envelope derivative of their height difference equals t_far exp(-r t_far)-t_near exp(-r t_near)>0, because t exp(-rt) decreases for t>1/r. At the fold edges the ordering reverses; hence there is exactly one equal-height q_b and one global hotspot jump, not two. Expansion of F_t around the cusp (r_c,2-sqrt2,q_c), with exact independently checked nonzero mixed and cubic coefficients, establishes the square-root peak separation and 3/2-width of bimodality, while separate near-1 and near-1/r expansions yield q_b=r-e+e(1-e/2)/r+O(r^-2). The normalization to real x and positive source parameters is exact. The result is for a fixed meteorological 1/x dispersion law, not variable stability or changing vertical dispersion exponents.

## originality

PASS

PASS, best of knowledge on the narrow contribution. The profile is exactly a positive multiple of a two-component Gamma(shape 2, different rates) mixture. Došlá (2009) Proposition 6 already classifies local bimodality and fold interval, and Ahmed–Goria–Hussein (2008) analyzes gamma mixture modal and inflection regions. This important mathematical coverage is acknowledged; it is not a novel discovery of multimodality. The submitted result adds a unique global equal-peak swap as q varies, its direction, and sharp large-rate and cusp expansions, which the inspected gamma mixture theorems and Zoumakis multiple-source numerical optimizer do not state. Earlier Maxwell-set/equal-mode theory could overlap, and this is a significant residual risk.

## value

PASS

PASS. For two positive ground-concentration profiles the global exposure hotspot can jump discontinuously while each local extremum moves smoothly. A complete one-switch phase diagram, critical height-contrast threshold, exact singular width scaling, and non-obvious q_b=r-e+... large-contrast law directly answer a motivated optimization problem beyond textbook derivative solving. The claim does not assert that a simple plume is a complete atmospheric hazard model; it is a mathematically sharp reference example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
