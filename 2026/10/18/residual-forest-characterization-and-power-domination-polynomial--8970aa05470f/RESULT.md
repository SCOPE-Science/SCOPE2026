# Residual-forest characterization and power-domination polynomials for multipartite line graphs

## Finding

Let \(H=K_{a_1,\ldots,a_r}\) be a complete multipartite graph with \(r\ge2\) and positive integer part sizes \(a_1,\ldots,a_r\); put \(G=L(H)\). Each vertex of \(G\) represents an edge of \(H\). A subset \(S\subseteq E(H)=V(G)\) is power dominating in \(G\) if and only if \(S\ne\varnothing\) and the graph induced by the vertices of \(H\) incident with no edge of \(S\) is a forest. Equivalently, if \(t_i\) counts these unused vertices in part \(i\), then at most one \(t_i\) is positive, or exactly two are positive and at least one equals \(1\).

This yields the following explicit polynomial counting every power-dominating edge selection by cardinality. For vectors \(\mathbf b=(b_1,\ldots,b_r)\) of nonnegative integers define
\[
Q_{\mathbf b}(z)=
\sum_{0\le j_i\le b_i}
(-1)^{\sum_i j_i}
\left(\prod_{i=1}^r\binom{b_i}{j_i}\right)
(1+z)^{\sum_{1\le i<k\le r}(b_i-j_i)(b_k-j_k)}.
\]
Write \(\mathscr F(\mathbf t)\) for the stated forest condition and \(\mathbf b=\mathbf a-\mathbf t\). Then
\[
\boxed{
\mathcal P_{L(H)}(z)
=\sum_{\substack{0\le t_i\le a_i\\\mathscr F(\mathbf t)\\\sum_i b_i\ge2}}
\left(\prod_{i=1}^r\binom{a_i}{t_i}\right)
Q_{\mathbf b}(z).
}
\]
Here \(\mathcal P_G(z)=\sum_{S\text{ power dominating in }G}z^{|S|}\) excludes the empty sensor set. The formula applies even when some parts are singletons.

For the rook graphs \(K_m\square K_n=L(K_{m,n})\), where \(2\le m\le n\), it gives the **previously known** minimum \(\gamma_P=m-1\) and additionally the following exact number of minimum sensor sets:
\[
\boxed{
N_{m,n}=\begin{cases}
m n^{m-1},&m<n,\\
2m^m-m^2(m-1)!,&m=n.
\end{cases}}
\]
For triangular graphs \(T_n=L(K_n)\), \(n\ge3\), the minimum is \(\lceil(n-2)/2\rceil\). The number of its minimum sets is
\[
\boxed{
N_{2k}=\frac{(2k)!}{2^k(k-1)!}\quad(k\ge2),\qquad
N_{2k+1}=\frac{(2k+1)!}{2^k k!}
+\begin{cases}0,&k=1,\\\dfrac{(2k+1)!}{2^k(k-2)!},&k\ge2.\end{cases}}
\]
Both families are covered by the same structural theorem, rather than being independent special-purpose claims.

## Assumptions and scope

All graphs are finite, simple and undirected. Part sizes are positive, and there are at least two parts. For a graph \(G\), the power-domination process first observes the chosen set \(S\) together with all its neighbors, then repeatedly permits any observed vertex with exactly one unobserved neighbor to observe that neighbor. A power-dominating set observes all vertices at termination. In a line graph, the vertices are edges of the underlying graph and adjacency means incidence. Every generating polynomial counts labeled subsets of the fixed graph, including the full vertex set but excluding the empty set.

A *forest* is an acyclic graph, including the empty graph and edgeless graphs. Thus a vector with zero or one positive coordinate satisfies \(\mathscr F\). A complete bipartite graph with part sizes \(u,v>0\) is a forest precisely when \(\min(u,v)=1\). These conventions cover all boundary cases.

## Proof

