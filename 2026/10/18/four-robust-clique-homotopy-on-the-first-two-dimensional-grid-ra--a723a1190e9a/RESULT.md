# Four-robust clique homotopy on the first two-dimensional grid range and square-symmetry characters

## Finding
For \(3\le m\le n\le5\), let \(G_{m,n}=P_m\square P_n\) and let \(K_{m,n}=\operatorname{Cliq}_4(G_{m,n})\). Then
\[
|K_{m,n}|\simeq\bigvee^{\binom{(m-1)(n-1)}{3}}S^5.
\]
The corresponding wedge multiplicities for \((m,n)=(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)\) are \(4,20,56,84,220,560\). The \((4,4)\) homotopy classification was established previously and is independently reproduced here only for a complete initial finite range; the new homotopy classifications are the other five cases.

For the three square cases, let \(D_4\) act by the eight square symmetries. Order its elements as identity, quarter-turn, half-turn, inverse quarter-turn, horizontal reflection, vertical reflection, main-diagonal reflection, and other-diagonal reflection. The complete degree-five rational homology characters are:

| Square side | Character in specified element order | Decomposition multiplicities \((A_1,A_2,B_1,B_2,E)\) |
| --- | --- | --- |
| 3 | (4,0,0,0,0,0,-2,-2) | (0,1,1,0,1) |
| 4 | (84,0,4,0,-10,-10,-10,-10) | (6,16,11,11,20) |
| 5 | (560,0,0,0,0,0,-28,-28) | (63,77,77,63,140) |

Here \(A_1,A_2,B_1,B_2\) denote the usual four rational one-dimensional representations of \(D_4\), and \(E\) its two-dimensional reflection representation. In particular the characters contain topological information absent from the known ordinary Betti-number tables.

## Assumptions and scope
Graphs are finite, simple and undirected, with \(P_m\) having exactly \(m\) vertices. Vertices of \(G_{m,n}\) are indexed by \((i,j)\), \(0\le i<m\), \(0\le j<n\), adjacent when Manhattan distance is one. For \(W\subseteq V(G_{m,n})\), \(\alpha(G_{m,n}[W])\) is the maximum number of pairwise nonadjacent vertices in its induced graph. Thus a nonempty set is a simplex of \(K_{m,n}\) exactly when it contains no independent four-subset. All homotopies and homology assertions are integral unless a coefficient field is specified. The classification asserts only the six displayed finite grids and does not establish the conjectured behavior for arbitrarily large grids or all square sequences.

## Proof
Every grid is bipartite. An admissible subset can contain at most three vertices of either bipartition color, since any four same-color vertices would be independent. Consequently every simplex has at most six vertices. The complete list of nonempty faces is obtained by enumerating all vertex subsets of cardinality one through six and discarding exactly those containing one of the exhaustively enumerated independent four-subsets. The bundled checker reconstructs both the graph adjacency and the independent four-subsets from these definitions, rather than trusting a stored face list.

The bundled binary certificate records a sequence of elementary simplicial free-face removals and declarations of residual maximal critical faces for each grid. A pair \((\sigma,\tau)\) is removed only after the verifier checks that \(\sigma\subset\tau\), that the two faces differ by one vertex, that \(\tau\) is the unique remaining immediate coface of \(\sigma\), and that \(\tau\) is maximal in the remaining complex. A critical face is likewise removed only when it is maximal. After all removals, the verifier independently constructs the entire original Hasse diagram, reverses every matched incidence, and checks acyclicity by an exhaustive topological sort. The six matchings have, respectively, \(192,697,1792,2363,5753,13518\) matched face pairs and exactly one critical vertex plus \(4,20,56,84,220,560\) critical five-simplices. The face counts for the six complexes are \(389,1415,3641,4811,11727,27597\). These checks yield a genuine acyclic discrete Morse matching, not just homology ranks. Forman's finite simplicial discrete Morse theorem reduces each geometric realization to a CW complex with a single zero-cell and the asserted number of five-cells, and no cells of intervening dimensions. All five-cell attaching maps therefore land in the one-point four-skeleton and are null; the complex is a wedge of five-spheres.

