# Shattered induced-edge traces: star forests, domination, and a sharp Poisson window

## Finding
For a finite simple graph \(G=(V,E)\), consider the range space on the **edges**
\[
\mathscr R(G)=\{E(G[U]):U\subseteq V\}.
\]
For \(G=K_n\), this is exactly the family of principal ideals of the Boolean lattice, restricted to its rank-two elements. A set \(F\subseteq E\) is shattered if every \(T\subseteq F\) equals \(F\cap E(G[U])\) for some \(U\subseteq V\). Then:

1. **Exact universal characterization.** \(F\) is shattered if and only if the graph \((V,F)\), including isolated vertices, is a star forest. Equivalently, \((V,F)\) contains neither a triangle nor a (not necessarily induced) path with three edges.
2. **Exact VC dimension and complexity.** For every finite simple \(G\),
   \[
   \operatorname{VCdim}(E,\mathscr R(G))=|V|-\gamma(G),
   \]
   where \(\gamma(G)\) is the domination number (isolates count as required members of every dominating set). Deciding whether this dimension is at least a given integer is NP-complete under standard polynomial reductions.
3. **Complete-graph shattering polynomial.** Let \(s_{n,k}\) be the number of shattered \(k\)-edge subsets of \(K_n\), and put \(S_n(t)=\sum_k s_{n,k}t^k\). Then
   \[
   \sum_{n\ge0}S_n(t)\frac{z^n}{n!}
     =\exp\!\left(ze^{zt}-\frac{z^2t}{2}\right).
   \]
   For \(n\ge1\) and \(0\le k\le n-1\), equivalently,
   \[
   s_{n,k}=\frac{n!}{(n-k)!}[u^k]\left(e^u-\frac u2\right)^{n-k},
   \]
   with \(s_{n,k}=0\) for \(k\ge n\) and \(s_{0,0}=1\).
4. **Sharp random threshold.** If \(F_n\) is uniform among the \(m=m(n)\) edges of \(K_n\) and \(m/n^{2/3}\to c\in[0,\infty)\), then
   \[
   \lim_{n\to\infty}\Pr(F_n\text{ is shattered})=e^{-4c^3}.
   \]
   If \(m/n^{2/3}\to\infty\), the probability tends to zero. In particular, the shattering property has a sharp scale \(n^{2/3}\), with a nontrivial Poisson limiting window.

## Assumptions and scope
Graphs are finite, undirected, loopless, and have no multiple edges. Ranges are edge sets **induced by arbitrary vertex subsets**, not graph neighborhoods, connected edge sets, or arbitrary edge subsets. A star forest is a disjoint union of graphs \(K_{1,r}\) for \(r\ge0\), permitting isolated vertices and single edges. The random model fixes the number of edges exactly, rather than choosing edges independently. The limiting assertion applies as \(n\to\infty\). The domination and structural statements include edgeless graphs and graphs with isolated vertices.

## Proof
**Obstructions and sufficiency.** Suppose \(F\) contains triangle edges \(ab,bc,ac\). The requested trace \(\{ab,bc\}\) necessarily chooses the three vertices and therefore also selects \(ac\), a contradiction. If \(F\) contains a three-edge path \(ab,bc,cd\) with distinct vertices, the trace \(\{ab,cd\}\) necessarily chooses all four endpoints and therefore selects \(bc\), again a contradiction. The argument works whether or not additional edges of \(G\) exist, since only intersection with \(F\) matters.

Conversely, a finite graph with no triangle and no three-edge path as an ordinary subgraph is a star forest. Indeed a cyclic component has either a triangle or a cycle of length at least four (and hence a three-edge path); an acyclic component that is not a star has diameter at least three. For a star forest \(F\), fix a center in each nontrivial star component, arbitrarily choosing one endpoint for a single-edge component. Given any \(T\subseteq F\), construct \(U\) by including the center of exactly those star components containing an edge of \(T\), together with the endpoints of their selected edges. Each edge of \(F\) belongs to the trace if and only if it belongs to \(T\). Edges outside \(F\) play no role. This proves the characterization.

**Domination correspondence.** Let \(F\subseteq E\) be shattered. Choose a center from every star component of \((V,F)\), including a representative from each isolated vertex. The chosen centers form a dominating set of \(G\). A forest with \(|F|\) edges on \(|V|\) vertices has exactly \(|V|-|F|\) components, so \(\gamma(G)\le|V|-|F|\). Conversely let \(D\subseteq V\) be a minimum dominating set, and for each \(v\notin D\) choose a neighbor \(d(v)\in D\). The edges \(vd(v)\) are distinct and form a star forest with \(|V|-\gamma(G)\) edges. Hence the bound is attained. A star forest of at least the requested size is a polynomially checkable certificate, establishing NP membership. NP-hardness follows by mapping the standard Dominating Set instance \((G,h)\) to the VC-dimension threshold \(|V|-h\); the equivalence is exact.

