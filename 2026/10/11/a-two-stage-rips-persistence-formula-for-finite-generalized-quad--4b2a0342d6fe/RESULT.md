# A two-stage Rips persistence formula for finite generalized quadrangles

## Finding
Let \(\mathcal Q=(P,L,I)\) be any finite generalized quadrangle of order \((s,t)\), where \(s,t\ge2\), and let \(G\) be its bipartite point–line incidence graph. Give every edge length one, and let \(\mathrm{VR}_{\le}(G;r)\) denote the clique complex of the graph on \(P\sqcup L\) whose distinct vertices have distance at most the real number \(r\). Write \(b=(st)^2\). Then
\[
\mathrm{VR}_{\le}(G;1)\simeq\mathrm{VR}_{\le}(G;2)\simeq\bigvee^{b}S^1,
\quad
\mathrm{VR}_{\le}(G;3)\simeq\bigvee^{b^2}S^3,
\quad
\mathrm{VR}_{\le}(G;r)\simeq *\ (r\ge4).
\]
More precisely the first inclusion \(G=\mathrm{VR}_{\le}(G;1)\hookrightarrow\mathrm{VR}_{\le}(G;2)\) is a simplicial-collapse equivalence. Thus, for any coefficient field, all positive-degree persistent homology is precisely \(b\) degree-one bars \([1,3)\) and \(b^2\) degree-three bars \([3,4)\). For the order-two symplectic generalized quadrangle, whose incidence graph is the Tutte–Coxeter graph, the respective counts are \(16\) and \(256\).

## Assumptions and scope
A generalized quadrangle of order \((s,t)\) is a finite point–line incidence geometry in which each point lies on \(t+1\) lines, each line contains \(s+1\) points, two distinct points lie on at most one common line, and for every nonincident point–line pair \((p,\ell)\) there is a *unique* point \(x\) of \(\ell\) collinear with \(p\). All assertions concern the ordinary shortest-path metric on the finite undirected incidence graph, with the weak distance inequality in the Rips definition, and all existing geometries of the indicated orders (not only the classical or self-dual examples).

The standard finite-generalized-quadrangle counting identities are
\[
|P|=(s+1)(st+1),\quad |L|=(t+1)(st+1),\quad
|E(G)|=(s+1)(t+1)(st+1).
\]
They follow by counting incidences and points not collinear with a fixed point. The incidence graph is connected, has girth eight and diameter four; distances between a point and a line are either one or three, and between distinct vertices of the same type are either two or four. These facts also follow directly from the unique-projection axiom. As a graph, \(G\) has cycle rank
\[
|E(G)|-|P|-|L|+1=(st)^2=b.
\]

## Proof
**Scale one.** The incidence graph has no three-cycles, so its scale-one Rips complex is precisely \(G\). Connectivity and the preceding Euler count give \(G\simeq\bigvee^bS^1\).

**Scale two: an actual simplicial collapse.** For each vertex \(v\) of \(G\), denote by \(S_v=\{v\}\cup N_G(v)\) its closed star, understood as a full simplex. Every clique in the graph square lies in some \(S_v\): if a clique contains at least two points and one line, every one of those points must be incident with the line, and dually; no clique can have two points *and* two lines, by the absence of four-cycles. For a clique all of whose vertices are points, each pair lies on a common line, and the absence of six-cycles forces all of them onto the same line; dually for an all-line clique. Therefore the maximal simplices of \(\mathrm{VR}_{\le}(G;2)\) are exactly the \(S_v\).

Fix any vertex \(v\). For every set \(T\subseteq N_G(v)\) with \(|T|\ge2\), in descending order of \(|T|\), pair its simplex \(T\) with \(T\cup\{v\}\). Since any two distinct members of \(N_G(v)\) have exactly one common graph neighbor (namely \(v\)), a simplex containing \(T\) cannot lie in any other maximal \(S_w\); after descending-cardinality removal the only remaining immediate coface of \(T\) is \(T\cup\{v\}\). Hence each is a valid free-face collapse. The pairs for different centers cannot conflict, because each deleted face has at least two vertices of a common type and is attached to its unique opposite-type center. The undeleted simplices are exactly the vertices and original graph edges. Thus
\[
\mathrm{VR}_{\le}(G;2)\searrow G.
\]
This collapse is relative to \(G\), and the persistence map on degree-one homology from scale one to scale two is therefore an isomorphism, integrally and over every field.

