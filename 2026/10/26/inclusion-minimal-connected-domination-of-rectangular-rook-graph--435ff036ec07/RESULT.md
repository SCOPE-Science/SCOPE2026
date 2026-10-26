# Inclusion-minimal connected domination of rectangular rook graphs via one-sided-leaf trees

## Finding

For integers \(p,q\ge 2\), let \(R_{p,q}=K_p\square K_q\) be the rook graph whose vertices are the squares of a labeled \(p\)-by-\(q\) board, two squares adjacent when they share a row or a column. Define
\[
\mathcal M_{p,q}(z)=\sum_{D\in\mathfrak M(R_{p,q})}z^{|D|},
\]
where \(\mathfrak M(R_{p,q})\) is the family of **inclusion-minimal connected dominating sets**, not merely minimum-cardinality sets. Let \(S(a,b)\) be a Stirling number of the second kind (the number of partitions of an \(a\)-element set into \(b\) nonempty blocks). Then
\[
\boxed{\begin{aligned}
\mathcal M_{p,q}(z)&=\sum_{c=1}^{m}\binom qc p^{c-1}c!S(p-1,c)z^{p+c-1}\\
&\quad+\sum_{r=1}^{m}\binom pr q^{r-1}r!S(q-1,r)z^{q+r-1},\\
m&=\min\{p-1,q-1\}.
\end{aligned}}
\]
The two sums count **disjoint** families of selected-square sets.

**Structural characterization.** Identify a selected-square set \(D\) with the edge set of a bipartite graph \(H_D\), with a row vertex for each occupied row, a column vertex for each occupied column, and one edge for every selected square. Then \(D\) is an inclusion-minimal connected dominating set if and only if **exactly one** of the following holds:

1. \(H_D\) is a tree occupying all \(p\) rows, fewer than \(q\) columns, and every leaf of \(H_D\) is a row vertex (equivalently, every occupied column has degree at least two).
2. \(H_D\) is a tree occupying all \(q\) columns, fewer than \(p\) rows, and every leaf is a column vertex.

For \(2\le p\le q\), the possible sizes of inclusion-minimal connected dominating sets are **exactly**
\[
\{p,p+1,\ldots,2p-2\}\ \cup\ \{q,q+1,\ldots,q+p-2\}.
\]
Therefore the minimum and maximum such sizes are \(p\) and \(p+q-2\). If \(q\ge2p\), exactly \(q-2p+1\) consecutive intermediate cardinalities occur in neither family. In particular the maximality spectrum can have arbitrarily long gaps, already for \(R_{2,q}\), whose only sizes are \(2\) and \(q\). For square boards the minimum size is \(p\), with exactly \(2p\) minimum connected dominating sets.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled. Both dimensions satisfy \(p,q\ge2\), including the boundary \(p=q=2\). A connected dominating set \(D\) is a nonempty dominating set whose induced subgraph \(R_{p,q}[D]\) is connected. Inclusion-minimality means that no **proper subset** remains connected and dominating. Equivalently, deleting any single selected vertex must destroy domination or connectivity: if a proper connected dominating subset \(E\subsetneq D\) existed, the connectedness of \(R_{p,q}[D]\) would permit adjoining vertices of \(D\setminus E\) adjacent to the growing subset until it has size \(|D|-1\), while preserving connectivity and domination. The proof below gives direct deletion obstructions.

The result concerns **connected and inclusion-minimal** dominating sets. Ordinary dominating-set polynomials count larger families, and minimum-cardinality counts do not determine the complete polynomial above.

## Proof

**Step 1 (domination and connectivity).** Regard \(D\) as an edge set of the labeled complete bipartite graph on row vertices \(A\) and column vertices \(B\). The selected squares dominate the rook graph exactly when every row or every column is occupied: an unoccupied row together with an unoccupied column would have an unselected and undominated intersection square, and the converse is immediate. The induced rook graph \(R_{p,q}[D]\) is the line graph of the edge-supporting bipartite graph \(H_D\). Consequently the rook-induced subgraph is connected if and only if the edges of \(H_D\) form one connected edge-containing component.

**Step 2 (no simultaneous full coverage).** Suppose all \(p\) rows and all \(q\) columns are occupied. If \(H_D\) has a cycle, removing any edge on that cycle preserves connectivity and both kinds of coverage. Otherwise \(H_D\) is a tree with at least two edges; removing a leaf edge leaves all vertices occupied on the bipartition side opposite to the leaf. The remaining edges stay connected and dominate the rook graph. Therefore \(D\) is not inclusion-minimal. Thus an inclusion-minimal set can occupy exactly one complete side.

