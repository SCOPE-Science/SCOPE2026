# Mixed-dimensional sphere wedges for bidirected friendship multipath complexes

## Finding

For an integer \(n\geq 2\), let \(F_n\) be the **friendship graph** formed by identifying one vertex of each of \(n\) otherwise disjoint triangles. Replace each edge by both directed arcs, obtaining \(\overleftrightarrow{F_n}\). Let \(X_n\) be its multipath complex (equivalently, its directed linear-forest complex). Then there is an integral homotopy equivalence

\[
\boxed{X_n\simeq S^{n-1}\vee\bigvee^{2n}S^n.}
\]

In particular, its only nonzero reduced integral homology groups are \(\widetilde H_{n-1}(X_n;\mathbb Z)\cong\mathbb Z\) and \(\widetilde H_n(X_n;\mathbb Z)\cong\mathbb Z^{2n}\). The \(2n\) top-dimensional classes have explicit representatives, one for each choice of a petal and a cyclic direction. The boundary case \(n=1\) is different: \(X_1\cong S^1\sqcup S^1\).

## Assumptions and scope

The underlying undirected graph has vertex set \(\{c,a_1,b_1,\ldots,a_n,b_n\}\) and edge set \(\{\{c,a_i\},\{c,b_i\},\{a_i,b_i\}:1\leq i\leq n\}\). Every edge appears in both directions. A simplex of \(X_n\) is a set of directed arcs whose selected subdigraph is a vertex-disjoint union of directed simple paths and isolated vertices. Equivalently, selected in- and outdegrees are at most one and there are no directed cycles, including directed two-cycles. We allow the empty face and work with the ordinary geometric realization of the nonempty face poset. The theorem is about **homotopy type over the integers**, not merely rational or mod-two homology.

For petal \(i\), abbreviate its external arcs by \(p_i=(a_i,b_i)\) and \(q_i=(b_i,a_i)\). Write its four arcs incident to \(c\) as \(r_i=(c,a_i)\), \(s_i=(c,b_i)\), \(u_i=(a_i,c)\), and \(v_i=(b_i,c)\). The integer \(n\) is not bounded above.

## Proof

**1. Exact central-arc fibers.** For a simplex \(\sigma\), let \(C(\sigma)\) be the set of its selected central arcs, namely the arcs incident to \(c\). Since a directed multipath has in- and outdegree at most one at every vertex, \(C(\sigma)\) is either empty, a singleton, or a pair consisting of one incoming and one outgoing arc with distinct outer endpoints. There are no larger possibilities.

The choices of external arcs conditional on \(C(\sigma)\) are exact:

* With no central arc, every petal independently permits none, \(p_i\), or \(q_i\), but not both. The fiber is the face poset of the join \(B_n=\mathop{\ast}_{i=1}^n\{p_i,q_i\}\cong S^{n-1}\), with the empty face deleted.
* With exactly one central arc, precisely one of \(p_i,q_i\) on its petal remains available: for \(r_i,v_i\) it is \(p_i\), while for \(s_i,u_i\) it is \(q_i\). All remaining petals independently give two-point choices. Thus the fiber of external choices is a cone.
* With two central arcs on different petals, each of those two petals has precisely one compatible external arc, and all other petals again supply two-point choices. Their external-choice fiber is a cone.
* With two central arcs on the **same** petal, they must be \(\{r_i,v_i\}\) or \(\{s_i,u_i\}\). In either case neither external arc on that petal can be chosen: one alternative violates an in/outdegree condition and the other completes a directed triangle. The external-choice fiber is \(\mathop{\ast}_{j\ne i}\{p_j,q_j\}\cong S^{n-2}\), including its empty face.

No further obstruction exists. A directed cycle using central arcs must lie entirely in one triangular petal; when the two central arcs lie in distinct petals, their optional external arcs instead lengthen an open directed path. In each petal, selecting both external orientations is prohibited as a directed two-cycle.

**2. Uniform discrete-Morse matching.** Map the nonempty face poset \(P(X_n)\) order-preservingly to the poset of central-arc subsets via \(\sigma\mapsto C(\sigma)\). In any fiber that is a cone, match each external subset to the subset obtained by toggling a fixed allowed external arc on a central-arc petal. This pairs the entire fiber, including the empty external subset.

For the fiber of an empty central set, and for each fiber corresponding to a same-petal central pair, apply the following standard lexicographic matching to the free petals in increasing order. Find the first free petal \(j\) for which \(q_j\) is **absent**, and toggle \(p_j\). If no such petal exists, leave the face unmatched. In the empty-central fiber, the exceptional toggle between the empty global face and \(\{p_1\}\) is not a legal face-poset pair, so \(\{p_1\}\) is also unmatched.

This is an acyclic matching. Indeed, along the directed Hasse diagram (matched covers reversed), any unmatched downward cover can only decrease the central-arc subset and every matched cover preserves it. Thus a directed cycle would lie in one fiber. In a cone fiber, the toggle arc is added only along matched upward steps and never removed along unmatched downward steps; a cycle is impossible. In a two-point-join fiber, the smallest index for which \(q_j\) is absent cannot increase along a directed path. If it remains fixed, \(p_j\) is likewise added only along matched steps and never removed along unmatched steps. The other directed steps strictly decrease face size, so again there is no cycle. The same argument handles the exceptional unmatched singleton in the empty-central fiber.

For \(n\geq2\), precisely the following critical simplices remain: one vertex \(\{p_1\}\); the \((n-1)\)-simplex \(\{q_1,\ldots,q_n\}\); and, for each \(i\), the two \(n\)-simplices

