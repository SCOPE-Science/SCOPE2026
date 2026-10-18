# Mixed-dimensional sphere wedges for alternating-spoke directed wheels

## Finding
For every integer \(m\ge2\), construct the alternately oriented directed wheel \(D_{2m}\) below. Its multipath complex satisfies
\[
X(D_{2m})\simeq S^{2m-2}\vee\bigvee^{m}S^{2m-1}.
\]
In particular, its reduced integral homology is \(\mathbb Z\) in degree \(2m-2\), \(\mathbb Z^m\) in degree \(2m-1\), and zero in every other degree. This is a homotopy equivalence, not only a calculation of Betti numbers.

## Assumptions and scope
Let \(n=2m\ge4\). Take outer vertices \(v_i\) indexed by \(i\in\mathbb Z/n\mathbb Z\), a central hub \(h\), and exactly the following \(2n\) arcs:
\[
e_i=(v_i,v_{i+1})\quad(0\le i<n),\qquad
 a_i=(v_i,h)\quad(i\text{ even}),\qquad
 b_j=(h,v_j)\quad(j\text{ odd}).
\]
The multipath complex \(X(D_n)\) has these arcs as its vertices. Its faces are the arc sets whose connected directed components are vertex-disjoint simple directed paths or isolated vertices. Equivalently, selected arcs give at most one outgoing and at most one incoming arc at each graph vertex and have no directed cycle. This is the ordinary arc-set complex, not directed path homology. The theorem concerns even outer-cycle length only; no assertion is made for other orientations.

For a finite arc set \(T\), let \(\Delta(T)\) denote the full simplex on \(T\), and \(\partial\Delta(T)\) its boundary complex. The join of simplicial complexes is denoted \(*\).

## Proof
**1. Rim and one-spoke layers.** Write \(E=\{e_0,\ldots,e_{n-1}\}\). Rim-only multipaths are exactly proper subsets of \(E\), so their complex is
\[
R=\partial\Delta(E)\cong S^{n-2}.
\]
There can be at most one selected spoke ending at the hub, and at most one starting there. For an even \(i\), a face containing \(a_i\) but no other spoke cannot contain \(e_i\) (two outgoing arcs at \(v_i\)); every subset of \(E\setminus\{e_i\}\) is otherwise allowed. For odd \(j\), a face containing only \(b_j\) cannot contain \(e_{j-1}\) (two incoming arcs at \(v_j\)), with no other rim restriction. Thus the at-most-one-spoke subcomplex is
\[
A=R\ \cup\ \bigcup_{i\text{ even}}\bigl(\Delta(a_i)*\Delta(E\setminus\{e_i\})\bigr)
\ \cup\ \bigcup_{j\text{ odd}}\bigl(\Delta(b_j)*\Delta(E\setminus\{e_{j-1}\})\bigr).
\]
Each added simplex meets the preceding union exactly along the facet it cones over, because no other previously added face contains its unique spoke. It therefore simplicially collapses onto that facet. Collapsing all one-spoke pieces gives \(A\simeq R\), fixing \(R\).

**2. Two-spoke links.** Every remaining face has exactly two spokes \(a_i,b_j\), where \(i\) is even and \(j\) is odd. Its allowed rim sets form a subcomplex \(F_{ij}\). Exclude \(e_i\) and \(e_{j-1}\) for the degree constraints, and let \(P_{ji}\subseteq E\) be the directed forward rim path from \(v_j\) to \(v_i\), of length \(\ell=(i-j)\bmod n\). The only additional forbidden directed cycle uses both spokes and all of \(P_{ji}\), so
\[
F_{ij}=\{T\subseteq E\setminus\{e_i,e_{j-1}\}:P_{ji}\not\subseteq T\}.
\]
The only possible cycles are the whole rim cycle (already prevented by the excluded rim arcs) and the cycle passing through the hub. The path length \(\ell\) is odd since \(i\) and \(j\) have opposite parity.

If \(j=i+1\pmod n\), the two forbidden rim arcs coincide, and \(P_{ji}=E\setminus\{e_i\}\). Hence
\[
F_{i,i+1}=\partial\Delta(E\setminus\{e_i\})\cong S^{n-3}.
\]
There are exactly \(m\) such adjacent spoke pairs.

If \(j\ne i+1\pmod n\), the two excluded rim arcs are distinct, and \(1\le\ell\le n-3\). The path \(P_{ji}\) avoids both excluded arcs. Let \(Q=E\setminus(\{e_i,e_{j-1}\}\cup P_{ji})\); then \(|Q|=n-2-\ell\ge1\) and
\[
F_{ij}=\partial\Delta(P_{ji})*\Delta(Q).
\]
This complex is a cone, because \(Q\ne\varnothing\). When \(|P_{ji}|=1\), \(\partial\Delta(P_{ji})\) is the complex consisting only of the empty face, and the same formula remains valid.

