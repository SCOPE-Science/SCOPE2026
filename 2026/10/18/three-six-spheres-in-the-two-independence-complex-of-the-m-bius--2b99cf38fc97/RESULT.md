# Three six-spheres in the two-independence complex of the Möbius–Kantor graph

## Finding

Let \(G\) be the Möbius–Kantor graph, realized as the generalized Petersen graph \(\operatorname{GP}(8,3)\). Its **two-independence complex** consists of all vertex subsets \(A\subseteq V(G)\) such that every connected component of the induced graph \(G[A]\) has at most two vertices. Then there is an integral homotopy equivalence

\[\operatorname{Ind}_2(G)\simeq S^6\vee S^6\vee S^6.\]

This is the same complex as the three-path-free **vertex-subset** complex; it is not the ordinary graph independence complex and is not an edge-matching complex. The reduced integral homology is \(\widetilde H_6\cong\mathbb Z^3\), with all other reduced homology zero.

## Assumptions and scope

The graph is finite, simple and explicitly fixed: its vertices are \(u_i,v_i\) for \(i\in\mathbb Z/8\mathbb Z\), with edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). For reproducibility identify \(u_i\) with integer \(i\) and \(v_i\) with \(8+i\), where \(0\le i<8\). A nonempty subset is a face precisely when it contains **no** three vertices forming a length-two path (the two edges of the path need not be an induced path). Equivalently, for every selected vertex, at most one of its three neighbors is also selected.

There are exactly 48 forbidden three-vertex subsets; each consists of one middle vertex together with two distinct neighbors. Every face is encoded by the integer bit mask of its selected vertices. The empty face is present in the abstract simplicial complex but, as usual, not included as a cell of the unreduced discrete-Morse CW model.

## Proof

**1. Complete complex.** Enumerating all \(2^{16}-1\) nonempty bit masks and rejecting any mask containing one of the 48 forbidden triples gives exactly 6,812 faces. The face counts in dimensions \(0\) through \(7\) are

\[(16,120,512,1324,2064,1840,816,120).\]

These integer claims are exhaustively reproduced by `verify_mk_ind2.py`, which constructs the graph from the three edge families above rather than relying on a stored face table.

**2. A full acyclic matching.** Let \(R\) initially be the set of all nonempty faces. Process vertex labels \(j=0,1,\ldots,15\) in that order. At stage \(j\), process the currently unpaired faces \(a\in R\) in increasing integer-mask order; whenever \(j\notin a\) and \(b=a\cup\{j\}\) also belongs to \(R\), pair \((a,b)\) and delete both from \(R\). The program reconstructs all 3,400 pairs. Orient every face-poset cover downward, except orient matched covers upward. It constructs **all 35,104 covers**, and a complete directed topological sort visits all 6,812 vertices. Thus the matching has no closed alternating path and is acyclic, not merely locally consistent. The critical cell masks are: dimension zero \([1]\); dimension four \([818]\); dimension five \([8916,10898,17304,17714]\); dimension six \([15048,18344,21924,23714,43684,58008]\). No other positive-dimensional critical cells remain. By discrete-Morse theory the original complex is homotopy equivalent to a CW complex with precisely these cells.

**3. Integral attaching degrees.** Orient each simplex by increasing vertex label. The signed incidence of a codimension-one face is \((-1)^j\) when the omitted vertex occupies position \(j\), starting from zero. In the algebraic Morse projection, a matched upper face is sent to zero and the matched lower face is expressed by the boundary equation for its upper partner; acyclicity makes these recursions terminating. Performing this signed integer calculation from the enumerated face poset gives the degree-five boundary (rows indexed by the critical four-cell, columns by the four critical five-cells)

\[D_5=\begin{pmatrix}-1&0&-1&-1\end{pmatrix},\]

and the degree-six boundary (rows indexed by the four critical five-cells, columns by the six critical six-cells)

\[D_6=\begin{pmatrix}
-1&0&0&0&1&-1\\
-1&0&-1&-1&1&0\\
0&1&0&0&0&1\\
1&-1&0&0&-1&0
\end{pmatrix}.\]

