# Scale-two Rips complexes of graphs with edge-disjoint hexagons

## Finding

**Theorem.** Let \(G\) be a finite connected simple graph of girth at least six (forests are allowed). Assume that any two distinct simple cycles of length six have disjoint edge sets. Let \(b=|E(G)|-|V(G)|+1\) and \(t=c_6(G)\), where each unoriented simple six-cycle is counted once. With shortest-path metric \(d_G\) on \(V(G)\), form the inclusive scale-two Vietoris--Rips complex \(K=\operatorname{VR}(V(G),d_G;2)\): a finite vertex subset spans a simplex precisely if each pair has graph distance at most two. Then

\[
|K|\simeq \bigvee^{b-t}S^1\vee\bigvee^t S^2.
\]

In particular, \(b\ge t\), and \(\widetilde H_1(K;\mathbb Z)\cong\mathbb Z^{b-t}\), \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^t\); all other reduced integral homology groups vanish. An empty wedge is a point. No torsion occurs.

The graph consisting of three internally vertex-disjoint paths of respective edge-lengths \(3,3,4\) between two common endpoints has \(b=2\) and \(t=1\), so its scale-two Rips complex is homotopy equivalent to \(S^1\vee S^2\). This example is not a cactus: its six- and seven-cycles share three edges.

## Assumptions and scope

All graphs are finite, simple, undirected, and connected; a one-vertex graph is permitted. A six-cycle is a six-vertex simple closed walk considered up to cyclic rotation and reversal, with no inducedness requirement. Girth at least six excludes cycles of lengths three through five; it also makes every six-cycle chordless. Distances are integer shortest-path distances and the Rips threshold is inclusive: \(d_G(u,v)\le 2\). The theorem does not assume bipartiteness, regularity, bounded degree, or any separation between seven-cycles. The six-cycle edge-disjointness hypothesis is essential to the following decomposition and is not claimed to be necessary for its conclusion.

## Proof

**1. Local-neighborhood complex.** For each vertex \(v\), let \(N[v]=\{v\}\cup N_G(v)\) and set \(K_0=\bigcup_{v\in V(G)}\Delta(N[v])\). Each \(\Delta(N[v])\) lies in \(K\), because its vertices are pairwise at graph distance at most two. Girth at least five ensures that distinct vertices at distance two have a unique common neighbor, and no two adjacent vertices have a third common neighbor.

We classify the triangles of \(K\) absent from \(K_0\). If a triple has a pair adjacent in \(G\), it lies in some \(N[v]\): otherwise the two shortest paths of length at most two from the third vertex to the endpoints of the adjacent edge create a cycle of length at most five. If all three distances are two, write their unique intermediate vertices on the three length-two paths. If two intermediate vertices agree then all three agree, so the triple lies in a common closed neighborhood. Otherwise the three intermediate vertices are distinct and, alternating with the three original vertices, form a simple six-cycle. Conversely, for each six-cycle \((v_0,v_1,\ldots,v_5)\), the two alternating triples \(\{v_0,v_2,v_4\}\) and \(\{v_1,v_3,v_5\}\) are triangles of \(K\) not in \(K_0\). The unique-intermediate-vertex property shows they determine that six-cycle uniquely; hence distinct cycles give distinct pairs of additional triangles.

**2. These triangles are maximal.** Suppose an alternating triangle \(\{a,b,c\}\), with respective pairwise middle vertices \(x,y,z\), were contained in a larger clique of \(G^2\). Let \(w\) be an extra vertex. It cannot be adjacent in \(G\) to any of \(a,b,c\): a length-one path from \(w\) to one triangle vertex and a length-at-most-two path to a second vertex, together with their unique two-edge path, would create a cycle of length at most five. Thus all three distances from \(w\) to \(a,b,c\) equal two. Let \(p\) and \(q\) be the unique middle vertices of \(w\)--\(a\) and \(w\)--\(b\). If \(p\ne q\), the simple six-cycle \(w,p,a,x,b,q,w\) shares the two edges of \(a,x,b\) with the original cycle. If \(p=q\), uniqueness of the common neighbor of \(a,b\) gives \(p=q=x\). Taking the middle vertex \(r\) of \(w\)--\(c\), the six-cycle \(w,x,a,z,c,r,w\) shares the two edges of \(x,a,z\) with the original cycle. In either case this is a distinct six-cycle sharing an edge, contrary to the hypothesis. Therefore no new triangle belongs to a four-vertex clique. Every clique of size at least three has a pair at graph distance two (otherwise it would span a triangle in the original triangle-free graph). Fix such a pair \(a,b\) with unique middle vertex \(x\). If every other vertex of the clique belongs to \(N[x]\), the whole clique lies in \(K_0\); otherwise a third vertex outside \(N[x]\) gives a triangle not in \(K_0\), which by Step 1 must be alternating on a six-cycle. Hence every clique outside \(K_0\) contains a special triangle. It follows that exactly \(2t\) two-dimensional simplices are missing from \(K_0\), and every proper face of each is already in \(K_0\):

\[K=K_0\cup\bigcup_{i=1}^{t}(\Delta T_i^+\cup\Delta T_i^-).\]

