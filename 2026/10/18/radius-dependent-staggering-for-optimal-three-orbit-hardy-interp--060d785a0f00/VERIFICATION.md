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

PASS: Reconstructed the exact squared Vandermonde product from three monic z^m-a discriminants and three pairwise resultants. The phase torus is covered by half-gap delta in [0,pi/2] and mean phi; the outer-distance product is strictly convex in cos(phi) and forces phi=pi away from a strictly suboptimal boundary. For t=-cos(delta) in [-1,0], derivative of (1-t²)(A-Bt)² has exactly one interior maximizing root with -1/2<t<0 because 0<B<A. Substitution fixes the displayed radical, unique unordered optimizer and maximum. For q=(r/s)^m, t=-2q+18q³+O(q^5), the normalized optimum/equal per-orbit factor tends 4/3 and m q->0, yielding (4/3)^m(1+o(1)). Independently recomputed 4 direct complex Vandermonde determinants (m=1,2,3,4) and exact resultant product at predicted phases; agreement 1e-8 relative. Singular radii r=s excluded, equality of phases zero determinant, m=1 included.

## originality

PASS

PASS best-of-knowledge: Neither general Vandermonde conditioning bounds, same-radius normalized Szegő kernel orbit optimization, nor the accessible historical interpolation construction mathematically implies the two-radius, three-cyclic-orbit D-optimal phase pair and exponential gain. Classical discriminant/resultant factorization is explicitly credited. Residual risk: older Sugiura–Torii full text unavailable and an unindexed weighted logarithmic-energy classification might apply.

## value

PASS

PASS: Maximizing the Gram determinant is a natural D-optimal interpolation-volume design for three regular sampling orbits in the Hardy polynomial basis. The explicit radius-contrast optimizer, rigorous uniqueness and exponential squared-volume advantage over equal spacing provide a precise, nontrivial infinite-family geometry classification; the work carefully distinguishes volume from least-singular-value conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
