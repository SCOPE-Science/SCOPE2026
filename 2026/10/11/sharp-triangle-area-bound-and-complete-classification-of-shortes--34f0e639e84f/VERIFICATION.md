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

For any nondegenerate triangle all sides are strictly shorter than semiperimeter s, hence a perimeter-halving pair cannot be contained in one edge. Choose the one of its two length-s arcs passing through the common vertex V of the endpoint edges (including vertex endpoint boundary cases). With distances u,v≥0 and u+v=s, law of cosines yields |pq|²=s²sin²(θ_V/2)+(u−v)²cos²(θ_V/2). This is ≥s²sin²(α/2). At a minimum-angle vertex the incident sides b,c exceed s/2 by c<a+b and a≤b≤c, so the two half-s arc points are feasible and attain equality. Positivity of cos(θ/2) and strict monotonicity of sin on (0,π/2) classify every minimizer; number is 1/2/3 depending on number of minimum-angle vertices. Heron and sin²(α/2)=yz/((x+y)(x+z)) for ordered tangents x=s−a≥y=s−b≥z=s−c>0 give A/h²=((x+y)(x+z)/s²)*sqrt(sx/(yz)). Here sx/(yz)≥3 and (x+y)(x+z)/s²≥4/9 (the latter from y≤(s−z)/2, z≤s/3), with simultaneous equality only x=y=z. Independent 3654 exact-rational ordered tangent triples and 505 direct piecewise boundary minimizations support but do not replace the continuum proof.

## originality

PASS

Best-of-knowledge originality for the combined all-triangle sharp area/halving-distance ratio, its equality class, and complete shortest-chord geometry. The old source explicitly identifies the ratio and equilateral candidate, and a weak universal convex-cycle bound, but inspected primary full-text results do not prove a sharp inequality for every triangle. The simple triangle dilation lower bound is implied by but does not imply the exact half-angle formula. Returned Resultary self-match is excluded as external priority. Inaccessible plausible thesis and 2007 source are specified as genuine risks rather than automatic failure.

## value

PASS

Area relative to minimum perimeter-halving chord squared is explicitly motivated by the primary convex-geometry question. The known equilateral ratio and weaker general convex-cycle bound leave an exact natural geometric extremal subcase for arbitrary triangles. A sharp triangle-only bound with rigid equilateral equality and a constructive complete classification of every minimizing chord is a meaningful resolved subcase of a broader open extremal topic. Elementary proof length does not negate its value; no general convex-cycle solution is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
