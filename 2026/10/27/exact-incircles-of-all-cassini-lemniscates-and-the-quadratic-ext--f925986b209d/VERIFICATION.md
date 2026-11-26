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

Expanding gives |z²−s²|²=(x²+y²−s²)²+4s²y². If s²≤1/2 and y²≥1−s², then y²≥s², so minimizing the first square over x gives at least (y²+s²)²≥1 overall. Equality at the top latitude requires x=0, even at the junction. For s²≥1/2 the second term alone bounds the height by r=1/(2s); equality requires x²=s²−r². Any disk attaining the strip bound must have real center, and its top point lies in the closed sublevel set, fixing all possible centers. The centered branch attains its bound by the triangle inequality. On the other branch take c²=s²−r²: the boundary modulus squared is 4r²(c²+r² sin² t)≤1, and strict interior inclusion follows by maximum modulus. At s=0 this gives the unit disk; at s=1/sqrt(2) the two formulas coincide, and the pinched s=1 and disjoint regimes cause no new cases. The derivative of c² at the junction is 2sqrt(2), giving the claimed onset. Rigid normalization of a monic quadratic preserves radii (with no rotation needed for coincident roots); strict decrease with separation gives the sharp unit-root bound and exactly the antipodal equality case. Read the rational checker and recorded run notes without executing the frozen code; the continuum proof is decisive.

## originality

PASS

Qualified to the complete unrestricted inradius and maximizing-center theorem and its arbitrary-quadratic extremal consequence. Prior work already has the antipodal model radius and displayed maximizing disks, the classical convexity threshold, and a Cassini double-tangent construction that includes the high-branch candidate. The retrieved statements do not supply the entire two-branch profile, strict containment and exhaustion of all optimal centers, or sharp minimization among all unit-disk quadratics.

## value

PASS

Largest contained disks are a natural sharp invariant of the full Cassini family, and the center classification is stronger than a radius or a tangent-circle construction. The exact bifurcation and rigidity hold over connected, pinched, and disconnected shapes and settle the unrestricted quadratic unit-root minimum with equality classification. This gives a precise finite-degree benchmark without claiming a higher-degree theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
