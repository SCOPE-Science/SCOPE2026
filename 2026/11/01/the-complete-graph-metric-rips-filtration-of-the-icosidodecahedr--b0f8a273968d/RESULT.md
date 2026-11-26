# An elementary collapse of the icosidodecahedral graph Rips complex from radius three onto radius two

## Finding

Let \(G\) be the icosidodecahedral graph with shortest-path distance, and let \(K_r=\operatorname{VR}_{\le r}(G)\) use the inclusive threshold. There is an elementary simplicial collapse
\[
K_3\searrow K_2
\]
that leaves **every simplex of the included radius-two complex** intact. The supplied sequence has 7,472 codimension-one free-face pairs. No subdivision, expansion, or replacement of the target by a homotopy-equivalent complex is used.

## Assumptions and scope

Construct the icosahedron with poles \(0,11\) and two five-cycles \(a_i=1+i\), \(b_i=6+i\), where \(0\le i<5\) and subscripts are taken modulo five. Its thirty edges are \(\{0,a_i\},\{11,b_i\},\{a_i,a_{i+1}\},\{b_i,b_{i+1}\},\{a_i,b_i\},\{a_i,b_{i-1}\}\). These edges in lexicographic order are the vertices of \(G\); two are adjacent if they occur in a common icosahedral triangle. A nonempty face of \(K_r\) is a vertex set all of whose pairs have distance at most \(r\) in this rectification graph. A face in the certificate is represented by its nonzero thirty-bit mask. The collapses are not asserted to be equivariant.

## Proof

Breadth-first distances in the rectification determine the graph powers, whose cliques are exactly the Rips simplices. Enumerating cliques by adding only vertices above the current largest label gives the following dimension-indexed counts, from vertices upward:
\[
\begin{aligned}
 f(K_2)&=(30,180,380,330,102),\\
 f(K_3)&=(30,300,1340,3150,4374,3800,2100,720,140,12).
\end{aligned}
\]
For each ordered pair \((\sigma,\tau)\) of the upper sequence in `collapse_certificate.json`, use the current face set, starting with \(K_3\). Check that both faces are present, that neither is in the independently enumerated \(K_2\), and that \(\sigma\subset\tau\) with \(|\tau|=|\sigma|+1\). Check that \(\tau\) is the unique remaining immediate coface of \(\sigma\) and is maximal, then delete both. These conditions are sufficient for an elementary collapse. After all 7,472 checks the surviving set equals the exact face set of \(K_2\), not merely a complex with the same number of faces. The count also equals \((15{,}966-1{,}022)/2\), as required for codimension-one pair deletions between these two fixed targets.

The companion certificate retains a contextual second sequence of 426 elementary pairs from \(K_2\) to a triangulation of the polyhedral boundary (twenty original triangles and lowest-index fans in the twelve pentagons). This surface has 30 vertices, 84 edges and 56 triangles, and it is a common deformation retract. The new relative assertion concerns the full \(K_2\) with all its simplices, not just preservation of this surface or of a fundamental cycle.

## Verification

The standalone `verify_icosidodecahedron.py` and `collapse_certificate.json` accompany the result. The replay command is `python3 verify_icosidodecahedron.py collapse_certificate.json`. The checker recomputes the graph, all thirty distance rows and the complete face sets, and checks both sequences against their exact targets. The recorded output is `verification_output.txt`. The proof is by exhaustive finite certificate; there is no extrapolation to other graphs.

## Relationship to prior work

The graph-metric homotopy filtration and its barcode are not claimed as new. The records `b96bd2d6e71b` (October 18) and `47f363238c0f` (October 25), and the separate November 1 record `3f8966c8984a`, give the full homotopy types and check integral degree-two persistence. In particular, `47f363238c0f` proves that the actual inclusion \(K_2\hookrightarrow K_3\) is a homotopy equivalence, by integral Morse calculations on the two complexes and evaluation on a common polyhedral cycle. Neither equivalence nor invariance of that cycle supplies elementary deletions leaving every radius-two simplex intact.

The Euclidean result `dbb207327dc1` (October 18) has substantial overlap. For its unit root coordinates, with \(\phi=(1+\sqrt5)/2\), the shortest Euclidean distance joins exactly the polyhedral edges. The graph-radius-two and graph-radius-three face sets agree with its squared Euclidean thresholds \(3-\phi\) and \(1+\phi\), respectively: this can be checked pairwise by building adjacency from squared distance \(2-\phi\), computing breadth-first distances, and comparing the threshold predicates on all thirty vertices. The previous Euclidean certificate collapses both of these complexes onto the strictly smaller squared-distance-one complex (362 nonempty faces), and then to a fan triangulation of the boundary. In particular the lower collapse to the polyhedral sphere is also covered in substance. At squared distance one the pentagons are full five-vertex simplices; they collapse to any prescribed fan, by coning a collapse of the tetrahedron on the other four vertices to the path of three edges along its pentagon. Thus the choice of labeling for the fan does not produce the new assertion. In the older collapse of the squared-distance-\(1+\phi\) complex, some pairs cross the radius-two target (404 in the published sequence); it does not itself supply a collapse that preserves this target.

Saleh, Titz Mite and Witzel, *Vietoris–Rips complexes of Platonic solids* ([arXiv:2302.14388](https://arxiv.org/abs/2302.14388)), treat graph distance on the twelve vertices of the icosahedron, not on the thirty vertices of its rectification. The high-girth criterion of Adamaszek, *Clique complexes and graph powers* ([arXiv:1104.0433](https://arxiv.org/abs/1104.0433), Proposition 2.2), does not apply to this triangular graph.

## References for catalogue comparisons

- [The icosidodecahedral graph has a two-scale persistent Rips two-sphere](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-the-icosidodecahedral-graph-has-a-two-scale-persistent-rips-two--b96bd2d6e71b).
- [Complete graph-metric Rips persistence of the icosidodecahedral graph](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-complete-graph-metric-rips-persistence-of-the-icosidodecahedral--47f363238c0f).
- [Complete integral Vietoris–Rips persistence of the icosidodecahedral graph](https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-complete-integral-vietoris-rips-persistence-of-the-icosidodecahe--3f8966c8984a).
- [A persistent integral two-sphere in the Euclidean Rips filtration of the icosidodecahedral root orbit](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-a-persistent-integral-two-sphere-in-the-euclidean-rips-filtratio--dbb207327dc1).

## Limitations

The result is for one fixed graph and one prescribed pair of filtration levels. No general relative-collapse criterion, equivariant collapse, or claim of exhaustive publication priority is made.
