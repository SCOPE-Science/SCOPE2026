# Exact perfect Roman domination and optimal-labeling census for middle graphs of \(K_{2,n}\)

## Finding
Let \(H_n=M(K_{2,n})\), for each integer \(n\ge 1\). Its perfect Roman domination number is
\[
\gamma_{pR}(H_n)=
\begin{cases}
3,&n=1,\\
5,&n=2,\\
n+4,&n\ge3.
\end{cases}
\]
The number \(A_n\) of functions attaining this minimum is
\[
A_n=
\begin{cases}
2,&n=1,\\
4,&n=2,\\
22,&n=3,\\
(n+1)^2,&n\ge4.
\end{cases}
\]
All these functions are classified below. In particular, for \(n\ge4\), their exact number is \((n+1)^2\), not merely their minimum weight. The result settles the two-by-\(n\) case of the complete-bipartite question posed as Problem 2.1 in Kim's 2021 paper; it does not solve that question for arbitrary left-part size.

## Assumptions and scope
The underlying graph \(K_{2,n}\) has distinct row vertices \(a_1,a_2\), column vertices \(b_1,\ldots,b_n\), and edges \(a_ib_j\). In its middle graph \(H_n\), each original edge becomes an *edge-vertex* \(e_{ij}\). Two edge-vertices are adjacent if their original edges share an endpoint, and an original vertex is adjacent precisely to its incident edge-vertices. The graph has \(3n+2\) vertices. In particular, each set \(\{b_j,e_{1j},e_{2j}\}\) induces a triangle.

A *perfect Roman dominating function* is \(f:V(H_n)\to\{0,1,2\}\) such that every vertex with label zero has **exactly one** adjacent vertex with label two. Its weight is \(\omega(f)=\sum_v f(v)\), and \(\gamma_{pR}(H_n)\) is the minimum weight. We count functions on the labeled graph, with no identification under automorphisms.

To specify the large family of optimal functions, independently for each row \(i\in\{1,2\}\) choose exactly one *provider* from \(\{a_i,e_{i1},\ldots,e_{in}\}\) and label both chosen providers two. No column-original vertex is labeled two. Assign label zero to every remaining vertex having exactly one adjacent selected provider, and label one to every other remaining vertex. These are the **regular functions**, one for each of \((n+1)^2\) ordered provider choices, and each has weight \(n+4\).

There is also an **exceptional family** consisting, for any \(n\ge1\), of exactly \(2n\) functions. Choose a row \(i\) and a column \(j\); label \(e_{ij}\) two and assign, to all other vertices, zero if adjacent to precisely this one label-two vertex and one otherwise. The weight is \(2n+1\). At \(n=1,2\) only the exceptional functions are optimal; at \(n=3\) both families are optimal; at \(n\ge4\) only the regular functions are optimal. The two families are disjoint because the regular family has a provider in each row whereas the exceptional family has a provider in exactly one row.

## Proof
**1. Cheapest completion for a fixed two-set.** Fix the set \(T=f^{-1}(2)\). Any vertex outside \(T\) that has exactly one neighbor in \(T\) may be labeled zero without affecting the condition at any other vertex, which depends only on \(T\). Conversely, a vertex outside \(T\) without exactly one such neighbor cannot be zero and must be labeled one. Thus the unique minimum-weight completion of \(T\) labels all eligible vertices zero and all ineligible non-two vertices one. Every globally minimum function has this form.

**2. Local support identity and column-block lower bound.** Put \(r_i=|T\cap\{e_{i1},\ldots,e_{in}\}|\) and \(x_i=\mathbf1_{\{a_i\in T\}}\), and let \(p_i=r_i+x_i\). In column \(j\), let \(c_j=|T\cap\{e_{1j},e_{2j}\}|\) and \(y_j=\mathbf1_{\{b_j\in T\}}\). A non-two edge-vertex \(e_{ij}\) has exactly \(p_i+c_j+y_j\) selected neighbors (since \(e_{ij}\notin T\)). An original row vertex \(a_i\notin T\) has exactly \(r_i\) selected neighbors; an original column vertex \(b_j\notin T\) has exactly \(c_j\).

Partition the graph into the two row-original vertices and \(n\) column triangles \(B_j=\{b_j,e_{1j},e_{2j}\}\). Every column triangle has label sum at least one: if all three labels were zero, then \(b_j\) would have no label-two neighbor. Moreover, a triangle has label sum **one** only when its \(b_j\) has label one and both edge-vertices have label zero. The support identity then forces \(p_1=p_2=1\). Hence if \((p_1,p_2)\ne(1,1)\), all column triangles have weight at least two. The two row-original labels cannot both be zero: that would require \(r_1=r_2=1\), so \(p_1=p_2=1\). Consequently,
\[
(p_1,p_2)\ne(1,1)\quad\Longrightarrow\quad\omega(f)\ge2n+1.
\]

**3. The regular regime \(p_1=p_2=1\).** Each row then has exactly one selected two-provider, either its original row vertex or a single incident edge-vertex. A selected \(b_j\) can be lowered from two to one without violating the perfect condition: every nonselected \(e_{ij}\) in its column already has at least the single row provider and its additional adjacency to \(b_j\), so none is labeled zero; other zero vertices are not adjacent to \(b_j\). Thus no optimal function with \(p_1=p_2=1\) uses a column-original vertex labeled two.

