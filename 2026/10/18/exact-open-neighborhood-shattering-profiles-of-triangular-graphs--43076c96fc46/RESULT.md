# Exact open-neighborhood shattering profiles of triangular graphs

## Finding
For an integer \(n\ge2\), let \(T_n=L(K_n)=J(n,2)\) have as vertices the two-element subsets of \([n]\); distinct vertices are adjacent when the corresponding edges intersect. Let \(\mathcal N_n=\{N_{T_n}(e):e\in E(K_n)\}\) be the family of **open** neighborhoods. Define \(s_j(n)\) to be the number of \(j\)-element subsets \(A\subseteq E(K_n)\) shattered by \(\mathcal N_n\): each of the \(2^j\) subsets of \(A\) must equal \(N_{T_n}(e)\cap A\) for some edge \(e\) of \(K_n\). Write \(\binom ab=0\) when \(b>a\ge0\).

**Theorem (complete shattering polynomial).** For every \(n\ge2\), the polynomial \(S_n(z)=\sum_j s_j(n)z^j\) has degree at most four and coefficients
\[
\begin{aligned}
s_0(n)&=1,\\
s_1(n)&=\mathbf1_{n\ge3}\binom n2,\\
s_2(n)&=\mathbf1_{n\ge5}\left(3\binom n3+3\binom n4\right),\\
s_3(n)&=\mathbf1_{n\ge6}\left(16\binom n4+30\binom n5\right),\\
s_4(n)&=\mathbf1_{n\ge7}\,125\binom n5+\mathbf1_{n\ge8}\,90\binom n6,\\
s_j(n)&=0\qquad(j\ge5).
\end{aligned}
\]
The \(s_2\) coefficient equals \(\binom{\binom n2}{2}\) whenever \(n\ge5\): **every pair of vertices is shattered**, whereas a uniformly sampled triple or quartet of distinct vertices is shattered with respective probabilities \(12/n+O(n^{-2})\) and \(48/n^2+O(n^{-3})\) as \(n\to\infty\).

An exact structural refinement is as follows (isolated vertices of the support graph are ignored). For \(n\ge2\), a two-edge set is shattered precisely when \(n\ge5\), regardless of its shape. A three-edge set is shattered precisely when \(n\ge6\) and its support graph is one of \(K_{1,3}\), \(P_4\), or \(P_3\sqcup K_2\). A four-edge set is shattered precisely when it is one of: \(K_{1,4}\), a five-vertex broom (one leaf edge of \(K_{1,3}\) subdivided), \(P_5\), all requiring \(n\ge7\); or \(P_3\sqcup P_3\), requiring \(n\ge8\). The singleton case is as above.

## Assumptions and scope
All graphs are finite, simple, and undirected. In \(T_n\), **open** means a vertex is not in its own neighborhood. The auxiliary support graph \(F_A=([n],A)\) may have isolated ground vertices; its *nonisolated support* \(V(F_A)\) has size \(v\le2|A|\). Write \(F\) for the graph formed by the nonisolated support and its selected edges. Its unlabeled isomorphism type is independent of the unused ground vertices. No claim is made for closed neighborhoods of \(T_n\) or for larger Johnson graphs \(J(n,k)\) with \(k>2\).

## Proof
For an edge \(e=\{a,b\}\) of \(K_n\) and an ordered listing \(A=\{f_0,\ldots,f_{j-1}\}\), its open-neighborhood trace has indicator mask
\[
M_A(e)=\sum_{i=0}^{j-1}2^i\,\mathbf1_{\{e\ne f_i\text{ and }e\cap f_i\ne\varnothing\}}.
\tag{1}
\]
Thus \(A\) is shattered if and only if the set of integers \(\{M_A(e):e\in E(K_n)\}\) is exactly \(\{0,\ldots,2^j-1\}\).

**Finite-support reduction.** Fix the graph \(F\) obtained by deleting the isolated vertices from \(F_A\); suppose it has \(v\) vertices. For each \(t\ge0\), let \(\mathcal T_t(F)\) be the set of masks in (1) for queries from the edges on \(V(F)\) together with \(t\) fresh vertices. Then
\[
\mathcal T_0(F)\subseteq\mathcal T_1(F)\subseteq
\mathcal T_2(F)=\mathcal T_3(F)=\cdots.
\tag{2}
\]
Indeed, every query has either zero, one, or two endpoints outside \(V(F)\); the identities of outside endpoints never affect its trace. Consequently all shattering questions for \(|A|\le4\) reduce to finitely many isolate-free graphs with at most four edges, evaluated with at most two extra vertices. This reduction is exact, not a finite-size extrapolation.

**Exhaustive small-graph case analysis.** Every connected graph with one edge is \(K_2\); with two edges, \(P_3\); with three edges, one of \(K_3,K_{1,3},P_4\); and with four edges, one of \(K_{1,4}\), a paw (triangle with pendant edge), a five-vertex broom, \(C_4\), or \(P_5\). Splitting four edges over disconnected components produces precisely the other six four-edge types in the table below. This proves completeness of the table's graph types by partitioning the edge count among components.

For each type, formula (1) evaluated on all query edges with \(t=0,1,2\) fresh vertices gives the following exact trace cardinalities. Each row is a finite integer calculation; for example, \(K_{1,4}\) has \(10,15,16\) distinct masks, while \(P_3\sqcup P_3\) has \(15,15,16\). The file `verify.py` implements (1) verbatim, checks all table entries, and independently enumerates all finite graph types.