**3. Collapse the neighborhood complex.** For each \(v\) and each subset \(\sigma\subseteq N_G(v)\) with at least two vertices, pair the face \(\sigma\) with \(\sigma\cup\{v\}\). Girth at least five ensures any face containing two neighbors of \(v\) is contained in the unique maximal neighborhood simplex \(\Delta(N[v])\); no other \(N[w]\) contains that pair. For each \(v\), perform these elementary collapses in decreasing order of \(|\sigma|\). Each \(\sigma\) is then a free face of \(\sigma\cup\{v\}\), and pairings for different centers cannot interfere. These remove every face of dimension at least two and every distance-two edge, leaving precisely the original one-dimensional graph \(G\). Thus \(K_0\searrow G\). Under this strong deformation retraction, every added distance-two edge \(\{u,w\}\) travels along its unique length-two path \(u-v-w\) in \(G\).

**4. Attach and cancel hexagon disks.** Attach the \(2t\) missing triangles to \(K_0\) as two-cells along their existing boundary loops. After the collapse of \(K_0\), each pair of triangle boundaries associated with a hexagon is homotopic in \(G\) to the same underlying simple six-cycle, with opposite orientations possible. This follows by replacing every distance-two edge of an alternating triangle with its unique two-edge path. Homotopy invariance of cell attachment along homotopic maps therefore gives a CW complex comprising \(G\) with two disks attached along each six-cycle.

First attach one disk for each of the \(t\) cycles. Since the cycles are edge-disjoint, select one different original graph edge on each cycle. In the resulting CW complex each selected edge occurs in the attaching boundary of precisely its own disk and occurs there once, so each disk and its selected edge form a free CW cell pair. Collapse these pairs. The remaining connected graph has \(|E(G)|-t\) edges and the original \(|V(G)|\) vertices, hence cycle rank \(b-t\). Each second disk is now attached along a loop nullhomotopic by the first disk on its same hexagon. Attaching such a two-cell is homotopy equivalent to wedging on \(S^2\). The entire space is consequently \(\bigvee^{b-t}S^1\vee\bigvee^{t}S^2\). All assertions follow. \(\square\)

## Verification

The accompanying `verify_hex.py` uses only the Python 3 standard library. It independently constructs graph distance matrices, enumerates all cliques of graph squares, enumerates all simple cycles up to length six, checks the entire simplex decomposition \(K\setminus K_0\) against precisely the two alternating triangles for every six-cycle, and computes boundary ranks modulo two and three. Run `python3 verify_hex.py`. It checks fourteen connected admissible graphs (cycles, theta graphs, two hexagons meeting at one vertex, and two hexagons connected by a bridge), twenty-eight modular homology comparisons, and a reproducible bounded random test of hundreds of candidate graphs, of which 252 satisfy the hypotheses. Expected output begins `VERIFY_OK 14 homology instances, 28 exact rank checks`. These finite checks are not used as a substitute for the all-parameter homotopy proof.

## Relationship to prior work

Michał Adamaszek, *Clique complexes and graph powers* (arXiv:1104.0433), Proposition 2.2, proves collapse of \(\operatorname{Cl}(G^2)\) to \(G\) for graphs with girth at least seven and analyzes individual cycle powers, including the octahedral sphere arising from the six-cycle. Those results cover the no-hexagon regime and a standalone hexagon but do not establish the mixed-dimensional formula for overlapping longer cycles such as the theta \((3,3,4)\) example.

*Vietoris--Rips and Čech Complexes of Metric Gluings* (SoCG 2018, DOI:10.4230/LIPIcs.SoCG.2018.3) establishes useful wedge decompositions for cycles glued along vertices or single edges and metric gluing at sufficiently short paths. Its path-gluing criterion does not cover the example of length-three overlapping paths on a girth-six theta graph at scale two; the present argument uses a different incidence restriction on all six-cycles.

Kazuhiro Kawamura's *A variant of the bipartite relation theorem and its application to clique graphs* concerns square-graph clique complexes and bipartite homological comparisons; it does not supply this full simple homotopy decomposition for arbitrary possibly nonbipartite graphs. Recent work on lattice Rips complexes by Gupta, Sarkar, and Shukla (arXiv:2511.04238, first publicly posted 2025-11-06) motivates investigating exact metric-threshold homotopy beyond isolated examples, but studies distinct lattice configurations. The present theorem has a graph-girth and nonoverlapping-hexagon scope.

## Limitations

The result does not apply without qualification when hexagons share original graph edges, and does not classify the complete Rips filtration, higher distance thresholds, intrinsic geometric realizations, or torsion of general graph Rips complexes. Edge-disjointness is sufficient, not asserted necessary. The modular computations are finite corroboration; the general claim rests on the explicit topological collapse-and-attachment proof. No independent assessment has been performed.

## References

- M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011).
- *Vietoris--Rips and Čech Complexes of Metric Gluings*, Proceedings of SoCG 2018, DOI:10.4230/LIPIcs.SoCG.2018.3.
- K. Kawamura, *A variant of the bipartite relation theorem and its application to clique graphs*, Contributions to Discrete Mathematics, DOI:10.55016/ojs/cdm.v6i2.62059 (2011).
- Gupta, Sarkar, and Shukla, *On Vietoris--Rips Complexes of Integer Lattices*, arXiv:2511.04238 (2025).
