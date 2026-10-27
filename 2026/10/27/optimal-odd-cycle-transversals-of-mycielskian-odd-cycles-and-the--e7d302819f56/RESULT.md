# Optimal odd-cycle transversals of Mycielskian odd cycles and their exchange graphs

## Finding

Let \(n\ge5\) be odd and let \(G_n=\mu(C_n)\) be the ordinary Mycielskian of the odd cycle. Label its original vertices \(x_i\), their shadows \(y_i\), and the apex \(w\), with indices \(i\in\mathbb Z/n\mathbb Z\). A vertex set \(D\) is an *odd-cycle transversal* (OCT) when \(G_n-D\) is bipartite. Then
\[
\operatorname{oct}(G_n)=3.
\]
Every minimum OCT is one of
\[
 A_i=\{w,x_i,x_{i+1}\},\qquad B_i=\{w,x_i,y_i\}\quad(i\in\mathbb Z/n\mathbb Z),
\]
with exactly five additional minimum OCTs when \(n=5\), namely
\[
 R_i=\{x_i,x_{i+1},x_{i+3}\}\quad(i\in\mathbb Z/5\mathbb Z).
\]
Thus the number of minimum OCTs is \(2n\) for odd \(n\ge7\), and \(15\) for \(n=5\).

Define the *single-vertex-exchange graph* \(\mathcal X_n\) on the minimum OCTs, joining distinct \(D,E\) when \(|D\cap E|=2\). For odd \(n\ge7\), this graph is the cycle on the \(A_i\), with one additional vertex \(B_i\) joined to both ends of edge \(A_{i-1}A_i\). It has \(2n\) vertices, \(3n\) edges, and is self-centered of radius and diameter \((n+1)/2\). If \(n=2k+1\ge7\), the numbers of unordered pairs at exchange distances \(d\) are
\[
 N_1=3n,\qquad N_d=4n\ (2\le d\le k),\qquad N_{k+1}=2n.
\]
For \(n=5\), the subgraph induced by the \(A_i,R_i\) is the Petersen graph: its outer pentagon is the \(A\)-cycle, its inner pentagram is the \(R\)-cycle, and its spokes are \(A_iR_i\). Each outer edge additionally receives the triangle vertex \(B_i\). Consequently \(\mathcal X_5\) has \(15\) vertices, \(25\) edges, radius and diameter \(3\), and unordered-pair distance counts \((25,55,25)\) at distances \(1,2,3\).

## Assumptions and scope

The ordinary Mycielskian used here is the simple undirected graph with vertex set
\[
\{x_i,y_i:i\in\mathbb Z/n\mathbb Z\}\cup\{w\}
\]
and edges \(x_ix_{i+1}\), \(x_iy_{i+1}\), \(y_ix_{i+1}\), and \(wy_i\) for each index \(i\); there are no further edges. The theorem is for *odd* \(n\ge5\) only. The term OCT is synonymous with vertex bipartization set or deletion set yielding an induced bipartite graph. Exchanges change precisely one selected vertex and require every intermediate set to be a minimum OCT. The distance enumerator counts unordered pairs, with distance zero excluded.

## Proof

**Step 1: Transversals containing the apex.** Assume \(w\in D\) and \(|D|=3\). The remaining original vertices induce paths obtained by removing selected \(x\)-vertices from the original odd cycle. Because \(w\) is deleted, the shadows have no edges among themselves. First, some \(x_i\) must be deleted, since the complete original odd cycle otherwise survives.

If exactly one original vertex \(x_i\) is deleted, the remaining deletion is a shadow, say \(y_j\). The odd cycle obtained by replacing \(x_i\) in the original cycle by \(y_i\) survives unless \(y_i\) is also deleted. Therefore \(j=i\), yielding precisely \(B_i\).

If two originals \(x_i,x_j\) are deleted, they must be adjacent. If nonadjacent, replacing *both* by \(y_i,y_j\) in the original odd cycle produces an intact odd cycle because there is no pair of consecutive replaced positions. Conversely, deleting adjacent originals \(x_i,x_{i+1}\) leaves the original layer as a path. Alternately two-color this path; every remaining shadow has at most two original neighbors, and when both survive they are two steps apart on that path and have the same color. Assign each shadow the opposite color of its original neighbors (arbitrarily when it has none). This is a bipartition, so all \(A_i\) work. The same argument with deleted \(x_i,y_i\) proves that all \(B_i\) work. (The sentence about two original deletions covers the case of exactly two \(x\)-vertices among the three deletions, since the third is \(w\).)

**Step 2: Transversals avoiding the apex.** Assume \(w\notin D\) and \(|D|=3\). In any bipartition of \(G_n-D\), all remaining shadows have the same color, opposite to that of \(w\). A retained original vertex \(x_i\) is therefore forced to have the color of \(w\) unless *both* its shadow neighbors \(y_{i-1},y_{i+1}\) were deleted. Call an original vertex not so forced *flexible*. Both endpoints of every original-original edge cannot be forced, so the flexible originals must cover the edges of the remaining original-layer graph.

Let \(s\) be the number of deleted original vertices. We have \(1\le s\le3\) because the original odd cycle must be hit. If \(s=1\), exactly two shadows are deleted, which can make at most one original flexible: for odd \(n\ge5\), each unordered pair \(\{y_{i-1},y_{i+1}\}\) determines at most one index \(i\). But the remaining original layer is the path on \(n-1\ge4\) vertices, whose edges cannot be covered by one flexible vertex. If \(s=2\), only one shadow is deleted, so no original is flexible; the remaining \(n-2\) originals would need to be independent in \(C_n\), impossible because \(n-2>(n-1)/2=\alpha(C_n)\). If \(s=3\), all shadows remain, so again all retained originals must be independent. This demands \(n-3\le(n-1)/2\), hence \(n\le5\). At \(n=5\), precisely the five choices leaving an independent pair of originals work. Written cyclically, their complementary three-element sets are exactly the \(R_i\).

