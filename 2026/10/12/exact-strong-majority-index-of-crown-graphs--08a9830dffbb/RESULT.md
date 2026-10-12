# Exact strong-majority index of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) have bipartition \(A=\{a_0,\ldots,a_{n-1}\}\) and \(B=\{b_0,\ldots,b_{n-1}\}\), with \(a_i b_i\) deleted for every \(i\). Then
\[
\operatorname{Maj}^{\prime}(\operatorname{Cr}_n)=
\begin{cases}
2,&n=4,\\
3,&n\ne4.
\end{cases}
\]
In particular, \(\operatorname{Cr}_4\) is the unique crown graph admitting a two-colour strong-majority edge-colouring.

## Assumptions and scope
Graphs are finite and simple. In a strong majority edge-colouring, for every edge \(e\) and every colour, at most half of the edges adjacent to \(e\) receive that colour. The parameter \(\operatorname{Maj}^{\prime}(G)\) is the least number of colours in such a colouring. Crown graphs here have \(n\ge3\), so they are connected and \((n-1)\)-regular.

## Proof
Every edge of \(\operatorname{Cr}_n\) has exactly \(2n-4\) adjacent edges. Hence a two-colour strong-majority colouring would force exactly \(n-2\) adjacent edges of each colour around every edge.

Assume such a two-colouring exists and encode one colour by \(x_{ij}\in\{0,1\}\) on the edge \(a_i b_j\), where \(i\ne j\). Put
\[
r_i=\sum_{j\ne i}x_{ij},\qquad c_j=\sum_{i\ne j}x_{ij},\qquad T=\sum_i r_i=\sum_j c_j.
\]
For every \(i\ne j\), exact balance around \(a_i b_j\) gives
\[
r_i+c_j-2x_{ij}=n-2.\tag{1}
\]
Summing (1) over \(j\ne i\), and separately over \(i\ne j\) with the column fixed, gives
\[
(n-3)r_i+T-c_i=(n-1)(n-2),
\]
\[
(n-3)c_i+T-r_i=(n-1)(n-2).
\]
Subtracting yields \((n-2)(r_i-c_i)=0\), so \(r_i=c_i\) for every \(i\). If \(n\ne4\), the first displayed equation then forces all \(r_i\) to have a common value \(r\). Equation (1) consequently forces all \(x_{ij}\) to be equal. The all-zero choice would give \(0=n-2\), while the all-one choice would give \(2n-4=n-2\); both are impossible for \(n\ge3\). Thus two colours are impossible unless \(n=4\).

For \(n=4\), colour 1 all edges incident with either endpoint of one deleted matched pair, say \(a_0\) or \(b_0\), and colour 0 all remaining edges. Every edge has exactly two adjacent edges of each colour, so this is a strong-majority two-colouring.

It remains to give three-colourings. For \(n\ge6\), decompose the crown into the \(n-1\) perfect matchings
\[
F_d=\{a_i b_{i+d}:i\in\mathbb Z/n\mathbb Z\},\qquad 1\le d\le n-1,
\]
and distribute these matchings among three colours as evenly as possible. If \(m_q\) matchings receive colour \(q\), then \(m_q\le\lceil(n-1)/3\rceil\) at every vertex. For an edge of colour \(q\), the number of adjacent edges of colour \(q\) is \(2(m_q-1)\), while for any other colour \(p\) it is \(2m_p\). Since
\[
2\left\lceil\frac{n-1}{3}\right\rceil\le n-2\qquad(n\ge6),
\]
the colouring is strong majority.

For \(n=3\), one three-colour witness, with rows indexed by \(a_i\), columns by \(b_j\), and the diagonal omitted, is
\[
\begin{pmatrix}
- & 1 & 2\\
1 & - & 0\\
2 & 0 & -
\end{pmatrix}.
\]
For \(n=5\), a witness is
\[
\begin{pmatrix}
- & 2 & 1 & 0 & 1\\
0 & - & 2 & 2 & 2\\
1 & 2 & - & 0 & 0\\
1 & 0 & 2 & - & 1\\
1 & 1 & 0 & 2 & -
\end{pmatrix}.
\]
Direct counting gives at most \(1\) same-colour occurrence among the two adjacent edges in the first matrix and at most \(3\) occurrences of any colour among the six adjacent edges in the second. Finally, one colour is impossible for every \(n\ge3\), because every edge has a nonempty edge-neighbourhood. This proves the formula.

## Verification
The bundled verifier checks the two explicit small witnesses, the balanced perfect-matching construction for every \(6\le n\le60\), and exhaustively enumerates every two-colouring for \(n=3,4,5\). It also checks the row-column identities used in the two-colour obstruction over a broad integer range. These finite checks corroborate the proof; the theorem itself follows from the symbolic argument above and is not inferred from enumeration.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak, and Woźniak introduced the strong majority edge-colouring parameter in arXiv:2605.23828. Antoniuk, Prorok, and Salia subsequently proved a universal five-colour bound for admissible graphs in arXiv:2607.00212. Pękała and Przybyło proved in arXiv:2608.04122 that minimum degree at least \(5\) guarantees a three-colour strong-majority edge-colouring; this supplies an independent published upper bound of \(3\) for crowns with \(n\ge6\), but it does not determine when two colours suffice. The present result adds the exact two-colour obstruction, resolves the degree-\(2\) and degree-\(4\) crowns, and identifies the unique exceptional crown \(\operatorname{Cr}_4\). A prior exact result for complete graphs has the same numerical pattern, but it is not an implication: the crown proof uses a row-column balance system induced by the missing one-factor rather than the complete-graph degree-sum system.

## Limitations
The theorem is specific to deleting a perfect matching from a balanced complete bipartite graph. It does not classify two-colour strong-majority edge-colourability for arbitrary regular bipartite graphs or for general matching-deleted bicliques. The later minimum-degree theorem already covers the three-colour upper bound for \(n\ge6\); the new content there is exactness via the two-colour obstruction.

## References
1. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1, 2026.
2. S. Antoniuk, M. Prorok, N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212v1, 2026.
3. P. Pękała, J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122v1, 2026.
