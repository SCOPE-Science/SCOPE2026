# A mixed-dimensional Rips sphere wedge on the edge graph of the four-cube

## Finding

Let \(Q_4\) be the graph whose vertices are the sixteen binary four-tuples, with edges between tuples of Hamming distance one. Let \(L(Q_4)\) denote the line graph, endowed with its shortest-path metric \(d_L\) (each edge has length one). For every real scale \(r\geq0\), the **inclusive** Vietoris–Rips complex \(\mathrm{VR}_{\leq}(L(Q_4);r)\) consists of all sets of line-graph vertices with pairwise distance at most \(r\). Then

\[
\mathrm{VR}_{\leq}(L(Q_4);r)\simeq
\begin{cases}
\bigsqcup^{32}\mathrm{pt},&0\leq r<1,\\
\bigvee^{17}S^1,&1\leq r<2,\\
S^3\vee\bigvee^{8}S^5,&2\leq r<3,\\
S^{15},&3\leq r<4,\\
\mathrm{pt},&r\geq4.
\end{cases}
\]

In particular, the entire ordinary persistent-homology barcode over **every** coefficient field has thirty-one degree-zero bars \([0,1)\), one degree-zero bar \([0,\infty)\), seventeen degree-one bars \([1,2)\), one degree-three bar \([2,3)\), eight degree-five bars \([2,3)\), and one degree-fifteen bar \([3,4)\). No other positive-length bars occur. Each homology group at an individual scale is free abelian.

## Assumptions and scope

The graph \(Q_4\) is the simple undirected four-dimensional hypercube. Its edges, not its original vertices, form the 32 vertices of \(L(Q_4)\). An edge in the original cube is indexed by a pair \((i,b)\), where \(0\leq i<4\), \(0\leq b<16\), and the bit \(i\) of \(b\) is zero: it has endpoints \(b\) and \(b\oplus2^i\). The vertex indexing orders these pairs lexicographically by \((i,b)\). The result concerns the unweighted shortest-path metric of the **line** graph and the closed inequality \(d_L\leq r\), not Euclidean distances, the original cube's Hamming-vertex filtration, or open Rips thresholds. Every assertion covers the single finite metric space at all real filtration parameters; no higher-dimensional generalization is asserted.

## Proof

**The graph metric and threshold cases.** For distinct cube edges \(e,f\), an edge path in the line graph corresponds to a chain of incident cube edges. The minimum number of steps is therefore
\[
d_L(e,f)=1+\min\{d_H(x,y):x\in e,\ y\in f\},
\]
where \(d_H\) is Hamming distance between endpoints. In particular, the diameter is four. At distance four, every edge is paired only with its complementary, parallel antipodal cube edge. Thus the distance-four graph is precisely sixteen disjoint edges, and there are no larger distances.

**Scale one.** The cube is triangle-free, hence every clique in \(L(Q_4)\) consists of original edges incident to one cube vertex. The flag complex at scale one is the union of sixteen tetrahedra, one for each cube-vertex star. Their intersections are single vertices for adjacent cube vertices and empty otherwise; no three distinct tetrahedra intersect. This is a good cover with nerve the original cube graph, so the complex is homotopy equivalent to \(Q_4\). Its cycle rank is \(32-16+1=17\), proving the degree-one wedge formula.

**Scale two: a complete acyclic matching.** A clique is enumerated by increasing indices among the 32 original cube edges, using the above exact distance formula. There are precisely \(13{,}896\) nonempty simplices with face numbers, by dimensions \(0,\ldots,7\), equal to
\[
(32,336,1568,3672,4512,2848,832,96).
\]
Perform vertex-toggle matching stages in the following fixed index order:

`16,25,18,31,29,20,0,4,10,7,14,17,22,28,15,12,13,27,1,24,6,19,8,9,21,23,5,26,11,30,2,3`.

At the stage for index \(j\), pair every still-unmatched face \(\sigma\) not containing \(j\) with \(\sigma\cup\{j\}\), when both remain and the union is a face. Remove these disjoint pairs before processing the next index. This gives \(6{,}943\) matched pairs and exactly ten critical cells: one vertex, one three-simplex, and eight five-simplices. To verify the nonstandard acyclicity assertion, orient **every** cover relation of the nonempty face poset from a face to its codimension-one subface, reversing precisely matched relations. The graph has \(13{,}896\) vertices and \(66{,}304\) arrows; a complete Kahn topological sort processes all \(13{,}896\) vertices. These integer-exact checks are reconstructed and asserted by `verify.py`, with the full fixed ordering above. Forman's discrete Morse theorem gives a CW complex with one \(0\)-cell, one \(3\)-cell, and eight \(5\)-cells. It is \(2\)-connected with integral homology \(\mathbb Z\) in dimension three and \(\mathbb Z^8\) in dimension five; it is not enough to infer a wedge merely from these counts, because a five-cell could attach by a nontrivial element of \(\pi_4(S^3)\).

