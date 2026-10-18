# The Clebsch two-independence complex is a four-sphere with sign-twisted symmetry

## Finding

Let \(C\) be the degree-five Clebsch graph, also called the folded five-cube or the Greenwood–Gleason graph. The two-independence complex \(X=\operatorname{Ind}_2(C)\) of all induced vertex subsets whose connected components have at most two vertices has exact **integral homotopy type**

\[
X\simeq S^4.
\]

The induced automorphism action on its rank-one integral fourth homology is the sign character of the natural quotient \(\operatorname{Aut}(C)\cong(\mathbb Z/2)^4\rtimes S_5\):

\[
\widetilde H_4(X;\mathbb Z)\cong\mathbb Z_{\mathrm{sgn}\circ\pi},
\qquad \pi:\operatorname{Aut}(C)\longrightarrow S_5.
\]

In particular the 16 translations act trivially, every transposition of the five canonical Cayley directions acts by \(-1\), and the whole automorphism group fixes no nonzero integral fourth-homology class. These statements concern the degree-five Clebsch graph, **not** its ten-regular complement.

## Assumptions and scope

Use the 16 vertices of \(V=\mathbb F_2^4\), encoded by the integers \(0,1,\ldots,15\) with bitwise XOR \(\oplus\). Join distinct vertices \(a,b\) precisely when \(a\oplus b\in\{1,2,4,8,15\}\). The graph has 40 edges and degree five. A face of \(X\) is a subset \(U\subseteq V\) for which every vertex of the induced graph \(C[U]\) has induced degree at most one. Equivalently, \(U\) contains no three distinct vertices forming a path of length two in \(C\). The empty face is included in the abstract complex.

This is the higher-independence parameter \(r=2\), distinct from the ordinary independence complex \(r=1\), the edge matching complex, and the Lovász neighborhood complex. Here \(X\) has 2,142 nonempty faces, with face counts by dimensions \(0,\ldots,7\) equal to \((16,120,400,660,576,280,80,10)\); it is nonpure and seven-dimensional.

## Proof

**1. Exhaustive face definition.** The graph is reconstructed solely from the five displayed XOR increments. For each vertex, choose two of its five neighbors; this produces precisely 160 distinct forbidden three-vertex subsets. The verifier evaluates all \(2^{16}\) subsets independently by the absence of a forbidden triple and by direct induced-degree counting; the truth values agree for every subset. Thus its list of 2,142 nonempty faces equals \(X\) without sampling or a graph lookup table.

**2. An acyclic integral Morse reduction.** Process vertex labels in the fixed order

`(12,11,7,13,6,0,8,3,9,4,10,2,5,14,15,1)`.

At each stage, pair every still-unpaired nonempty face not containing the selected vertex with its still-unpaired union with that vertex. Each eligible lower face is paired at most once, and matching only pairs codimension-one faces. There are exactly 1,069 disjoint matching pairs. Direct the face-poset cover relation upward for a matched pair and downward for every other covering. Enumerating all 9,280 such covers gives a complete directed topological ordering of all 2,142 face vertices. Consequently the matching is acyclic, not merely a partial experiment.

The four unmatched nonempty faces, recorded by the sum of their binary vertex-indicator powers, are \(4096\) (dimension zero), \(33552\) (dimension three), and \(33046,34328\) (dimension four). An acyclic simplicial Morse matching yields a CW model with precisely these four cells.

**3. Exact attaching degrees.** Orient each simplex by increasing vertex label. For each matched pair \((a,b)\) with \(a\) a codimension-one face of \(b\), the integer incidence \([\partial b:a]\) is \(+1\) or \(-1\). Eliminate the pair by substituting

\[
a=-[\partial b:a]^{-1}\sum_{c\ne a}[\partial b:c]\,c
\]

into the projected lower-dimensional chains. Acyclicity makes this recursion terminate; the reproducible program recomputes every incidence and projection from the actual face list. The exact Morse differential from the two oriented four-cells to the single three-cell is

\[
\partial_4^{\mathrm{Morse}}=\begin{pmatrix}1&1\end{pmatrix}.
\]