To compute the square symmetry character, the checker exhaustively enumerates all eight coordinate permutations realizing \(D_4\). For each symmetry \(g\), the reduced Lefschetz number is
\[
-1+\sum_{\emptyset\ne\sigma\in K_{n,n},\ g\sigma=\sigma}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]
This is the alternating trace on the reduced oriented simplicial chain complex, with \(\operatorname{sgn}(g|_\sigma)\) evaluated using the canonical increasing vertex order. Because the reduced rational homology is supported only in degree five, its trace equals the negative of this reduced Lefschetz number. The exact values are those in the table. The multiplicity vector is obtained by inner products with the five ordinary rational irreducible characters of \(D_4\); all multiplicities are nonnegative integers and reproduce the homology dimensions.

## Verification
Reproduce the complete calculation using only the Python standard library: place `grid4_morse.py` and `grid4_morse_certificate.json.gz` side by side and execute `python grid4_morse.py`. This independently regenerates every nonempty face and forbidden independent four-subset, checks the recorded individual free-face incidences, confirms that every face is accounted for, verifies the complete matched-Hasse directed acyclicity, and evaluates all square symmetry characters and representation decompositions. The script was executed successfully on the exact two files included here. The face vectors, with entry \(f_i\) at simplex dimension \(i\), are:

| Grid | \((f_0,f_1,f_2,f_3,f_4,f_5)\) |
| --- | --- |
| 3 by 3 | (9,36,84,120,100,40) |
| 3 by 4 | (12,66,220,434,466,217) |
| 3 by 5 | (15,105,455,1089,1323,654) |
| 4 by 4 | (16,120,560,1415,1788,912) |
| 4 by 5 | (20,190,1140,3343,4594,2440) |
| 5 by 5 | (25,300,2300,7626,11194,6152) |

The independently computed reduced Euler characteristic equals minus the claimed number of spheres for each case. The exact finite certificate is a proof of these six cases because every finite incidence and acyclicity condition can be rechecked; merely observing a pattern of ranks would not prove a general theorem.

## Relationship to prior work
Filakovský [1] proves the wedge formula for robust clique parameter \(k=2,3\) on all rectangular grids, and for arbitrary \(k\) on edge-only square attachment sequences. The same paper explicitly identifies the \(k>3\) corner-gluing step as an unresolved obstacle and formulates a more general wedge conjecture. The six grids here concern \(k=4\), including genuine corner-gluing, which is not covered by those results. Bayer et al. [2] report several corresponding **Betti numbers** for the Alexander-dual *total* four-cut complexes; those tables do not supply a homotopy classification of these robust clique complexes, an explicit acyclic matching for them, or their \(D_4\) characters. Chandrakar et al. [3] treat total cut complexes for two-row grids at general parameter and for three-row grids at parameter three; neither proves the present four-robust claim. The nonequivariant \(4\times4\) homotopy statement had already been established separately and is not claimed as new here. The novelty is a five-case initial homotopy extension and the complete square-dihedral homology modules for sizes three through five.

## Limitations
This is an exact finite classification, not an induction in grid size. The specific ranks for several cases follow from published Betti-number data or conjectured formulas; what is established beyond them is actual integral homotopy type, while the symmetry characters provide additional rational equivariant invariants. Published literature outside the inspected materials or unindexed equivalent statements remain possible. The certificate establishes non-equivariant homotopy equivalences and separately computes equivariant homology characters; it does not claim the exhibited Morse matchings themselves are equivariant or that the homotopy equivalences are \(D_4\)-equivariant. No independent audit has been performed.

## References
1. Marek Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365v4 (first posted 11 February 2026), Sections 1–3, in particular Theorem 1, Corollary 3, and Conjecture 5. https://arxiv.org/html/2602.11365
2. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Total cut complexes of graphs*, arXiv:2209.13503, Section 5, Tables 2–3 and Conjecture 5.2. https://arxiv.org/pdf/2209.13503
3. H. Chandrakar, N. R. Hazra, D. Rout, and A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646, Introduction and Theorem 1.1. https://arxiv.org/pdf/2408.07646
