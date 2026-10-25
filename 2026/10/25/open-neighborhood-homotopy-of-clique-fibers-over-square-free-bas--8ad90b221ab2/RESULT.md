# Open-neighborhood homotopy of clique fibers over square-free base graphs

## Finding
Let \(H\) be a finite connected simple graph on \(n\geq2\) vertices and \(e\geq1\) edges, containing no four-cycle (not necessarily induced). For every integer \(m\geq4\), the Lovász open-neighborhood complex of the Cartesian graph product \(G=H\square K_m\) has integral homotopy type
\[
\mathcal N(G)\simeq\bigvee^{e-n+1}S^1\ \vee\ \bigvee^{n}S^{m-2}\ \vee\ \bigvee^{e(m^2-3m+1)}S^2.
\]
Coincident sphere degrees are counted with multiplicity; for \(m=4\) there are \(n+5e\) two-sphere summands. In particular, its fundamental group is free of rank \(e-n+1\), and every integral homology group is torsion-free. This covers branching trees, triangular bases, and bases with several independent cycles, not just a single base edge or cycle.

## Assumptions and scope
For a simple graph \(G\), define its *open-neighborhood complex* \(\mathcal N(G)\) to have nonempty simplices \(\sigma\subseteq V(G)\) whenever some vertex is adjacent to all vertices of \(\sigma\). The center is not in its own neighborhood. Write \(V(G)=\{(v,i):v\in V(H),\ i\in\{1,\dots,m\}\}\), and let \(R_v=\{(v,i):1\le i\le m\}\) be a clique fiber. Two distinct product vertices are adjacent if they are in the same fiber with different color, or have the same color and adjacent base vertices. The *four-cycle-free* requirement is equivalent to requiring any pair of distinct base vertices to have at most one common neighbor; triangles are allowed. The theorem concerns the ordinary open-neighborhood complex, not the closed-neighborhood or Čech nerve and not a Vietoris–Rips complex.

## Proof
**1. Neighborhood generators.** For each base vertex \(v\) and color \(i\), the neighborhood simplex centered at \((v,i)\) has vertex set
\[
F_{v,i}\sqcup W_{v,i},\qquad F_{v,i}=R_v\setminus\{(v,i)\},\qquad W_{v,i}=\{(w,i):vw\in E(H)\}.
\]
Every simplex in \(\mathcal N(G)\) is a face of one of these \(nm\) simplices. A pair of distinct vertices of \(W_{v,i}\) can occur together in no other neighborhood generator: any second center would supply a second common base neighbor and thus a four-cycle. Color constraints rule out generators centered at a different color. This uniqueness also holds when \(H\) has triangles.

**2. A complete elementary collapse.** Fix a pivot \(p_{v,i}\in F_{v,i}\) for every center. For each subset \(T\subseteq W_{v,i}\) of size at least two and every \(A\subseteq F_{v,i}\setminus\{p_{v,i}\}\), pair the face \(T\cup A\) with \(T\cup A\cup\{p_{v,i}\}\). Process pairs in decreasing cardinality of their lower face, in any fixed order among equal sizes. The uniqueness from Step 1 guarantees that, when processing a lower face, every other codimension-one coface within its unique generator has already been removed. Its unique remaining coface is the displayed upper face; the pair is therefore a genuine elementary free-face collapse. No two centers share one of these pairs. Exactly
\[
m\,2^{m-2}\sum_{v\in V(H)}\bigl(2^{\deg_H(v)}-\deg_H(v)-1\bigr)
\]
elementary pairs are removed. The remaining complex \(L\) consists precisely of faces that meet at most one neighboring fiber outside their center fiber. More explicitly, for each edge \(uv\in E(H)\), define
\[
P_{uv}=A_{u,uv}\cup A_{v,uv},\quad A_{u,uv}=\bigcup_{i=1}^m\Delta\bigl((R_u\setminus\{(u,i)\})\cup\{(v,i)\}\bigr),
\]
with \(A_{v,uv}\) defined symmetrically. Then \(L=\bigcup_{uv\in E(H)}P_{uv}\).

**3. The edge-block intersection.** Let \(S_v=\partial\Delta(R_v)\cong S^{m-2}\). Within \(A_{u,uv}\), each \((v,i)\) is the apex of exactly one simplex attached along its full base face in \(S_u\); removing these attached simplices by elementary collapses retracts \(A_{u,uv}\) onto \(S_u\), with \(S_u\) fixed. The same holds at \(v\). Their intersection \(J_{uv}=A_{u,uv}\cap A_{v,uv}\) is exactly the crown graph \(K_{m,m}\) with the \(m\) equal-color edges deleted: its cross edges are \(\{(u,i),(v,j)\}\) for \(i\ne j\). It is connected for \(m\geq3\) and has
\[
\beta_1(J_{uv})=m(m-1)-2m+1=m^2-3m+1=:q_m.
\]
Consequently \(J_{uv}\simeq\bigvee^{q_m}S^1\).

