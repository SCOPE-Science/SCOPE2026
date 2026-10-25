---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For odd n, support directions decompose into n vertex cones and n arc cones each length 2alpha=pi/n, giving equal-weight distribution of R cos T and w-R cos T, T uniform[0,alpha]. For m independent Haar rotations, hull support maximum has CDF F^m; Cauchy support formula and integration yield exact perimeter formula and strict monotonicity, Barbier case m=1. Taylor/Watson endpoint integral gives 8pi R alpha²/m² deficit; upper CDF tail gives fixed-direction 2R alpha² E² weak limit. Phase rotations modulo q=2pi/n yield largest cyclic gap G_m, and on G_m<q/2 support is R cos(nearest vertex angular distance), yielding exact Delta_m=R(1-cos(G_m/2)); exceptional event probability <=m 2^(-(m-1)). Dirichlet exponential spacing representation implies mG_m/q-log m => Gumbel and logarithm-square Hausdorff scale. Fixed-m large-n beta integral gives coefficient A_m=(4-2^(1-m))/((m+1)(m+2)). Independent SciPy quadrature confirmed m=1 exactly pi w and m=2 closed formula for n=3,5,9 and m=5,30 trends; asymptotic proof is analytic.

## originality

PASS

Classical Cauchy perimeter/Barbier and maximum-spacing Gumbel results are credited. Falcó–Myroshnychenko identify geometry/area minimization of regular odd Reuleaux polygons, not random hull perimeters. Compared published random rotation intersection, Minkowski average and polygonal random-inscription findings with different set operations and objects. No exact outer hull profile or phase-gap transfer found in bounded searches; full related article access unavailable and residual priority risk explicit.

## value

PASS

The regular Reuleaux bodies are a canonical symmetry-constrained constant-width extremal family. Exact finite-m expected perimeter plus two sharply different convergence scales (pointwise versus worst direction) supply a natural measurable classification of random rotational convexification and a nontrivial geometric reduction to maximal circular spacings; not a relabeling of standard spacing law alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
