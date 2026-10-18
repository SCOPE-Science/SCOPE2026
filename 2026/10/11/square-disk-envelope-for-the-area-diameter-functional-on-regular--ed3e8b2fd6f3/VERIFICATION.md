---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Even regular n has scale-free x=θ/(πsinθ), y=cosθ/4 for θ=π/n. Direct differentiation gives positive d²y/dx² on (0,π/4], using g(θ)=2θcos2θ+4θ−3sin2θ, g′=4h, h′′=4θsin2θ>0 with vanishing initial data; hence strict square–disk chord separation. Odd n and even 2n have the same x but the even y exceeds odd y by sin²(π/(2n))/(4cos(π/(2n)))>0. Every Fα=(1−α)x+αy is bounded by the larger endpoint, square or disk; equality and attainment follow from strictness, crossover exact α*=2(√2π−4)/(π(√2+2)−8). Independent exact symbolic derivatives, odd-even identity and crossover check. This does not solve the global convex-body problem.

## originality

PASS

The inspected 18-page 2014 source explicitly poses the global convex-body c(alpha) as its Question 2 and provides a separate perimeter bound, but does not solve the regular-polygon family or state the strict square–disk chord and exact crossover. The new result is deliberately only the regular-polygon subproblem; literature search did not reveal a stronger regular-polygon formula. Best-of-knowledge originality leaves unindexed elementary observations as a real risk.

## value

PASS

The functional is a specific explicitly posed question in Glazyrin--Morić, so eliminating an infinite natural competitor family for every α with an exact phase transition and strict equality case is independently useful even though it does not solve the whole convex-body problem. Chord convexity and odd-to-even domination are nontrivial geometric structure, not just tabulated regular polygons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
