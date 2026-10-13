# Independent-domination polynomial and induced matchings of once-subdivided graphs

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph, including a disconnected or edgeless graph, and write \(n=|V|\). Its *full one-subdivision* \(S(G)\) replaces every edge \(e=uv\) with the two-edge path \(u z_e v\), using one distinct new vertex \(z_e\) per edge. An independent dominating set is an independent vertex set meeting the closed neighborhood of every vertex; equivalently, it is a maximal independent set. Let \(\mathcal D_i(H;x)=\sum_{D}x^{|D|}\), summed over all independent dominating sets of \(H\).

**Theorem (all-set classification and enumerator).** For each \(W\subseteq V\), set
\[
D_W=(V\setminus W)\cup\{z_e:e\in E(G[W])\}.
\]
Then \(W\mapsto D_W\) is a bijection between subsets \(W\) for which \(W=\varnothing\) or \(G[W]\) has minimum degree at least one, and independent dominating sets of \(S(G)\). Consequently,
\[
\boxed{\mathcal D_i(S(G);x)=\sum_{\substack{W\subseteq V\\W=\varnothing\ \mathrm{or}\ \delta(G[W])\ge1}}x^{n-|W|+|E(G[W])|}.}
\]
Here the minimum-degree condition applies only to nonempty induced subgraphs, and empty vertex and edge sets are permitted.

Let \(\operatorname{im}(G)\) be the maximum number of pairwise vertex-disjoint edges whose endpoints induce precisely those edges (the *induced matching number*). The enumerator has the exact lower support endpoint
\[
\boxed{i(S(G))=n-\operatorname{im}(G).}
\]
Moreover, the coefficient of its minimum-degree monomial counts exactly those \(W\) for which \(G[W]\) is a disjoint union of \(\operatorname{im}(G)\) nontrivial trees. In the edgeless case this means the unique empty choice.

**Algorithmic consequence for forests.** If \(F\) is any forest, a three-state recursion on each rooted component computes every coefficient of \(\mathcal D_i(S(F);x)\) using polynomially many integer-arithmetic operations; the explicit recursion appears in the proof below.

## Assumptions and scope

All graphs are finite, simple and undirected; there is no connectivity or minimum-degree hypothesis on \(G\). Every base edge is subdivided **exactly once**, and the inserted vertices are pairwise nonadjacent. The empty graph has polynomial one under the standard empty-set convention. Cardinalities count selected vertices of \(S(G)\), which has \(n+|E|\) vertices. The independent-domination polynomial is not the ordinary independence polynomial and is not the graph's ordinary domination polynomial. The induced matching number allows the empty matching.

## Proof

**1. Forced vertex choices.** Fix an independent dominating set \(D\) of \(S(G)\), put \(U=D\cap V\), and let \(W=V\setminus U\). A subdivision vertex \(z_{uv}\) has precisely two neighbors, the original endpoints \(u\) and \(v\). If either endpoint lies in \(U\), independence excludes \(z_{uv}\) from \(D\). If neither endpoint lies in \(U\), then the subdivision vertex has no selected neighbor, so domination forces \(z_{uv}\in D\). Thus its membership is fixed by \(U\):
\[
D=U\cup\{z_{uv}:u,v\in W,\ uv\in E\}=D_W.
\]
The resulting set is always independent, since original vertices have no edges between them in \(S(G)\), and an included subdivision vertex has no selected endpoint. Every subdivision vertex is dominated, either by itself or by an included endpoint. An original vertex in \(U\) is dominated by itself; an original vertex \(w\in W\) is dominated if and only if some inserted vertex \(z_{wv}\in D_W\) exists, which is equivalent to \(w\) having a neighbor inside \(W\) in \(G\). This proves both necessity and sufficiency of the stated no-isolated-vertex criterion and the bijection. Its cardinality is \(n-|W|+|E(G[W])|\), proving the polynomial identity.

**2. Exact minimum and minimum-set multiplicity.** For any admissible \(W\ne\varnothing\), let \(t(W)\) be the number of tree components of \(G[W]\); every such component has at least one edge. Let its other components be connected cyclic graphs. A tree component contributes exactly one to \(|W|-|E(G[W])|\), while a cyclic connected component contributes at most zero. Hence
\[
|W|-|E(G[W])|\le t(W).
\]
Choose one edge from every tree component. There is no edge in \(G\) between endpoints belonging to distinct components of the *induced* graph \(G[W]\), so these chosen edges form an induced matching of \(G\). Thus \(t(W)\le\operatorname{im}(G)\). For \(W=\varnothing\) the same bound is immediate. We have proved
\[
|D_W|=n-(|W|-|E(G[W])|)\ge n-\operatorname{im}(G).
\]
Conversely, take an induced matching of cardinality \(\operatorname{im}(G)\) and let \(W\) be its set of endpoints. By definition, \(G[W]\) consists of exactly those disjoint matching edges, so \(|W|=2\operatorname{im}(G)\) and \(|E(G[W])|=\operatorname{im}(G)\). The corresponding set has cardinality \(n-\operatorname{im}(G)\), proving equality. Equality in the two preceding inequalities requires exactly \(\operatorname{im}(G)\) tree components and no cyclic components. This establishes the minimum-set coefficient characterization, including the empty case.

