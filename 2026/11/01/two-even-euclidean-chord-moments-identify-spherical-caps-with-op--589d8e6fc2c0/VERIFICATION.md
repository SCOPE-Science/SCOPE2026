---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For surface-area-uniform independent points on sphere radius R>0, cutoff z in [-1,1), axial u uniform [z,1], azimuth uniform, gives E(U dot V)=((1+z)/2)^2 and E(U dot V)^2=tr(EUU^T)^2. Independent algebra verifies μ=R²(1-z)(z+3)/2 and ν=2R⁴(1-z)^2(z²+4z+5)/3. Thus κ=ν/μ²=(4/3)(1+t²), t=(1+z)/(3+z)∈[0,1/2), exactly feasible μ>0, 4/3<=κ<5/3. Inverse z=(3t-1)/(1-t) and R²=μ(1-t)²/(2(1-2t)). Cut-height estimate |Δz|<=2sqrt(3)|Δκ|^(1/2) is sharp by s=0,t↑1/2; angle exponent1/4 is sharp by full-sphere α→π, κ-4/3≈(π-α)^4/12. Analytic inequalities, not finite parameter samples, prove sharpness and universality.

## originality

PASS

Earlier complete-sphere chord distribution is forward and contains z=-1. More general forward geodesic-distance distributions for prescribed convex spherical caps support moment computation but do not state the full family of arbitrary cutoff (including caps >hemisphere), two-moment unknown-radius inverse, or sharp conditioning exponents. Priority is bounded.

## value

PASS

Determines both scale and opening from only two natural chord moments with exact feasible moment wedge, explicit globally sharp cut-height constant and optimal 1/4 angular inverse exponent; this is a complete motivated inverse and conditioning classification of a natural cap family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