Let \(k\in\{0,1,2\}\) be the number of row providers chosen among edge-vertices. The two row-original vertices contribute \(4-2k\) to the weight. In a column containing \(c\in\{0,1,2\}\) selected edge-vertices, the column-triangle weight is \(1+2c\): the column vertex is zero exactly when \(c=1\); for \(c=0\) it has label one and both edges label zero; for \(c=1\) the remaining edge must be one; for \(c=2\) both edges are two and the column vertex is one. Summing over columns yields \(n+2k\). Thus the total is always \(n+4\), and independent provider choices give exactly \((n+1)^2\) distinct regular functions.

**4. Equality in the nonregular bound.** Suppose \((p_1,p_2)\ne(1,1)\) and the weight equals \(2n+1\). The row-original labels must contribute exactly one, and every column triangle exactly two. Up to swapping rows, \(f(a_1)=1\) and \(f(a_2)=0\). Neither row-original vertex is labeled two, so \(p_1=r_1\), while \(f(a_2)=0\) forces \(r_2=p_2=1\). Since the configuration is nonregular, \(r_1\ne1\).

If \(r_1\ge2\), take a selected edge-vertex \(e_{1j}\) in the first row. The other edge-vertex \(e_{2j}\), if not selected, is adjacent to at least two label-two vertices: the unique second-row provider and \(e_{1j}\). It therefore cannot be labeled zero; the column triangle has weight at least three. If \(e_{2j}\) is selected, that triangle has weight at least four. Both contradict the assumed weight two. Therefore \(r_1=0\). The only selected edge-vertex is now \(e_{2j_*}\) for some unique \(j_*\). A selected original column vertex \(b_j\) in any different column would force that column's nonselected \(e_{2j}\) to have two selected neighbors (the row provider and \(b_j\)), making its triangle weight at least three; a selected \(b_{j_*}\) makes the exceptional column weight at least four. Hence there is no selected column vertex. The unique minimum completion of this singleton two-set has weight exactly \(2n+1\): in its column the triangle weighs two; in each other column the labels on \(b_j,e_{1j},e_{2j}\) are \(1,1,0\); and the row-original labels are \(1,0\). Conversely these \(2n\) choices all attain equality, so there are no other nonregular functions of weight \(2n+1\).

**5. Compare regimes and settle the small boundary.** The regular functions have weight \(n+4\), and every nonregular function has weight at least \(2n+1\). For \(n\ge4\), the latter exceeds the former. For \(n=3\) they coincide, giving \(16+6=22\) minima. For \(n=2\), the exceptional constructions attain five, below the regular value six, and the equality analysis gives exactly four minima. For \(n=1\), the graph has five vertices; any function with no two has weight five, and any function with at least two twos has weight at least four. A function with just one two has minimum weight \(5+1-\deg(v)\), which equals three exactly for the two edge-vertices (the only vertices of degree three). These are precisely the two exceptional functions. This proves both formulas and the complete classification for all \(n\ge1\).

## Verification
The accompanying `verify_middle_K2n.cpp` constructs the middle graph directly from the incidence definition and enumerates every possible set of label-two vertices for \(1\le n\le8\), computing the unique least-weight valid completion through exact neighborhood counts. In addition, for \(1\le n\le4\) it independently enumerates all ternary labelings and verifies the perfect Roman constraint vertex by vertex. Across the eight profiles, the two-support search checks 76,695,840 subsets; both approaches agree on every overlap. Compilation and recorded output are in `verify_middle_K2n_output.txt` and `VERIFICATION.md`. The proof above, not the finite computations, establishes the infinite-family theorem.

## Relationship to prior work
K. Kim, *Perfect Roman domination in middle graphs*, Discrete Mathematics Letters 7 (2021), 94–97, DOI 10.47443/dml.2021.0066, explicitly asks in Problem 2.1 for the exact perfect middle Roman domination number of a complete bipartite graph. The 2021 work determines other cases, notably paths, cycles and a family of Kneser graphs, but does not settle the two-by-\(n\) slice considered here. Its publicly verifiable arXiv submission was dated 3 June 2021 (arXiv:2106.01539). K. Kim, *Italian, 2-rainbow and Roman domination numbers in middle graphs*, RAIRO - Operations Research 58 (2024), 2045–2053, DOI 10.1051/ro/2024072, proves a scalar equality for ordinary Roman and related variants on middle graphs, not the **perfect** Roman function classification here. The graph operators and perfect-versus-ordinary domination conditions are materially different.

## Limitations
The result addresses \(K_{2,n}\), not arbitrary \(K_{m,n}\) with \(m>2\). It counts labeled functions rather than equivalence classes under graph automorphisms. The correctness proof is self-contained; computed checks cover only finite orders. Bibliographic novelty is assessed against accessible primary texts and indexed searches, not independently certified; obscure or later equivalent work may exist. No independent scientific audit has been performed.

## References
1. K. Kim, *Perfect Roman domination in middle graphs*, Discrete Mathematics Letters **7** (2021), 94–97, https://doi.org/10.47443/dml.2021.0066; preprint https://arxiv.org/abs/2106.01539 (publicly submitted 3 June 2021).
2. K. Kim, *Italian, 2-rainbow and Roman domination numbers in middle graphs*, RAIRO - Operations Research **58** (2024), 2045–2053, https://doi.org/10.1051/ro/2024072.
