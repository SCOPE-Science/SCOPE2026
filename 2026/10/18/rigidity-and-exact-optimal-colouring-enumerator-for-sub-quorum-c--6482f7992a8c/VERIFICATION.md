---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Direct proof reconstruction for every integer n>=1. For a colored a_i of color c, the colored closed neighborhood has a colored A-vertices plus delta_i at the matched b_i, with u_c+epsilon_i same-colored, hence exactly 2(u_c+epsilon_i)>=a+delta_i. Since epsilon_i<=delta_i<=1, each A-color class has at least ceil((a-1)/2) vertices; three distinct colors in A with a>=4 would require 3ceil((a-1)/2)>a, while a<=2 cannot contain three. Thus a three-color layer has exactly three distinct singletons, and the inequality forces each matched b_i to be colored identically. Then the other layer contains those exact three and no other colored vertices, so a four-color global coloring has at most two colors in each layer. Four colors imply two disjoint palettes of two per layer; epsilon_i=0 throughout. For class sizes u,v with u+v=a, 2u>=a+delta_i and 2v>=a+delta_j force u=v=a/2 and delta_i=delta_j=0 for all colored positions. The converse meets local majority with equality. Such four-color supports exist precisely for n>=4; direct graph arguments cover n=1 (edge: two colors), n=2 (four-cycle: at most two), n=3 (three singletons exist but no four). Assign ordered distinct names c1..c4, distribute a,a,b,b disjoint column sets and divide the four within-layer name swaps, giving (k)_4/4 times n!/((a!)^2(b!)^2(n-2a-2b)!). The exponential formula follows from e^z for blank columns and positive I0(2z)-1 terms for the two balanced pairs. A separate direct adjacency enumerator, independent of the repository verifier, enumerated 5,52,877,21147,678570 canonical partial assignments for n=1..5 and obtained maxima 2,2,3,4,4, with six and thirty unlabelled four-color optimizers at n=4,5; multiplying by 4! gives F_4(4)=144,F_5(4)=720. No finite experiment was used as a proof for all n.

## originality

PASS

Best-of-knowledge priority after statement-level checks. In R_n=K_2 square K_n=L(K_{2,n}), two cliques of size n have only a perfect matching between them. The inspected full accessible 2026 initiating article treats P_2 square P_n ladders, complete and complete multipartite hosts, coronas/joins, grids and cubes, not this two-clique matching join or its exact four-colour structural enumerator; its degree upper bound floor(2n^2/(2n-1)) does not force four for n>=5. The full 2013 foundational journal article presents sub-quorum as Problem 11 rather than solving this family; its earlier exact K_{m,n} statement is for total quorum colouring of the bipartite graph itself, not the partial colouring of its line graph. Semantic published-mathematics and web searches under line-graph, crown complement, co-bipartite, rook-graph and clique-prism aliases found results about different invariants, not implication coverage. The newest v4 preprint full text was not accessible, so the v1 whole-body comparison is not a v4 noncoverage assertion.

## value

PASS

The graph L(K_{2,n}) is a natural infinite dense regular family, and sub-quorum is a motivated partial defensive-alliance coloring invariant. The tight upper bound remains four as degree n and order 2n grow, whereas the applicable known general degree upper bound grows with n. Every extremal assignment is classified: disjoint even balanced supports with no doubly colored matching column. The labelled named-palette enumeration and Bessel exponential generating function describe all optimizers rather than a tiny isolated example or a routine restatement of the lower bound. This is a useful exact structural benchmark for future generalizations to K_m square K_n, co-bipartite matching joins or other partial coloring enumerators; those broader results are not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
