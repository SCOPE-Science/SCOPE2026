---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For N8(s,t)=max(|s|,|t|,(|s|+|t|)/sqrt(2)), the unit circle is an 8-edge centrally symmetric octagon with vertices ±(1,sqrt(2)−1), ±(sqrt(2)−1,1) and counterparts. Parametrize γ(s) affinely on edges with period 8 and let D(s,g)=N8(γ(s+g)−γ(s)). For cyclic directed gaps 0≤g≤5/2, 4 convex polygonal cells in phase/g coordinates cover the domain, so exact vertex maxima 2(sqrt(2)−1), sqrt(2), L, L bound D≤L, L=1+1/sqrt(2). If g=5/2+h, 0<h<1/2, direct edge affine formulas yield D>L iff u=s mod 1<1/2, or u>1/2 and u+h>1, with u=1/2 excluded. If all three pairwise distances exceeded L, cyclic gap sum 8 forces each g_i=5/2+h_i with ∑h_i=1/2; the strict phase criterion plus u_{i+1}=(u_i+1/2+h_i) mod1 forces all phases on the same side and summation would give ∑h_i=3/2, contradiction. Witness x=(1/sqrt2,1/sqrt2), y=((sqrt2−1)/2,−1), z=(−1,(sqrt2−1)/2) are unit and pairwise distance L, giving J_T=L<sqrt3. Independent exact quadratic-field checker source inspected; independently evaluated cell extrema and thousands of strict-gap grid points; continuum bound follows from affine/phase proof, not sampling.

## originality

PASS

Ni–Liu–Zhou–Xia 2024 introduce precisely J_T as the unrestricted three-unit-vector maximin, and assert sqrt3 universal lower bound; their full source includes Hilbert and hexagonal cases but no regular-octagon equality identified. The octagon shows the universal finite-dimensional assertion fails; published regular-polygon equilateral studies use more constrained triples, so do not directly imply an unrestricted maximin upper bound. Unindexed Minkowski packing equivalents remain a risk.

## value

PASS

A natural exact 3-point packing invariant of the symmetric regular-octagonal Banach unit circle is classified by a complete boundary optimization, with an explicit extremal equilateral triple. Crucially L<sqrt3 supplies a concrete 2D counterexample exposing the dimension error in a prior stated universal lower bound. This is a substantive motivated correction and exact invariant, not an arbitrary slice or simple numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
