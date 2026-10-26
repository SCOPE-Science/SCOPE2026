# A perfect-matching sieve from total domination of middle graphs

## Finding
Let \(G=(V,E)\) be any finite simple graph with \(|V|\ge 1\). The **middle graph** \(M(G)\) has vertices \(V\sqcup\{\widehat e:e\in E\}\); an original vertex is adjacent to precisely its incident edge-vertices, and two distinct edge-vertices are adjacent when their original edges share an endpoint. A set is *total dominating* when every vertex, including each selected vertex, has a selected neighbor.

For commuting indeterminates \(\mathbf y=(y_e:e\in E)\), let
\[
\mathcal Z_G(\mathbf y)=\sum_{S\subseteq V(M(G))\,\text{total dominating}}(-1)^{|S|}\prod_{\widehat e\in S}y_e.
\]
Then the following **multivariate identity** holds for every \(G\), without assumptions of connectivity or existence of a perfect matching:
\[
\boxed{\mathcal Z_G(\mathbf y)=\sum_{P\subseteq E\,\text{a perfect matching}}\ \prod_{e\in P}y_e.}
\]
In particular, if \(D_t(H;z)=\sum_{S\subseteq V(H)\,\text{total dominating}}z^{|S|}\) and \(\operatorname{pm}(G)\) is the number of perfect matchings of \(G\), then
\[
\boxed{D_t(M(G);-1)=\operatorname{pm}(G).}
\]
Consequently the number of even-cardinality total dominating sets of \(M(G)\) minus the number of odd-cardinality ones is nonnegative, and it is positive precisely when \(G\) has a perfect matching.

An exact ordinary polynomial expansion also follows. For any edge cover \(C\subseteq E\) (meaning every original vertex is incident with an edge in \(C\)), let \(i(C)\) be the number of edges isolated in the subgraph with edge set \(C\), equivalently the number of \(uv\in C\) for which both endpoints have \(C\)-degree one. If \(n=|V|\), then
\[
\boxed{D_t(M(G);z)=\sum_{C\,\text{an edge cover}}z^{|C|}(1+z)^{n-2i(C)}(2z+z^2)^{i(C)}.}
\]
For graphs with isolated vertices both sides of the last formula are zero (the edge-cover sum is empty). The usual \(0\)-vertex convention is not needed.

## Assumptions and scope
Graphs are finite, undirected, loopless, and have no parallel edges. Original vertices and edge-vertices in \(M(G)\) are distinguished types even when they carry the same labels. The empty original graph is excluded, so the empty-graph convention for total-domination polynomials does not intervene. No connectedness, minimum-degree, bipartiteness, or planarity is required. A perfect matching contains pairwise disjoint original edges incident with every original vertex exactly once. All polynomial identities are formal identities with integer coefficients.

## Proof
**1. Canonical edge projection.** Write any proposed total dominating set uniquely as \(S=T\sqcup\{\widehat e:e\in C\}\), with \(T\subseteq V\) and \(C\subseteq E\). Every original vertex has only incident edge-vertices as neighbors, so \(S\) totally dominates the original vertices **if and only if** \(C\) is an edge cover.

Assume \(C\) is an edge cover. Any unselected edge-vertex \(\widehat e\), with \(e=uv\notin C\), is adjacent to some selected edge-vertex: choose an edge of \(C\) incident with \(u\). That selected edge is not \(e\), and the two edge-vertices are adjacent. If \(e\in C\) has an incident *different* edge \(f\in C\), then \(\widehat e\) is dominated by \(\widehat f\). The remaining selected edge-vertices are exactly those \(\widehat e\) for which \(e=uv\) is isolated in \((V,C)\); they are dominated precisely when \(u\in T\) or \(v\in T\). Therefore
\[
S\text{ is total dominating}\iff C\text{ is an edge cover and }T\cap\{u,v\}\neq\varnothing\text{ for each isolated }uv\in C.
\]
The isolated edges of \(C\) are pairwise vertex-disjoint, so the endpoint pairs in these conditions are disjoint.

**2. Ordinary enumerator.** For fixed edge cover \(C\), each isolated edge requires a nonempty subset of its two endpoints, with size enumerator \(2z+z^2\). All other \(n-2i(C)\) original vertices can independently be selected or omitted, giving \((1+z)^{n-2i(C)}\). The selected edge-vertices contribute \(z^{|C|}\). Summing over the unique edge projections \(C\) proves the displayed ordinary polynomial identity, without overcounting.

