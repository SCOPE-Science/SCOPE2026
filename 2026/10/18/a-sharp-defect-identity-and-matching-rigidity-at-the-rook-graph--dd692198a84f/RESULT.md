# A sharp defect identity and matching rigidity at the rook-graph colouring threshold

## Finding

For every integer \(n\ge2\), consider a proper colouring of the rook graph \(R_{n,n}=K_n\square K_n\) using colours from a named palette of size \(n+1\). A vertex is *defective* when no colour appears exactly once in its open neighbourhood. Let \(a_s\) denote the number of board rows in which palette colour \(s\) is absent, and let \(U\) denote the number of defective vertices. Then the **exact defect identity** is

\[
U=\sum_{s=1}^{n+1}a_s^2,\qquad \sum_{s=1}^{n+1}a_s=n.
\]

More precisely, when the defective cells are viewed as edges between the row-index set and the column-index set, their graph is a disjoint union of complete balanced bipartite components \(K_{a_s,a_s}\) over symbols with \(a_s>0\). In particular, \(U\ge n\), and **equality holds if and only if every colour is absent from at most one row**. In the equality case the defective vertices occupy the cells of a perfect matching between rows and columns. For every \(n\ge2\) there exists a proper \(n+1\)-palette colouring attaining equality, so the minimum unavoidable defect is **exactly** \(n\). The defect count always has the same parity as \(n\) and is at most \(n^2\), with the latter endpoint attained by a Latin-square colouring with one unused palette colour.

The established adjacent-vertex-distinguishing edge-colouring theory already implies the numerical fact \(\chi_{\mathrm{pcf}}(R_{n,n})=n+2\). The contribution claimed here is the stronger **quantitative failure census and classification of all minimum-defect configurations one colour below that threshold**, not a priority claim for that numerical chromatic value.

## Assumptions and scope

Throughout \(n\) is an integer with \(n\ge2\). The graph \(R_{n,n}\) has one vertex \((i,j)\) per cell of an \(n\)-by-\(n\) board; distinct cells are adjacent precisely when they share a row or a column. All colourings are vertex colourings with named colours, and a palette of size \(q\) may contain unused colours. A proper colouring makes all symbols distinct in each row and each column. A witness for \((i,j)\) means a colour occurring exactly once among the \(2(n-1)\) neighbours of that vertex, excluding the vertex itself. The defect statement quantifies over **all** proper square-board colourings using at most \(n+1\) named colours, including colourings with an unused symbol. No asymptotic assumption is made.

## Proof

**1. Row-column witness lemma.** Properness means that a colour appears at most once in any row or column. For a cell \((i,j)\) of colour \(c\), let \(S_i\) and \(T_j\) denote its row and column colour sets. Every colour \(s\ne c\) occurs among the open neighbours precisely \(\mathbf1_{s\in S_i}+\mathbf1_{s\in T_j}\) times, because the row and column meet only at the original cell. Thus the cell is defective exactly when \(S_i=T_j\): equality rules out a uniquely occurring neighbour colour, and inequality provides a witness in the symmetric difference. This lemma also shows why proper conflict-free colourings of rook graphs are equivalent to adjacent-vertex-distinguishing proper edge colourings of the corresponding complete bipartite graphs; each board cell represents an edge, and rows/columns are its endpoints.

**2. One missing colour at each row and column.** Because the matrix is \(n\)-by-\(n\) and its palette has size \(n+1\), each row omits a unique symbol \(r_i\), while each column omits a unique symbol \(c_j\). Their palettes coincide precisely when \(r_i=c_j\). Therefore the defective cells are exactly those pairs \((i,j)\) satisfying this equality.

**3. The exact counting identity.** Let \(a_s=|\{i:r_i=s\}|\) and \(b_s=|\{j:c_j=s\}|\). Colour \(s\) appears at most once per row and column, so its total multiplicity equals both \(n-a_s\) and \(n-b_s\). Hence \(a_s=b_s\) for every palette symbol. The rows omitting \(s\) and columns omitting \(s\) span every corresponding defective cell, and no defective cell connects sets belonging to different symbols. This is exactly a vertex-disjoint union of bicliques \(K_{a_s,b_s}=K_{a_s,a_s}\) on the indexed row/column bipartition. Counting their edges gives

\[
U=\sum_{s=1}^{n+1}a_sb_s=\sum_{s=1}^{n+1}a_s^2.
\]

Each row misses precisely one colour, so \(\sum_s a_s=n\). For every nonnegative integer \(a_s\), we have \(a_s^2\ge a_s\), with equality exactly when \(a_s\in\{0,1\}\). It follows that \(U\ge n\), with equality precisely when all omitted-row colours are pairwise distinct. Since the multisets of row-missing and column-missing colours are identical, those \(n\) defects then use every row and every column exactly once: they form a perfect matching. Conversely, every equality case has this matching structure. Moreover \(a_s^2\equiv a_s\pmod2\), so \(U\equiv n\pmod2\), and \(U\le n^2\) by nonnegativity and \(\sum a_s=n\).