**Step 3 (the two types).** Suppose all rows are occupied but at least one column is unoccupied. A cycle edge could be removed without affecting connectedness or complete row coverage, so \(H_D\) is a tree. If an occupied column were a leaf, its unique incident edge could be removed: the connected remaining edges still occupy all rows (because the neighboring row is attached to the rest of a tree occupying at least two rows). Conversely, if \(H_D\) is such a tree and every occupied column has degree at least two, every removed edge either destroys connectivity by separating two components with selected edges (both endpoints previously had degree at least two), or isolates a row leaf. In the latter case both a row and a column are unoccupied, hence domination is destroyed. Any proper connected dominating subset would have a removable single edge as its first step, so this establishes inclusion-minimality. Interchanging the sides yields the second type.

**Step 4 (count by bipartite Prüfer words).** Fix the \(c\) occupied columns in the first type. A labeled tree on \(p\) row vertices and \(c\) column vertices has a bipartite Prüfer coding consisting of an arbitrary word of length \(c-1\) over the \(p\) row labels and a word of length \(p-1\) over the \(c\) column labels. Each column's degree is one plus the number of its appearances in the second word. Therefore every column has degree at least two precisely when the second word is surjective. There are \(p^{c-1}\) first words and \(c!S(p-1,c)\) surjective second words. The condition is possible exactly when \(1\le c\le p-1\), and the existence of an unoccupied column imposes \(c\le q-1\). There are \(\binom qc\) choices of occupied columns, and each associated tree has \(p+c-1\) edges. This proves the first sum; the second follows by symmetry.

**Step 5 (size spectrum).** Both Stirling factors are strictly positive throughout their indicated ranges. For \(p\le q\), the two families contribute precisely the integer intervals \([p,2p-2]\) and \([q,q+p-2]\). The assertions about extrema, gaps, and the \(2p\) minimum configurations for square boards follow.

## Verification

The accompanying standalone `verify.py` enumerates all vertex subsets of seven small labeled rook graphs, independently checks the original graph-theoretic definition by adjacency, breadth-first connectivity, and every single-vertex removal, and compares the complete coefficient dictionary with the Stirling formula. The tested board dimensions are \((2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4)\). Example outputs are \(\mathcal M_{3,3}(z)=6z^3+36z^4\) and \(\mathcal M_{4,4}(z)=8z^4+288z^5+768z^6\). The verifier also calculates independent incidence-tree signatures for each enumerated set and checks the two structural types, rather than only total coefficients.

These finite checks are consistency checks, not a proof of the infinite-family formula; the proof is Steps 1–5.

## Relationship to prior work

Stephan Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716 (first public version 2024-01-01), develops the polynomial of **all** dominating rook arrangements and identifies row/column coverage and the minimum dominating-set number. Its published text, including the principal polynomial theorem and its edge-cover treatment, does not furnish the connected, inclusion-minimal census in this finding. Applying ordinary domination coefficients does not select connected and irredundant configurations without additional incidence-graph structure.

F. N. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff, and K. Mann, *Enumerating Minimal Connected Dominating Sets*, ESA 2022, DOI 10.4230/LIPIcs.ESA.2022.1, addresses general graph enumeration algorithms, extremal numbers, and complexity, not a closed rook-graph family polynomial. Standard bipartite Prüfer coding supplies the tree-counting ingredient; that ingredient itself is not new. The new statement is the joint classification and exact polynomial for rectangular rook graphs.

## Limitations

The statement is restricted to rectangular rook graphs with both dimensions at least two. It does not classify minimal connected dominating sets of arbitrary line graphs or graphs formed by deleting board squares. No independent review has been performed. A literature search and inspection of the cited primary works did not identify identical coverage, but unindexed or differently phrased earlier results remain a priority risk.

## References

- Stephan Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716, first posted 2024-01-01. https://arxiv.org/abs/2401.00716 ; published full text https://cs.uwaterloo.ca/journals/JIS/VOL27/Mertens/mertens6.pdf .
- Faisal N. Abu-Khzam, Henning Fernau, Benjamin Gras, Mathieu Liedloff, Kevin Mann, *Enumerating Minimal Connected Dominating Sets*, ESA 2022. DOI 10.4230/LIPIcs.ESA.2022.1, https://drops.dagstuhl.de/storage/00lipics/lipics-vol244-esa2022/LIPIcs.ESA.2022.1/LIPIcs.ESA.2022.1.pdf .
- Wolfram Research, *GraphData* reference, entry for `MinimalConnectedDominationPolynomial`: https://reference.wolfram.com/language/ref/GraphData.html .
