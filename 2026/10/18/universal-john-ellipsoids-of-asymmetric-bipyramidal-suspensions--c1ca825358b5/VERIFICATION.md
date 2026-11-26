---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Uniqueness and horizontal reflection force the unrestricted John ellipsoid to have zero horizontal center and zero horizontal–vertical cross block. At each z between apices the body section is min(1+z/a,1−z/b)B: the base weight in a convex combination is at most both affine bounds and the smaller one is realized by using only the apex on that side. For a horizontal middle ellipsoid E_0, containment thus depends only on the smallest u with E_0⊂uB; replacing E_0 by uJ(B) preserves feasibility and strictly improves the determinant unless E_0 already equals uJ(B). Taking support maxima on the upper unit semicircle gives the two root constraints √(a²u²+v²)≤a+c and √(b²u²+v²)≤b−c, including the axial endpoint requirements. Their summed bound must be tight by scaling and then fixes c. For t=v/u the objective is proportional to t/(X+Y)^d, whose log derivative is 1/t−dt/(XY). The ratio XY/t² decreases strictly from infinity to 1; this gives a unique interior optimum and the positive quartic root with the displayed scales. The sign follows from b²X²−a²Y²=(b²−a²)t², and the determinant gives the volume. For fixed positive u,v and a+b, the sum of the two roots is strictly convex and symmetric as a function of a, hence increases strictly with imbalance. The imbalanced optimizer is strictly feasible at a more balanced pair, where joint dilation improves the objective. Section integration gives the constant host volume, and the stationary equation at a=b and in the one-sided limit gives the stated sharp ratio and sqrt(e d)/2 asymptotic. The cone endpoint is excluded from the positive-height class. The frozen `python3 verify.py` was inspected, not executed: its 6,132 batches sample identities, nearby aspect ratios and profiles in d=2 through 15 at numerical tolerances. The additional three-dimensional optimizer comparisons are reported without a replay program in this package and are not needed by the proof.

## originality

PASS

Credit the planar John-ellipse instance and endpoint comparisons to the broader quadrilateral theory, the cone limit and shape reduction for frusta to the corresponding cone/frustum results, and general extremality and uniqueness to John's theory. The supported distinct content is the exact coupled two-apex optimizer for positive unequal heights, including d≥3 and arbitrary origin-symmetric bases, and the strict fixed-total-height decrease of its John filling fraction with the sharp general-dimensional factor. The closest inspected matches concern one-sided cones or frusta, planar quadrilaterals, or a different extremal invariant of the same bipyramid. This judgment is bounded by the inspected sources.

## value

PASS

The horizontal determinant reduction treats nonsmooth and nonround bases without a new optimization for each shape. The height law is a strict extremal comparison across a natural family with equal host volume, with an attained symmetric maximum and a sharp limiting loss of order √d. This compares full deformations, not just known isolated cone or planar endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
