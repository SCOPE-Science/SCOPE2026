---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Near strictly interior minimizer t, unconstrained exact line searches are feasible and analytic; each vertex update derivative is the H-orthogonal projector P_i=I−n_i n_i^T H/(n_i^T H n_i). The 3-projector sweep has norm |c12 c23| in chosen order, trace c12 c23 c31 and J²=(trace J)J. With at most one orthogonal vertex pair, consecutive pair gives J=0 and quadratic one-sweep error; first/third orthogonal pair gives nonzero square-zero J and quadratic two-sweep error. The exceptional targets lie on the pair metric-circle interior arc iff opposite H-angle acute. Independently reconstructed exact rational example derivative J_(1,3,2)=[[1/5,-1/10],[2/5,-1/5]], J²=0 and J_(1,2,3)=0, and geometric circle identity; nonlinear quadratic expansions rely on source rational substitution.

## originality

PASS

Best-knowledge PASS: Products of orthogonal projections and nilpotent rank-one matrices are classical, but here the projections are actual linearizations of bounded away-step PolyCD updates with a nontrivial local-feasibility argument. Generic cyclic block Frank–Wolfe is not the same update. Mazumder–Wang Theorem 3.2 gives global linear convergence of PolyCDwA, which neither excludes nor characterizes nongeneric local quadratic convergence; related identification papers treat separable proximal coordinate descent rather than this vertex-directed away-step map.

## value

PASS

A sharp order-dependent one-versus-two-sweep local rate classification for a concrete practical constrained optimization method. The exceptional metric-circle geometry explains the non-generic superlinear phenomena and distinguishes away steps from ordinary forward-only PolyCD.

The dated certificate retains the supplied scientific assessment, sources and limitations.