**3. Attaching each spoke pair.** The new faces associated with the pair \(a_i,b_j\) form the simplicial subcomplex
\[
B_{ij}=\Delta(\{a_i,b_j\})*F_{ij}.
\]
The intersection of \(B_{ij}\) with \(A\), or with any union of other pair blocks and \(A\), is exactly
\[
L_{ij}=\partial\Delta(\{a_i,b_j\})*F_{ij},
\]
since a face containing both spokes uniquely specifies its pair. For nonadjacent pairs \(F_{ij}\) is a nonempty cone; both \(L_{ij}\) and \(B_{ij}\) are then contractible, so their inclusion is a homotopy equivalence of simplicial CW complexes. Attaching these blocks along their subcomplexes does not change homotopy type. After all nonadjacent pairs are handled, the remaining base is homotopy equivalent to \(R\).

For an adjacent pair, \(F_{i,i+1}\cong S^{n-3}\). Its block is a PL \((n-1)\)-ball, with boundary \(L_{i,i+1}\cong S^{n-2}\). Hence each of the \(m\) adjacent pairs attaches one \((n-1)\)-cell to the base \(A\), up to the homotopy equivalences just described.

**4. The attaching maps have degree zero.** Fix the odd rim arc \(e_1\). Define a map on the vertices of \(X(D_n)\) that fixes every rim-arc vertex and sends *every spoke-arc vertex* to \(e_1\). Any face with at least one spoke omits at least one even-indexed rim arc, whereas \(e_1\) has odd index; its image is therefore a proper rim-arc subset. Faces without spokes are already proper subsets of \(E\). This defines a simplicial retraction
\[
r:X(D_n)\longrightarrow R
\]
fixing \(R\) pointwise. In particular, the restriction \(r|_A:A\to R\) is a homotopy inverse to the inclusion \(R\hookrightarrow A\), because \(A\) collapses onto \(R\).

The attaching map \(L_{i,i+1}\to A\) of each adjacent block becomes null-homotopic after composing with \(r|_A\), since the composite extends across the whole ball \(B_{i,i+1}\) via the simplicial map \(r\). Because \(r|_A\) is a homotopy equivalence, that attaching map is itself null-homotopic. The already attached nonadjacent blocks are homotopically removable relative to \(A\), and the distinct adjacent blocks meet only inside \(A\); thus the \(m\) null-attached \((n-1)\)-cells add a wedge of \(m\) spheres. Consequently
\[
X(D_n)\simeq R\vee\bigvee^m S^{n-1}\simeq S^{n-2}\vee\bigvee^m S^{n-1}.
\]
This completes the integral, all-parameter proof.

## Verification
The included standalone program `verify_wheel.py` generates every arc subset for \(n=4,6,8,10\), checks directed indegree/outdegree and all directed cycles, verifies the proposed one- and two-spoke links face by face, verifies the simplicial rim retraction, and computes mod-two homology by exact boundary reduction. The observed face counts (excluding the empty face) are respectively \(64,413,2386,12967\); the nonzero positive-degree mod-two Betti numbers are respectively \((1,2)\) in degrees \((2,3)\), \((1,3)\) in \((4,5)\), \((1,4)\) in \((6,7)\), and \((1,5)\) in \((8,9)\). These checks test the definitions and link decomposition. They are finite corroborations and do not substitute for the preceding proof for arbitrary \(m\).

## Relationship to prior work
Caputi, Collari, Di Trani, and Smith (2022 preprint, 2024 journal version) introduce multipath complexes and classify several families including directed polygons, lines, small grids, and transitive tournaments. Their dynamical-module theorem gives general join decompositions. The present wheels have a hub and are not polygons or the other enumerated families. All rim arcs belong to the coherent rim cycle, and every spoke lies on a hub-and-rim directed cycle, so no proper edge-containing dynamical region can isolate part of the graph under their cycle-containment condition. Thus that theorem does not itself compute this family. The 2022 work on path posets studies realization of mixed-dimensional sphere wedges, but it does not give this wheel classification. The 2026 study of *bidirectional polygonal digraphs* has both orientations on each rim edge and no hub; its homology computation concerns a different directed graph family.

## Limitations
The theorem covers exactly the stated even-wheel orientation, not arbitrary wheel orientations or bidirected wheels. The statement is an integral homotopy classification; the finite program computes homology only over \(\mathbb F_2\) and does not independently verify arbitrary-parameter homotopy. The comparison with indexed work and inspected primary texts is not a proof of absolute novelty; unindexed equivalent work or changes in the final journal version remain possible. No publication priority or external mathematical validation is claimed.

## References
1. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first posted 2022-08-09), §§2, 4, 5. https://arxiv.org/pdf/2208.04656
2. L. Caputi, C. Collari, and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, Journal of Algebraic Combinatorics (2022 online), §§1, 6, DOI:10.1007/s10801-022-01180-9. https://link.springer.com/article/10.1007/s10801-022-01180-9
3. L. Caputi, C. Collari, and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (2026), §2. https://arxiv.org/pdf/2601.05670
