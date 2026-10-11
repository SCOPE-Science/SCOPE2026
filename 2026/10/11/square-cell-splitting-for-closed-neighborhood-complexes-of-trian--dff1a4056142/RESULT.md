# Square-cell splitting for closed neighborhood complexes of triangle-free graphs

## Finding

Let \(G=(V,E)\) be a finite connected simple graph with no triangles and no subgraph \(K_{2,3}\). Define its **closed neighborhood complex** \(\mathcal N[G]\) by declaring \(\sigma\subseteq V\) a simplex precisely when \(\sigma\subseteq N_G[v]=\{v\}\cup N_G(v)\) for some vertex \(v\). Let \(\mathscr Q(G)\) be the set of unoriented simple four-cycles, \(q=|\mathscr Q(G)|\), and let \(X_G\) be the CW complex obtained by attaching a two-disk along each four-cycle of the graph \(G\).

**Theorem.** There is a sequence of elementary simplicial collapses
\[
\mathcal N[G]\searrow K_G=G\cup\bigcup_{C\in\mathscr Q(G)}\partial\Delta^3_{V(C)},
\]
where the four-vertex tetrahedral boundary is viewed as the two-dimensional simplicial sphere consisting of all proper subsets of the four vertices of \(C\). Furthermore,
\[
|\mathcal N[G]|\simeq |X_G|\vee\bigvee^q S^2.
\]
The prescribed sequence has exactly
\[
\sum_{v\in V}(2^{\deg(v)}-\deg(v)-1)-4q
\]
elementary collapses. The graph-theoretic hypotheses are directly checkable: no pair of vertices has three common neighbors and no triple of vertices forms a triangle.

**Grid consequence.** For all integers \(m,n\ge2\), the rectangular grid graph \(P_m\square P_n\) satisfies the hypotheses. Its four-cycles are its \((m-1)(n-1)\) square faces, and \(X_G\) is a cellulated closed rectangle. Hence
\[
\mathcal N[P_m\square P_n]\simeq\bigvee^{(m-1)(n-1)}S^2.
\]

## Assumptions and scope

All complexes are finite, and all simplicial faces below are nonempty unless the empty face is explicitly mentioned. The symbol \(\partial\Delta^3_{V(C)}\) means the simplicial boundary on the *four vertices* of a four-cycle, not a geometric triangle in the original graph. A four-cycle is counted once up to reversal and cyclic rotation. Each such cycle is induced because the graph is triangle-free. The condition that no two vertices have three common neighbors is equivalent to forbidding \(K_{2,3}\) as a not necessarily induced subgraph. The wedge is a homotopy equivalence of realizations, not a claim of homeomorphism or simplicial isomorphism.

## Proof

**Step 1: identify the exceptional neighbor pairs.** Fix \(v\in V\), and consider \(F\subseteq N_G(v)\), \(|F|\ge2\). Any closed neighborhood containing \(F\) is centered at a common neighbor of the vertices of \(F\), or at a vertex of \(F\) adjacent to the others. The latter is impossible: vertices of \(N_G(v)\) are pairwise nonadjacent, since \(G\) has no triangles. For \(|F|\ge3\), the center is uniquely \(v\), as a second common neighbor would give three common neighbors to the two distinct centers, forbidden by the \(K_{2,3}\) assumption. For \(F=\{a,b\}\), besides \(v\) there is a second center if and only if \(v-a-w-b-v\) is a four-cycle for some \(w\ne v\); that second center, when it exists, is unique by the same common-neighbor bound. Call such pairs **exceptional**.

**Step 2: elementary collapses.** For each integer \(k\) decreasing from the maximum degree to \(2\), for each vertex \(v\) in any fixed order, and for every \(k\)-subset \(F\subseteq N_G(v)\), omit only exceptional pairs when \(k=2\); otherwise pair \(F\) with \(F\cup\{v\}\) and delete both. The lower simplex \(F\) is free at its turn. Indeed its center is uniquely \(v\), so every remaining coface lies inside \(N_G[v]\); any coface of dimension greater than \(k\) was removed in an earlier descending step, and any coface of cardinality \(k+1\) other than \(F\cup\{v\}\) is a larger neighbor subset already removed at the preceding step. The upper simplex \(F\cup\{v\}\) has no other closed-neighborhood center, since any different center adjacent to both \(v\) and any vertex of \(F\) would create a triangle. Hence none of these deletions interferes with another pairing, and each is an elementary collapse.

