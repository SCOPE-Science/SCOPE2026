# Private-square-edge collapse theorem for ordinary three-cut complexes

## Finding
Let \(G=(V,E)\) be a finite simple triangle-free graph on \(N\ge8\) vertices. Assume that any two distinct vertices have at most two common neighbors, and **every four-cycle contains at least one edge occurring in no other four-cycle**. Let \(q(G)\) denote the number of four-cycles and let \(d(v)\) denote vertex degrees. Define the ordinary three-cut complex \(\Delta_3(G)\) to have facets \(V\setminus T\) for the three-vertex subsets \(T\) inducing disconnected graphs. Then
\[
\Delta_3(G)\simeq\bigvee^{B(G)} S^{N-4},\qquad
B(G)=\binom{N-1}{2}-\sum_{v\in V}\binom{d(v)}2+q(G).
\]
The zero-fold wedge is a point. Thus the only potentially nonzero reduced integral homology is free abelian of rank \(B(G)\) in degree \(N-4\). No connectivity assumption is imposed on \(G\).

In particular, the Möbius ladder \(M_{2m}\), with vertices \(\mathbb Z/(2m)\), rim edges joining consecutive vertices, and antipodal edges joining vertices at distance \(m\), satisfies for every \(m\ge4\):
\[
\Delta_3(M_{2m})\simeq\bigvee^{2m^2-8m+1}S^{2m-4}.
\]
Unlike the edge-disjoint-square case, consecutive four-cycles of this ladder share edges; its rim edges are private to their respective four-cycles.

## Assumptions and scope
All graphs are simple, undirected and finite. A four-cycle is an unordered set of four cycle edges; in a triangle-free graph its four vertices induce exactly those four edges. A *private edge* of a four-cycle belongs to no other four-cycle, although it may lie in additional two-edge paths. The common-neighbor condition excludes a \(K_{2,3}\) subgraph; it permits overlapping four-cycles (with shared edges). The ordinary cut complex is not the *total* cut complex: disconnected, rather than necessarily independent, induced triples determine its facets. Throughout, \(\bigvee^0 S^j\) denotes a point.

## Proof
**1. The Alexander dual.** Put \(K=\Delta_3(G)^\vee\), the combinatorial Alexander dual on \(V\). A subset \(F\) is a face of \(K\) exactly when every three-subset of \(F\) induces a connected subgraph of \(G\). Thus \(K\) contains all \(N\) vertices and all \(\binom N2\) edges. Since \(G\) is triangle-free, its two-faces are exactly the induced two-edge paths, of which there are \(T=\sum_v\binom{d(v)}2\). Four-vertex faces are precisely the four-cycles: if all four triples are connected, counting at least two edges per triple shows that the induced graph has at least four edges; triangle-freeness gives at most four, and equality forces a four-cycle. Conversely each four-cycle has all triples connected. There are no five-vertex faces: ten triples would demand at least twenty triple-edge incidences and hence at least seven induced edges, contradicting the triangle-free bound of six edges on five vertices. Therefore the only three-simplices of \(K\) are the \(q=q(G)\) square tetrahedra and there are no higher simplices.

**2. Removing two-edge paths outside squares.** Every triangle of \(K\) not contained in a square has two nonadjacent endpoint vertices of the corresponding path. Such endpoints have exactly one common neighbor: two common neighbors would form a four-cycle, and the triangle would lie in its tetrahedron. The edge joining the endpoints therefore belongs to exactly one triangle of \(K\) and no tetrahedron, so it is a free simplicial face. Collapse each nonsquare path triangle along that endpoint edge. The common-neighbor bound ensures that no path triangle is contained in two different squares. We remove precisely \(T-4q\) triangle-edge pairs, independently of order. All square tetrahedra and their boundary triangles remain.

**3. Removing overlapping squares without deleting shared edges.** Distinct square tetrahedra share no triangle: if three vertices belonged to two four-cycles, the nonadjacent pair in their two-edge path would have at least three common neighbors, contrary to hypothesis. Likewise, a diagonal of a square occurs in no triangle of a different square. In each square choose one private *cycle edge*, and label its vertices cyclically \(a,b,c,d\) so that the private edge is \(da\). Carry out the following elementary collapses in this order:

- delete tetrahedron \(abcd\) with free triangular face \(acd\);
- delete triangle \(abc\) with free diagonal edge \(ac\);
- delete triangle \(abd\) with free private edge \(ad\);
- delete triangle \(bcd\) with free diagonal edge \(bd\).