**Step 1 (the initial observation).** Fix a nonempty edge set \(S\subseteq E(H)\). Let \(U\subseteq V(H)\) be the union of its endpoints and let \(W=V(H)\setminus U\). In \(G=L(H)\), the first observation step colors exactly those original edges having at least one endpoint in \(U\). Consequently, the unobserved vertices of \(G\) are exactly \(E(H[W])\). Since every selected original edge joins distinct parts, \(U\) meets at least two different parts. Hence each vertex \(v\in W\) has an original neighbor \(u\in U\): choose a represented part other than the part containing \(v\). The original edge \(uv\) is observed from the first step.

**Step 2 (cycles cannot be broken).** Suppose \(H[W]\) contains a cycle. Every edge of this cycle is initially unobserved. If a cycle edge were ever observed by forcing, choose the first such edge \(e\). Its forcing source \(f\) is a previously observed, distinct original edge incident with an endpoint \(v\) of \(e\). At that time both cycle edges incident to \(v\) are still unobserved, and both are neighbors of \(f\) in \(L(H)\). This contradicts the one-unobserved-neighbor rule. Therefore \(S\) does not power dominate.

**Step 3 (forest leaf stripping).** Conversely, assume \(H[W]\) is a forest. If any unobserved edge remains, its subgraph is a nonempty forest, so some vertex \(v\in W\) has exactly one incident unobserved original edge \(vw\). Select an original edge \(uv\) with \(u\in U\), which exists by Step 1. The line-graph vertex \(uv\) has been observed since the first step; every edge incident with \(u\) is observed, while \(vw\) is the only unobserved edge incident with \(v\). Thus \(uv\) forces \(vw\). Removing one unobserved edge retains the forest property; finite repetition observes every edge. This proves the equivalence.

**Step 4 (the part-size criterion).** The induced graph \(H[W]\) is complete multipartite with part sizes \(t_i=|W\cap A_i|\). Three positive coordinates give a triangle, and two coordinates each at least two give a four-cycle. If neither occurs, the graph is edgeless or is a star. Hence it is a forest precisely under \(\mathscr F(\mathbf t)\).

**Step 5 (coefficient enumeration).** Fix exact unused-vertex counts \(\mathbf t\), hence exact used-vertex counts \(\mathbf b=\mathbf a-\mathbf t\). The exact unused vertices can be chosen in \(\prod_i\binom{a_i}{t_i}\) ways. Once those vertices are fixed, an edge set has precisely the complementary used-vertex set \(U\) if and only if it uses only edges of the multipartite graph on \(U\), with none of the vertices of \(U\) isolated in the chosen edge set. Inclusion–exclusion on the \(\sum_i b_i\) vertices of \(U\) gives \(Q_{\mathbf b}(z)\): after requiring \(j_i\) specified vertices of part \(i\) to be isolated, there are \(\sum_{i<k}(b_i-j_i)(b_k-j_k)\) available cross-edges, yielding the factor \((1+z)\) to that exponent. The condition \(\sum_i b_i\ge2\) excludes the empty selection, and the forest condition is exactly the power-domination criterion. Every edge selection has unique unused vertices, so summation is disjoint and exact.

**Step 6 (rook-graph minima and multiplicities).** For \(H=K_{m,n}\), the induced graph on unused vertices is a forest exactly when at most one unused vertex lies on at least one of the sides. Thus an edge set is power dominating if and only if its selected edges meet at least \(m-1\) left-side vertices or at least \(n-1\) right-side vertices. If \(m\le n\), fewer than \(m-1\) selected edges can do neither; \(m-1\) edges in distinct left-side rows suffice. The minimum \(m-1\) agrees with Soh and Koh's earlier result. If \(m<n\), each minimum selection has one edge in each of \(m-1\) distinct left-side rows, giving \(m n^{m-1}\) possibilities. If \(m=n\), the minimum families meeting \(m-1\) left or \(m-1\) right vertices each have \(m^m\) members. Their intersection consists of partial permutation matrices of size \(m-1\), numbering \(m^2(m-1)!\). Inclusion–exclusion gives the stated exact count.

