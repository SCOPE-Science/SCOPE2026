# Review of Super and connected-super domination of crown graphs

## Correctness
PASS. For a super dominating set \(S\), an omitted \(a_i\) must be witnessed by some selected \(b_j\) whose omitted-neighborhood intersection is exactly \(\{a_i\}\). Since \(b_j\) misses only \(a_j\) on the opposite side, there can be at most two omitted \(A\)-vertices; symmetrically there can be at most two omitted \(B\)-vertices. This gives the lower bound \(2n-4\). Equality forces two omissions on each side, and the witness condition forces the two index pairs to be disjoint. Those disjoint pairs also give explicit witnesses, proving attainability and uniqueness of the structural form. The induced selected subgraph is \(K_{2,2}\) at \(n=4\) and is connected by a short alternating path argument for \(n\ge5\). Exhaustive definition-level computation for \(3\le n\le7\) matches the theorem and isolates the \(n=3\) boundary.

## Originality
PASS. The closest primary super-domination source gives \(\gamma_{\mathrm{sp}}(K_{n,n})=2n-2\), not the perfect-matching-deleted crown. The 2018 connected-super paper treats common graphs and standard graph products but targeted full-text searches found no crown or complete-bipartite specialization. The 2022/2024 graph-classes-and-enumeration paper restates the complete-bipartite value and studies neighborhood coronas, clique gluings, Hajós sums, and selected enumeration families; targeted inspection found no crown or perfect-matching-deletion theorem. Indexed literature searches under crown, matching-deletion, ordinary super, and connected-super aliases found no equivalent statement. Complete-multipartite formulas are inapplicable because a crown graph is not complete multipartite for \(n\ge3\).

## Value
PASS. Crown graphs are the canonical one-factor deletion of balanced complete bipartite graphs. The theorem measures a sharp structural change under that minimal symmetric deletion: the super domination number drops by exactly two, while the connected-super constraint costs nothing at the optimum. The exact disjoint-pair classification and count describe every optimum rather than only a scalar parameter value, giving a natural benchmark for edge-deletion sensitivity in super domination.

Self-review: passed. Independent audit: not yet performed.
