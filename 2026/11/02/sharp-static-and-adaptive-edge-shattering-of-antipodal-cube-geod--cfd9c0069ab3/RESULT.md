# Sharp static and adaptive edge shattering of antipodal cube geodesics

## Finding

For each integer \(d\ge1\), let \(Q_d\) be the graph on the subsets of \([d]=\{1,\ldots,d\}\), with an edge between sets differing in one element. Let \(\mathcal G_d\) consist of the edge sets of **all** shortest paths from \(\varnothing\) to \([d]\). The query domain is the undirected edge set \(E(Q_d)\), and a concept answers one precisely on the edges in its path. Equivalently, this is the incidence relation between the \(d!\) coordinate permutations and the oriented upward cube edges.

**Theorem.** For every \(d\ge1\),
\[
\operatorname{VCdim}(\mathcal G_d)=\left\lfloor\frac{2d}{3}\right\rfloor,
\qquad
\operatorname{Ldim}(\mathcal G_d)=d-1.
\]
The first strict separation occurs at \(d=4\), when these dimensions are \(2\) and \(3\). For all dimensions the difference is exactly
\[
\operatorname{Ldim}(\mathcal G_d)-\operatorname{VCdim}(\mathcal G_d)
=\left\lceil\frac d3\right\rceil-1.
\]
In particular, the gap is unbounded even though the two antipodal endpoints are fixed and every hypothesis is a shortest path of equal length.

**Complete static support characterization.** Let \(d\ge2\). An edge set \(S\subseteq E(Q_d)\) is VC-shattered if and only if there exists an antipodal shortest path \(P=(e_1,\ldots,e_d)\) containing \(S\), such that the index set \(T=\{i:e_i\in S\}\) contains neither \(\{1,2\}\) nor \(\{d-1,d\}\), and contains no three consecutive indices. This condition, if met on one containing path, is also met on every containing path. When \(d=1\), only the empty query support is shattered.

## Assumptions and scope

All graphs, paths and set systems are finite. The cube edges have unit length, and every shortest path from \(\varnothing\) to \([d]\) adds each coordinate exactly once. No assumption of unique shortest paths is made: the full set of \(d!\) paths is essential. The queries are **edge membership**, not vertex membership, coordinate comparisons or membership in an arbitrary graph path. Littlestone dimension is the largest depth of a complete, adaptively edge-labeled binary tree for which every answer sequence has a consistent path hypothesis. A depth-zero tree is allowed. The empty query support is shattered by the nonempty concept class.

## Proof

**1. Reduction of static supports to one canonical path.** Every shattered support has an all-positive witness \(P\), so \(S\subseteq E(P)\). Permuting coordinates acts transitively on all antipodal shortest paths and preserves the hypothesis class and edge-query answers. We may therefore take the canonical path obtained by adding coordinates \(1,2,\ldots,d\) in that order, and write \(e_i\) for its edge at step \(i\). Other paths are permutations \(\pi\in\mathfrak S_d\). Such a path contains \(e_i\) precisely if its first \(i-1\) entries form \(\{1,\ldots,i-1\}\) and its \(i\)-th entry equals \(i\).

**2. The three forbidden index patterns are necessary.** If a path contains \(e_2\), its first step must have been \(e_1\). Similarly, containing \(e_{d-1}\) forces the last step to be \(e_d\). Therefore a shattered support cannot contain both edges of either end pair. If a path contains \(e_i\) and \(e_{i+2}\), there is exactly one step between them, necessarily \(e_{i+1}\). Thus a support containing three consecutive canonical edges cannot realize the trace selecting the outer two and omitting the middle. These arguments apply to every containing witness path.

**3. These patterns are sufficient.** Suppose an index set \(T\) avoids the forbidden patterns. For an arbitrary requested positive trace \(U\subseteq T\), build a permutation with each \(e_i\) for \(i\in U\) as a fixed anchor. Between successive anchored steps \(a<b\), place the intervening coordinate labels \(a+1,\ldots,b-1\) in **decreasing** order. Also place the labels before the first anchor and after the last anchor in decreasing order. In the absence of anchors, reverse all \(d\) coordinates. This permutation includes each anchored edge. In any free block of length at least two, no internal canonical edge occurs: at every internal step the next label or the accumulated prefix differs from that of the canonical path. A free block of length zero has no internal edge; one of length one can force its unique canonical edge. Such a forced singleton can occur only immediately before an anchor at index \(2\), immediately after an anchor at index \(d-1\), or between anchors at indices \(i\) and \(i+2\). If the forced edge were also a query in \(T\setminus U\), this would produce one of the forbidden patterns. Hence all unselected queries are absent. Every trace is realized.

**4. The sharp VC count.** Since no valid \(T\) has three consecutive indices, a block of three indices contributes at most two. If \(d=3k\), partition \([d]\) into \(k\) triples to obtain \(|T|\le2k\). If \(d=3k+1\) with \(k\ge1\), partition into the initial pair \(\{1,2\}\), then \(k-1\) triples, then the final pair \(\{d-1,d\}\); the end-pair restrictions give \(|T|\le2k\). If \(d=3k+2\), partition into \(\{1,2\}\) and \(k\) triples, giving \(|T|\le2k+1\). Conversely, select all indices congruent to \(0\) or \(1\) modulo \(3\); when \(d\equiv1\pmod3\), omit the last index. The resulting set avoids all forbidden patterns and has size \(\lfloor2d/3\rfloor\). The case \(d=1\) is immediate because the sole edge belongs to the sole hypothesis.