**3. Signed multivariate sieve.** In the multivariate alternating sum, fixing \(C\) supplies a factor \((-1)^{|C|}\prod_{e\in C}y_e\). Summing \((-1)^{|T|}\) over admissible \(T\) gives zero whenever at least one of the \(n-2i(C)\) unrestricted original vertices exists, because toggling that vertex pairs the contributions with opposite signs. If no unrestricted vertex exists, the original vertex set is partitioned into the \(i(C)\) isolated selected edges. Since these edges cover every vertex and have \(C\)-degree one at both endpoints, \(C\) consists *exactly* of those edges and is a perfect matching.

For each such matching edge, the signed sum of nonempty subsets of its endpoint pair is \((-1)+(-1)+(+1)=-1\). Since then \(|C|=i(C)\), the factor \((-1)^{|C|}\) cancels the \((-1)^{i(C)}\) from these endpoint choices. Thus the coefficient of \(\prod_{e\in C}y_e\) is one for every perfect matching \(C\) and zero for every other edge set. This proves the multivariate identity.

**4. Specialization.** Substituting \(y_e=1\) for all original edges gives \(\mathcal Z_G(\mathbf 1)=D_t(M(G);-1)\). The right side becomes the number of perfect matchings. When \(G\) has an isolated vertex, \(M(G)\) has that isolated vertex as well, so both sides are zero. All boundary cases in the stated domain are covered.

## Verification
The accompanying standard-library script `verify.py` constructs middle graphs and enumerates total dominating sets **directly from their adjacency relation**. It independently constructs the edge-cover polynomial, enumerates perfect matchings, and checks all monomial coefficients of the multivariate signed identity. The recorded results in `verification_output.txt` cover 725 labeled connected-or-disconnected test graphs and 1,246,184 candidate subsets of middle-graph vertices, as well as an isolated-vertex boundary test. The script includes examples \(K_2\), \(P_3\), and \(K_3\). Run with `python verify.py` in a directory containing the two files. Finite checks support reproduction but are not used as proof of the universally quantified identities.

## Relationship to prior work
Kazemnejad, Pahlavsay, Palezzato, and Torielli (2022) study the **minimum number** of selected vertices needed for total domination of \(M(G)\), including bounds and several families. Their Lemma 2.1 replaces selected original vertices by edge-vertices for minimum-size purposes; it does not count *all* total dominating sets or establish the signed perfect-matching identity. Our canonical edge-cover decomposition counts these distinct sets rather than replacing them.

Hu, Shan, Wang, Wang, and Wei (2016) develop general total-domination-polynomial recurrences and study special values at \(-1\), particularly for forests. Those general reductions do not state the matching-parameter identity for middle graphs; for instance, a middle graph of a graph with adjacent edges contains a triangle and need not be a forest. Latheesh Kumar (2025) identifies the ordinary total-domination polynomial with an open-neighborhood-hypergraph transversal polynomial and derives formulas for three-arm trees. That general formulation does not state the specialized multivariate cancellation for middle graphs or identify perfect matchings as the surviving monomials.

The contribution assessed here is the multivariate sieve relating the entire signed family to the perfect-matching polynomial. No claim is made that computing either side is efficient for unrestricted graphs.

## Limitations
The result is an exact formal identity, not an assertion that the perfect-matching count can be computed in polynomial time on arbitrary graphs. The ordinary edge-cover expansion may contain exponentially many terms. Published equivalents outside the inspected texts or in unindexed literature remain possible. The results have not received independent mathematical review.

## References
1. F. Kazemnejad, B. Pahlavsay, E. Palezzato, and M. Torielli, *Total domination number of middle graphs*, Electronic Journal of Graph Theory and Applications **10** (2022), 275–288. DOI: 10.5614/ejgta.2022.10.1.19. Public preprint: arXiv:2204.07040, submitted 2022-04-13.
2. J. Hu, E. Shan, S. Wang, C. Wang, and B. Wei, *Total domination polynomials of graphs*, arXiv:1607.00400, submitted 2016-07-01.
3. L. Kumar A. R., *On a New Approach to Total Domination Polynomials*, Asian Research Journal of Mathematics **21** (2025), 11–20, DOI: 10.9734/arjom/2025/v21i7954.
