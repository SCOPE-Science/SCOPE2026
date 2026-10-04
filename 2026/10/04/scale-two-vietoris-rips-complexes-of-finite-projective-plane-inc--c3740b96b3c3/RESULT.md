# Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs
## Finding
For every finite projective plane \(\Pi\) of order \(q\ge 2\), if \(G_\Pi\) is its incidence graph with the shortest-path metric, then \(\mathrm{VR}(G_\Pi;2)\simeq\bigvee^{q^3}S^2\). Consequently its positive-dimensional Vietoris–Rips persistence has exactly \(q^3\) degree-\(1\) bars with birth \(1\) and death \(2\), exactly \(q^3\) degree-\(2\) bars with birth \(2\) and death \(3\), and no other positive-dimensional bars.

## Assumptions and scope
A finite projective plane \(\Pi\) of order \(q\ge 2\) has \(N=q^2+q+1\) points and \(N\) lines; each point lies on \(q+1\) lines, each line contains \(q+1\) points, every two distinct points lie on a unique common line, and every two distinct lines meet in a unique point. Let \(G_\Pi\) be the bipartite incidence graph on the point set and line set. Every graph edge has length \(1\), and \(\mathrm{VR}(G_\Pi;r)\) contains a simplex precisely when its vertices have pairwise graph distance at most \(r\). The convention is inclusive at the scale boundary.

The result applies to every finite projective plane, not only Desarguesian planes. It makes no existence assertion for orders for which finite projective planes are unknown or impossible.

## Proof
Write \(P\) for the set of points and \(L\) for the set of lines. Two distinct vertices in the same bipartition class have distance \(2\): two points share their unique joining line, and two lines share their unique intersection point. A point and a line have distance \(1\) when incident and distance \(3\) otherwise. Hence \(G_\Pi\) has diameter \(3\).

For \(1\le r<2\), the Vietoris–Rips complex is the clique complex of the original bipartite graph. Since the graph is triangle-free, the complex is just \(G_\Pi\). It is connected, has \(2N\) vertices and \((q+1)N\) edges, so its first Betti number over any field is
\[
(q+1)N-2N+1=(q-1)(q^2+q+1)+1=q^3.
\]
Thus \(\mathrm{VR}(G_\Pi;r)\simeq\bigvee^{q^3}S^1\) on this scale interval.

Now put \(K=\mathrm{VR}(G_\Pi;2)\). Every pair of points is adjacent in the distance-two graph, as is every pair of lines. A clique containing at least two points and at least two lines cannot exist: two distinct points are incident with at most one common line. Therefore every mixed clique is contained either in \(\{\ell\}\cup P(\ell)\) for one line \(\ell\), or in \(\{p\}\cup L(p)\) for one point \(p\).

Let \(U\) be the union of the simplex on all of \(P\) with the simplices \(\{\ell\}\cup P(\ell)\) over all lines \(\ell\). Let \(V\) be the union of the simplex on all of \(L\) with the simplices \(\{p\}\cup L(p)\) over all points \(p\). The clique classification gives \(K=U\cup V\). In \(U\), each line vertex occurs in a unique maximal simplex \(\{\ell\}\cup P(\ell)\), so deleting line vertices one by one is a sequence of dominated-vertex collapses, leaving the simplex on \(P\). Hence \(U\) is contractible. Symmetrically, \(V\) collapses to the simplex on \(L\) and is contractible.

The intersection \(U\cap V\) contains exactly the vertices and the point-line incidence edges, hence \(U\cap V=G_\Pi\) as a simplicial complex. Because these are finite simplicial complexes and the intersection inclusions are cofibrations, the union is a homotopy pushout. Replacing the two contractible pieces by points identifies that homotopy pushout with the unreduced suspension:
\[
K\simeq \Sigma G_\Pi.
\]
A connected graph with first Betti number \(q^3\) is homotopy equivalent to \(\bigvee^{q^3}S^1\), so suspension yields
\[
\mathrm{VR}(G_\Pi;2)\simeq \bigvee^{q^3}S^2.
\]
For \(r\ge3\), the diameter calculation makes every pair of vertices adjacent, so the Vietoris–Rips complex is the full simplex and is contractible. Since all graph distances are integral, no change occurs between consecutive integer scales. The stated positive-dimensional persistence bars follow immediately.

## Verification
The accompanying standard-library verifier independently constructs \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\), checks all projective-plane incidence axioms used in the proof, recomputes all graph distances, obtains the scale-two maximal cliques by Bron–Kerbosch search, independently constructs the proof's expected maximal-clique family, and requires the two families to agree. It then computes every scale-two simplex and exact mod-\(2\) boundary rank.

For order \(2\), it finds \(331\) nonempty simplices, face vector \((14,63,112,84,42,14,2)\), boundary ranks \((13,50,54,30,12,2)\), and Betti vector \((1,0,8,0,0,0,0)\). For order \(3\), it finds \(16720\) nonempty simplices, face vector \((26,208,728,1534,2600,3432,3432,2574,1430,572,156,26,2)\), boundary ranks \((25,183,518,1016,1584,1848,1584,990,440,132,24,2)\), and Betti vector \((1,0,27,0,0,0,0,0,0,0,0,0,0)\). It also verifies directly that the two proof subcomplexes intersect in exactly the incidence graph. These computations corroborate the general proof; they are not used to extrapolate from finite examples.

## Relationship to prior work
Adams and Coskunuzer identify graph-power filtrations with Vietoris–Rips filtrations of shortest-path graph metrics and emphasize the geometric information carried by higher-dimensional persistence. Their paper supplies the literature-led setting for the present exact family but does not treat incidence graphs, bipartite graphs, the Heawood graph, or finite projective planes.

Adamaszek studies clique complexes of graph powers and gives exact homotopy types for cycle powers, including the familiar dimension jump for a six-cycle, and a separate theorem for squares of edge-subdivision graphs. The projective-plane incidence graph is not an edge-subdivision graph of that type when \(q\ge2\), and the inspected full text contains no projective-plane or bipartite-square theorem covering the claim here.

Larrión, Pizaña, and Villarroel-Flores prove that for a finite connected bipartite graph, the clique complex of its square and the clique complexes induced by the two bipartition classes have isomorphic fundamental groups. Applied here this is compatible with simple connectivity at scale \(2\), but it does not determine the second homology, the wedge multiplicity \(q^3\), or the homotopy type. Parks and Marchette give general persistence bounds for graph-power filtrations from girth and chordality; those bounds likewise do not imply the scale-two suspension calculation.

## Limitations
The originality search cannot exclude every unindexed thesis, note, or computation. The finite verifier covers only the Desarguesian planes of orders \(2\) and \(3\); correctness for all finite projective planes rests on the structural proof from the projective-plane axioms. No claim is made about generalized incidence geometries in which two points or two lines can have more than one common neighbor, nor about weighted graph metrics.

## References
Adams, H.; Coskunuzer, B. *Geometric Approaches on Persistent Homology*. arXiv:2103.06408, first submitted 2021-03-11. MSC 55N31, 55U10, 57R19, 62R40.

Adamaszek, M. *Clique complexes and graph powers*. arXiv:1104.0433, first submitted 2011-04-03.

Larrión, F.; Pizaña, M. A.; Villarroel-Flores, R. *The fundamental group of the clique graph*. European Journal of Combinatorics 30 (2009), 288–294. DOI: 10.1016/j.ejc.2007.12.006.

Parks, A. D.; Marchette, D. J. *Persistent homology in graph power filtrations*. Royal Society Open Science 3 (2016), 160228. DOI: 10.1098/rsos.160228.
