# Exact strong majority index of complete graphs
## Finding
For every integer \(n\ge 3\), the complete graph \(K_n\) has strong majority index
\[
\operatorname{Maj}'(K_n)=
\begin{cases}
2,&n=4,\\
3,&n\ne4.
\end{cases}
\]
Here a strong majority edge-colouring of a graph assigns colours to edges so that, for every edge \(e\) and every colour \(\alpha\), at most half of the edges adjacent to \(e\) have colour \(\alpha\). The strong majority index \(\operatorname{Maj}'(G)\) is the least number of colours in such a colouring.

## Assumptions and scope
Graphs are finite and simple. The theorem concerns \(K_n\) for integers \(n\ge3\). For an edge of \(K_n\), exactly \(2n-4\) other edges are adjacent to it, so the strong-majority threshold for each colour is \(n-2\).

## Proof
First classify possible two-colourings. Call one colour red and let \(d(v)\) be the red degree of a vertex \(v\). If \(uv\) is red, then the number of red edges adjacent to \(uv\) is \(d(u)+d(v)-2\). If \(uv\) is blue, that number is \(d(u)+d(v)\). In a two-colouring the two colour-counts around every edge sum to \(2n-4\), while each is at most \(n-2\); therefore each count is exactly \(n-2\). Consequently
\[
d(u)+d(v)=
\begin{cases}
n,&uv\text{ is red},\\
n-2,&uv\text{ is blue}.
\end{cases}
\]

If \(n\) is odd, both allowed sums are odd. Three vertices cannot have all three pairwise degree sums odd, because two odd sums sharing one degree force the remaining two degrees to have the same parity. Thus no two-colouring exists for odd \(n\).

Suppose \(n\) is even. For every two vertices the red-degree sum belongs to \(\{n-2,n\}\). Hence all red degrees have the same parity and any two differ by at most \(2\). The degrees cannot all be equal: if every pair sum were \(n\), every edge would be red, while if every pair sum were \(n-2\), every edge would be blue, and either alternative contradicts the corresponding red degree for \(n\ge3\). Thus exactly two red-degree values occur, say \(a\) and \(a+2\). If both degree classes contained at least two vertices, then the three distinct pair sums \(2a\), \(2a+2\), and \(2a+4\) would all occur, impossible because only two sums are allowed. Therefore one degree class is a singleton.

If the unique vertex has the larger red degree, then low-low pairs are blue and mixed pairs are red, so the red graph is a star. Its two red degrees are \(1\) and \(n-1\), whose difference is \(n-2\); this must equal \(2\), hence \(n=4\). If the unique vertex has the smaller red degree, the red graph is a clique on the other \(n-1\) vertices plus an isolated vertex. Its red degrees are \(0\) and \(n-2\), again forcing \(n=4\). Thus a two-colour strong majority edge-colouring exists only when \(n=4\). For \(K_4\), colour a three-edge star red and the complementary triangle blue. Every edge then has exactly two red and two blue adjacent edges, proving \(\operatorname{Maj}'(K_4)=2\).

It remains to give three-colourings. For \(n=3\), give the three edges distinct colours. For \(n=5\), on vertices \(0,1,2,3,4\), use colour classes
\[
\{03,04,23\},\qquad
\{01,02,12,14\},\qquad
\{13,24,34\}.
\]
A direct count gives at most \(3=n-2\) adjacent edges of any one colour around every edge.

For \(n=7\), decompose \(K_7\) into the three Hamilton cycles
\[
(0,1,2,3,4,5,6),\quad
(0,2,4,6,1,3,5),\quad
(0,3,6,2,5,1,4),
\]
and give each cycle its own colour. Every vertex then has colour-degree \(2\) in every colour. Around an edge, its own colour occurs on exactly \(2\) adjacent edges and either other colour occurs on exactly \(4\), both at most \(5=n-2\).

For \(n=6\) and for every \(n\ge8\), partition the vertices equitably into \(A,B,C\). Colour edges inside \(A\) together with edges between \(B\) and \(C\) by colour \(0\); cyclically, colour edges inside \(B\) together with edges between \(C\) and \(A\) by colour \(1\), and edges inside \(C\) together with edges between \(A\) and \(B\) by colour \(2\). At every vertex, every colour-degree is at most \(\lceil n/3\rceil\). Hence for every edge and every colour, the number of adjacent edges of that colour is at most \(2\lceil n/3\rceil\), and
\[
2\lceil n/3\rceil\le n-2
\]
for \(n=6\) and every \(n\ge8\). This proves the required three-colour upper bound. Together with the two-colour classification, the formula follows.

## Verification
The accompanying verifier checks the explicit colourings for \(n=3,4,5,7\), checks the equitable three-part construction for \(n=6\) and every \(8\le n\le200\), and exhaustively tests all two-colourings of \(K_n\) for \(3\le n\le6\). These finite checks supplement, but do not replace, the parity and degree-sum argument proving the infinite lower bound and the symbolic inequality proving the infinite upper construction.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak and Woźniak introduced the strong majority index in 2026 and established general bounds and several graph-class results. Pękała and Przybyło subsequently proved that every graph of minimum degree at least \(5\) has strong majority index at most \(3\). That theorem already supplies the upper bound for \(K_n\) when \(n\ge6\), but it does not determine whether two colours suffice, does not isolate the exceptional complete graph, and does not cover the small complete graphs \(K_3,K_4,K_5\). The present result determines the exact index for the whole complete-graph family and gives a direct elementary construction.

## Limitations
The argument is specialized to complete graphs. It does not classify all graphs with strong majority index \(2\), nor does it improve the general three-colour minimum-degree threshold. The literature comparison found no statement implying the exact complete-graph formula, but absence from the sources inspected is not an absolute novelty guarantee.

## References
1. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, “Strong majority colorings of graphs,” arXiv:2605.23828, first posted 2026-05-22.
2. P. Pękała, J. Przybyło, “On Strong Majority Edge Colourings with Few Colours,” arXiv:2608.04122, first posted 2026-08-04.