| Number of selected edges | Nonisolated support type | \(v\) | \((|\mathcal T_0|,|\mathcal T_1|,|\mathcal T_2|)\) |
|---:|---|---:|---|
| 1 | \(K_2\) | 2 | \((1,2,2)\) |
| 2 | \(P_3\) | 3 | \((3,3,4)\) |
| 2 | \(2K_2\) | 4 | \((2,4,4)\) |
| 3 | \(K_{1,3}\) | 4 | \((3,7,8)\) |
| 3 | \(K_3\) | 3 | \((3,3,4)\) |
| 3 | \(P_4\) | 4 | \((3,7,8)\) |
| 3 | \(P_3\sqcup K_2\) | 5 | \((7,8,8)\) |
| 3 | \(3K_2\) | 6 | \((4,7,7)\) |
| 4 | \(K_{1,4}\) | 5 | \((10,15,16)\) |
| 4 | paw | 4 | \((3,7,8)\) |
| 4 | broom | 5 | \((10,15,16)\) |
| 4 | \(K_{1,3}\sqcup K_2\) | 6 | \((8,13,13)\) |
| 4 | \(K_3\sqcup K_2\) | 5 | \((7,8,8)\) |
| 4 | \(C_4\) | 4 | \((3,7,8)\) |
| 4 | \(P_5\) | 5 | \((10,15,16)\) |
| 4 | \(P_4\sqcup K_2\) | 6 | \((8,13,13)\) |
| 4 | \(P_3\sqcup P_3\) | 6 | \((15,15,16)\) |
| 4 | \(P_3\sqcup2K_2\) | 7 | \((11,13,13)\) |
| 4 | \(4K_2\) | 8 | \((7,11,11)\) |

A row is shattered in an ambient \(K_n\) precisely when its column indexed by \(t=n-v\) contains \(2^j\) masks (use the final column when \(t\ge2\)). This gives exactly the structural classification and the sharp minimum ground sizes stated in the finding. There is no need to check any larger ambient ground size, by (2).

For \(j\ge5\), invoke the already established theorem of Adler, Benediktsson, and Macpherson, Theorem 3.6, that the open-neighborhood VC dimension of every Johnson graph is at most four; the specialized graph \(T_n=J(n,2)\) satisfies its hypotheses. Thus the displayed list includes every possible size of shattered set. The proof of that published upper bound is not being claimed as a contribution here.

**Exact labeled enumeration.** An unlabeled isolate-free graph \(F\) on \(v\) vertices occurs on a chosen \(v\)-element subset of \([n]\) in exactly \(v!/|\operatorname{Aut}(F)|\) ways. For the successful types, these numbers are: \(K_2:1\); \(P_3:3\), \(2K_2:3\); \(K_{1,3}:4\), \(P_4:12\), \(P_3\sqcup K_2:30\); \(K_{1,4}:5\), broom:\(60\), \(P_5:60\), \(P_3\sqcup P_3:90\). Their sharp ambient-size thresholds from the table therefore yield exactly the coefficient formulas in the finding, with no duplicate counting between types.

Indeed, pair universality can also be seen directly: if the two selected edges meet, a query on two unused vertices realizes the empty trace, while queries through the two exclusive endpoints realize the two singletons; if the selected edges are disjoint, querying a selected edge realizes the empty trace, an edge joining the two selected edges realizes the full trace, and an edge from a selected endpoint to a fifth vertex realizes either singleton. All witnesses exist for \(n\ge5\). Algebraically, \(3\binom n3+3\binom n4=\binom{\binom n2}{2}\), proving pair universality again. Finally \(s_3(n)\sim n^5/4\) and \(s_4(n)\sim n^6/8\), while \(\binom{\binom n2}{3}\sim n^6/48\) and \(\binom{\binom n2}{4}\sim n^8/384\). Division gives the two probabilities.

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. It enumerates the nineteen isolate-free graph types for one through four selected edges, calculates each of the 57 table cells directly from (1), independently checks the orbit multipliers, and enumerates every selected edge subset with sizes zero through four for \(2\le n\le10\), checking the resulting coefficients. Its successful output ends with `VERIFY_OK`. The finite table together with the support reduction (2) constitutes an exact finite case proof; the additional runs over \(n\le10\) are corroborative checks, not an extrapolation to arbitrary \(n\).

## Relationship to prior work
Adler, Benediktsson, and Macpherson [1] proved the general VC-dimension upper bound four for open neighborhoods of Johnson graphs, displayed a four-point witness already in \(J(7,2)\), and studied sixteen local patterns in their proof. The upper bound and that witness are **prior work**. Their theorem and local analysis do not give the displayed global, all-\(n\), rank-by-rank counts of shattered subsets or their limiting proportions. The present statement refines their extremal VC-dimension result to a complete enumeration for the triangular subfamily, and gives an independent edge-support classification and finite trace table.

Coudert, Csikós, Ducoffe, and Viennot [2] developed exact algorithms for general-graph VC dimension, primarily for the closed-neighborhood convention. General algorithms for testing a given set are not an all-parameter exact shattering polynomial of \(T_n\). The closed neighborhood of the Kneser graph \(KG(n,2)\) is the pointwise complement of the open neighborhood of \(T_n\); therefore the same shattered subsets occur for that equivalent family, without any additional novelty assertion.

## Limitations
The combinatorial enumeration here covers \(J(n,2)\), not general \(J(n,k)\). The proof depends on the previously published general upper bound four for open Johnson neighborhoods. Formula (2) and the complete trace table are independently checked inside the supplied package. A prior equivalent shattering-polynomial formula under another terminology remains a possible publication-priority risk; no claim of formal external certification is made. The numerical tests alone would not establish the infinite theorem.

## References
[1] I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first version July 31, 2020; Theorems 3.6 and 3.7 and Section 3. https://arxiv.org/abs/2007.16042

[2] D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588, first version May 13, 2024. https://arxiv.org/abs/2405.07588
