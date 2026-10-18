# The second path digraph of a transitive tournament: an exact circle-and-sphere wedge

## Finding

Let \(T_n\) be the transitive tournament on \(0,\ldots,n-1\), with an arc \(i\to j\) exactly when \(i<j\). Form the **strict second path digraph** \(P^{(2)}(T_n)\) as in Caputi--Riihimäki: its vertices are the ordered directed triangles \((a,b,c)\) with \(a<b<c\); two distinct vertices \(\sigma,\tau\) satisfy \(\sigma\to\tau\) when \(d_i\sigma=d_j\tau\) for some \(0\le i<j\le2\), where \(d_i\) deletes entry \(i\). Let \(X_n\) be the geometric realization of the directed flag complex of this digraph. For **every integer \(n\ge3\)**,

\[
X_n\simeq\bigvee^{5\binom{n-2}{3}}S^1\ \vee\ \bigvee^{\binom{n-3}{5}}S^2.
\]

Here \(\binom{a}{b}=0\) for integers \(a\ge0\) and \(b>a\). Thus \(X_3\) and \(X_4\) are contractible; \(X_5\simeq\bigvee^5 S^1\); and two-dimensional homology first appears at \(n=8\), where \(X_8\simeq\bigvee^{100}S^1\vee S^2\). In particular all its integral homology is torsion-free, and its reduced homology vanishes except in degrees one and two with the stated ranks.

## Assumptions and scope

All graphs are finite and loop-free. A directed simplex means a strictly ordered clique whose arcs point forward in the displayed order, not an undirected clique carrying arbitrary cyclic orientations. The **strict** condition \(i<j\) is essential: the relaxed construction allowing \(i\le j\) is not covered. The theorem concerns the second path digraph of the complete acyclic orientation of a complete graph, **not** its iterated line digraph, its ordinary path-homology chain complex, or a multipath complex on edge subsets. The homotopy equivalences are nonequivariant.

## Proof

**1. A canonical cover by three-part joins.** Fix a two-element subset \(\{u,v\}\subseteq\{0,\ldots,n-1\}\) with \(u<v\). Let \(B_{uv}\) be the subcomplex of \(X_n\) on the directed triangles \((a,b,c)\) whose underlying three-set contains \(u,v\). Partition the third element into the intervals

\[
L_{uv}=\{w:w<u\},\quad M_{uv}=\{w:u<w<v\},\quad R_{uv}=\{w:w>v\}.
\]

For a vertex with third element in \(L_{uv},M_{uv},R_{uv}\), respectively, deletion of the common pair's *other* element occurs at position \(0,1,2\), respectively. More precisely, the third element itself is deleted in position \(0,1,2\) to obtain the common face \((u,v)\). Consequently two different triples containing \(u,v\) are joined by a strict path-digraph arc if and only if their third elements belong to **different** interval classes, and that arc points in the order \(L\to M\to R\). Every ordered selection from distinct nonempty classes is a directed clique. Therefore \(B_{uv}\) is precisely the simplicial join of the three discrete interval sets (omitting empty factors), i.e. the clique complex of a complete tripartite graph with the empty parts discarded.

Any arc of \(P^{(2)}(T_n)\) joins two triples sharing exactly two input vertices, so belongs to a **unique** block \(B_{uv}\). A directed three-clique must also belong to one block: three distinct three-subsets that pairwise share two elements either have a common two-subset or are three of the four three-subsets of one four-subset. In the latter situation, for \(a<b<c<d\) the permitted undirected adjacency pairs are exactly

\[
\{abc,acd\},\quad\{abc,bcd\},\quad\{abd,bcd\},
\]

which form a four-vertex path and contain no triangle. Thus every three-clique is contained in a unique \(B_{uv}\). Four-cliques are impossible: in the common-pair case there are only three interval classes, and in the four-subset case the induced adjacency graph is a path. Hence \(X_n\) is two-dimensional and is the union of the \(B_{uv}\), with all edges and triangles assigned to unique blocks. Distinct blocks intersect in at most one vertex: a triple containing two different input pairs exists only if those pairs share one input vertex, in which case their union uniquely determines the triple.

**2. Homotopy of the blocks and of their point-gluing.** Write \(\ell=u\), \(m=v-u-1\), and \(r=n-1-v\) for the sizes of the three interval classes. When all are positive, \(B_{uv}\) is the join of three nonempty discrete sets and has homotopy type \(\bigvee^{(\ell-1)(m-1)(r-1)}S^2\), with zero wedge summands interpreted as a point. Indeed, the join of the first two sets is a complete bipartite graph, a wedge of \((\ell-1)(m-1)\) circles; joining with a discrete \(r\)-set gives \((r-1)\) suspensions of that connected graph. If exactly two classes are nonempty, the block is a complete bipartite graph and is a wedge of circles. If at most one is nonempty, it is a discrete set (possibly empty).

We use the elementary **point-gluing lemma**: if a connected finite CW complex is assembled from finitely many spaces, each homotopy equivalent to a wedge of positive-dimensional spheres or a point, solely by identifying specified zero-cells between these spaces (no higher-dimensional cells are shared), then the resulting complex is itself homotopy equivalent to a wedge of the constituent spheres and some additional circles. For completeness, take disjoint copies of the connected components of the spaces and implement each prescribed vertex identification by attaching an interval between the corresponding copies, using a spanning tree of intervals for all copies of each identified vertex. Contracting each such interval tree, a contractible subcomplex, is a homotopy equivalence and recovers the original identification space. Attaching these intervals successively either joins two components without changing their positive-dimensional wedge summands, or joins two points in one component and introduces exactly one circle up to homotopy. Thus no higher attaching map is created. Applied to the blocks \(B_{uv}\), this proves that the connected \(X_n\) is a wedge of circles and two-spheres.

