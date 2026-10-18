---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Use Adam-Day et al structural theorem for finite PL_2 rooted frames: height<=2, depth-one points have at most two strict successors, strict upset of root connected. Exactly-height-two frames therefore correspond bijectively to connected bipartite incidence systems with each depth-one labeled point incident with one or two labeled tops. For a partition π of top set, permissible choices per depth-one label are t+sum_B choose(|B|,2); Möbius inversion coefficient (-1)^(|π|-1)(|π|-1)! gives N_(t,e). Two-sort exponential formula log sum exp(choose(t+1,2)y)x^t/t! counts connected systems; choose top labels for global R_m. Independently enumerated 20 small (t,e) grids and matched partition lattice counts. Finite verification supplemental to combinatorial bijection.

## originality

PASS

Adam-Day et al establish exact frame structure, but the identified results do not enumerate these rooted PL_2 frames by t,e. Standard partition-lattice Möbius inversion and exponential formula are not new. The new claimed object-specific all-parameter enumeration transfers that structure to a natural logical census; t=2 case 3^e−2^e is explicitly classical.

## value

PASS

Exact labeled count of finite frames for the logic of a fixed two-dimensional convex polyhedron is a natural structural invariant useful for finite-model enumeration and complexity benchmarking, not a random parameter slice. Full bivariate census and generating function are self-contained despite using standard combinatorial tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
