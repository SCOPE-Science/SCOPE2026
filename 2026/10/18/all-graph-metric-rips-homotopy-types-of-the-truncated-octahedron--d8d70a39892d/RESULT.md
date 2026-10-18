# All graph-metric Rips homotopy types of the truncated octahedron

## Finding
Let \(G\) have vertex set the 24 coordinate permutations of \((0,\pm1,\pm2)\), where the nonzero signs are independent; join two vertices when their squared Euclidean distance is \(2\). This is the edge graph of the truncated octahedron, with 36 edges. Give \(V(G)\) its shortest-path graph metric \(d_G\). The inclusive Vietoris--Rips complex \(R_r\) has all nonempty subsets of graph-metric diameter at most \(r\) as faces. For every real \(r\ge0\),

\[
R_r\simeq
\begin{cases}
\bigvee^{23}S^0,&0\le r<1,\\
\bigvee^{13}S^1,&1\le r<2,\\
\bigvee^{9}S^2,&2\le r<3,\\
S^2,&3\le r<4,\\
\left(\bigvee^{5}S^4\right)\vee\left(\bigvee^{2}S^5\right),&4\le r<5,\\
S^{11},&5\le r<6,\\
\mathrm{pt},&r\ge6.
\end{cases}
\]

This is a classification of homotopy types at individual scales, not a classification of every inclusion-induced persistence map. In particular, the fourth graph-distance threshold exhibits nonzero homotopy in two adjacent dimensions.

## Assumptions and scope
The edge graph is *not* the Euclidean distance metric restricted to the vertices. All thresholds are inclusive. Distances are integral, so the homotopy type is constant on the seven ranges displayed above. The graph has 24 vertices, 36 edges, girth four, and diameter six; the number of unordered vertex pairs at distances \(1,2,3,4,5,6\) is respectively \(36,60,72,60,36,12\).

## Proof
The coordinate description specifies every edge without relying on external graph-data files. Breadth-first search from each vertex gives the stated distance histogram and verifies that each vertex has one unique distance-six vertex, its coordinatewise negative.

At threshold zero there are 24 isolated vertices. At threshold one the clique complex is exactly the graph itself: its 36 edges contain no triangles. Since the graph is connected, its cycle rank is \(36-24+1=13\), proving the two low-scale cases.

For thresholds two, three, and four, enumerate every clique in the graph whose edges join pairs with graph distance at most the threshold. Represent simplices as vertex bitmasks using lexicographic order on the 24 coordinate triples. The complete nonempty face counts by dimensions zero upward are:

- Threshold two: \((24,96,112,30)\), totaling 262.
- Threshold three: \((24,168,472,618,384,92)\), totaling 1,758.
- Threshold four: \((24,228,1112,3042,4848,4592,2592,822,112)\), totaling 17,372.

Use a staged vertex-toggle matching: in the given vertex order, pair each currently unmatched simplex not containing that vertex with the simplex obtained by adjoining it, whenever the latter remains unmatched. For thresholds two and three, the order is

`4,18,2,8,3,15,14,22,12,16,19,1,7,0,6,9,10,5,13,21,17,23,11,20`.

For threshold four, use the natural order `0,1,...,23`. The resulting matchings have 126, 878, and 8,681 pairs, respectively. The unmatched cells by dimension are: one vertex and nine two-cells at threshold two; one vertex and one two-cell at threshold three; and one vertex, six four-cells, and three five-cells at threshold four. A complete directed-Hasse-graph topological sort on 648, 6,696, and 93,480 arrows respectively visits *every* nonempty face, verifying acyclicity in all three cases.

Discrete Morse theory therefore proves the sphere-wedge descriptions at thresholds two and three. At threshold four the Morse CW complex has one zero-cell, six four-cells and three five-cells. Orient every simplex by increasing vertex index, and recursively expand the faces of each critical five-cell along the complete signed four/five-dimensional gradient-path relations. In ordered critical bases, the resulting **integral** Morse boundary matrix (six rows, three columns) is

\[
\partial^{\mathrm{Morse}}_5=
\begin{pmatrix}
-1&-1&0\\
0&0&0\\
1&1&0\\
0&0&0\\
1&1&0\\
1&1&0
\end{pmatrix}.
\]

It has rank one and its unique nonzero Smith factor is \(1\). Hence its image in the free fourth chain group is primitive. The four-skeleton is a bouquet of six four-spheres and is three-connected. By the Hurewicz isomorphism \(\pi_4(\bigvee^6S^4)\cong\mathbb Z^6\), all attaching maps of the three five-cells are classified by their integer degree columns. Integral changes of bases reduce this matrix to a single unit entry. Cancelling the resulting four/five-cell pair leaves a bouquet of five four-spheres and two five-spheres, proving the scale-four claim **as a homotopy equivalence**, not just as a homology calculation.

At threshold five the only forbidden pairs are the 12 coordinatewise antipodal pairs (the unique distance-six pairs). Hence the complex is exactly the join of 12 copies of a two-point discrete complex, the boundary of the 12-dimensional cross-polytope, homeomorphic to \(S^{11}\). At threshold six every subset is a simplex, and the complex is contractible. This completes all scales.

## Verification
Run `python3 verify_truncated_octahedron_rips.py` using Python 3 and its standard library. The program constructs the graph and graph metric from integer coordinates, enumerates complete clique sets, reproduces all three matchings, and checks every oriented Hasse arrow for acyclicity. It recomputes the signed integral critical-cell boundary at threshold four and independently reduces the **original simplicial boundary matrices over \(\mathbb F_2\)** at thresholds two, three, and four. The respective nonzero reduced mod-two Betti ranks are \(\beta_2=9\), \(\beta_2=1\), and \((\beta_4,\beta_5)=(5,2)\). These finite enumerations are exhaustive for the explicitly defined 24-vertex graph. The output ends with `VERIFY_OK vertices=24 graph_edges=36 diameter=6 rips_faces_r4=17372`.

## Relationship to prior work
Saleh, Titz Mite and Witzel [1] classify the Vietoris--Rips complexes of the five Platonic solids, and explicitly identify Archimedean solids as a potential generalization. Their general elementary penultimate-scale observation already explains why a centrally symmetric graph with a unique antipode at graph diameter has a cross-polytope boundary; that ingredient at threshold five is not asserted as new. The truncated octahedron is an Archimedean solid, not one of their Platonic cases. Feng and Nukala [2] calculate scale-two complexes of families of subsets equipped with symmetric-difference distance, which is not the present 24-vertex graph metric. Previously published computations for a truncated **cube**, a truncated **tetrahedron**, and the Euclidean **cuboctahedron** concern different graphs or a different metric. The middle-scale mixed-dimensional classification here is not implied by those statements.

## Limitations
Only the specified 24-vertex truncated-octahedral graph and its shortest-path metric are covered; no analogous assertion for other Archimedean solids follows. The theorem gives individual-scale homotopy types, not a complete barcode or equivariant homotopy models. The homotopy proof is finite and computationally certified by a directly inspectable exhaustive discrete-Morse construction; the mod-two calculations alone would not prove integral homotopy type. An independently conducted audit has not been performed. An unindexed equivalent result could still exist.

## References
1. N. Saleh, T. Titz Mite and S. Witzel, *Vietoris-Rips complexes of Platonic solids*, arXiv:2302.14388v1 (first public 2023-02-28), especially introduction, Lemma 2.2, and discussion of Archimedean generalizations.
2. Z. Feng and N. C. P. Nukala, *On Vietoris-Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664 (2023).
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. **134** (1998), 90–145.
