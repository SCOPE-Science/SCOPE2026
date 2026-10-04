# Graph 2-cores classify Stong cores of incidence posets
## Finding
Let \(G\) be a nonempty finite simple graph and let \(P(G)\) denote its incidence poset: the elements are \(V(G)\sqcup E(G)\), every vertex is minimal, every edge is maximal, and \(v<e\) exactly when \(v\) is an endpoint of \(e\). Let \(C_2(G)\) be the graph-theoretic 2-core obtained by repeatedly deleting vertices of degree less than two, and let \(t(G)\) be the number of connected components of \(G\) that are trees, including isolated vertices as one-vertex trees. Then
\[
\operatorname{core} P(G)\cong P(C_2(G))\sqcup D_{t(G)},
\]
where \(D_m\) is a discrete \(m\)-point finite space. In particular,
\[
|\operatorname{core} P(G)|=|V(C_2(G))|+|E(C_2(G))|+t(G).
\]
Therefore, for nonempty finite simple graphs \(G\) and \(H\),
\[
P(G)\simeq P(H)\quad\Longleftrightarrow\quad C_2(G)\cong C_2(H)\text{ and }t(G)=t(H).
\]
Thus finite-space homotopy of graph incidence posets forgets all attached trees but remembers the entire graph-theoretic 2-core, not merely its first Betti number.

## Assumptions and scope
Graphs are finite, simple, undirected, and nonempty. A tree component includes an isolated vertex. The graph-theoretic 2-core is the unique maximal induced subgraph of minimum degree at least two; it may be empty. The notation \(P(\varnothing)\) denotes the empty poset, so if every component of \(G\) is a tree the displayed core is simply \(D_{t(G)}\).

The conclusion concerns ordinary homotopy equivalence of finite \(T_0\)-spaces in Stong's sense, which is stronger than weak homotopy equivalence of their order complexes. For example, the incidence posets of a triangle and a square both have order complexes homotopy equivalent to \(S^1\), but they are minimal finite spaces with respectively six and eight points, so they are not homotopy equivalent as finite spaces.

## Proof
In \(P(G)\), a graph vertex \(v\) is a minimal poset element. Its strict upper set consists exactly of the edges incident with \(v\), and those edges are pairwise incomparable. Hence \(v\) is an up beat point exactly when \(v\) has graph degree one. A graph edge \(e=uv\) is maximal, and its strict lower set is \(\{u,v\}\), whose two elements are incomparable, so no edge is a beat point while both endpoints remain.

Suppose \(v\) is a graph leaf with unique incident edge \(e=uv\). Delete \(v\) from \(P(G)\). This is a beat-point deletion. In the remaining poset the strict lower set of \(e\) is the singleton \(\{u\}\), so \(e\) is now a down beat point. Deleting \(e\) leaves precisely the incidence poset of the graph obtained from \(G\) by deleting the leaf \(v\) and its incident edge. Thus every graph leaf-pruning step lifts to two successive Stong beat-point deletions.

Iterating these paired deletions on each connected component has the standard graph-theoretic outcome. A component containing a cycle reduces to its nonempty 2-core. A tree component reduces to a single isolated graph vertex, because repeatedly deleting a leaf and its incident edge terminates at one vertex. Therefore the resulting finite subspace is \(P(C_2(G))\sqcup D_{t(G)}\).

It remains to check minimality. Every vertex of \(C_2(G)\) has degree at least two, so its strict upper set in \(P(C_2(G))\) has at least two incomparable elements and has no minimum. Every edge still has exactly two incomparable endpoints below it, so its strict lower set has no maximum. Isolated points of \(D_{t(G)}\) have neither strict upper nor strict lower elements and are not beat points. Hence the displayed subspace has no beat points and is a Stong core.

Stong's core theorem says that two finite \(T_0\)-spaces are homotopy equivalent exactly when their cores are isomorphic. An isomorphism between nontrivial incidence-poset components preserves minimal elements, maximal elements, and incidence, so it induces an isomorphism of the corresponding simple graphs. Singleton core components are exactly the contributions from tree components. This proves the classification criterion.

## Verification
The proof above is symbolic and applies to every nonempty finite simple graph. The bundled program `verify.py` supplies an independent finite regression check. It enumerates every labeled simple graph on one through six vertices, for a total of \(33{,}867\) graphs. For each graph it computes the graph 2-core and the number of tree components, then replays the paired poset beat-point deletions, verifies that each claimed vertex deletion is an up-beat deletion and each following edge deletion is a down-beat deletion, checks the predicted final cardinality and surviving 2-core incidences, and confirms that the final poset has no beat points.

The replay reports `VERIFY_OK`, checks \(78{,}152\) beat-point deletions, and separately confirms the six-point versus eight-point cores of the triangle and square incidence posets. These finite checks corroborate boundary cases but are not used as the proof of the all-graph theorem.

## Relationship to prior work
Barmak and Minian give the beat-point/core framework for finite spaces and characterize cardinality-minimal finite models of connected finite graphs. Their 2006 preprint does not state a core formula for the incidence poset of an arbitrary graph or a homotopy classification by graph 2-cores. Barmak's monograph defines face posets and records the relation between beat-point removal and simplicial collapse, but the inspected sections do not give the graph-specific 2-core classification above.

A later paper of Costoya, Gomes, and Viruel explicitly uses incidence posets of simple graphs and minimum-degree-at-least-two graphs to construct minimal finite spaces. This is the closest directly overlapping published setup found: it supports the minimality mechanism for leafless incidence posets, but the inspected section does not treat arbitrary graphs, leaf pruning, Stong cores, or the equivalence criterion in terms of \(C_2(G)\) and \(t(G)\).

## Limitations
The theorem is restricted to incidence posets of finite simple graphs. It does not claim the same formula for multigraphs, graphs with loops, higher-dimensional face posets, or arbitrary height-two posets. The originality assessment is based on targeted database searches and inspection of the most relevant accessible primary/background sources; search non-detection is not a proof that no equivalent statement exists elsewhere.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156, first public version 2006-11-06; especially the beat-point/core preliminaries and the section on minimal finite models of graphs.
2. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, Springer, 2011; especially Sections 1.3, 1.4, and 4.1.
3. C. Costoya, R. Gomes, and A. Viruel, *Realization of Permutation Modules via Alexandroff Spaces*, Results in Mathematics 79 (2024), Article 169, DOI 10.1007/s00025-024-02199-z; especially Section 3 on incidence posets.
