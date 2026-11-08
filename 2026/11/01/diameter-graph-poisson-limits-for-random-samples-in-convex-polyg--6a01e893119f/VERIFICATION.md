---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For any fixed convex polygon P with no redundant listed vertices and uniform iid points, all true diameter pairs are pairs of distinct polygon vertices by strict convexity of squared Euclidean distance along edges. At each diameter incidence the inward edge-ray projections onto diameter direction are strictly positive, giving local deficit D-|x-y|=u_v·z+u_w·q+O(|z|²+|q|²) and localization. Joint √n-rescaled point processes at different polygon vertices converge to independent intensity-1/A Poisson processes; the same process is retained for all edges incident to each vertex, yielding the stated min-of-edge-sums limit. Cone simplex area gives γ=sinθ/[2A(u·a)(u·b)] and exact void union law. Overlap at shared vertex gives strict positive covariance, while disjoint edges use disjoint processes. Two independent corner deficits yield t⁴/6 γ_vγ_w; intersections of low-edge events use >=3 distinct small cones and are O(t⁶), giving complete lower tail; the separate two-point tail counts both edge orientations and is ε⁴/3 Σγ_vγ_w+O(ε⁵). Independently recomputed the nonregular isosceles triangle rates 1/3 and 1/2, and coefficients 1/18,1/9. Finite geometric examples do not prove the Poisson weak limit, which follows from the point-process argument.

## originality

PASS

Best-of-knowledge PASS for arbitrary-polygon diameter graph Poisson limit with shared vertex incidence correlations, matching-graph independence iff classification, and the two sharp fourth-power laws. The accessible Lao theorem assumes disjoint diametral corners in even regular polygons. Appel–Najim–Russo 2002 may contain related general hypotheses, but only its abstract was accessible; its full text is a material historical-priority risk, not asserted non-covering.

## value

PASS

General polygon sample-diameter extremes are a natural stochastic geometry problem. Shared diametral vertices defeat the formerly convenient independent-edge model; the theorem gives the correct full correlated process, an exact diameter-graph matching criterion for independence, and sharp rare-event coefficients in the genuinely nonregular shared-apex example. The result is a complete geometric class extension rather than another special polygon table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