For connectedness, the graph on all three-subsets with edges whenever they intersect in two elements (the Johnson graph) is connected. Every such edge lies in the four three-subsets of a four-set, and the permitted path-digraph edges among those four form the connected four-vertex path displayed above. Therefore the one-skeleton of \(X_n\) is connected for \(n\ge4\); for \(n=3\) it has one vertex.

**3. Exact two-sphere count.** Identifications at vertices cannot change second homology. Each block contributes \((\ell-1)(m-1)(r-1)\) integral two-spheres if all three interval classes are nonempty, and zero otherwise. Since \(\ell+m+r=n-2\), the total two-sphere count is

\[
\begin{aligned}
\beta_2(X_n)
&=\sum_{\substack{\ell,m,r\ge1\\\ell+m+r=n-2}}(\ell-1)(m-1)(r-1)\\
&=[z^{n-2}]\left(\sum_{a\ge1}(a-1)z^a\right)^3\\
&=[z^{n-2}]\frac{z^6}{(1-z)^6}=\binom{n-3}{5}.
\end{aligned}
\]

This expression is zero until \(n=8\), when it equals one.

**4. Exact circle count.** There are \(\binom n3\) vertices, one for each three-subset. Each four-subset contributes precisely the three distinct arcs from step 1, and every arc has a unique union four-subset, so the number of edges is \(3\binom n4\). A triangle belongs to a unique common-pair block and consists of one third element from each of the three interval classes. Such a triangle corresponds bijectively to a five-subset \(a<b<c<d<e\), with three vertices \((a,b,d),(b,c,d),(b,d,e)\); hence there are \(\binom n5\) two-simplices. Consequently,

\[
\chi(X_n)=\binom n3-3\binom n4+\binom n5.
\]

Since \(X_n\) is connected and homotopy equivalent to a circle-and-two-sphere wedge, \(\chi(X_n)=1-\beta_1+\beta_2\). Substituting the two-sphere count and using the binomial identity

\[
1-\binom n3+3\binom n4-\binom n5+\binom{n-3}{5}=5\binom{n-2}{3}
\]

establishes the claimed number of circles and completes the proof, including integral torsion-freeness and the full homotopy type.

## Verification

A separate, finite exhaustive implementation is included as `verify_pathdigraph.py` (Python 3 standard library only). It constructs vertices and arcs from the original \(d_i=d_j\), \(i<j\), rule rather than from the local model; independently generates every directed triangle; checks the predicted three-part pair-block edge decomposition, absence of four-cliques, connectivity and face counts; and computes the mod-two rank of the two-boundary by exact bit elimination. It checks every \(3\le n\le11\), including the first nonzero two-sphere stage. A run exits with the line `PATH_DIGRAPH_TOURNAMENT_2_FLAG_FINITE_CHECKS_OK`. These finite checks do **not** prove the all-parameter result; the argument above supplies that proof.

## Relationship to prior work

Caputi and Riihimäki introduced the strict higher path-digraph functor in Definition 3.20 of arXiv:2204.00462 (first public 2022-04-01), proved that it preserves acyclicity, and explicitly asked in Question 3.33 for the homotopy type and Betti numbers of associated directed flag complexes. Their examples and pseudomanifold discussion do not classify the second path digraph of the transitive tournament. The present theorem gives an exact all-size answer for this canonical input family.

Riihimäki's arXiv:2202.07307 studies different directed \(q\)-connectivity preorders, with face-map choices and simplices of varying dimensions; it does not provide the strict \(i<j\) second path-digraph wedge classification here. The published scale-one Johnson-graph clique-complex classification concerns the **full** Johnson adjacency graph on three-subsets, whereas the graph here retains only three of the six possible edges on each four-subset. That stronger-adjacency complex is simply connected in its stated range; \(X_n\) has positive first Betti number for \(n\ge5\), so its homotopy type cannot follow by identifying these complexes. The multipath complex of Caputi, Collari, Di Trani and Smith is instead a simplicial complex on edge subsets supporting disjoint directed paths and is a different construction.

## Limitations

The theorem treats one class of input digraphs and the strict second path-digraph only. No persistence maps, higher path-digraph indices, arbitrary orientations, or relaxed face-map condition are classified. The homotopy equivalences are not asserted equivariant. The literature comparison covers the identified primary sources and research records; an unindexed equivalent argument may exist. No independent mathematical audit has been performed.

## References

1. L. Caputi and H. Riihimäki, *Hochschild homology, and a persistent approach via connectivity digraphs*, arXiv:2204.00462v1, 2022-04-01, Definition 3.20, Proposition 3.26, Question 3.33; doi:10.1007/s41468-023-00118-9.
2. H. Riihimäki, *Simplicial q-connectivity of directed graphs with applications to network analysis*, arXiv:2202.07307v1, 2022-02-15, Sections 3–4; doi:10.1137/22M1480021.
3. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, 2022-08-09, introductory definitions and abstract.
4. *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sphere-wedge-collapse-of-scale-one-johnson-graph-rips-complexes--c10287ed1518, statement and proof sections.