\[
\{r_i,v_i\}\cup\{q_j:j\ne i\},\qquad
\{s_i,u_i\}\cup\{q_j:j\ne i\}.
\]

Forman's discrete Morse theorem therefore gives a CW model with **one zero-cell, one \((n-1)\)-cell, and exactly \(2n\) \(n\)-cells**, with no others. In particular the rank of degree-\(n\) integral homology cannot exceed \(2n\).

**3. Integral top cycles and their independence.** In petal \(i\), the three arcs \(r_i,p_i,v_i\) form a directed triangle, and every proper two-arc subset is an admissible directed path. Their three two-element faces consequently form a simplicial circle \(T_i^+\), represented by the oriented cycle \(\partial[r_i,p_i,v_i]\), where the bracket is a *formal* forbidden two-simplex. Similarly \(\partial[s_i,q_i,u_i]\) defines a circle \(T_i^-\). For each other petal \(j\), the reduced zero-cycle \([p_j]-[q_j]\) represents \(S^0\). Their oriented simplicial joins

\[
Z_i^\pm=T_i^\pm*\mathop{\ast}_{j\ne i}([p_j]-[q_j])
\]

are integral \(n\)-cycles. The join is a subcomplex because all other petals are disjoint away from \(c\).

For each \((i,\pm)\), the coefficient of its distinguished critical \(n\)-simplex from Step 2 in \(Z_i^\pm\) is \(\pm1\). It is zero for every \(Z_{k}^\delta\) with \((k,\delta)\ne(i,\pm)\). Moreover, no distinguished critical \(n\)-simplex has an \((n+1)\)-dimensional coface: its central pair saturates both in- and outdegree at \(c\), its own petal admits no external arc, and the other \(n-1\) petals already each contribute one external arc. Coefficients at these facets therefore vanish on every integral boundary from dimension \(n+1\). Taking these \(2n\) coefficient functionals shows that \([Z_i^\pm]\) are \(2n\) linearly independent integral homology classes.

The Morse model has exactly \(2n\) cells in degree \(n\), so these cycles force its entire cellular differential from degree \(n\) to degree \(n-1\) to vanish over \(\mathbb Z\). Thus its \((n-1)\)-cell first forms \(S^{n-1}\), and each \(n\)-cell has attaching map of degree zero into this sphere. Since \(\pi_{n-1}(S^{n-1})\cong\mathbb Z\) for every \(n\geq2\), all these maps are nullhomotopic. This proves the announced integral wedge decomposition.

For \(n=1\), the six arc vertices split into two disjoint three-edge polygonal components of the multipath complex, one for each cyclic orientation of the triangle. Each component is a circle, proving the exceptional statement.

## Verification

Two independent Python 3 scripts are supplied. `verify.py` enumerates admissible faces using central/external choices, executes the actual lexicographic matching, checks its involution and dimensions, orients **every** face-poset Hasse cover, and topologically sorts the resulting digraph to confirm acyclicity for \(1\le n\le6\). The \(n=6\) check covers 54,188 nonempty faces, 27,087 matching pairs, and 295,128 Hasse covers. It also checks the distinguished critical facets have no larger cofaces.

`homology_check.py` independently enumerates faces by increasing arc subsets, computes exact mod-two boundary ranks by sparse bitset elimination, and confirms the predicted Betti numbers for \(1\le n\le5\). Both programs use only the Python standard library; run `python3 verify.py` and `python3 homology_check.py` in the extracted artifact directory. Their recorded outputs are included. These finite checks supplement, and do not replace, the all-parameter proof above.

## Relationship to prior work

Caputi, Collari and Smith (2026, arXiv:2601.05670) analyze bidirected paths and **single** polygons, including their connectivity and homology; the \(n=1\) boundary case is part of that setting. A flower with \(n\ge2\) triangles glued at one vertex is neither a path nor a single polygon. Their homology calculation for polygons does not imply the present mixed-dimensional integral homotopy classification.

Deshpande and Sawant (2026, arXiv:2602.14936) introduce conflict graphs and hypergraphs for directed linear-forest complexes, prove structural vertex-decomposability results under cycle conditions, and explicitly raise broader homotopy classification as a problem. The bidirected friendship graph has genuine directed triangles, so its no-long-cycle reduction is not applicable; their results do not state this homotopy type.

Caputi, Collari, Di Trani and Smith (2022, arXiv:2208.04656) prove a dynamical-module decomposition and compute other graph families. Here all triangle petals interact through the common vertex and the corresponding decomposition is not a join of individual triangle multipath complexes. Their results do not supply the two adjacent-dimensional cell counts or attaching maps above. A separately published homotopy classification for bidirected double-star **trees**, and published matching-complex results for undirected Dutch windmills, concern different digraphs or different simplicial complexes; neither implies this theorem.

## Limitations

The explicit classification is restricted to the bouquet of bidirected **triangles** with one common vertex; it does not classify longer petal cycles, arbitrary cactus graphs, or general directed graph complexes. The disconnected \(n=1\) case must not be substituted into the connected wedge formula. The finite checks do not certify infinitely many sizes; that scope is covered by the acyclic-matching construction and the top-cycle argument. Searches cannot rule out all unindexed or unpublished equivalent classifications.

## References

1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first posted 2026-01-09; https://arxiv.org/abs/2601.05670.
2. P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936, first posted 2026-02-16; https://arxiv.org/html/2602.14936v1.
3. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first posted 2022-08-09; https://arxiv.org/html/2208.04656v1.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
