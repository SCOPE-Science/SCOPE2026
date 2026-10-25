---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For every finite connected simple G with n>=2 and m edges, reconstruct Q(S(G))-2I as [[D-2I,B],[B^T,0]], with unsigned incidence B. A rank-r saddle matrix has r positive and r negative directions plus inertia of C on ker B^T, and m-r null directions. Rank B=n for nonbipartite G, n-1 for bipartite G, where the residual quadratic form on the bipartition sign vector equals 2(m-n). The unsigned-incidence Gram transfer from Q(S(G)) to A(L(S(G)))+2I has m-n+1 extra zero Gram eigenvalues (hence extra -2 adjacency eigenvalues) but removes the one zero eigenvalue of Q; this yields exactly (n,m-n,m), (n-1,0,n-1), (n-1,2,n-1), or (n,m-n+1,m-1) in the stated mutually exhaustive cases. Boundary K2/tree, odd C5, even C4, bipartite bicyclic K2,3 independently had numerical inertias (1,0,1),(5,0,5),(3,2,3),(5,2,5); a P4 had (3,0,3). The arbitrary-n result is the congruence and incidence argument, not these finite spectra.

## originality

PASS

Best-of-knowledge PASS for the complete three-parameter inertia of L(S(G)) over arbitrary irregular connected G. Earlier full-spectrum formulas already imply the regular-input special case; neither that case nor the saddle incidence identity is new. The fresh mathematical target is an unrestricted irregular-source classification and its nonpositive-signature boundary, with an uninspected plausible 2009 publisher full text explicitly noted.

## value

PASS

The clique-insertion/para-line operation is natural in spectral graph theory. Exact inertia and zero-eigenspace multiplicity collapse from a priori degree-dependent matrices to n,m and bipartiteness across all connected irregular graphs. It sharply identifies when the line-graph signature is zero, a structural theorem extending a known regular formula rather than a routine numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
