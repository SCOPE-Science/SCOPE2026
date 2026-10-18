# A sharp width-three boundary for forest–forest total colourings of \(K_{1,a,b}\)

## Finding
For a finite graph \(G\), let \(\tau(G)=\chi''_{\mathcal D_1,\mathcal D_1}(G)\) be the minimum number of colors assigned jointly to its vertices and edges, with each single-color vertex-induced subgraph a forest, each single-color edge subgraph a forest, and each edge colored differently from both endpoints.

**Theorem.** For integers \(1\le a\le b\) and \(a\le3\),
\[
\tau(K_{1,a,b})=\begin{cases}
3,&a=1,\\
4,&a=2,\\
4,&a=3\ \text{and}\ 3\le b\le5,\\
5,&a=3\ \text{and}\ b\ge6.
\end{cases}
\]
More sharply, every four-color forest–forest total coloring of \(K_{1,3,5}\) makes the edges bearing color \(c\) form a spanning tree on all vertices *not* colored \(c\), for each of its four colors. In particular, the graph \(K_{1,3,5}\) is a sharp exception to the natural construction using separate colors for the two hub stars and a minimum forest decomposition of \(K_{3,5}\): that construction needs five colors, while the exact answer is four.

## Assumptions and scope
All graphs are finite, simple, undirected. \(K_{1,a,b}\) has three independent parts: one hub vertex \(h\), an \(a\)-vertex part \(A\), and a \(b\)-vertex part \(B\), with all interpart edges and no intrapart edges. The theorem covers every positive \(a,b\) with \(\min(a,b)\le3\), by swapping the two nonsingleton parts. No result for larger minimum parts is asserted. Empty graph or zero-part cases are excluded.

## Proof
**Universal counting bound.** Put \(N=a+b+1\) and \(M=ab+a+b\). Since \(a,b\ge1\), the graph contains a triangle, and hence no vertex color class in a valid coloring contains all \(N\) vertices. Let \(s_c\) be the number of vertices colored \(c\). An edge colored \(c\) avoids every such vertex; because its edge-color graph is a forest on the other \(N-s_c\ge1\) vertices, it has at most \(N-s_c-1\) edges. For a coloring using \(k\) available colors (including any unused ones), \(\sum_c s_c=N\). Counting the graph's edges therefore yields
\[
M\le\sum_c(N-s_c-1)=k(N-1)-N,
\quad\text{so}\quad
k\ge\left\lceil\frac{ab+2a+2b+1}{a+b}\right\rceil.
\]
For \(a=1\), the right-hand side equals \(3\). For \(a=2\) and \(b\ge2\), it equals \(\lceil4-3/(b+2)\rceil=4\). For \(a=3\), it equals \(\lceil5-8/(b+3)\rceil\), which is \(4\) when \(3\le b\le5\) and \(5\) when \(b\ge6\).

**Universal star construction.** Give the hub color \(0\), all \(A\)-vertices color \(1\), and all \(B\)-vertices color \(2\). Color every \(hA\)-edge \(2\), every \(hB\)-edge \(1\), and for each indexed \(A\)-vertex give all its \(AB\)-edges one star color. Use star color \(0\) for the first \(A\)-vertex, color \(3\) for the second (if any), and color \(4\) for the third (if any). Thus \(a+2\) colors suffice for \(a=1,2,3\). All vertex-color classes are independent, all edge-color classes are stars, and no edge matches an endpoint's color. This proves the asserted upper bounds when \(a\in\{1,2\}\) and when \(a=3,b\ge6\).