**4. Sharpness and the upper endpoint.** Take the cyclic addition Latin square of order \(q=n+1\), in which entry \((i,j)\) is \(i+j\pmod q\), and delete its row \(0\) and column \(0\). The remaining \(n\)-by-\(n\) array is proper; surviving row \(i\) omits exactly colour \(i\), and surviving column \(j\) omits exactly colour \(j\). The defects are exactly its \(n\) diagonal cells, forming a perfect matching. For the opposite endpoint, colour the \(n\)-by-\(n\) array by \(i+j\pmod n\) and regard it as a colouring with one additional unused palette colour. All rows and columns have the same colour set, so every one of the \(n^2\) cells is defective. This finishes the proof for every \(n\ge2\).

## Verification

The standalone standard-library script `verification/check_rook.py` checks the row/column witness criterion directly from neighbour multiplicities. It tests constructive rectangular and square proper conflict-free colourings as background checks, along with the sharp deleted-Latin-square defect example. It independently enumerates every proper labelled matrix for square orders \(n=2,3\) and palettes \(q\in\{n,n+1,n+2\}\), and tests the new defect identity and matching equality cases on all \(n+1\)-palette matrices. This includes all \(1{,}056\) proper four-palette colourings of the three-by-three board. The finite checks support the infinite proof, but do not substitute for it.

## Relationship to prior work

The row-column palette criterion is exactly the classical translation of **adjacent-vertex-distinguishing edge colourings** from \(K_{n,n}\) to the line graph \(L(K_{n,n})=R_{n,n}\). This is an essential equivalence, not merely an analogy. Balister, Győri, Lehel and Schelp (2007) prove the general bound \(\chi'_a(G)\le\Delta(G)+2\) for bipartite graphs and discuss the one-extra-colour obstruction for regular bipartite examples. Combining that upper bound with the standard omission-counting obstruction yields the known exact numerical chromatic value \(\chi_{\mathrm{pcf}}(R_{n,n})=n+2\); that value is explicitly excluded from the novelty claim here. The new object studied here is the **number and spatial structure of vertices still violating the witness condition in every almost-admissible colouring** using \(n+1\) symbols, especially the exact sum-of-squares formula, its balanced-biclique decomposition, its sharp minimum, and the perfect-matching rigidity of minimizers. The 2007 article's published first-page lower-bound argument is related but does not state this defect distribution or classify all its minimum-defect colourings.

Pradhan and Sharma's 11 August 2026 preprint studies complexity and algorithms for the same proper conflict-free vertex-colouring invariant. Its accessible abstract lists block graphs, proper interval graphs, chain graphs and pseudo-split graphs, not rook-graph defect enumerations; the complete text was not accessible for thorough comparison. Jiménez and collaborators' study gives general quasi-line-graph bounds for the same parameter (Theorem 1.10), but not a defect census for proper colourings below the threshold. An earlier complete-multipartite evaluation already includes the four-cycle \(R_{2,2}\) value, but does not count subthreshold defects. Searches under the classical edge-colouring aliases and the PCF terminology found no theorem implying the exact quantitative claim; this is not a proof of priority.

## Limitations

The claim concerns proper vertex colourings of square rook graphs **with precisely a palette budget of \(n+1\)**, including possible unused colours. It does not enumerate all proper colourings having each allowed defect profile, and it does not claim the numerical chromatic threshold as new. Neither the 2007 classical edge-colouring theory nor the inaccessible portions of the 2026 motivating preprint have been checked exhaustively for equivalent quantitative formulations; bibliographic priority remains subject to independent scrutiny. Computation covers bounded cases only. No independent audit or formal proof certification has been conducted.

## References

1. D. Pradhan and V. Sharma, *Complexity and algorithms for proper conflict-free coloring in graphs*, arXiv:2608.10874, first posted 11 August 2026. https://arxiv.org/abs/2608.10874
2. P. N. Balister, E. Győri, J. Lehel and R. H. Schelp, *Adjacent Vertex Distinguishing Edge-Colorings*, SIAM J. Discrete Math. 21 (2007), 237–250, DOI:10.1137/S0895480102414107. Full author-hosted text: https://www.memphis.edu/msci/people/pbalistr/avdec.pdf
3. A. Jiménez, K. Knauer, C. N. Lintzmayer, M. Matamala, J. P. Peña, D. A. Quiroz, M. Sambinelli, Y. Wakabayashi, W. Yu and J. Zamora, *Boundedness for proper conflict-free and odd colorings*, arXiv:2308.00170, 2023; Theorem 1.10. https://arxiv.org/abs/2308.00170
4. *Exact proper conflict-free colorings of complete multipartite graphs*, published mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-proper-conflict-free-colorings-of-complete-multipartite-gr--5943975f038c (relevant only to the smallest four-cycle boundary).