**Step 7 (triangular-graph minima and multiplicities).** For \(H=K_n\), every vertex is a singleton multipartite part; a power-dominating edge set covers at least \(n-2\) original vertices. Its cardinality is therefore at least \(\lceil(n-2)/2\rceil\), attained by near-perfect matchings. If \(n=2k\), a minimum set of \(k-1\) edges must be a matching covering exactly \(2k-2\) vertices; choosing the two uncovered vertices and pairing the others yields the even formula. If \(n=2k+1\), a minimum set of \(k\) edges covers either \(2k\) vertices (a matching) or \(2k-1\) vertices (one two-edge path and \(k-2\) disjoint edges). The matching count is \((2k+1)!/(2^k k!)\). For \(k\ge2\), the second type chooses two isolates, a three-vertex set and its middle vertex, and a matching of the remaining \(2k-4\) vertices, totaling \((2k+1)!/(2^k(k-2)!)\). No other edge-component profile reaches the required number of covered vertices. The case \(k=1\) has only the matching type.

## Verification

A standalone standard-library Python program, `verify_power_multipartite.py`, constructs each complete multipartite graph and its line graph independently. For each selected edge subset it simulates closed-neighborhood observation and subsequent vertex-by-vertex forcing without using the theorem. It separately calculates the exact set of unused original vertices and evaluates the forest criterion. Finally it computes every polynomial coefficient using the displayed inclusion–exclusion formula. Exhaustive agreement held for \(27\) multipartite profiles and \(255318\) edge subsets in total. Independent arithmetic checks reproduced the rook minimum-set counts in tested parameters and the triangular-graph minimum counts for \(3\le n\le8\).

To reproduce, run `python verify_power_multipartite.py`. Its output is included in `verification_output.txt`. The finite checks support the analysis but are not used as an infinite proof.

## Relationship to prior work

Brimkov, Patel, Suriyanarayana and Teich introduced the power-domination polynomial, proved general properties and evaluated other families (2018, arXiv:1805.10984). Soh and Koh had already determined the **power-domination number** of Cartesian products of two complete graphs (2014); their scalar minimum is not claimed as new here. Koh and Soh's subsequent study (2016) also recalls that established value. Girish, Asiri and Somasundaram (2026) study fault-tolerance transfer to line graphs, rather than all-set enumerators. The present result addresses a different question: the complete power-dominating-set family for line graphs of *arbitrary* complete multipartite graphs, its exact weight enumerator, and exact counts of minimum sets in two natural subfamilies.

## Limitations

The equivalence relies on the complete multipartite structure, specifically that every unused original vertex has an incident edge to the set of endpoints covered by the selected edges. No equivalence is asserted for arbitrary line graphs. The explicit multipartite formula is a finite inclusion–exclusion sum; no uniform polynomial-time complexity bound is claimed when the number of parts varies. The literature comparison does not establish worldwide priority, and independent scientific assessment has not been performed.

## References

1. B. Brimkov, R. Patel, V. Suriyanarayana and A. Teich, “Power domination polynomials of graphs,” arXiv:1805.10984, first posted 28 May 2018. https://arxiv.org/abs/1805.10984
2. K. W. Soh and K. M. Koh, “A note on power domination problem in diameter two graphs,” AKCE International Journal of Graphs and Combinatorics **11** (2014), 51–55, Theorem 3.3. https://doi.org/10.1080/09728600.2014.12088762
3. K. M. Koh and K. W. Soh, “Power domination of the Cartesian product of graphs,” AKCE International Journal of Graphs and Combinatorics **13** (2016), 22–30. https://doi.org/10.1016/j.akcej.2016.02.004
4. L. Girish, A. Asiri and K. Somasundaram, “Fault-tolerance amplification in line graphs: a framework for resilient PMU placement in power networks,” Scientific Reports **16** (2026), 25388. https://doi.org/10.1038/s41598-026-54352-z
