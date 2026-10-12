# Strong majority index of complete bipartite graphs
## Finding
Let \(1\le m\le n\). The graph \(K_{1,2}\) admits no strong majority edge coloring. For every other finite complete bipartite graph \(K_{m,n}\),
\[
\operatorname{Maj}'(K_{m,n})=
\begin{cases}
1,&(m,n)=(1,1),\\
4,&(m,n)\in\{(1,4),(3,4),(4,5)\},\\
2,&m=2\text{ and }n\text{ is even},\\
3,&\text{otherwise}.
\end{cases}
\]
Thus, with both parts of size at least two, the complete two-color family is exactly \(K_{2,2r}\), and the only four-color exceptions are \(K_{3,4}\) and \(K_{4,5}\).

## Assumptions and scope
All graphs are finite and simple. A strong majority edge coloring assigns colors to the edges so that for every edge \(e\) and every color \(\alpha\), at most half of the edges adjacent to \(e\) have color \(\alpha\). The strong majority index \(\operatorname{Maj}'(G)\) is the least number of colors in such a coloring when one exists. We write \(K_{m,n}\) with \(m\le n\). For an edge of \(K_{m,n}\), the number of adjacent edges is \(m+n-2\).

## Proof
First consider stars. In \(K_{1,n}\), every two edges are adjacent. Put \(H=\lfloor(n-1)/2\rfloor\). If \(n\ge3\) and a color class has size \(s\), then any edge outside that class sees all \(s\) edges of that color, so every color class has size at most \(H\). Conversely, any partition of the \(n\) edges into color classes of size at most \(H\) is strong majority: an edge in a class of size \(s\) sees \(s-1\) edges of its own color and all edges of every other class. Hence the minimum number of colors is \(\lceil n/H\rceil\), which equals \(3\) for \(n=3\) and for every \(n\ge5\), and equals \(4\) for \(n=4\). For \(K_{1,1}\) the condition is vacuous and one color suffices. For \(K_{1,2}\), each edge has one adjacent edge, so the unique adjacent edge already exceeds one half for its color; therefore no strong majority edge coloring exists.

Now assume \(m,n\ge2\). We classify two-colorings. If \(m+n-2\) is odd, two color counts around any edge cannot both be at most half while summing to \(m+n-2\), so two colors are impossible. Suppose \(m+n-2=2H\). For one of the two colors, let \(r_i\) be its number of edges in row \(i\), let \(c_j\) be its number of edges in column \(j\), and let \(x_{ij}\in\{0,1\}\) indicate whether cell \((i,j)\) has that color. Since the two color counts adjacent to every edge sum to \(2H\), each must equal \(H\). Therefore
\[
r_i+c_j=H+2x_{ij}.
\]
For any two rows, their row sums differ by at most \(2\), and the same holds for any two columns. If both the row sums and the column sums assumed two distinct values, then the four combinations of their low and high values would span an interval of length \(4\), whereas the displayed equation allows only \(H\) and \(H+2\), a contradiction. Hence all row sums are equal or all column sums are equal. If all row sums are equal, each column is monochromatic. Since a nontrivial two-coloring uses both colors, comparing a monochromatic column of each color in the displayed equation gives \(m=2\); the common row sum is then \(n/2\), so \(n\) is even. The column-constant case is symmetric. Conversely, for \(K_{2,2r}\), color \(r\) whole columns with one color and the other \(r\) columns with the second color. Every edge then sees exactly \(r\) adjacent edges of each color. This proves that two colors occur exactly for \(K_{2,2r}\).

It remains to prove the three- and four-color cases. For \(m,n\ge3\), color cell \((i,j)\) by \(i+j\pmod 3\). Every color occurs at most \(\lceil n/3\rceil\) times in a row and at most \(\lceil m/3\rceil\) times in a column. Thus the coloring is strong majority whenever
\[
\left\lceil\frac m3\right\rceil+\left\lceil\frac n3\right\rceil\le \left\lfloor\frac{m+n-2}{2}\right\rfloor.
\]
If \(m+n\ge14\), the left side is at most \((m+n+4)/3\), which is at most \((m+n-2)/2\). Checking the finitely many pairs with \(3\le m\le n\) and \(m+n\le13\) shows that the displayed inequality fails only for \((3,4)\), \((4,4)\), \((4,5)\), and \((4,7)\). The pairs \((4,4)\) and \((4,7)\) have explicit strong majority three-colorings given by the following matrices, whose entries are colors:
\[
\begin{pmatrix}
1&2&1&1\\
3&3&1&2\\
1&2&2&3\\
3&3&2&1
\end{pmatrix},
\qquad
\begin{pmatrix}
3&1&2&3&2&1&3\\
1&2&3&1&3&2&2\\
2&1&1&2&1&3&3\\
3&2&1&3&1&2&2
\end{pmatrix}.
\]
For \(K_{2,n}\) with odd \(n\ge3\), use three monochromatic column classes whose sizes differ by at most one. Their largest size is at most \(\lfloor(n-1)/2\rfloor\), so this is a strong majority three-coloring.

For \(K_{3,4}\), every edge has five adjacent edges, so each color may occur at most twice in an edge neighborhood. Fix one color and consider its color subgraph. If it has at least four edges, the local bound forces maximum degree at most two unless it is a three-edge star; chasing any degree-two vertex across the complete bipartite host then forces every nonisolated adjacent vertex to be joined by a colored edge. Consequently every color class with at least four edges is a \(4\)-cycle and has exactly four edges. A three-coloring of the twelve edges would therefore split the edge set into three \(4\)-cycles, making every vertex degree even in their union, contradicting the degree-three vertices of \(K_{3,4}\). Hence at least four colors are needed. Four colors suffice by the proper coloring \(c(i,j)=i+j\pmod4\).

For \(K_{4,5}\), every edge has seven adjacent edges, so a fixed color may occur at most three times in every edge neighborhood. Let \(F\) be one color class, with row degrees \(r_i\) and column degrees \(c_j\). For every cell, writing \(x_{ij}=1\) when it lies in \(F\),
\[
r_i+c_j-2x_{ij}\le3.
\]
We claim \(|F|\le6\). If some column has degree \(4\), every incident row has degree at most \(1\), so \(|F|\le4\). If some column has degree \(3\), its three incident rows have degree at most \(2\), while the fourth row has degree \(0\), so \(|F|\le6\). Hence assume all column degrees are at most \(2\). A row of degree \(5\) is impossible. If a row has degree \(4\), its four incident columns have degree at most \(1\), so \(|F|\le6\). If a row has degree \(3\), the two nonincident columns must have degree \(0\), so again \(|F|\le6\). Finally, if every row has degree at most \(2\) and \(|F|\ge7\), then at least three rows have degree \(2\) and at least two columns have degree \(2\). Every intersection of such a row and column would have to lie in \(F\), because a missing intersection would give \(2+2>3\); but then each degree-two column would contain at least three colored edges, a contradiction. Thus every color class has at most six edges, so three colors cover at most eighteen of the twenty edges. Four colors are therefore necessary. They suffice with \(c(i,j)=i+j\pmod4\): each row contains any color at most twice and each column exactly once, so an edge sees at most three adjacent edges of any color.

Combining these cases gives the stated formula.

## Verification
The accompanying `verify.py` checks the constructive colorings for every \(1\le m\le40\) and \(m\le n\le60\); verifies that the cyclic three-color sufficient inequality has exactly the four claimed exceptions in that range; exhaustively checks all \(3^{12}=531441\) three-colorings of \(K_{3,4}\); exhaustively checks all \(2^{20}\) candidate single-color classes in \(K_{4,5}\), confirming maximum size \(6\); and exhaustively checks two-color feasibility for all tested bicliques with at most sixteen edges. The final replay reports `ALL CHECKS PASSED`.

The finite checks support, but do not replace, the analytic arguments above. In particular, the general two-color classification, the cyclic construction bound, and the \(K_{4,5}\) obstruction are proved symbolically.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak, and Woźniak introduced the strong majority index in 2026 and established general bounds and examples. Their accessible full text does not state a complete-bipartite classification. Pękała and Przybyło later proved that minimum degree at least \(5\) guarantees a strong majority edge three-coloring and explicitly proved that \(K_{3,4}\) is not three-colorable. A published published-finding corpus record, `2026/9/17/SCOPE005`, gives a broader bipartite threshold for generalized strong \(1/k\)-majority edge coloring and identifies \(K_{k^2,k^2+1}\) as the sharp obstruction; for \(k=2\), this already covers the obstruction \(K_{4,5}\). These results therefore imply parts of the classification above, but none of the inspected sources states the exact strong majority index for every complete bipartite graph, the two-color characterization \(K_{2,2r}\), or the complete low-degree transition.

## Limitations
The originality comparison is limited to the inspected primary preprints, targeted web searches, published-finding corpus searches, and the available published record summaries. The published-finding corpus record `2026/9/17/SCOPE005` was available through its indexed title and summary rather than a separately fetched full public text, so an unindexed corollary in that record remains a residual discoverability risk. The theorem concerns only complete bipartite graphs and does not classify arbitrary bipartite graphs of minimum degree below five.

## References
1. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1, first public 2026-05-22. MSC 05C15, 05C70.
2. P. Pękała, J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122v1, first public 2026-08-04.
3. published-finding corpus record `2026/9/17/SCOPE005`, *Exact bipartite threshold for generalized strong-majority edge colouring*.