**Labeled enumeration.** For a connected star on \(r\) prescribed labeled vertices, there is one possibility when \(r=1\) or \(r=2\), and exactly \(r\) possibilities for \(r\ge3\) (choose its unique center). A star on \(r\) vertices contributes \(r-1\) edges. Its connected labeled bivariate exponential generating series is
\[
C(z,t)=z+\frac{z^2t}{2}+\sum_{r\ge3}\frac{r z^r t^{r-1}}{r!}
=ze^{zt}-\frac{z^2t}{2}.
\]
The labeled exponential formula for unordered sets of disjoint components gives the displayed exponential generating function. Expanding by the number \(j\) of components gives
\[
\exp\bigl(z(e^{zt}-zt/2)\bigr)
=\sum_{j\ge0}\frac{z^j}{j!}(e^{zt}-zt/2)^j.
\]
Every forest with \(n\) vertices and \(k\) edges has \(j=n-k\) components, so coefficient extraction proves the formula for \(s_{n,k}\).

**Poisson law in the fixed-edge model.** Write \(N=\binom n2\) and \(X_n\) for the number of copies of the three-edge path \(P_4\) whose entire edge set lies in \(F_n\). There are exactly \((n)_4/2\) unoriented copies. For \(m/n^{2/3}\to c\in(0,\infty)\),
\[
\mathbb E X_n=\frac{(n)_4}{2}\frac{(m)_3}{(N)_3}\longrightarrow4c^3.
\]
For every fixed positive integer \(r\), the contribution to \(\mathbb E (X_n)_r\) from ordered \(r\)-tuples of vertex-disjoint paths tends to \((4c^3)^r\). Every other tuple has a union with \(v\) vertices and \(e\) edges satisfying \(v<4e/3\): the three-edge path is strictly balanced, since every nonempty proper subgraph has edge/vertex ratio strictly below \(3/4\); adding an overlapping distinct copy increases the edge/vertex ratio of a union of disjoint copies, and later additions cannot undo the strict inequality. Each fixed overlap type contributes \(O(n^v(m/N)^e)=O(n^{v-4e/3})=o(1)\). There are finitely many overlap types for fixed \(r\). Thus all factorial moments converge to those of \(\mathrm{Poisson}(4c^3)\), and \(X_n\) converges to that law.

The expected number of triangles in \(F_n\) is
\[
\binom n3\frac{(m)_3}{(N)_3}=O(n^{-1})\to0.
\]
By the exact star-forest characterization, \(F_n\) is shattered precisely when it contains no \(P_4\) and no triangle. Therefore its probability tends to the zero-count probability \(e^{-4c^3}\). When \(c=0\), both forbidden-subgraph expectations tend to zero by the first-moment bound, and the limit is one. When \(m/n^{2/3}\to\infty\), couple the fixed-size edge samples by random ordering of all \(N\) edges. Shattering is downward closed under edge deletion, so for every fixed \(C>0\), the limiting upper bound is \(e^{-4C^3}\); let \(C\to\infty\). This proves the sharp threshold.

## Verification
The accompanying `verify.py` performs independent exhaustive shattering tests for all edge subsets of \(K_n\) for \(1\le n\le6\) (33,867 subsets). For each subset it enumerates all possible vertex-induced traces and compares them with a separate graph-components test for the star-forest condition. It verifies the rank polynomials using a separate labeled-component recurrence. It also exhaustively checks the domination identity across all 1,099 labeled graphs on at most five vertices, and tests 3,586 additional cases on deterministically sampled host graphs. Its final output is `VERIFY_OK` if every assertion holds. These finite checks do not prove the asymptotic Poisson theorem, whose proof is analytic and combinatorial.

## Relationship to prior work
Adler, Benediktsson, and Macpherson (first public arXiv version July 31, 2020) study VC dimension and density for **single-vertex open-neighborhood ranges** of Johnson and Hamming graphs, a different range family. Kranakis, Krizanc, Ruf, Urrutia, and Woeginger (1994) investigate several graph-induced vertex/edge VC dimensions, including **connected edge-set** ranges. Their edge-set requirement is not the present vertex-induced-edge requirement. Coudert, Csikós, Ducoffe, and Viennot (2024) study computation of VC dimension for graph **closed-neighborhood ranges**, again different. Our proof uses familiar star-forest, domination, labeled exponential-formula, and Poisson subgraph tools, none of which is separately asserted to be new. The proposed combined contribution is the exact identification of these tools for the vertex-induced-edge range system and its full labeled/random profile.

## Limitations
This is a theoretical statement about one specified range system. It is not a theorem about the usual neighborhood VC dimension. The probability law uses uniformly random edge subsets of a complete graph, not random host graphs or arbitrary nonuniform sampling. It establishes no effective numerical error bound in the finite-\(n\) Poisson approximation. Independent publication-priority review and independent mathematical validation have not been performed; prior equivalent results under alternative range-space or monomial terminology remain a risk.

## References
- B. G. Benediktsson, D. Macpherson, I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first publicly posted 2020-07-31, https://arxiv.org/abs/2007.16042.
- E. Kranakis, D. Krizanc, B. Ruf, J. Urrutia, G. J. Woeginger, *VC-Dimensions for Graphs*, SCS-TR-255, Carleton University (November 1994), https://carleton.ca/scs/wp-content/uploads/sites/260/TR255.pdf, particularly Sections 1, 2, and 7.
- D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588, first publicly posted 2024-05-13, https://arxiv.org/abs/2405.07588.