Every original edge remains (no lower pair has cardinality one). A higher-dimensional simplex not deleted must be a triple \(\{v,a,b\}\) with \(a,b\in N_G(v)\) exceptional, or a face of such a triple. Each such exceptional pair determines an induced four-cycle \(v-a-w-b-v\). The four triples of its vertex set appear from the four choices of center, and form precisely \(\partial\Delta^3_{V(C)}\); a four-vertex simplex on this cycle cannot exist, since opposite vertices are nonadjacent and any external common center of all four vertices would give three common neighbors to an opposite pair. This proves the displayed collapse target. Each vertex \(v\) contributes \(2^{\deg(v)}-\deg(v)-1\) neighbor subsets of size at least two, and each four-cycle accounts for exactly four exceptional centered pairs. The collapse count follows.

**Step 3: separate one sphere per square.** For each square \(C=(v_0v_1v_2v_3v_0)\), choose one diagonal, say \(v_0v_2\). Within its tetrahedral boundary take the two triangles meeting along that diagonal; they form a triangulated disk filling \(C\). The union of the graph and these chosen disks over all squares is a simplicial realization of \(X_G\): distinct squares cannot share an *opposite vertex pair*, because such a pair would then have at least three common neighbors. Consequently their new diagonals are distinct, and no new diagonal is already an original graph edge (which would make a triangle). The remaining two triangles of each tetrahedral boundary form another closed disk attached along the same four-cycle. That attaching loop already bounds the first disk in \(X_G\), so its attaching map is null-homotopic. Adjoining a two-cell along a null-homotopic loop to a connected CW complex is homotopy equivalent to wedging on \(S^2\). Apply this fact successively to the \(q\) second disks to obtain \(|K_G|\simeq |X_G|\vee\bigvee^qS^2\), completing the theorem.

**Step 4: grid consequence.** The Cartesian product of two paths has no triangles; any distinct pair of grid vertices has at most two common neighbors. Its simple four-cycles are precisely unit grid cells. Filling those cells yields a rectangular two-dimensional disk, and the asserted grid wedge follows.

## Verification

The standalone `VERIFIER.py` reconstructs *all* simplices of closed-neighborhood complexes, executes every proposed collapse while independently checking its lower face has exactly one proper coface, and compares the complete final face set with the asserted graph-plus-tetrahedral-boundaries description. It additionally computes mod-two Betti numbers and compares them with the square-filled CW model and the proposed \(q\) sphere summands. It covers rectangular grids, hypercubes, cycles, the Petersen graph, and 90 reproducibly seeded admissible connected graphs, totaling 118 graph instances. Its successful final message is `VERIFY_OK 118 graph instances; 90 seeded random admissible connected graphs with homology-splitting tests; complete free-face and residual tests`.

The finite tests corroborate but do not substitute for the general free-face and attaching-map arguments above. Neither exact integral homology for arbitrary input nor a classification outside the stated graph hypotheses is asserted. The collapse procedure is an actual elementary collapse, stronger than the homotopy equivalence it implies.

## Relationship to prior work

Matsushita, *Closed neighborhood complexes of graphs* (arXiv:2511.12608, initially publicly submitted November 16, 2025), introduced and studied the same closed-neighborhood construction; its core general results identify alternative constructions and fundamental groups, rather than this explicit simple-homotopy normal form for triangle-free graphs with four-cycles. Adams, Shukla, and Singh, *Čech complexes of hypercube graphs* (arXiv:2212.05871), identify the scale-two graph Čech complex with this closed-neighborhood complex (Lemma 2.2) and obtain a wedge-of-spheres classification for hypercube graphs (Theorem 4.2). Our theorem specializes to their hypercube result but includes arbitrary admissible graphs and retains the square-filled graph homotopy data even when noncontractible. Their Lemma 2.3 covers the girth-at-least-five regime by a different sufficient condition, where our four-cycle sum is zero. The gluing methods in *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings* (arXiv:1712.06224) apply to certain clique/small-interface gluings; arbitrary rectangular grids with intersecting square boundaries are not consequences of those gluing hypotheses. The finite verification tests are not novelty evidence by themselves.

## Limitations

Graphs containing triangles or a pair of vertices with three common neighbors need not obey the stated collapse sequence or splitting. No claim is made about such graphs, about Čech filtration scales other than two, about torsion or homotopy of the square-filled complex \(X_G\) itself, or about a canonical based wedge decomposition. The finding has received only a same-model scientific review; an independent audit has not been performed. No priority claim beyond the actual literature comparisons is implied.

## References

1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v1 (first public date 2025-11-16), 24 pp., especially definitions, principal theorems and discussion of closed-graph fundamental groups.
2. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, especially Lemmas 2.2, 2.3 and Theorem 4.2.
3. M. Adamaszek et al., *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224, especially the gluing results.
