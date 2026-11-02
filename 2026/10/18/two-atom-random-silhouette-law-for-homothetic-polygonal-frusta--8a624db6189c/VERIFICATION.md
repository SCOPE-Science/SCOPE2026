---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For u_z != 0, projection along the normal onto the horizontal plane induces an invertible affine map from the orthogonal shadow plane, preserving the face lattice. The two base images are K and tK+s, with c=s/(1-t)=-h(u_x,u_y)/((1-t)u_z). By convexity and support functions, c inside K iff tK+(1-t)c is contained in K. For a generic exterior c, the two support rays from c to K touch two vertices; the homothetic hull has exactly two cross-bridges, two copies of tangent endpoints, and one of each other n-2 labels, yielding n+2. Generic interior c gives n. Exceptional horizontal rays, boundary centers and edge-line tangent alignments form null sets. Gaussian ratios give bivariate Cauchy center density lambda/[2pi(lambda²+|c|²)^(3/2)], integrating over K is its normalized solid angle and yields the radial formula. Its derivative is -1/(2pi)*integral rho²/(lambda²+rho²)^(3/2)<0, with endpoint limits 1 and 0 and analyticity on positive lambda. As lambda tends to infinity the leading density is 1/(2pi lambda²), giving area(K)/(2pi lambda²)+O(lambda^-4). A regular polygon decomposes into n center-to-edge triangles and the classical triangle solid-angle formula reduces to the displayed arctangent. No step is inferred from finite trials.

## originality

PASS

Best-of-knowledge originality for the full all-convex-polygon two-atom law and its exact Cauchy/solid-angle distribution, not for homothetic containment, the angular Jacobian, classical cone-angle formulas, or regular-polygon triangulation alone. In particular, known general mean projection bounds and known homothetic hull volumes do not themselves state the n versus n+2 exhaustive complement; once that geometric event is established, the distribution integrates to the precise formula. No exact stronger published theorem was found among inspected statements; historical priority remains qualified.

## value

PASS

The number of visible shadow vertices of a fixed frustum is a natural stochastic-geometric invariant with a direct geometric shape-observation interpretation. For every convex n-gon including asymmetric bases, the theorem gives the full discrete distribution, excludes all intermediate complexity and reduces its sole parameter to a normalized solid angle. Strict monotonicity identifies the effective aspect h/(1-t) for known base geometry while proving the natural nonidentifiability of h and t separately; the regular polygon closed form and large-aspect decay provide useful benchmarks. This goes beyond renaming a standard calculation, yet is expressly limited to directly homothetic frusta, not arbitrary polyhedra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