**Exceptional nine-vertex certificate.** Write \(A=\{a_1,a_2,a_3\}\) and \(B=\{b_1,\ldots,b_5\}\). The following is an explicit valid four-coloring of \(K_{1,3,5}\), using the colors \(0,1,2,3\). Its vertex colors are
\[
\begin{array}{c|ccccccccc}
\text{vertex}&h&a_1&a_2&a_3&b_1&b_2&b_3&b_4&b_5\\\hline
\text{color}&0&2&1&3&3&3&3&1&3
\end{array}.
\]
Give the three edges \((h,a_1),(h,a_2),(h,a_3)\) respective colors \((1,3,2)\); the five edges \((h,b_1),\ldots,(h,b_5)\) colors \((1,2,1,3,2)\); and color the \(AB\)-edges using the matrix with rows \(a_1,a_2,a_3\), columns \(b_1,\ldots,b_5\):
\[
\begin{pmatrix}
0&1&0&3&0\\
2&0&2&0&2\\
1&0&0&2&1
\end{pmatrix}.
\]
Inspection of these finite arrays shows that no edge matches either endpoint, the four vertex-color induced graphs are (respectively) one vertex, one edge, one vertex, and one star, and the four edge-color graphs are trees on respectively \(8,7,8,4\) allowed vertices, containing \(7,6,7,3\) edges. These trees use all \(23\) edges. Restricting this same coloring to any subgraph obtained by keeping \(3\le b\le5\) vertices of \(B\) proves the remaining upper bounds. (More generally it also supplies \(b=2\), which is already covered by relabeling.)

**Rigidity at equality.** At \((a,b)=(3,5)\), \(N=9\), \(M=23\), and the universal four-color edge capacity equals \(4(N-1)-N=23\). Hence *each* of the four forest edge classes must attain its individual upper bound \(N-s_c-1\). A forest on the \(N-s_c\) eligible vertices with exactly \(N-s_c-1\) edges is a connected spanning tree. This holds for **every** optimal four-coloring, not just the displayed witness. All cases are proved.

## Verification
The standalone standard-library program `verify.py` reconstructs the witness, its induced restrictions, and the explicit star constructions. For each \(a=1,2,3\) and each \(a\le b\le200\), it checks that the assignment covers every edge exactly once, that every incidence is properly colored, and that the monochromatic vertex and edge graphs have no cycles. It independently computes the sharp counting lower bound and checks equality with the assigned color count. It additionally checks capacity saturation of every edge-color class for \(K_{1,3,5}\). Execution: `python3 verify.py`. Observed output: `CHECKS_PASSED instances=597 all_graph_edges=182077 special_K_1_3_5=23 saturation=YES`. These are finite consistency checks; the proof above is valid for all allowed board sizes independently of testing.

## Relationship to prior work
Borowiecki, Kemnitz, Marangio, and Mihók (2011), Theorem 8, established \(\tau(K_n)=\lfloor n/2\rfloor+2\) for complete graphs and discussed vertex/edge arboricity, but their examined theorem is about complete graphs, not the complete tripartite cone family here. Cara and Dorfling (arXiv:2608.19294, publicly posted August 19, 2026) investigate forest–forest total coloring in specific planar graph families; this theorem addresses a nonplanar tripartite family and pinpoints a four-color exceptional case. Karafová (2013) studies fractional generalized total coloring of complete graphs; that distinct fractional invariant neither supplies nor implies this integral tripartite classification. Searches of relevant current mathematical records and prior work did not identify a theorem implying the stated exact width-three boundary. These comparisons do not establish definitive publication priority.

## Limitations
The conclusion is restricted to complete tripartite graphs \(K_{1,a,b}\) with \(\min(a,b)\le3\). It does not determine larger widths, count every valid coloring, or address list/fractional variants. The finite verifier is supplementary and independent mathematical assessment has not been performed. No claim of definitive bibliographic novelty is made.

## References
1. P. Cara and S. Dorfling, *On Generalized Total Colourings of Planar Graphs*, arXiv:2608.19294 (first public posting 2026-08-19), https://arxiv.org/abs/2608.19294.
2. M. Borowiecki, A. Kemnitz, M. Marangio and P. Mihók, *Generalized total colorings of graphs*, Discuss. Math. Graph Theory 31 (2011), 209–222. DOI:10.7151/dmgt.1540.
3. G. Karafová, *Generalized fractional total coloring of complete graphs*, Discuss. Math. Graph Theory 33 (2013), 665–676. DOI:10.7151/dmgt.1697.
4. M. Borowiecki and I. Broere, *Hamiltonicity and Generalised Total Colourings of Planar Graphs*, Discuss. Math. Graph Theory 36 (2016), 243–257.
