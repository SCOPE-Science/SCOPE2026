# Uniform edge-deletion splitting for the rhombic dodecahedral matching complex

## Finding

Let \(R\) be the graph of the rhombic dodecahedron, represented as the incidence graph between the eight vertices of a three-dimensional cube and its six square faces. Let \(\mathcal M(G)\) be the **ordinary matching complex** of a finite graph \(G\): its vertices are graph edges and its simplices are sets of pairwise disjoint edges. For **every** graph edge \(e=\{u,v\}\) of \(R\), there are integral homotopy equivalences
\[
\mathcal M(R)\simeq\bigvee^{39} S^4,\qquad
\mathcal M(R-e)\simeq\bigvee^{26} S^4,\qquad
\mathcal M(R-\{u,v\})\simeq\bigvee^{13} S^3.
\]
Moreover the natural vertex-deletion cofibration of \(\mathcal M(R)\) splits, for every such \(e\), as
\[
\mathcal M(R)\simeq\mathcal M(R-e)\vee\Sigma\mathcal M(R-\{u,v\}).
\]
Here \(R-e\) removes **one graph edge**, whereas \(R-\{u,v\}\) removes its **two graph endpoints** and all incident edges. The statement is about ordinary graph-edge matchings, not perfect matching complexes or graph Morse complexes.

## Assumptions and scope

Work with finite simple graphs and ordinary, unreduced simplicial realizations. Number cube corners by the lexicographically ordered binary triples \(b=(b_0,b_1,b_2)\in\{0,1\}^3\), assigned vertices \(0,\ldots,7\). Number cube faces by \((j,s)\), where \(j\in\{0,1,2\}\), \(s\in\{0,1\}\), assigned graph vertices \(8+2j+s\). A corner \(b\) is adjacent to face \((j,s)\) exactly when \(b_j=s\). Thus \(R\) has 14 vertices and 24 edges; eight vertices have degree three and six have degree four. The representative graph edge used in the computation is \(e_0=\{0,8\}\), corresponding to corner \((0,0,0)\) and the face \((0,0)\).

All homotopy equivalences are ordinary (non-equivariant) homotopy equivalences of geometric realizations. No assertion of a canonical splitting map or of equivariant compatibility among all 24 edge choices is made.

## Proof

**Finite exhaustive enumeration.** Encode each graph matching as an integer bitset on its ordered graph edges, and enumerate *every* bitset whose selected edges are pairwise endpoint-disjoint, including the empty simplex in the enumeration. For \(R\), the number of nonempty simplices of respective dimensions zero through five is
\[
(24,216,912,1848,1632,464),
\]
for 5096 nonempty simplices. For deletion of \(e_0\), the vector is \((23,198,798,1540,1292,348)\), giving 4199 nonempty simplices. For deletion of its two graph endpoints, the vector is \((18,114,308,340,116)\), giving 896 nonempty simplices.

**Acyclic reductions.** In each of the three enumerated complexes, iteratively pair available faces \(\sigma\) and \(\sigma\cup\{i\}\) by increasing simplicial vertex index \(i\), never reusing a face; initially include the empty simplex, then remove its pair to retain one critical vertex. The executable verifier constructs the complete directed face-incidence graph, reversing precisely the matched arrows, and confirms acyclicity by exhausting a topological sort. For the three complexes the matching sizes are, respectively, 2514, 2079, and 438 pairs, and the numbers of directed nonempty face incidences checked are 21504, 17498, and 3092.

The resulting critical cell dimensions and multiplicities are
\[
\begin{array}{c|ccc}
\text{complex}&\#C_0&\#C_d&\#C_{d+1}\\
\mathcal M(R)&1&14\ (d=3)&53\\
\mathcal M(R-e_0)&1&7\ (d=3)&33\\
\mathcal M(R-\{0,8\})&1&3\ (d=2)&16
\end{array}
\]
with no other critical cells. (The cell dimensions in this table refer to the three-dimensional and four-dimensional levels of each *Morse CW model*, and not to the largest dimension of the original simplicial complex.)

**Integral attaching degrees.** Orient a simplex by increasing bit index. For each matched lower/higher face pair, recursively substitute the corresponding incidence relation with pivot coefficient \(\pm1\), preserving exact integer signs, to project the boundary of every critical upper cell to the critical lower cells. This is the signed integral algebraic discrete-Morse boundary. Its three matrices have sizes \(14\times53\), \(7\times33\), and \(3\times16\), respectively. Independent pivot-column selection followed by fraction-free integer determinant verification gives square full-row-rank minors of determinant \(-1\) in **all three cases**. Hence all nonzero Smith invariant factors are one, and the Morse boundary is equivalent over the integers to a matrix with an identity block and zeros elsewhere.