**Scale three: a join of two graph models.** Every point–line distance is at most three. Let \(X\) be the clique complex of the point-collinearity graph, and \(Y\) the clique complex of the dual line-concurrency graph. A pair of distinct points has distance at most three precisely when it is collinear; likewise, lines have distance at most three precisely when they meet. All cross-type pairs have distance at most three. Consequently this is an equality of abstract simplicial complexes:
\[
\mathrm{VR}_{\le}(G;3)=X*Y.
\]
The cliques of the point-collinearity graph are exactly the subsets of single lines: if three points are pairwise collinear along different lines, they violate the unique-projection axiom; larger cliques inherit this obstruction. Thus \(X\) is obtained by gluing a full \(s\)-simplex along each line of the geometry, two such simplices meeting in at most a vertex. Perform a stellar subdivision of each maximal simplex at its barycenter, labeling that new vertex by the corresponding line. Inside each resulting cone, collapse the face pairs \((T,T\cup\{\ell\})\) with \(T\) a set of at least two old point vertices, in descending cardinality. Such a face belongs to no other line simplex, so these are valid free-face collapses and leave the subdivided incidence edges between a line-center and its points. The surviving complex is exactly \(G\), with its line vertices represented by barycenters. Hence \(X\simeq G\simeq\bigvee^bS^1\). Reversing points and lines gives the same conclusion for \(Y\).

For nonempty based connected CW complexes, \(X*Y\simeq\Sigma(X\wedge Y)\). Because \(X\) and \(Y\) are wedges of \(b\) circles, their smash product is a wedge of \(b^2\) two-spheres. Suspending gives
\[
\mathrm{VR}_{\le}(G;3)\simeq\bigvee^{b^2}S^3.
\]
There are no hidden torsion contributions: all the displayed sphere wedges have free integral homology.

**Scale four and the barcode.** The incidence graph has diameter four, so at scale four the Rips complex is the full simplex on its vertex set; it stays contractible thereafter. Integral scales are the only times the graph-metric filtration changes. The scale-one-to-scale-two homotopy equivalence established above guarantees all \(b\) degree-one classes survive from birth at scale one until death at scale three. The degree-three classes are first present at scale three and die at four. The homotopy types at all integer scales have no other positive-dimensional homology; hence there are no other positive-dimensional intervals.

## Verification
The included standard-library Python file `verify.py` independently constructs the symplectic generalized quadrangles of orders \((2,2)\) and \((3,3)\) over prime fields and their bipartite incidence graphs. It computes every vertex-to-vertex distance by breadth-first search; independently enumerates maximal cliques in the squared graph and both homogeneous collinearity graphs; checks the exact scale-two closed-star simplices; and actually executes each proposed free-face collapse, asserting that precisely the incidence graph remains. It then verifies the exact scale-three join adjacency and computes the complete reduced mod-two Betti vectors of both factors via explicit simplex-boundary elimination.

Run `python3 verify.py` from the directory containing that script. The output for orders two and three respectively gives graph cycle ranks \(16\) and \(81\); the two factor complexes each have reduced first Betti ranks \(16\) and \(81\), and no other reduced mod-two Betti numbers. The corresponding derived join third Betti counts are \(256\) and \(6561\). The finite verifier corroborates the symbolic proof but is not used to extrapolate it to arbitrary orders. The checked console output is included as `verification_output.txt`.

## Relationship to prior work
Adamaszek and Adams establish the Vietoris–Rips/flag-complex framework and detailed results for metric circles. Adamaszek's graph-power results include a high-girth collapse for a square graph, which is compatible with the scale-two result here; those graph-power statements do not identify the scale-three join, high-dimensional sphere multiplicity, or barcode for generalized-quadrangle incidence graphs. McCabe's study of Vietoris–Rips approximation considers generalized-quadrangle incidence metrics and uses their short-scale cycle persistence; its inspected generalized-quadrangle section does not calculate the scale-three Rips homotopy type or the full two-stage barcode. A nearby exact formula for *projective-plane* incidence graphs concerns geometries with different girth and diameter, so it does not imply this result by specialization.

## Limitations
This theorem applies only to finite thick generalized quadrangles, with the ordinary unweighted graph metric and weak-threshold Rips filtration. It is not a statement about generalized polygons of other diameters or about arbitrary perturbations of edge lengths. Only the positive-degree barcode is asserted; zero-dimensional bars, including those disappearing when the graph first becomes connected, are outside the stated formula. The verification examples cover only two prime-power orders, whereas the proof applies to every existing finite quadrangle of order \((s,t)\) with \(s,t\ge2\). A literature comparison cannot rule out an equivalent statement in unindexed or differently worded graph-power or incidence-topology work.

## References
1. M. Adamaszek and H. Adams, “The Vietoris–Rips complexes of a circle,” arXiv:1503.03669 (first public version, 2015-03-12). Published classification includes primary MSC 55U10. https://arxiv.org/abs/1503.03669
2. M. Adamaszek, “Clique complexes and graph powers,” arXiv:1104.0433 (2011). In particular, the high-girth graph-power collapse criterion. https://arxiv.org/abs/1104.0433
3. K. McCabe, “Lower Bounds for Approximating the Vietoris–Rips Filtration,” arXiv:2607.06524 (2026), section on generalized quadrangles. https://arxiv.org/abs/2607.06524
