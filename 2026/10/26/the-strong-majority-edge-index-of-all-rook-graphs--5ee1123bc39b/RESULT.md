# The strong-majority edge index of all rook graphs

## Finding
For every pair of integers \(2\le m\le n\), the rook graph \(R_{m,n}=K_m\square K_n\) satisfies
\[
\operatorname{Maj}'(R_{m,n})=
\begin{cases}
2,&(m,n)=(2,2),\\
3,&\text{otherwise}.
\end{cases}
\]
Moreover, with two named colours, the number of strong-majority edge colourings of \(R_{m,n}\) is exactly four for \((m,n)=(2,2)\) and zero for every other parameter pair. In particular, the two distinct degree-four rook graphs \(R_{2,4}\) and \(R_{3,3}\) both admit strong-majority three-edge-colourings despite falling outside the general minimum-degree-five theorem.

## Assumptions and scope
Graphs are finite, simple and undirected. Vertices of \(R_{m,n}\) are pairs \((i,j)\), with \(0\le i<m\), \(0\le j<n\); two distinct vertices are adjacent precisely when they agree in one coordinate. This graph is regular of degree \(d=m+n-2\). A strong-majority edge colouring assigns a colour to every edge such that, for every edge, each colour appears on at most half of its *other* (adjacent) edges. The index \(\operatorname{Maj}'\) is the smallest palette size. Colours need not be proper. Two named colours are distinct labels, not a quotient by interchange.

## Proof
**Two-colour rigidity on regular graphs.** Suppose a \(d\)-regular graph has a strong-majority colouring with named colours red and blue. Let \(r(v)\) denote the number of red edges at \(v\). Each edge has \(2d-2\) other adjacent edges, so the two colour counts among them must each equal \(d-1\). For a red edge \(uv\), the adjacent red count is \(r(u)+r(v)-2\); hence \(r(u)+r(v)=d+1\). For a blue edge, the adjacent red count is \(r(u)+r(v)\); hence \(r(u)+r(v)=d-1\). Set \(s(v)=2r(v)-d\). Then, for every edge \(uv\),
\[
s(u)+s(v)=\begin{cases}2,&uv\text{ red},\\-2,&uv\text{ blue}.\end{cases}
\]
Summing the left side over neighbors of a vertex \(v\), the right side has \(r(v)\) positive and \(d-r(v)\) negative terms. Consequently \(d\,s(v)+(As)(v)=2s(v)\), or
\[
As=(2-d)s,
\]
where \(A\) is the adjacency matrix. The vector \(s\) is nonzero, because the displayed edge sums cannot all vanish. Thus \(2-d\) must be an adjacency eigenvalue; this is a necessary condition, not a general sufficient condition.

**Spectrum of the rook graph.** Its adjacency operator is \((J_m-I_m)\otimes I_n+I_m\otimes(J_n-I_n)\), and therefore its distinct possible eigenvalues are
\[
d=m+n-2,\qquad m-2,\qquad n-2,\qquad -2.
\]
For \(m,n\ge2\), the first three are nonnegative. The required eigenvalue is \(2-d=4-m-n\). If \(m+n=5\), it is \(-1\), which is absent; if \(m+n\ge7\), it is smaller than \(-2\), again absent. Thus a two-colour candidate exists only when \(m+n=4\) or \(m+n=6\).

**The two spectral boundary exceptions are impossible.** If \(m+n=6\), the required eigenvalue is \(-2\). Writing \(s\) as an \(m\)-by-\(n\) array, its \(-2\)-eigenvector equation is equivalent to all row sums and all column sums being zero: indeed, at \((i,j)\), \((As)_{ij}=\sum_k s_{kj}+\sum_l s_{il}-2s_{ij}\); hence each row sum is the negative of each column sum, and comparing their grand totals forces them all to vanish. For \((m,n)=(2,4)\), every column has two entries summing to zero; these two vertices are adjacent, contradicting the necessary edge-sum value \(\pm2\). For \((m,n)=(3,3)\), each row has three entries summing to zero. Since the sum of every pair of entries within a row equals \(\pm2\), each individual entry equals \(\pm2\), but three such numbers cannot sum to zero. These contradictions exclude both cases. One colour is impossible for any rook graph in scope, since each edge has \(2d-2>0\) adjacent edges.

**The four smallest constructions.** The unique case with two colours is \(R_{2,2}\cong C_4\), whose cyclic edge pattern \(0,0,1,1\) is feasible. Each edge's two adjacent edges must receive opposite colours, forcing exactly its four cyclic shifts; hence precisely four named colourings exist.

For \(R_{2,3}\) and \(R_{3,3}\), use palette \(\{0,1,2\}\) and colour each horizontal edge \((i,j)(i,k)\) by \(i+j+k\pmod3\), and each vertical edge \((i,j)(h,j)\) by \(i+h+j\pmod3\). The formulas colour every edge exactly once. Direct substitution into the six- or four-edge adjacency neighbourhoods verifies the strong-majority bound for every edge; the finite standalone checker explicitly iterates all nine or eighteen edges.

For \(R_{2,4}\), give each of its two horizontal \(K_4\) layers the same proper three-edge-colouring: edges \(01,23\) have colour \(0\), edges \(02,13\) have colour \(1\), and edges \(03,12\) have colour \(2\). Give the four matching rungs, indexed by their common column \(j=0,1,2,3\), respective colours \(0,0,1,2\). Every rung has exactly two adjacent horizontal edges of each colour. For a horizontal edge of colour \(c\), among its four adjacent horizontal edges each of the two other colours occurs exactly twice and colour \(c\) does not occur. The two remaining adjacent edges are its endpoint rungs. A count could exceed three only if both rungs had an equal colour different from \(c\); the sole repeated rung colour is \(0\) at columns \(0,1\), whose horizontal edge has colour \(0\). Hence every colour count is at most three of the six adjacent edges.

**All remaining cases.** When \(m+n\ge7\), the rook graph has minimum degree \(d\ge5\). The theorem of Pękała and Przybyło (August 2026, Theorem 4) asserts that every graph with minimum degree at least five has a strong-majority edge-colouring using three colours. Combined with the two-colour impossibility already proved, the index is exactly three. All parameter pairs are now covered.

## Verification
The dependency-free file `verify.py` reconstructs the rook graphs, checks the four explicit colourings, and independently enumerates every named two-colouring of the four small cases. Its recorded output is in `verify_output.txt`. The two-colouring counts for \(R_{2,2}\), \(R_{2,3}\), \(R_{2,4}\), \(R_{3,3}\) are respectively \(4,0,0,0\). The infinite lower bound is spectral and does not rely on finite enumeration. The infinite three-colour upper bound uses the cited published theorem rather than a computer certificate.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak and Woźniak introduced the invariant and studied cycles, complete graphs, and general bounds. Antoniuk, Prorok and Salia strengthened bounds for admissible graphs and observed three-colour constructions in some Eulerian cases, including those with edge count divisible by three. Thus the three-colour upper bound for \(R_{3,3}\), an Eulerian graph with eighteen edges, is also a consequence of their construction; it is not claimed as new. Pękała and Przybyło established the minimum-degree-five general upper bound, which covers rook graphs of degree at least five but does not prove that their index is exactly three. The contribution here is the full two-parameter sharp classification and rigorous exclusion of every other two-colour case, including both degree-four graphs outside that upper-bound hypothesis; the explicit three-colouring of \(R_{2,4}\) covers a boundary instance with sixteen edges not covered by the mentioned multiple-of-three Euler-tour construction.

## Limitations
The statement does not classify or count all optimal three-colourings, nor does it strengthen the existing universal three-colour upper bound at minimum degree at least five. The spectral obstruction is necessary, not sufficient, for arbitrary regular graphs. The originality assessment is relative to the inspected sources and searches; mathematically equivalent results may exist under other terminology. Independent validation and peer review have not been performed.

## References
1. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1 (first publicly posted 2026-05-22), especially Section 3. https://arxiv.org/abs/2605.23828
2. S. Antoniuk, M. Prorok, N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212v1 (first publicly posted 2026-06-30), Introduction and Section 1. https://arxiv.org/abs/2607.00212
3. P. Pękała, J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122v1 (first publicly posted 2026-08-04), Theorem 4 and Section 5. https://arxiv.org/abs/2608.04122
