# The complete integral forest filtration of the icosahedral graph

## Finding
For the icosahedral graph \(I\), the induced-forest filtration has the complete integral homotopy classification
\[
F_d(I)\simeq\begin{cases}
S^2\vee\bigvee^6S^1,&d=0,\\
\bigvee^{20}S^3,&d=1,\\
\bigvee^{40}S^4,&d\geq2.
\end{cases}
\]
For integer filtration degrees the full reduced persistence barcode, over every field, consists of six degree-one bars \([0,1)\), one degree-two bar \([0,1)\), twenty degree-three bars \([1,2)\), and forty degree-four bars \([2,\infty)\). These are complete homotopy types, not merely Betti-number calculations.

## Assumptions and scope
The vertices of \(I\) are \(0,11\), two five-vertex rings \(A_i=1+i\) and \(B_i=6+i\) indexed by \(i\in\mathbb Z/5\mathbb Z\). Its edges are \(0A_i\), \(11B_i\), \(A_iA_{i+1}\), \(B_iB_{i+1}\), \(A_iB_i\), and \(A_iB_{i-1}\), with all indices modulo five; this graph has twelve vertices and thirty edges and is isomorphic to the icosahedral graph. For each integer \(d\ge0\), a simplex \(S\subseteq V(I)\) belongs to \(F_d(I)\) precisely when \(I[S]\) is a forest and every vertex of \(I[S]\) has degree at most \(d\). The empty simplex is included; geometric realizations are used for homotopy equivalences. All homology groups in the proof are integral unless a coefficient field is specified.

## Proof
**Saturation at degree two.** Every open neighborhood in the icosahedral graph induces a five-cycle. If a vertex in an induced forest had three selected neighbors, two of those neighbors would be adjacent, because the independence number of the five-cycle is two. They and the vertex would form a triangle, contrary to the forest condition. Thus no induced forest has maximum degree exceeding two, and \(F_d(I)=F_2(I)\) for \(d\ge2\).

**Degree zero.** The independence complex \(F_0(I)\) has twelve vertices, thirty-six edges and twenty triangles. The twenty triangles, together with their thirty distinct edges, form a connected closed combinatorial surface: each edge lies in exactly two triangles and every vertex link is a five-cycle. Its Euler characteristic is \(12-30+20=2\), so by the classification of closed connected surfaces it is a two-sphere. The six remaining independent-set edges each attach to this connected sphere along their two endpoints. Attaching six one-cells between pairs of points of a path-connected space gives \(F_0(I)\simeq S^2\vee\bigvee^6S^1\).

**Degree one.** The 323 nonempty faces of \(F_1(I)\) admit the explicitly listed acyclic face-poset matching in `CERTIFICATE.json`: 147 face-coface pairs leave one critical zero-cell, four critical two-cells, and twenty-four critical three-cells, with no critical one-cells. This supplies a CW model obtained by attaching twenty-four three-cells to a wedge of four two-spheres. Integer elementary chain cancellations, reproduced in `VERIFY.py`, give its signed attaching-degree matrix. Four rows indexed by masks \(100,146,164,1042\) and four columns indexed by masks \(616,680,720,1112\) have determinant one. An integer change of bases on the two- and three-cells and homotopy classification of maps to a wedge of two-spheres therefore cancel all four two-cells. The resulting space is \(\bigvee^{20}S^3\).

**Degree two.** The 983 nonempty faces of \(F_2(I)\) admit a listed acyclic matching of 471 pairs leaving only one zero-cell and forty four-cells. Discrete Morse theory directly identifies a CW model with those cells and no others; hence \(F_2(I)\simeq\bigvee^{40}S^4\).

**Persistence.** All homology groups are free abelian in the dimensions listed above. A positive-degree class at one stage has zero image in the next stage because the corresponding reduced homology group there vanishes. There are no nonzero maps between same-degree classes across different filtration stages. This proves precisely the asserted intervals, over every field and integrally as persistence of free modules.

## Verification
The accompanying self-contained `VERIFY.py` and `CERTIFICATE.json` use only the Python standard library. From the thirty explicitly defined graph edges, they enumerate all \(2^{12}=4096\) subsets at each of the three distinct degree bounds using two independent graph-acyclicity tests. The face counts, **including the empty simplex**, are \(69,324,984\) respectively. The face-poset matchings cover respectively \(132,972,3972\) Hasse incidences, and an acyclicity test exhausts the reversed matched-edge directed graph. Exact signed integer Morse reductions compute the degree-one unimodular minor; independent mod-two boundary ranks match the resulting free integral Betti ranks. The graph-neighborhood condition and surface links are also exhaustively checked. To reproduce: put `VERIFY.py` and `CERTIFICATE.json` in the same directory and execute `python3 VERIFY.py`. No external packages are required.

## Relationship to prior work
Carnero Bravo's *The Forest Filtration of a Graph* (first submitted July 25, 2023) defines these complexes, identifies degree zero with the independence complex and degree one with the two-independence complex, and treats several graph families and operations. The present calculation addresses the icosahedral graph, outside the explicitly treated path, cycle, cactus, double-star and graph-operation examples. The earlier literature on acyclic-set polynomials counts induced forests but does not determine these three integral homotopy types. Icosahedral open-neighborhood, Čech, and ordinary three-cut complexes are different simplicial constructions: equality of the underlying graph does not imply their homotopy results determine this filtration.

## Limitations
The result concerns exactly the finite icosahedral graph and its induced-forest filtration; no assertion is made about arbitrary 5-regular planar graphs or functorial equivalences between the stages. The computed matchings and integer minors establish intrinsic homotopy types, not explicit geometric sphere embeddings. The degree-zero structure is included to complete the filtration, while the middle and stabilized stages provide the principal new calculations. The existence of unindexed equivalent prior work cannot be excluded merely by indexed searches.

## References
1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first submitted July 25, 2023), https://arxiv.org/abs/2307.13271.
2. C. Barton, J. I. Brown, and D. A. Pike, *Acyclic polynomials of graphs*, arXiv:2011.01735, https://arxiv.org/abs/2011.01735.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, doi:10.1006/aima.1997.1650.