After forming the one-vertex Morse CW model, the \(d\)-skeleton is a wedge of \(d\)-spheres. For \(d=2\) or \(d=3\), the Hurewicz isomorphism \(\pi_d(\bigvee S^d)\cong H_d(\bigvee S^d;\mathbb Z)\) identifies the attaching maps of the \((d+1)\)-cells with those integer boundary columns. Integral elementary operations on this matrix are realized by homotopy changes of the cell attachments. All unit columns can therefore be cancelled, leaving a wedge of \(53-14=39\) four-spheres, \(33-7=26\) four-spheres, and \(16-3=13\) three-spheres, respectively. This establishes integral *homotopy*, not just field homology.

**Every edge and the splitting.** Permute the three cube-coordinate directions and independently complement any subset of coordinates. These \(6\cdot8=48\) transformations induce graph automorphisms and send \(e_0\) onto every edge of \(R\). The verifier explicitly checks both edge-set preservation and the full 24-edge orbit. Thus the three computations apply to arbitrary \(e=\{u,v\}\).

Finally set \(K=\mathcal M(R)\) and regard the graph edge \(e\) as a vertex of \(K\). Its deletion is \(K\setminus e=\mathcal M(R-e)\), and its link is \(\operatorname{lk}_{K}(e)=\mathcal M(R-\{u,v\})\). The standard cone attachment gives \(K=(K\setminus e)\cup(e*\operatorname{lk}_{K}(e))\). By the computed homotopy types, the link has the homotopy type of a wedge of three-spheres and the deletion has the homotopy type of a wedge of four-spheres. Every map from that three-sphere wedge to this three-connected target is null-homotopic. Therefore the cone attachment is along a null-homotopic map and splits as the displayed wedge with the suspension of the link.

## Verification

The self-contained standard-library Python scripts `artifacts/verify_primary.py` and `artifacts/crosscheck_field.py` reconstruct the graph from the coordinate incidences; they require only a Python 3 interpreter. The primary script enumerates all faces, verifies all matched face pairs, acyclicity and integer-minor claims; no precomputed matrix or external data file is assumed. Specifically, it checks the complete 21504, 17498 and 3092 directed incidences for the three cases. The cross-check independently enumerates faces and computes complete simplicial boundary ranks modulo two and modulo three. Reduced Betti numbers from either field are \(39\) in dimension four, \(26\) in dimension four, and \(13\) in dimension three, respectively, with no other reduced Betti numbers. See `artifacts/verification_output.txt` and `VERIFICATION.md` for the literal replay results. The field computations are corroboration only: the integral homotopy claim rests on the signed Morse certificates and unimodular minors, not on modular ranks.

## Relationship to prior work

Engström's *Independence complexes of claw-free graphs* (arXiv:math/0512420v1; publicly submitted 2005-12-17, primary MSC 57M15) supplies a topology-oriented framework and connectivity theorems for independence complexes. Since \(\mathcal M(R)=\operatorname{Ind}(L(R))\) and line graphs are claw-free, this literature applies in principle, but its stated results do not determine any of the three exact homotopy types or the uniform deletion splitting. The comparison uses its actual definitions, Lemmas 2.4–2.5 and Theorem 2.8, not just its title.

Bayer, Jelić Milutinović and Vega's *Matching Complexes of Outerplanar Graphs* (arXiv:2411.04601) proves wedge decompositions for **outerplanar** graphs. The present graph is not outerplanar: every outerplanar graph has a vertex of degree at most two, whereas \(R\) has minimum degree three. Their theorem therefore does not cover this instance or the claimed edge-deletion formulas. Bayer, Goeckner and Jelić Milutinović's *Manifold Matching Complexes* (arXiv:1906.03328) classifies homology-manifold matching complexes; the present complex is nonpure, with both five-edge and six-edge maximal matchings, so it is not in that hypothesis. The graph itself is identified by MathWorld also as the Levi graph of the Miquel configuration and as the Fruchard graph. These graph aliases were included in overlap searches.

## Limitations

The result concerns this fixed graph and all 24 of its graph edges, not an infinite family or a general formula for all polyhedral graphs. The cellular equivalences are not asserted to preserve graph automorphism actions. The original simplicial complexes are nonpure, and homotopy equivalence to wedges does not assert simplicial collapsibility. Published and indexed literature searches and statement-level comparisons reduce but cannot eliminate the risk that an equivalent calculation appears under an unindexed alias. The exact homotopy types follow from integral signed Morse certificates; no equivariant or infinite-family theorem is asserted.

## References

1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1 (first public version 2005-12-17), https://arxiv.org/abs/math/0512420.
2. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, https://arxiv.org/abs/2411.04601.
3. M. Bayer, B. Goeckner, and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328, https://arxiv.org/abs/1906.03328.
4. E. W. Weisstein, *Rhombic Dodecahedral Graph*, MathWorld, https://mathworld.wolfram.com/RhombicDodecahedralGraph.html.
