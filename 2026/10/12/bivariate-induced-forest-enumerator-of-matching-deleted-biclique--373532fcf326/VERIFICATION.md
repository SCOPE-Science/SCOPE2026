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

For a selected subset with a left vertices, b right vertices and d missing matching pairs, the induced graph has ab-d edges with d<=min(a,b,t). If a,b>=3, any selected 3-by-3 contains at least 9-3=6 edges on six vertices, hence a cycle; if (a,b) dominates (2,4) or (4,2), the 2-by-4 subgraph has at least 8-2=6 edges on six vertices, hence a cycle. The only forest cases left are subsets contained in one side; subsets with exactly one vertex of one side (a star possibly plus its unique nonadjacent matched vertex); (2,2) with precisely one missing matching pair yielding P4 or two missing pairs yielding 2K2; and (2,3)/(3,2) with exactly two missing matching pairs yielding P5. The one-small-side generating-function terms count unmatched/matched center choices and an isolate when the partner is selected; both directions double-count exactly (1,1) cross selections, whose adjacent/nonadjacent weights are subtracted. The one- and two-missing-edge 2-by-2 counts are t(p-1)(q-1)-t(t-1) and binom(t,2); the 2-by-3 count is binom(t,2)(p+q-4). This gives the asserted Phi for all p,q>=2 and 0<=t<=min(p,q). P4/P5 and maximum-induced-forest/feedback vertex consequences follow by reading coefficients, with crown special values (6,32,2n for n=3,4,n>=5). Independent new standard-library DFS enumeration for 163 parameter triples and 413040 vertex subsets confirmed all bivariate coefficients and both path counts, plus crown maxima n=3..9. A bounded check is corroboration only; the general theorem comes from exhaustive mathematical category proof.

## originality

PASS

Best-of-knowledge PASS for the FULL three-parameter order-by-component induced-forest enumerator, not for its individual P4 consequence. Two earlier published exact results for precisely K_{p,q} minus a matching already imply the P4 coefficient t((p-1)(q-1)-t+1): respectively the number of disjoint maximal-clique/maximal-stable-set pairs and the number of length-three geodesics between missing matched pairs. They do not determine the entire forest polynomial, the P5 enumeration or the component-stratified all-size counts. The 2022 acyclic polynomial covers the univariate INVARIANT in general, but did not provide this family's matching deletion formula; the 2011 Q(G;x,y) counts ALL induced subgraphs, including cycles, rather than their forest-only subset, and treats K_{p,q} without deletions in Corollary 19. Related graph-wide extremal/induced-arboricity papers do not imply the family-specific coefficient theorem. Search failure is not novelty proof; older obscure tables/derivations remain possible.

## value

PASS

The complete vertex-induced forest polynomial is a natural refinement of the acyclic polynomial and feedback-vertex-set number: for one basic three-parameter graph family it gives every order-by-component stratum and minimum feedback-set solution multiplicity, rather than an arbitrary finite slice. Matching deletion changes the unperturbed biclique star-only structure by exactly P4, 2K2 and P5 exceptions, a motivated finite structural classification. Although the P4 number by itself is known, neither that number nor a generic graph-polynomial definition determines the full bivariate component-resolved distribution; counting all disjoint forests is independently useful. The balanced P4-versus-P5 equality criterion and crown maximum-forest counts are exact consequences of that enumeration and not offered as independent unrelated achievements. No general arbitrary-deletion complexity result or a substantially more general graph family is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