**3. Complete forest recursion.** Suppose \(F\) is a forest. For an admissible choice \(W\), its induced graph is a forest; if \(c(F[W])\) is its number of connected components, then \(|E(F[W])|=|W|-c(F[W])\). Therefore
\[
\mathcal D_i(S(F);x)=x^n\sum_{\substack{W\subseteq V(F)\\W=\varnothing\ \mathrm{or}\ \delta(F[W])\ge1}}x^{-c(F[W])}.
\]
Root each component of \(F\) arbitrarily. For a rooted subtree with root \(v\), give each included vertex the formal weight \(x^{-1}\) and each edge whose two endpoints are included the weight \(x\). Define three Laurent-polynomial states: \(A_v\), in which \(v\) is excluded and every included descendant has an included neighbor within its subtree; \(B_v\), in which \(v\) is included and has an included child and all other included descendants are supported; and \(C_v\), in which \(v\) is included, has no included child, and would need an included parent outside its subtree. Writing \(\mathrm{ch}(v)\) for its children, direct partition by the children's states gives
\[
\begin{aligned}
A_v&=\prod_{u\in\mathrm{ch}(v)}(A_u+B_u),\\
B_v&=x^{-1}\left[\prod_{u\in\mathrm{ch}(v)}\bigl(A_u+x(B_u+C_u)\bigr)-\prod_{u\in\mathrm{ch}(v)}A_u\right],\\
C_v&=x^{-1}\prod_{u\in\mathrm{ch}(v)}A_u.
\end{aligned}
\]
An empty product equals one, so at leaves \(A_v=1\), \(B_v=0\), \(C_v=x^{-1}\). When an included child joins an included parent, the factor \(x\) is precisely the weight of their selected connecting edge. The subtraction in \(B_v\) excludes the case with no included child. At the root \(r\) of a component, \(C_r\) is inadmissible because there is no parent. Thus the desired polynomial is
\[
\boxed{\mathcal D_i(S(F);x)=x^n\prod_{\text{component roots }r}(A_r+B_r).}
\]
The three states partition every admissible choice and preserve its exact weight, so the recursion is exact. Each state is a Laurent polynomial with integer coefficients and degree range bounded linearly by the subtree size. Ordinary polynomial convolutions over the \(n\) vertices yield a polynomial-time coefficient algorithm, for instance within \(O(n^3)\) integer-arithmetic operations using straightforward array multiplication. The final shifted product has nonnegative exponents.

## Verification

The supplied standalone script `CHECK.py` independently enumerates all subsets of the one-subdivided graph, checks independence and domination directly, and compares the exact coefficients against the induced-subgraph formula. It also computes induced matchings by an unrelated edge-subset enumerator, and checks the three-state forest recursion against subset enumeration. The captured output is `CHECK_OUTPUT.txt`; run `python CHECK.py` with Python 3.10 or newer (NetworkX supplies additional nonisomorphic-tree and random-forest tests).

The direct comparison passed on all \(1{,}100\) labeled graphs of order at most five (\(1{,}901{,}463\) tested subsets), plus \(119\) random base graphs of orders six and seven (\(1{,}328{,}512\) tested subsets). The forest recurrence agreed on \(201\) nonisomorphic trees of orders one through ten and \(640\) random forests. The script separately checked the three-rung ladder. These finite checks support the proof but do not replace its unbounded argument.

For the ladder \(L_3=P_3\square K_2\), direct enumeration gives
\[
\mathcal D_i(S(L_3);x)=x^4+27x^5+7x^6+x^7.
\]
An explicit independent dominating set of cardinality four comprises the two middle-column original vertices and the two subdivision vertices replacing the first and last rungs. This check is material to the literature comparison below.

## Relationship to prior work

The independent-domination polynomial and general identities for it precede this work; see Dod and Jahari–Alikhani. Their general inclusion–exclusion or graph-product formulas can in principle be evaluated for a subdivision graph, but they do not give the present induced-subgraph no-isolate bijection, the induced-matching optimization identity, or the explicit three-state forest formula. Tsukuda establishes topological relations between independence complexes of incidence graphs and Alexander duals; a homotopy equivalence alone does not count maximal faces by cardinality. Babikir, Dettlaff, Henning and Lemańska study the *minimum number of edges to subdivide* to change an independent-domination number, a different input/output invariant.

Stella Arputha Mary and Santhanamariammal investigate independent-domination numbers for several fully subdivided graph families. Their Theorem 3.4 reports value \(2\lceil(3k-2)/3\rceil\) for the full subdivision of a \(k\)-rung ladder, which gives six for \(k=3\). For the same explicitly defined ladder, the present four-vertex certificate and an exhaustive \(8{,}192\)-subset check instead give four. Thus that specific reported formula cannot establish the claim here. This records a concrete, testable discrepancy, not a general assessment of the earlier work.

## Limitations

The theorem assumes exactly one inserted vertex per edge; it does not claim an analogous identity for selective subdivision, repeated subdivision or multigraphs. The forest recursion does not assert polynomial-time computation for arbitrary base graphs. The literature comparison cannot exclude all unindexed or implicit earlier derivations. The supplied computer tests are finite and do not independently certify the universal proof. No independent scientific audit has been performed.

## References

1. S. Jahari and S. Alikhani, “On the independent domination polynomial of a graph,” arXiv:1808.07369, first posted 21 August 2018. https://arxiv.org/abs/1808.07369
2. M. Dod, “The Independent Domination Polynomial,” arXiv:1602.08250 (2016). https://arxiv.org/abs/1602.08250
3. A. Babikir, M. Dettlaff, M. A. Henning and M. Lemańska, “Independent Domination Subdivision in Graphs,” *Graphs and Combinatorics* 37 (2021), 691–709. https://doi.org/10.1007/s00373-020-02269-3
4. S. Tsukuda, “Independence complexes and incidence graphs,” *Contributions to Discrete Mathematics* 12 (2017), 28–46. https://doi.org/10.55016/ojs/cdm.v12i1.62277
5. V. L. Stella Arputha Mary and L. Santhanamariammal, “Independent Domination in Some Subdivision Graphs,” *Journal of Emerging Technologies and Innovative Research* 6(4) (2019), 129–137. https://www.jetir.org/papers/JETIR1904I23.pdf
