# Review — Sharp dissociation-independence gap in connected bipartite graphs

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The order-only bound is the sum of two independently necessary inequalities: `diss(G)<=n-1` for connected graphs of order at least three and `alpha(G)>=ceil(n/2)` for bipartite graphs. Equality therefore forces both inequalities to be tight.

The equality classification was checked adversarially. If a maximum dissociation set omits one vertex `x`, then every component of `G-x` is `K_1` or `K_2`. Connectivity forces an edge from `x` to every component, while bipartiteness forbids two such edges into a `K_2` component. This forces a subdivided-star structure and excludes additional cycles or chords. The formula `alpha(H(q,r))=q+max(r,1)` then gives the stated even/odd classifications.

The dual 3-path-cover formulation follows exactly from complementing the vertex set. Finite checks agree for all connected bipartite Graph Atlas graphs through order 7 and all nonisomorphic trees through order 17.

## Originality

**PASS, to the best of our knowledge.** The directly relevant 2023 paper by Bock, Pardey, Penso, and Rautenbach was inspected in accessible full text. It studies the same pair of parameters and gives degree-sensitive results for bipartite graphs, but the inspected statements and proofs do not contain this fixed-order gap theorem or its equality classification. The 2013 vertex-k-path-cover paper was inspected for the dual formulation, and searches were repeated using dissociation, independence, vertex-cover, and 3-path-cover terminology.

No equivalent theorem was found in the checked sources or in the current SCOPE archive. The main residual originality risk is an unindexed or differently phrased result, especially one stated only in 3-path-cover language.

## Value

**PASS.** Although the numerical upper bound is obtained from two simple inequalities, equality is rigid: among all connected bipartite graphs, every extremal graph is forced to be a tree, and the extremal isomorphism classes are completely determined for every order. The exact defect decomposition separates the two sources of non-extremality, and the dual statement gives the exact largest possible saving when replacing vertex cover by 3-path vertex cover in this graph class.

## Scientific limitations

- Originality is to the best of our knowledge, not an exhaustive proof of absence from all literature.
- Equivalent statements under 3-path vertex-cover terminology remain the most plausible source of hidden prior coverage.
- The theorem is restricted to finite simple connected bipartite graphs.