**Step 3: Minimality.** No one- or two-vertex OCT exists for odd \(n\ge5\). With \(w\) deleted, one additional deletion must lie among the originals to meet the original odd cycle; replacing that original by its shadow gives a surviving odd cycle. With \(w\) retained, a size-two deletion removes at most two originals. If it removes no original, the original odd cycle survives; if it removes one, no original can be flexible (at most one shadow is deleted) and the remaining original path contains an edge with both endpoints forced; if it removes two, all shadows remain and the \(n-2\) retained originals cannot be independent. Monotonicity of bipartization under enlarging deletion sets then excludes smaller OCTs as well. Steps 1--3 prove the optimum and its complete classification.

**Step 4: Exchanges.** For odd \(n\ge7\), the complete classification gives the following and *only* these exchanges:
\[
 A_iA_{i+1},\quad A_iB_i,\quad A_iB_{i+1}\qquad(i\in\mathbb Z/n\mathbb Z).
\]
Indeed, two optimal three-sets exchange one vertex exactly when they share two entries. No two distinct \(B\)-sets do so. This is the stated triangular decoration of the cycle. Write \(n=2k+1\). The \(A\)-vertices follow cycle distances \(1,\ldots,k\); for each \(A_i\), there are two \(B\)-vertices at every distance \(1,\ldots,k\) and one at distance \(k+1\); for each fixed \(t\in\{1,\ldots,k\}\), there are \(n\) unordered pairs of \(B\)-vertices at distance \(t+1\). Summing the three classes \(A\!A,A\!B,B\!B\) gives the displayed \(N_d\) formula. Every \(A\)- and \(B\)-vertex has a partner at distance \(k+1\), establishing the common eccentricity.

At \(n=5\), the five extra \(R_i\) obey \(R_iR_{i+2}\) and \(R_iA_i\) exchanges and have no other neighbors. The \(A,R\) induced graph is therefore the usual Petersen presentation. Each \(B_i\) attaches to \(A_{i-1},A_i\). Direct distance counting by the three vertex classes gives \(25\) unordered pairs at distance one, \(55\) at distance two, and \(25\) at distance three; every vertex has eccentricity three. This can also be reproduced by the standalone finite verifier.

## Verification

The accompanying `oct_mycielski_verifier.py` constructs \(\mu(C_n)\) from the given edge rule, tests every deletion subset of cardinality at most three, and checks bipartiteness by two independent procedures: graph traversal with two-color propagation and parity union-find. It compares the complete resulting optimum family with the displayed formulas for every odd \(3\le n\le25\), including the out-of-scope triangular base case \(n=3\) as a boundary check. For odd \(n\in\{5,7,9,11,13\}\), it also constructs the exchange graph from pairwise intersections independently of its stated structural description, verifies exact adjacency, performs breadth-first searches from every optimum, and checks the claimed sizes and diameters. Run `python oct_mycielski_verifier.py`; success ends with `VERIFY_OK`. The universal theorem is established by the above argument, **not** by extrapolating those finite checks.

## Relationship to prior work

Odd-cycle transversal is a classical graph bipartization problem; Jansen and Kratsch (2011, arXiv:1107.3658) treat general structural kernelization, not a complete exact classification for this construction. The ordinary Mycielski graph construction is classical; the present result concerns all *minimum bipartizing sets* and their reconfiguration graph, not the chromatic number. Esperet and Stehlik (arXiv:1509.07716, first submitted 2015) study odd-cycle transversals and face-width in non-bipartite projective quadrangulations and prove general bounds, including their Theorems 1.2 and 4.2, rather than this exact family-wise solution-set formula and metric. Dabrowski et al. (2018, DOI:10.4230/LIPIcs.MFCS.2018.63) study the price of requiring independent OCTs for three-colorable classes; those results do not imply a classification of arbitrary OCTs in the four-chromatic graphs here. Related computations for other canonical graphs and other invariants of the Grötzsch graph do not imply the present formulas. These distinctions are about actual mathematical implications, not title matching.

## Limitations

The graph family is the *ordinary*, single-shadow-layer Mycielskian of odd cycles; no theorem is asserted for arbitrary or iterated Mycielskians, even cycles, weighted bipartization, or multi-vertex reconfiguration moves. All distances concern minimum transversals, not arbitrary bipartizing sets. This work gives an exact elementary proof and reproducibility checks, but does not claim an independent audit or an exhaustive worldwide novelty guarantee. Unindexed earlier calculations or nomenclature variants for graph vertex bipartization may contain related classifications.

## References

1. B. M. P. Jansen and S. Kratsch, *On Polynomial Kernels for Structural Parameterizations of Odd Cycle Transversal*, arXiv:1107.3658, submitted 19 July 2011. https://arxiv.org/abs/1107.3658
2. L. Esperet and M. Stehlik, *The width of quadrangulations of the projective plane*, arXiv:1509.07716, initially submitted 25 September 2015. https://arxiv.org/abs/1509.07716
3. K. K. Dabrowski, M. Johnson, G. Paesani, D. Paulusma, and V. Zamaraev, *On the Price of Independence for Vertex Cover, Feedback Vertex Set and Odd Cycle Transversal*, MFCS 2018, DOI:10.4230/LIPIcs.MFCS.2018.63. https://doi.org/10.4230/LIPIcs.MFCS.2018.63
4. SageMath, graph generators documentation, `MycielskiStep`, for the standard definition and identification of \(\mu(C_5)\) with the Grötzsch graph. https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/generators/families.html