Each indicated face is free at the stated step: the four square triangles do not occur in other tetrahedra, both diagonals are square-specific, and \(ad\) occurs in no other square and all nonsquare path triangles were already removed. Thus the square collapses can be performed independently even if two squares share other cycle edges. The resulting simplicial complex \(L\) is a graph with all \(N\) vertices and exactly
\[
\binom N2-(T-4q)-3q=\binom N2-T+q
\]
edges. It is connected, since elementary collapses preserve components and the original one-skeleton of \(K\) was complete. Hence \(K\simeq L\simeq\bigvee^{B(G)}S^1\), where
\[
B(G)=\binom N2-T+q-N+1=\binom{N-1}{2}-T+q.
\]
In particular the integer homology of \(K\) is torsion-free.

**4. Homotopy type of the cut complex.** Complementary faces reverse elementary simplicial collapses: dualizing an elementary pair of \(K\) supplies a corresponding elementary expansion on its Alexander dual. Hence \(\Delta_3(G)=K^\vee\simeq L^\vee\). As \(L\) has dimension one, \(L^\vee\) contains every subset of at most \(N-3\) vertices, hence the full \((N-4)\)-skeleton of the simplex. It is therefore \((N-5)\)-connected, and is simply connected for \(N\ge8\). Combinatorial Alexander duality yields
\[
\widetilde H_i(L^\vee;\mathbb Z)\cong \widetilde H^{N-i-3}(L;\mathbb Z),
\]
which is \(\mathbb Z^{B(G)}\) in degree \(N-4\) and zero otherwise. Since \(L^\vee\) is \((N-5)\)-connected and has dimension \(N-4\), Hurewicz and the cellular Whitehead theorem identify it with the stated wedge of \((N-4)\)-spheres. (Equivalently apply duality directly to \(K\), then the full low skeleton of \(\Delta_3(G)\).)

**5. Möbius-ladder specialization.** For \(m\ge4\), the Möbius ladder has \(N=2m\), all degrees three, exactly \(m\) four-cycles bounded by consecutive antipodal chords and two opposite rim edges, and no triangles or \(K_{2,3}\). Every such square has two private rim edges, while neighboring squares share their chord edges. Thus \(T=2m\binom32=6m\) and \(B=\binom{2m-1}{2}-6m+m=2m^2-8m+1\), proving the displayed family formula.

## Verification
The standalone `verify.py` reconstructs the Alexander dual from adjacency, enumerates all connected triples and four-cycles, checks the hypotheses, executes the specified elementary collapses with actual free-face checks, and measures the final connected graph rank. It independently verifies reduced mod-two homology of the ordinary three-cut complex for the first two Möbius ladders. Running `python3 verify.py` returns `VERIFY_OK`; tests cover Möbius ladders with \(4\le m\le12\), five open ladders with overlapping squares, and a disconnected sample. These are finite corroborations only: the proof above establishes the theorem for all eligible graphs.

## Relationship to prior work
Bayer et al., *Topology of Cut Complexes of Graphs* (2023), defined and studied ordinary cut complexes, including cycles, forests, and clique prisms, but not this general family of overlapping four-cycles. Their sequel (2024) treats grid graphs and related constructions. The published result *Three-cut complexes of triangle-free graphs with edge-disjoint squares* covers the stricter class in which no two four-cycles share an edge; its proof and statement explicitly do not cover intersecting square edge sets. Our square-specific private-edge collapse applies to a strictly broader class, witnessed by every Möbius ladder in the stated range. The published circular-ladder theorem *Sphere-wedge topology of three-cut complexes of circular ladders* has an identical numerical formula for \(C_m\square K_2\), but that is a distinct graph and does not imply a statement for the Möbius ladder \(M_{2m}\). Published Möbius-ladder total-three-cut calculations concern a different simplicial complex with different defining facets and sphere dimensions.

## Limitations
The theorem requires triangle-freeness, at most two common neighbors, a private cycle edge for every square, and \(N\ge8\). Graphs with \(K_{2,3}\), without private square edges, or with triangles are not addressed. No automorphism character, shellability or larger-cut parameter statement is asserted. A literature search cannot exclude equivalent unindexed results; the principal remaining originality risk is a pre-existing collapse criterion expressed in hypergraph or combinatorial Alexander-duality language. The finite checker is not an infinite-range certificate.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 2023-04-26), https://arxiv.org/abs/2304.13675 .

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public 2024-07-11), https://arxiv.org/abs/2407.08158 .

[3] *Three-cut complexes of triangle-free graphs with edge-disjoint squares*, publicly released 2026-10-11, section 'Proof' (full text compared).

[4] *Sphere-wedge topology of three-cut complexes of circular ladders*, publicly released 2026-10-11, section 'Proof' (full text compared).