There are no critical cells in dimensions one or two. The zero-cell and three-cell together constitute an embedded \(S^3\) subcomplex of the Morse CW structure. Attaching one four-cell by a degree-one map makes a contractible CW subcomplex. Attaching the remaining four-cell to this contractible CW subcomplex yields a space homotopy equivalent to \(S^4\). This gives the claimed **integral homotopy equivalence**, not merely field-valued homology. An independent full simplicial boundary computation over \(\mathbb F_2\) confirms the reduced Betti vector has one unit in degree four and zero elsewhere.

**4. Full symmetry character.** Let \(S=\{1,2,4,8,15\}\). Its only linear relation over \(\mathbb F_2\) is the sum of all five elements, so every permutation of \(S\) extends to a unique linear automorphism of \(V\); together with translations these form \((\mathbb Z/2)^4\rtimes S_5\). Conversely any graph automorphism maps vertex zero to one of 16 vertices, and after a translation fixing zero it permutes its five neighbors. Every other vertex is uniquely determined by the pair of neighbors of zero to which it is adjacent (the Clebsch parameters are \((16,5,0,2)\)). Thus the entire automorphism group is exactly the stated semidirect product.

For any simplicial automorphism \(g\), apply the reduced Lefschetz trace identity

\[
\operatorname{tr}\bigl(g\mid\widetilde H_4(X;\mathbb Q)\bigr)
=-1+\sum_{d=0}^{7}(-1)^d\operatorname{tr}\bigl(g\mid C_d(X;\mathbb Q)\bigr).
\]

Each cellular trace is computed independently as the sum, over setwise-fixed \(d\)-simplices, of the parity of the induced permutation of their ordered vertices. The verifier finds trace \(+1\) for translation by the direction \(1\), and trace \(-1\) for the swaps of directions \(1\leftrightarrow2\) and \(8\leftrightarrow15\). All five directions are conjugate under \(S_5\) and span the translation subgroup, so all translations act by \(+1\). Every transposition in \(S_5\) is conjugate; hence the one-dimensional integral character is exactly the sign character on the quotient. The integral action is by \(\pm1\) since the homology is \(\mathbb Z\).

## Verification

Run `python verify_clebsch_2ind.py` using the Python standard library. Compare the complete standard output to `verification_output.txt`. The program exhaustively enumerates all \(65,536\) vertex subsets, checks both face definitions, constructs and verifies the complete 1,069-pair acyclic matching, derives the **exact signed** Morse attaching matrix, and independently computes the full mod-two simplicial homology. It also computes signed simplicial Lefschetz traces for one generating translation and two transpositions. The printed line `ALL_CHECKS_PASSED` is the last line and is conditional on all assertions succeeding. The mathematical argument above specifies why these finite, exhaustive checks imply the global claimed homotopy type and symmetry statement.

## Relationship to prior work

The definition and motivation for higher-independence complexes follow Deshpande–Singh and the 2026 tree vertex-decomposability study by Sawant. The latter identifies the three-vertex-path-free construction with the two-independence complex; its primary theorem concerns trees, whereas the Clebsch graph has induced four-cycles and is not a tree or a chordal graph. Deshpande–Singh determine homotopy types for complete multipartite graphs, fully whiskered graphs, cycles, and perfect rooted trees, but do not supply this folded-cube classification. Existing exact results for the **ordinary** independence complex of the Clebsch graph give a wedge of nine three-spheres, a different complex; the already known higher-independence result for the Petersen graph likewise concerns a different graph. No cited stronger general result supplies either the four-sphere equivalence for \(\operatorname{Ind}_2(C)\) or its full sign symmetry.

## Limitations

The assertion is an exact classification for one canonical graph at the natural higher-independence parameter two; it does not classify higher-independence complexes for all folded cubes, all parameters, or all strongly regular graphs. It makes no assertion about integral equivariant homotopy types, only the induced action on one integral homology group. Literature indexing may omit equivalent independent calculations; absence from a search is not a proof of novelty. Independent external scientific audit has not been performed.

## References

1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first submitted 2026-05-24, https://arxiv.org/abs/2605.25150.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, https://arxiv.org/html/2001.05448v2.
3. R. Abdelmalek et al., *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863, https://arxiv.org/abs/2106.10863.
4. Ghosh and Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, https://arxiv.org/abs/2505.06614.