**Scale two: ruling out Hopf attachments.** Each attaching map of a five-cell into the three-skeleton \(S^3\) lies in \(\pi_4(S^3)\cong\mathbb Z/2\). The nontrivial class is the suspended Hopf map and is detected by nonzero \(\mathrm{Sq}^2:H^3(-;\mathbb F_2)\to H^5(-;\mathbb F_2)\) on its mapping cone. Consequently all eight maps are null if this Steenrod operation vanishes on the entire complex. `steenrod_check.py` computes an explicit mod-two three-cocycle \(\alpha\) representing the unique nonzero class in \(H^3\), verifies \(\delta\alpha=0\) and \(\alpha\notin\mathrm{im}\,\delta\), and evaluates the classical simplicial cup-one formula \(\mathrm{Sq}^2[\alpha]=[\alpha\smile_1\alpha]\). For each ordered six-vertex face \((v_0,\ldots,v_5)\), the cochain formula is
\[
(\alpha\smile_1\alpha)(v_0,\ldots,v_5)=
\sum_{j=0}^{2}
\alpha(v_0,\ldots,v_j,v_{j+3},\ldots,v_5)
\alpha(v_j,\ldots,v_{j+3})\pmod2.
\]
Here \(\alpha\) is supported on 95 three-simplices, while its cup-one square is supported on 20 five-simplices. Exact Gaussian elimination verifies that the square is a cocycle **and** belongs to the image of \(\delta:C^4\to C^5\); the latter map has rank \(2104\). Thus \(\mathrm{Sq}^2=0\), all eight attaching maps vanish, and the scale-two homotopy type is \(S^3\vee\bigvee^8S^5\). This is an integral homotopy conclusion, not merely a mod-two Betti-number observation.

**Scale three and persistence.** At radius three all edges between line-graph vertices are present except the sixteen antipodal pairs. Its flag complex is the join of sixteen two-point discrete spaces, or \(S^{15}\). At radius four it is a full simplex. The scales have disjoint positive homology dimensions; all intervening persistence maps in positive degrees are therefore zero. The connected-component barcode follows from the connectedness of \(L(Q_4)\) at scale one. This proves the entire stated barcode and homotopy classification.

## Verification

The accompanying three plain-Python programs are `verify.py`, `homology_check.py`, and `steenrod_check.py`, using Python 3 standard library only. Run them in a common directory, in the displayed sequence, as `python3 verify.py`, `python3 homology_check.py`, and `python3 steenrod_check.py`. The checks reconstruct cube edges, shortest-path distances, all simplices, the full acyclic matching, exact mod-two simplicial boundary ranks, a nonzero cohomology generator, and its cup-one square. The required success markers are `VERIFY_OK`, `HOMOLOGY_OK`, and `STEENROD_OK`. The topological implications additionally use the standard nerve lemma, Forman's discrete Morse theorem, \(\pi_4(S^3)\cong\mathbb Z/2\), and the mod-two Steenrod detection of the suspended Hopf attachment.

## Relationship to prior work

Kozlov [1] develops constructive elementary-collapse methods for graph-related topology and provides the archive-era methodology; it does **not** compute this Rips filtration. Adamaszek [2] treats clique complexes of graph powers and, importantly, identifies the ordinary clique complex of a line graph with a two-skeleton construction in its section on line graphs; that addresses radius one here, not the clique complex of the **square** of the line graph at radius two. Goyal, Shukla, and Singh [3] study clique complexes of line graphs themselves, again not this squared line graph. Adamaszek and Adams [4] study Rips complexes of **vertices** of hypercube graphs under Hamming distance rather than cube-edge vertices under line-graph distance. In contrast, the distinguishing statement here is the mixed-dimensional \(S^3\)-and-\(S^5\) wedge at the intermediate radius, with the required Steenrod-square obstruction calculation.

## Limitations

The computation establishes one exact finite metric and its complete filtration; it does not establish a formula for every hypercube dimension or arbitrary graph. The exhaustive checks are exact only because all faces and incidence data of this finite complex were enumerated. The acyclic-matching rank information alone would not show the wedge decomposition without the independent Steenrod test; mod-two homology alone cannot rule out suspended Hopf attachments. Originality remains qualified by the possibility of unindexed, equivalent statements concerning powers of line graphs. No independent human audit has been performed.

## References

[1] D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613 (first public version 2005-03-28; primary MSC 57Q10).

[2] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011), especially its discussion of line graphs and graph powers.

[3] S. Goyal, S. Shukla, and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (2020).

[4] M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (2021).
