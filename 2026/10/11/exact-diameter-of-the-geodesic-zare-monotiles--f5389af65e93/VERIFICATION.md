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

Reconstructed the exact hyperbolic geometry of T_q (q>=2; curvature -1), not merely prior logs. A simple geodesic polygon triangulates into triangles with original vertices using the Klein model; convexity of distance on geodesics reduces the ambient diameter to original vertex pairs. For the source vertices, max cosh distances are C_low=1+(q+1)^2/(2q^4), C_up=1+1/(2q^2), C_cross=1+(2q^2+2q+1)/(2q^3(q+1)). C_low>C_up, while C_cross-C_low=(q^3-q^2-2q-1)/(2q^4(q+1)). Its numerator is negative at q=2 and strictly positive for every integer q>=3 (successive difference 3q^2+q-2>0), establishing all extremizers and both exact branches. The limits follow analytically from q^2(C_cross-1)->1, arcosh(1+x)~sqrt(2x), and source area 2atan(1/(2q^2))~1/q^2. Independent Lorentz-model exact computations checked all 156940 vertex pairs for q=2..60, with 59/59 matching formulas and extremizers; these checks supplement rather than prove the infinite result.

## originality

PASS

The inspected original construction provides an upper bound <3/q but not the exact diameter; Zare gives the underlying combinatorial idea, not this metric evaluation. No independent covering result appeared in targeted mathematical searches; updated uninspected versions remain a priority risk.

## value

PASS

This is the source paper's canonical nonconvex geodesic counterexample family exhibiting arbitrarily small diameter as the number of sides grows. Its exact diameter and extremizing pairs are natural quantities needed when benchmarking efficient small monotiles; the proof upgrades an explicit 3/q upper bound to the sharp asymptotic scale sqrt(2)/q and shows the exceptional q=2 endpoint regime. The area-diameter ratio is a natural scale-invariant comparison. No universal extremality claim is asserted; usefulness is specific quantitative information for this already motivated construction, not computational novelty alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