**4. Glue all blocks simultaneously.** Two distinct edge blocks intersect only when their base edges meet, and their intersection is exactly the common fiber-boundary sphere \(S_v\); disjoint edge blocks do not meet. Any three or more blocks have common intersection only when every base edge is incident to the same vertex, and this intersection is \(S_v\). These are gluings of simplicial subcomplexes and hence of cofibrations. Their global union is modeled by the homotopy colimit of a graph-of-spaces diagram with vertex spaces \(S_v\), two half-blocks over every base edge, and interface space \(J_{uv}\) over that edge. Replace each half-block by its deformation retract \(S_u\) or \(S_v\). The two maps from \(J_{uv}\) to the neighboring spheres are null-homotopic, since \(J_{uv}\) is a connected graph and \(S_u,S_v\) are simply connected when \(m\geq4\). Diagramwise homotopy invariance permits replacing all these maps by constant maps, independently for each base edge.

The homotopy pushout for one edge is two vertex spaces joined by an interval, together with \(\Sigma J_{uv}\simeq\bigvee^{q_m}S^2\). Performing this replacement at every base edge gives a connected graph of intervals homeomorphic to the base graph \(H\), one attached fiber sphere \(S_v\) for each vertex, and \(q_m\) two-spheres for each edge. Contracting a spanning tree of the interval graph produces \(e-n+1\) circles, while preserving all attached spheres. The stated wedge decomposition follows. The integral homology and fundamental group conclusions are immediate. The proof applies to every finite graph and clique width in the hypotheses, without extrapolation from finite computation.

## Verification
Run `python3 verify_clique_squarefree_open.py` with Python 3's standard library in the directory containing this document. It independently constructs the full open-neighborhood face set from graph adjacency, verifies every proposed elementary free-face collapse, compares the remaining face set with the exact edge-block union, and calculates reduced simplicial homology over \(\mathbf F_2\) by independent exact boundary-matrix ranks. It passes 14 cases: clique widths \(4\) and \(5\) over an edge, a path, a three-leaf star, a branched tree, a triangle, a five-cycle, and a multi-cycle theta graph. All fourteen tests conclude successfully with `VERIFY_OK`. These finite checks corroborate but do not establish the uniform homotopy theorem, which rests on Steps 1–4. The four-cycle-free condition is a structural uniqueness requirement, not an assertion about all graphs containing four-cycles.

## Relationship to prior work
Shukla [1] classifies open-neighborhood homotopy types for bounded-degree graphs and certain four-regular circulants; these families do not imply the present unbounded-clique-width and arbitrary-base theorem. A published classification [2] gives exactly the specialization to a single base edge (a clique prism); another published classification [3] gives the specialization to a single base cycle of length at least five. The present claim strictly covers branching and multi-cycle bases, including triangle-containing bases, by an additional global graph-of-spaces assembly. A closely related published result [4] treats the *closed-neighborhood/Čech* nerve of clique fibers over girth-five bases, which is not the same object: it has \(e(m-1)^2\) two-spheres rather than the present high-dimensional fiber spheres and \(eq_m\) two-spheres. For example, the open complex of \(K_4\square K_2\) has seven two-spheres, whereas the corresponding scale-two closed-neighborhood complex has nine. The compared published results do not assert the present square-free-base open-neighborhood formula; unindexed or differently formulated prior results remain possible.

## Limitations
The result is nonequivariant and does not determine canonical maps, graph automorphism representations, or persistence filtrations. It does not cover \(m\le3\), disconnected base graphs, or base graphs having a four-cycle; no extrapolation past those boundaries is asserted. The graph-of-spaces reduction is a homotopy equivalence, not necessarily a simplicial collapse all the way to a wedge. The computational checker is finite, whereas the proof is uniform. No independent audit has been performed; neither literature retrieval nor this review certifies universal novelty.

## References
[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1, first public 2018-02-13. https://arxiv.org/abs/1802.04526

[2] *Open-neighborhood complexes of clique prisms: a mixed-dimensional sphere decomposition*, public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-open-neighborhood-complexes-of-clique-prisms-a-mixed-dimensional--d1fca5b06808

[3] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-homotopy-of-complete-graph-cycle--3a53c8927b3c

[4] *Clique-fiber Čech nerves over graphs of girth at least five*, public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-clique-fiber-ech-nerves-over-graphs-of-girth-at-least-five--bcf5b8b96c75

[5] H. Adams, S. Shukla, and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871v1, first public 2022-12-12. https://arxiv.org/abs/2212.05871
