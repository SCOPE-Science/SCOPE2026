---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The exposed opposite-sign pair condition requires both grid indices distinct; the same-sign faces are Cartesian products of simplices and give rook edges, so each of 2pq vertices has degree pq-1. The adjacency matrix is [[R,S],[S,R]], where R is rook adjacency and S=(J_p-I_p) tensor (J_q-I_q). Even/odd diagonalization and eigenvalues p-1,-1 and q-1,-1 of the tensor factors give all six eigenvalue families with multiplicities totaling 2pq, one zero. Kirchhoff gives the exact tree product; comparison of odd-block entries gives the spectral gap and the exceptional p=q=2 multiplicity 3. Independently constructed Laplacians for (p,q)=(2,2),(2,3),(3,3) match the exact characteristic polynomials and cofactors, including 384 trees at (2,2). These finite checks supplement the all-parameter proof.

## originality

PASS

Complete bipartite symmetric edge polytopes were studied for facets, h*, volume and triangulations; none of the read primary statements gives the one-skeleton eigenvalues. The general signed-two-cover block lemma is credited and only the actual geometric signed-rook-complement graph and its all-parameter eigenanalysis are assessed as the contribution. Resultary searches under symmetric edge/adjacency polytope and 2-lift terminology returned no exact earlier equivalent spectral formula.

## value

PASS

Complete-bipartite symmetric edge polytopes are classical lattice polytope families with extensive facet/Ehrhart study. Their graph-theoretic Laplacian, complete multiplicities, tree complexity, and Fiedler transition (uniform gap for p=2 versus growing balanced gap) form a natural two-parameter connectivity classification not furnished by the known defining-graph tree counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
