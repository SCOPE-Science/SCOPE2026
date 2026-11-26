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

In logit coordinates the derivative of the return map is exp(∫a x(1−x)dt)>1, and the displacement has opposite limiting signs; thus the unique interior fixed point is repelling and separates the pure-state basins. On that orbit h1<ell<u<h2, ascent and descent traverse the same interval, and the weighted residence density w is the sum of the two reciprocal phase velocities after removing a_i. Its mass is abar T and its first moment is abar hT by integrating the logit drift. Differentiating these two moments gives w(u)u'=abar(h−ell)/(u−ell) and −w(ell)ell'=abar(u−h)/(u−ell), establishing endpoint order and (TV)'=(h−ell)(u−h). The expectation of (x−ell)(u−x) is strictly positive, so TV'>0. The logit and frequency fixed-point multipliers agree by conjugacy, and the weighted mean gives Lambda=abar[h(1−h)−V]. For small T the width is O(T); smooth positive w near h makes the midpoint differ from h by O(T²), and the first phase then gives width vT+O(T²). The normalized smooth density differs relatively from uniform by O(T), giving the variance coefficient v²/12. For large T the divergent ascent and descent times force ell→h1 and u→h2 respectively, and averaging (TV)' gives the asserted limit. Its positivity is the selection-weighted average of h_i(1−h_i) multiplied by abar. Independently at (a1,a2,h1,h2,p,T)=(3,3,1/3,2/3,1/2,12), symmetry and bisection on the elementary ascent-time integral give ell=0.33814357714 and u=0.66185642286. Integrating 1/(x−h1)+1/(h2−x) from ell to u and dividing by T gives Lambda=0.70397655882, and the identity gives V=0.01534114706.

## originality

PASS

The supported distinction is the exact derivative and strictly decreasing per-unit-time exponent, with its endpoint rates for all fixed-duty parameter choices. Shu–Fu's exact same scalar model, interior periodic constructions and stage-time formulas are prior art, not discoveries of the frozen record. The compared published and indexed results do not establish the variance/Floquet law on this domain.

## value

PASS

The residence derivative resolves the direction of a natural switching-timescale comparison that uniqueness and repulsion cannot answer. Its connection to strict variance growth identifies how the orbit widens while weakening the repulsion per unit time and yields both limiting rates; this is a structural quantitative result rather than another oscillating example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
