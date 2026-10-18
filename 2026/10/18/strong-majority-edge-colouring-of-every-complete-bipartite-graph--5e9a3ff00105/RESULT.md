# Strong-majority edge-colouring of every complete bipartite graph

## Finding

Let \(K_{a,b}\) be the finite simple complete bipartite graph with integers \(2\le a\le b\). An edge-colouring is **strong-majority** when, for each edge and each colour, no more than half the edges adjacent to that edge have that colour. The **strong-majority index** \(\operatorname{Maj}'(G)\) is the least number of colours in such an edge-colouring. Then

\[
\boxed{\operatorname{Maj}'(K_{a,b})=
\begin{cases}
2,&a=2\text{ and }b\text{ is even},\\
4,&(a,b)\in\{(3,4),(4,5)\},\\
3,&\text{otherwise}.
\end{cases}}
\]

The four-colour obstruction at \(K_{4,5}\) was already known; the contribution is the complete two-parameter classification, the additional \(K_{3,4}\) obstruction, and the classification of all optimal two-colourings. Specifically, for even \(b\ge4\), all named two-colourings of \(K_{2,b}\) are obtained by assigning one colour to both edges at each of \(b/2\) vertices on the size-\(b\) side and the other colour to the remaining \(b/2\) vertices. Their number is \(\binom{b}{b/2}\). For \(K_{2,2}\), there are exactly four named two-colourings.

## Assumptions and scope

The vertices on the size-\(a\) side are indexed by \(0\le i<a\), those on the size-\(b\) side by \(0\le j<b\), and an edge is denoted \((i,j)\). Colours are labels, not necessarily a proper edge-colouring. Adjacent edges share a vertex, and the edge itself is never counted as adjacent to itself. The neighborhood of each edge has exactly \(a+b-2\) edges, so the maximum permitted occurrences of each colour there is \(t=\lfloor(a+b-2)/2\rfloor\).

For any given colour \(\gamma\), write \(r_i(\gamma)\) for its number of occurrences in row \(i\), and \(s_j(\gamma)\) for its number of occurrences in column \(j\). The exact admissibility test is

\[
r_i(\gamma)+s_j(\gamma)-2\mathbf1_{\{c(i,j)=\gamma\}}\le t
\quad\text{for every }i,j,\gamma.\tag{1}
\]

The indicator is doubled because \((i,j)\) is included once in each of its row and column counts but is excluded from its own edge-neighborhood. Formula (1) also applies to colours not used on a particular edge.

## Proof

**1. The two-colour rigidity.** Write two colours as signs \(\epsilon_{ij}\in\{-1,+1\}\). As the number of adjacent edges of each colour must both be at most half the neighbourhood, they must be equal. Set \(R_i=\sum_j\epsilon_{ij}\), \(C_j=\sum_i\epsilon_{ij}\), and \(S=\sum_{i,j}\epsilon_{ij}\). The equality of adjacent-colour counts is exactly

\[
R_i+C_j-2\epsilon_{ij}=0.\tag{2}
\]

Summing (2) over each row and column gives

\[
(b-2)R_i+S=0,\qquad (a-2)C_j+S=0.\tag{3}
\]

If \(a,b>2\), (3) forces all \(R_i\) to be equal and all \(C_j\) to be equal. Equation (2) then forces every \(\epsilon_{ij}\) equal, a contradiction. If \(a=2<b\), the column relation forces \(S=0\), the row relation forces \(R_i=0\), and (2) forces \(\epsilon_{1j}=\epsilon_{0j}\) at every column. Thus \(b\) is even and exactly half the columns have each sign. Conversely, every such split satisfies (2). Finally, \(K_{2,2}\) has line graph a four-cycle; its two-colourings satisfying (2) are the two opposite-row patterns and two opposite-column patterns, exactly four. One colour fails because every edge has a nonempty neighbourhood.

**2. Three colours whenever \(a=2\).** Give the two edges in column \(j\) the colour \(j\bmod3\). Every edge sees exactly as many edges of colour \(\gamma\) as the number of columns of that colour, since its other edge in the same column compensates for removing itself from its row. Every colour occupies at most \(\lceil b/3\rceil\) columns, and \(\lceil b/3\rceil\le\lfloor b/2\rfloor\) for \(b\ge3\). For \(b=2\), use the two distinct column colours. Thus three colours always suffice on this strip (and two suffice exactly in the even cases).

**3. A universal three-colour construction except four small pairs.** For \(a,b\ge3\), colour edge \((i,j)\) by \((i+j)\bmod3\). Each colour appears at most \(\lceil b/3\rceil\) times in any row and at most \(\lceil a/3\rceil\) times in any column. Hence (1) holds whenever

\[
\left\lceil\frac a3\right\rceil+\left\lceil\frac b3\right\rceil
\le \left\lfloor\frac{a+b-2}{2}\right\rfloor.\tag{4}
\]

For \(a+b\ge14\), the left side is at most \((a+b+4)/3\), which is at most \((a+b-2)/2\). For \(a+b\le13\), direct evaluation of the two sides of (4) shows that the only failures with \(3\le a\le b\) are \((3,4),(4,4),(4,5),(4,7)\).

The following two matrices, with colours \(0,1,2\), directly satisfy (1), completing the three-colour upper bound at the two nonexceptional failures:

\[
K_{4,4}:\quad
\begin{pmatrix}0&2&2&0\\1&2&0&1\\1&0&1&2\\0&1&2&0\end{pmatrix},
\qquad
K_{4,7}:\quad
\begin{pmatrix}
0&2&1&0&1&2&0\\
1&2&0&2&2&0&1\\
1&0&1&2&0&1&2\\
0&1&2&0&2&1&0
\end{pmatrix}.\tag{5}
\]

For \((a,b)=(3,4)\) or \((4,5)\), the four-colour assignment \(c(i,j)=(i+j)\bmod4\) satisfies (1): the row/column maxima are respectively \((1,1)\) and \((2,1)\), giving upper bounds \(2=t\) and \(3=t\). It remains to show that three colours fail in exactly these cases.

**4. The new \(K_{3,4}\) obstruction.** Fix any one colour and let \(H\) be the subgraph formed by its edges. Double-counting the incidences of this colour with the twelve edge-neighbourhoods gives \(5|E(H)|\le12\cdot2\), so \(|E(H)|\le4\). If \(K_{3,4}\) used three colours, each colour class would have exactly four edges.

We now show that every feasible four-edge colour class is precisely a \(K_{2,2}\). Let \(r_i,s_j\) denote its row and column degrees. A row of degree three would have a nonedge at which \(r_i+s_j>2\); a row of degree four fails (1) at any of its own edges. Thus every row degree is at most two. A column of degree three would make every incident row degree at most one by (1), contradicting four total edges. Thus every column degree is at most two. Some row has degree two. Every nonedge in that row must have column degree zero; otherwise the corresponding count is at least three. Hence all four edges lie in the two columns occupied by that row, each of which must have degree two. At a column of degree two, its omitted row must have degree zero, again by (1). The two columns therefore occupy exactly the same two rows, giving \(K_{2,2}\).

But in any decomposition of the twelve edges into three such \(K_{2,2}\) colour classes, each of the four columns would have even total degree, while it actually has degree three. Contradiction. Thus \(\operatorname{Maj}'(K_{3,4})=4\).

**5. The previously known \(K_{4,5}\) obstruction, independently reconstructed.** Let \(H\) be one colour class in \(K_{4,5}\). Now (1) reads \(r_i+s_j-2\mathbf1_H(i,j)\le3\). A row of degree four has a missing-column violation and a row of degree five violates (1) on its own edges, so no row degree exceeds three. If some row has degree three, its two missing columns have degree zero; the other three columns have degree at most two unless the case below already applies, so \(|E(H)|\le6\). A column of degree four forces all its incident row degrees to be at most one, giving at most four edges. A column of degree three forces the fourth row to have degree zero and each other row to have degree at most two, giving at most six edges. In the remaining case all row and column degrees are at most two. If one bipartition side has no degree-two vertex, there are at most five edges. Otherwise, every degree-two row and degree-two column must meet in an edge, since a nonedge between them violates (1). Therefore at most two rows can have degree two, and counting over the four rows gives \(|E(H)|\le 2\cdot2+2\cdot1=6\). Thus every colour class has at most six edges, and three classes cover at most eighteen of the twenty edges. Hence \(\operatorname{Maj}'(K_{4,5})=4\).

Parts 1–5 jointly prove the full classification, including all parameter boundaries.

## Verification

Run `python3 artefacts/check_biclique.py` in a directory containing this file and the artefacts subdirectory. The script uses only the Python standard library, independently checks (1) for the explicit matrices and modular constructions for \(2\le a\le20\), \(a\le b\le30\), checks exhaustive two-colour cases, and enumerates all \(2^{12}\) one-colour subsets of \(K_{3,4}\) and all \(2^{20}\) of \(K_{4,5}\). The observed one-colour maximum cardinalities are four (18 feasible maximizers, all rectangles) and six (1,900 feasible maximizers), respectively. These finite checks support, but do not replace, the general proof and the independent small-exception arguments above.

## Relationship to prior work

Kalinowski, Kamyczura, Pilśniak and Woźniak introduced the strong-majority edge index and proved general bounds in their May 22, 2026 preprint [1]. Antoniuk, Prorok and Salia subsequently proved a general five-colour bound [2]. Pękała and Przybyło [3] proved the three-colour upper bound for minimum degree at least five and discussed the sharp \(K_{4,5}\) obstruction; a public mathematical record [4] independently establishes the latter obstruction in a generalized threshold setting. Thus neither the existence of three colours when both parts have order at least five nor the \(K_{4,5}\) obstruction is claimed as new. The present theorem adds the complete boundary classification across all \(a,b\ge2\), including \(K_{3,4}\) and the two-colour rigidity/census; it is not obtained simply by substituting the family into any quoted general minimum-degree bound.

## Limitations

The theorem concerns only ordinary strong-majority edge colourings with the threshold one half, not the generalized threshold \(1/k\), list-colourings, multigraphs, or prescribed palette class sizes. The finite enumerations are exhaustive only for their explicitly stated graphs. The three- and four-colour constructions are infinite-family proofs because of the preceding arithmetic bounds. A complete full-text comparison with [3] could not be obtained through available lawful access paths; the known overlapping \(K_{4,5}\) case is expressly excluded from novelty, and further unindexed or privately circulated equivalent results remain a bibliographic risk. No external independent validation is asserted.

## References

[1] R. Kalinowski, M. Kamyczura, M. Pilśniak and M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828, first public May 22, 2026, https://arxiv.org/abs/2605.23828 .

[2] S. Antoniuk, M. Prorok and N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212, first public June 30, 2026, https://arxiv.org/abs/2607.00212 .

[3] P. Pękała and J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122, first public August 4, 2026, https://arxiv.org/abs/2608.04122 .

[4] *Exact bipartite threshold for generalized strong-majority edge colouring*, public research record, September 17, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE005 .