**5. A disjoint-domain product lemma.** If two binary concept classes \(\mathcal A\) and \(\mathcal B\) have disjoint query domains, the class of independent pairs of hypotheses has Littlestone dimension at most \(\operatorname{Ldim}(\mathcal A)+\operatorname{Ldim}(\mathcal B)\). To prove this, induct on the sum of the two dimensions. The root of any nonconstant query tree belongs to one factor. At least one of its two answer restrictions decreases that factor's Littlestone dimension by at least one; otherwise that factor would itself shatter a tree one level deeper. The induction bound on that branch prevents a tree deeper than the stated sum. Empty factors and constant queries are harmless.

**6. The adaptive upper bound.** Induct on \(d\). For \(d=1\) the class has one hypothesis and dimension zero. Fix any queried cube edge \(e=(A,A\cup\{i\})\) with \(s=|A|\). Among paths answering one, the coordinates in \(A\) occur in arbitrary order first, coordinate \(i\) comes next, and the remaining \(d-s-1\) coordinates occur afterward in arbitrary order. Other nonconstant edge queries belong to one of these two disjoint subcubes. Thus the positive restriction is an independent product of \(\mathcal G_s\) and \(\mathcal G_{d-s-1}\), interpreting \(\mathcal G_0\) as a singleton class. By the product lemma and induction its Littlestone dimension is at most
\[
\max\{0,s-1\}+\max\{0,d-s-2\}\le d-2
\qquad(d\ge2).
\]
A complete depth-\(d\) tree would require a positive child of depth \(d-1\) at its root, impossible. Hence \(\operatorname{Ldim}(\mathcal G_d)\le d-1\).

**7. An explicit adaptive lower bound.** At a node with fixed permutation prefix \(A\) (in its specified order) and at least two unused coordinates, choose distinct unused coordinates \(a,b\). Query the cube edge from the set of used coordinates to that set with \(a\) added. On the positive child restrict to paths taking \(a\) next; on the negative child restrict to paths taking \(b\) next. Both restricted families contain all permutations of the remaining \(r-1\) coordinates, with no restrictions on subsequent edges. Repeat until one unused coordinate remains. Every answer sequence gives a distinct complete path witness, and all query answers on that witness are correct. This is a complete depth-\(d-1\) shattered tree, proving \(\operatorname{Ldim}(\mathcal G_d)\ge d-1\).

## Verification

Run `python3 verify_geodesic_edges.py` from this directory. This standalone Python 3 program uses only the standard library. Direct enumeration of all permutations and an independently written dynamic program over used-coordinate subsets agree on every canonical edge trace through dimension \(9\). The program checks every canonical support against the complete forbidden-pattern criterion through dimension \(12\), and explicitly constructs and replays adaptive depth-\(d-1\) trees through dimension \(11\), verifying every branch and the uniqueness of every terminal path witness. In the largest adaptive replay, there are \(1024\) distinct leaves. The final success marker is `ALL_ANTIPODAL_GEODESIC_EDGE_SHATTERING_CHECKS_PASS`.

The finite tests are independent sanity checks; they do not replace the proof in arbitrary dimension. The support classification is a statement about all edge supports, because any shattered support is contained in a witness path and every such path is coordinate-permutation equivalent to the canonical one.

## Relationship to prior work

Kranakis, Krizanc, Ruf, Urrutia and Woeginger (1994) introduce edge-VC dimensions for graph path families, and analyze unrestricted paths, connected edge sets and related graph parameters. Their Section 7 does not yield this fixed-endpoint, shortest-path cube classification. Abraham, Delling, Fiat, Goldberg and Werneck (2011), Theorem 2, prove a two-dimensional bound for **vertex sets of unique shortest paths**; the uniqueness assumption and the vertex query domain both differ from the present all-geodesics edge-incidence class. Ghazi, Golowich, Kumar and Manurangsi (first posted July 7, 2020) study general Littlestone-dimension closure bounds; their aggregation estimates do not determine this exact incidence class. Johnson and Wickes (first posted December 3, 2021) study permutation-pattern shattering by families of permutations; their query asks about relative orders of fixed label subsets, not whether a specified *prefix edge* is present in a permutation path.

Related public research records and previously available edge-path and permutation-comparison claims were checked by implications, including unrestricted Hamiltonian paths and Hamiltonian cycles of complete graphs. Those classes, graph families and query languages do not imply the present characterization. The comparison is evidence of noncoverage among inspected sources, not a proof of global publication priority.

## Limitations

The result concerns exactly the shortest paths between opposite vertices of an unweighted Boolean cube. It does not classify edge-query complexity of all shortest paths in arbitrary graphs, paths with other endpoints, nongeodesic paths, vertex-membership queries or weighted cubes. No independent mathematical audit or exhaustive historical-priority certification has been performed. The cited sources and searched public records may miss alternate terminology or later unindexed results.

## References

1. E. Kranakis, D. Krizanc, B. Ruf, J. Urrutia and G. J. Woeginger, *VC-Dimensions for Graphs*, Carleton University Technical Report TR-255, November 1994. https://carleton.ca/scs/wp-content/uploads/sites/260/TR255.pdf . Especially Sections 5 and 7.
2. I. Abraham, D. Delling, A. Fiat, A. V. Goldberg and R. F. Werneck, *VC-Dimension and Shortest Path Algorithms*, ICALP 2011, pp. 690–699. https://renatowerneck.wordpress.com/wp-content/uploads/2016/06/adfgw11-vc-dimension.pdf . Especially Section 3 and Theorem 2.
3. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight Closure Bounds for Littlestone and Threshold Dimensions*, arXiv:2007.03668, first public version July 7, 2020; ALT 2021. https://arxiv.org/abs/2007.03668 .
4. J. R. Johnson and B. Wickes, *Shattering k-sets with Permutations*, arXiv:2112.01946, first public version December 3, 2021. https://arxiv.org/abs/2112.01946 .
