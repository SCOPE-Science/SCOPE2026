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

For G=K_p∨independent_q in zero-sum H dimension d=p+q−1, project onto clique contrasts, independent contrasts and one between-part direction. Clique roots have support square 2a; cross roots support square (p−1)a/p+(q−1)b/q+Nc/(pq), N=p+q. Piecewise a,b,c are positive and cross support one. Construct weighted Laplacian from all cross edges weight w and clique edges v: when q≥p+1 use (w,v)=(1/(pq),0); else (2/[d(p+1)],2(p+1−q)/[dp(p+1)]). Their weights sum 1 and eigenvalues invert the proposed S via S=(dL)^{-1}. Any translated inscribed ellipsoid has tr(LT)≤1; AMGM det(L)det(T)≤d^{-d}, equality gives T=S and cross-root spanning forces center zero. Therefore unique global John ellipsoid, not just symmetric optimum. Clique support 2a≤1 hits equality exactly q≤p+1, but becomes strict q≥p+2. Bipartite ellipsoid comparison yields invisibility iff q≥p+1. Independent exact rational checks p,q=(3,2),(3,4),(3,5),(4,3),(4,5),(5,8) including boundary and Laplacian inverses passed.

## originality

PASS

Best-of-knowledge original relative to the named same-object, general-method and neighboring-formulation publications inspected. Exact statement/implication comparisons do not establish prior coverage; limitations on partially read related records remain recorded explicitly. Mathematically equivalent primal/dual and weighted-Laplacian formulations explicitly considered. The generic dual does not itself evaluate optimal graph-specific weights or contact transition. Neither neighboring family contains K_p∨independent_q as an edge-preserving special case for all p≥3; general optimality theory is a tool not a previously computed sharp threshold.

## value

PASS

Sharp and somewhat surprising geometric edge-screening phenomenon: adding all clique edges strictly shrinks the Lipschitz polytope yet leaves its John ellipsoid unchanged beyond a precise threshold, including a tangency-but-zero-multiplier boundary. Complete all-p,q formulas with contact classification are reusable in graph geometry and optimal designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