The product \(D_5D_6\) vanishes identically. Crucially, the \(-1\) in the first entry of \(D_5\) is the attaching degree of the first five-cell onto the four-sphere arising from the unique four-cell. The CW subcomplex consisting of the zero-cell, four-cell, and that first five-cell is the degree-\(-1\) mapping cone, hence contractible. Since it is a CW subcomplex, collapsing it induces a homotopy equivalence.

**4. Identify the cofiber.** The quotient CW complex has a point, three five-cells, and six six-cells. Its entire five-skeleton is \(S^5\vee S^5\vee S^5\). Its integral six-cell attaching matrix is obtained by deleting the first row of \(D_6\):

\[B=\begin{pmatrix}
-1&0&-1&-1&1&0\\
0&1&0&0&0&1\\
1&-1&0&0&-1&0
\end{pmatrix}.\]

The first three columns of \(B\) have determinant \(+1\). Consequently \(B\) is split-surjective over \(\mathbb Z\) and has Smith invariant factors \((1,1,1)\). Because the five-skeleton is four-connected, Hurewicz identifies all attaching maps in \(\pi_5(S^5\vee S^5\vee S^5)\) with their integral degree vectors. Integral unimodular row/column changes are realized by homotopy equivalences between wedges of five- and six-spheres. The attaching map is therefore equivalent to the projection given by three identity maps and three zero maps. Its cofiber has the claimed homotopy type \(S^6\vee S^6\vee S^6\). This proves the theorem integrally.

## Verification

`verify_mk_ind2.py` is a standalone Python 3 program using only the standard library. Execute `python3 verify_mk_ind2.py` in the directory containing it. It re-enumerates the graph, all 6,812 faces, all 3,400 matching pairs and all 35,104 Hasse covers; tests directed acyclicity; constructs the exact signed Morse matrices above; checks the unit minor; and separately computes all mod-two original simplicial boundary ranks. The raw exact output is in `verify_mk_ind2.out`. The independent mod-two boundary ranks are \((0,15,105,407,917,1147,693,120)\), yielding reduced mod-two Betti ranks \((0,0,0,0,0,0,3,0)\). This secondary check is corroborative, not a replacement for the integral attaching-map argument.

## Relationship to prior work

Sawant's 2026 paper defines higher independence complexes and proves vertex decomposability of \(\operatorname{Ind}_r(T)\) **for trees**. It explicitly observes that the three-path-free complex is \(\operatorname{Ind}_2\), but its tree theorem does not apply to the cubic cyclic graph \(\operatorname{GP}(8,3)\). The 2023 work of Abdelmalek and collaborators focuses on chordal-graph and shedding-vertex questions, and does not state an exact homotopy classification of the present nonchordal graph. Distinct indexed calculations exist for the **ordinary** independence complex and for the **edge-matching** and **three-cut** complexes of the Möbius–Kantor graph; those are different functors and none implies this two-independence homotopy equivalence. Likewise a two-independence classification for the **Petersen** graph concerns a different generalized Petersen graph.

## Limitations

This is an exact result for one canonical sixteen-vertex graph, not a theorem covering all generalized Petersen graphs, arbitrary cubic graphs, or larger incidence graphs. The program exhaustively certifies finite matching/computation premises; the claimed homotopy type also requires the mathematical CW cancellation and Hurewicz arguments given above. Literature/database searches cannot establish global uniqueness; overlapping unindexed or differently named results remain possible. A particularly relevant same-graph source is Knill (2026), whose abstract concerns Cayley-group, metric and Lefschetz topology, but whose full manuscript could not be inspected here; possible unreported overlap remains a residual risk. Independent scientific audit has not been performed.

## References

- R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first public version 24 May 2026, https://arxiv.org/abs/2605.25150. Especially Theorem 1.1 / 3.6 and the equivalence of three-path-free complexes with \(\operatorname{Ind}_2\) on page 2.
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, International Journal of Algebra and Computation 33 (2023), 481–498; bibliographic data as cited in Sawant.
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, for the discrete-Morse homotopy equivalence.
- O. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799 (first public 29 May 2026), https://arxiv.org/abs/2605.30799. Its abstract concerns the graph’s Cayley, metric, and Lefschetz structures; the full manuscript was not accessible for this comparison.
- `verify_mk_ind2.py` and `verify_mk_ind2.out`, included in this package (full finite certificate).
