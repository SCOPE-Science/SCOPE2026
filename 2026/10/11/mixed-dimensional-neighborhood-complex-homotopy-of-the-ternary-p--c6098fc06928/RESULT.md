# Mixed-dimensional neighborhood-complex homotopy of the ternary projective nonincidence graph

## Finding
Let \(G\) be the 26-vertex point-line **nonincidence** graph of the projective plane \(\operatorname{PG}(2,3)\), with a point and a line joined exactly when the point does not lie on the line. Its ordinary open Lovász neighborhood complex has the integral homotopy type
\[\boxed{\mathcal N(G)\simeq \left(\bigvee^{39}S^4\vee S^5\right)\sqcup\left(\bigvee^{39}S^4\vee S^5\right).}\]
The components correspond canonically to the point and line vertex classes. This is a complete homotopy classification for the stated finite graph, not a statement about all projective planes.

## Assumptions and scope
The field is \(\mathbb F_3\). Projective points are one-dimensional subspaces of \(\mathbb F_3^3\), represented uniquely by nonzero triples whose first nonzero coordinate is \(1\). Projective lines have nonzero coefficient triples, normalized identically. Point \(p\) lies on line \(\ell\) precisely when the dot product of representative vectors is zero modulo \(3\). There are 13 points, 13 lines, four points on each line, and four lines through each point. The graph \(G\) is simple and bipartite, with the two copies of the projective plane as vertex classes and 9 neighbors per vertex.

For a simple graph \(H\), \(\mathcal N(H)\) is the simplicial complex of nonempty vertex subsets having a common *open* graph neighbor. No closed-neighborhood convention, metric Vietoris–Rips construction, or incidence-adjacency convention is used.

Because \(G\) is bipartite, each face of \(\mathcal N(G)\) lies in exactly one vertex class. On the points, the facets are the thirteen nine-element complements of projective lines. More explicitly, a nonempty point set is a face if and only if some projective line is disjoint from it. This is the intrinsic nonblocking-set complex of the ternary projective plane. The line-side component is isomorphic to it by projective point-line duality (the symmetric dot-product incidence pairing).

## Proof
Write \(K\) for the point-side nonblocking complex. The preceding characterization reduces the claim to computing the homotopy type of this single 13-vertex complex. The following exhaustive finite enumeration and acyclic matching supply an exact combinatorial proof; full standalone source is included in `check_plane_neighborhood.py`.

Represent a face by the 13-bit mask of its point set. For each projective line, enumerate all subsets of its nine-point complement. Deduplication gives exactly 3,861 nonempty faces, with dimension-ordered face vector
\[(13,78,286,702,1170,1014,468,117,13).\]
Include the empty face temporarily and process pivot vertices in ascending label order. At each pivot, pair all still-unpaired faces \(\sigma\) with \(\sigma\cup\{v\}\) when the latter is also still unpaired. Remove the pair containing the empty face, leaving its singleton as the critical vertex in the ordinary complex. The resulting matching consists of **1,910 disjoint codimension-one pairs** and has exactly **one critical vertex, 39 critical four-simplices and one critical five-simplex**.

To certify the discrete-Morse condition, direct every cover relation in the nonempty-face poset downward, except each matched cover relation, which is directed upward. The verifier constructs every one of the **20,085** directed incidences and topologically sorts the full 3,861-vertex directed graph. Every face is sorted, proving there is no directed cycle. By Forman's discrete Morse theorem, \(K\) is homotopy equivalent to a CW complex with one zero-cell, 39 four-cells and one five-cell.

It remains to determine the attaching map of the five-cell. The relevant attaching degrees form the signed integral Morse boundary \(C_5^{\mathrm{Morse}}\to C_4^{\mathrm{Morse}}\), a \(39\)-by-\(1\) integer matrix. Order simplex vertices by their bit positions. For a four-simplex \(f\), define an exact integer-valued projection \(R(f)\): critical four-simplices map to their corresponding basis vectors, four-simplices matched upward from a three-simplex map to zero, and, when \(f\) is paired upward with a five-simplex \(t\), use the signed simplicial boundary relation
\[ R(f)=-[\partial t:f]\sum_{g\subset t,\ \dim g=4,\ g\ne f}[\partial t:g]\,R(g). \]
The matching's acyclicity ensures the recursion terminates. Applying this projection to the signed boundary of the unique critical five-simplex gives **all 39 coefficients equal to zero**, as checked by the embedded integer verifier. Thus the five-cell attaches by a map representing zero in \(\pi_4(\bigvee^{39}S^4)\). The Hurewicz isomorphism \(\pi_4(\bigvee^{39}S^4)\cong H_4(\bigvee^{39}S^4;\mathbb Z)\) shows that this attaching map is null-homotopic. Therefore \(K\simeq\bigvee^{39}S^4\vee S^5\). The dual line-side component has the same type, proving the asserted disjoint union.

## Verification
Run `python3 check_plane_neighborhood.py` using Python 3 and only its standard library. It reconstructs the projective incidence structure, all faces, all pairs, every directed cover incidence, the complete topological sort and the signed integral Morse boundary. The exact outputs are the 3,861-face vector above, 1,910 pairs, 41 critical faces, 20,085 incidences, and the zero integer boundary in all 39 rows.

Independently run `python3 independent_plane_check.py`. This implementation uses a different explicit listing of projective coordinates and separately tests all subsets against each neighborhood. Its exact mod-two boundary ranks, starting with the reduced zero-dimensional differential, are
\[(1,12,66,220,482,649,364,104,13),\]
which give the reduced mod-two Betti vector in dimensions zero through eight
\[(0,0,0,0,39,1,0,0,0).\]
The mod-two calculation checks the enumeration and Betti numbers independently; it does not substitute for the integral attaching-degree proof.

## Relationship to prior work
Lovász's neighborhood construction relates graph coloring to topology. Matsushita's *Fundamental Groups of Neighborhood Complexes* (first arXiv release in 2012; subsequently published in 2017) gives a general fundamental-group interpretation and introduces related neighborhood constructions, but it does not determine this exact graph's higher-dimensional homotopy type. The point/line *incidence* graph, the present *nonincidence* graph, and metric Vietoris–Rips complexes of incidence graphs are distinct objects; results for the former do not by themselves supply the latter's mixed four/five-dimensional wedge. The object here can also be described in finite geometry as the simplicial complex of point sets that fail to block at least one line.

## Limitations
The classification is restricted to \(\operatorname{PG}(2,3)\) and its specific point-line nonincidence graph. It does not establish a formula for arbitrary projective-plane orders, and it does not assert uniqueness against all inaccessible or unpublished literature. The finite certificate proves this exact finite case only. No independent external scientific audit has been performed.

## References
1. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1 (first publicly submitted 2012-10-10); *Journal of Mathematical Sciences, University of Tokyo* 24 (2017), 321–353, especially the definition of the neighborhood complex and Theorem 1.1. https://arxiv.org/abs/1210.2803
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (2010). Background methodology for graph-associated simplicial complexes, not an asserted source of the present exact decomposition. https://arxiv.org/abs/1007.0418
