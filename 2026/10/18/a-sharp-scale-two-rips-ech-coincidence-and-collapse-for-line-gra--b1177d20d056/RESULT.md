# A sharp scale-two Rips–Čech coincidence and collapse for line graphs of high-girth graphs

## Finding

**Theorem (uniform high-girth line-graph stability).** Let \(G\) be any finite connected simple graph with at least one edge, and assume that \(G\) contains no cycles of lengths \(3,4,5,6\). Trees are included. Write \(H=L(G)\) for its line graph, whose vertices are the edges of \(G\), equipped with shortest-path distance. Write \(\operatorname{VR}_{\leq r}(H)\) for the clique complex of vertex pairs at distance at most \(r\). Let \(\mathcal C_2(H)\) be the closed-neighborhood Čech complex whose faces lie in a closed radius-one graph ball centered at some vertex of \(H\). Then

\[
\boxed{\operatorname{VR}_{\leq2}(H)=\mathcal C_2(H)
\searrow\operatorname{VR}_{\leq1}(H)
\simeq G\simeq\bigvee^{|E(G)|-|V(G)|+1}S^1.}
\]

The arrow \(\searrow\) denotes a genuine sequence of elementary simplicial collapses onto the **included** scale-one complex. In particular the inclusion of scale one into scale two induces isomorphisms on all integral homology and all homotopy groups, not merely equality of Betti numbers. No degree or bipartiteness restrictions are imposed.

**Sharpness of the girth hypothesis as a uniform bound.** For \(G=C_6\), the line graph is again \(C_6\), but \(\operatorname{VR}_{\leq2}(L(C_6))\cong\partial\mathcal O_3\simeq S^2\), while \(\operatorname{VR}_{\leq1}(L(C_6))\simeq S^1\). The analogous uniform theorem therefore fails if six-cycles are allowed.

## Assumptions and scope

All graphs are finite, simple, connected, and undirected. A tree has girth infinity. For each vertex \(v\) of \(G\), let \(S_v=\{e\in E(G):v\in e\}\) denote its incident edge set. For an edge \(c=uv\), the closed radius-one neighborhood of the corresponding line-graph vertex is \(B[c]=S_u\cup S_v\). Hence

\[
\mathcal C_2(H)=\bigcup_{uv\in E(G)}\Delta(S_u\cup S_v),\qquad
Y=\operatorname{VR}_{\leq1}(H)=\operatorname{Cl}(H)=\bigcup_{v\in V(G)}\Delta(S_v).
\]

Here \(\Delta(A)\) is the full simplex on the finite set \(A\). The scale parameter \(r\) refers to the integer graph distance **between vertices** in \(H\). The scale-two Čech convention uses closed **graph-radius-one** balls, with centers restricted to vertices; the statement does not invoke arbitrary continuous ball centers. The assertion is an equality of abstract simplicial complexes followed by a simple-homotopy collapse.

## Proof

**1. High-girth ball-Helly lemma for line-graph squares.** We prove that every clique \(\sigma\) in the distance-two graph of \(H\) lies in \(B[c]\) for some edge \(c\) of \(G\). If all graph edges in \(\sigma\) intersect pairwise, the absence of triangles in \(G\) forces them all to share one endpoint: two edges incident at \(v\) and an edge meeting both but not \(v\) would create a triangle. Then \(\sigma\subseteq S_v\subseteq B[c]\) for any \(c\in S_v\); the empty face is automatic.

Otherwise choose two disjoint edges \(a,b\in\sigma\) of \(G\). Their line-graph distance is two, so at least one edge \(c\) connects an endpoint of \(a\) to an endpoint of \(b\). Such a connecting edge is unique: two distinct connectors sharing an endpoint would form a triangle with \(a\) or \(b\); two with distinct endpoints would make a four-cycle. Fix this unique \(c\).

For any other \(f\in\sigma\), choose line-graph walks of length at most two from \(a\) to \(f\) and from \(b\) to \(f\). Regard each visited vertex of these walks as an edge of the original \(G\). Along with \(a,c,b\), the union \(T\) uses at most six edges of \(G\): \(a,b,c,f\) and at most one additional intermediate edge from each of the two selected walks. Its underlying graph is connected (all three selected walks meet through \(a,b,f\)), and it has at most six edges. Therefore it is a **tree**, by the girth-seven hypothesis.

In the metric realization of \(T\) with unit-length edges, denote the midpoint of edge \(d\) by \(m_d\). The selected walks give

\[
 d_T(m_a,m_f)\le2,\qquad d_T(m_b,m_f)\le2,
 \qquad d_T(m_a,m_b)=2,
\]

and \(m_c\) is the midpoint of the unique geodesic segment from \(m_a\) to \(m_b\). Indeed, disjointness of \(a,b\) and their common connector \(c\) give precisely a two-step edge-midpoint path in the tree. A standard metric-tree midpoint argument now gives \(d_T(m_c,m_f)\le1\). Explicitly, let the projection of \(m_f\) to the length-two segment \([m_a,m_b]\) be at coordinate \(s\in[0,2]\), with perpendicular branch distance \(t\ge0\). The two inequalities give \(t+s\le2\) and \(t+2-s\le2\); consequently \(t\le\min(s,2-s)\), so

\[
 d_T(m_c,m_f)=t+|s-1|\le1.
\]

Two distinct edge midpoints at distance at most one in a simplicial tree correspond to incident edges. Thus \(f=c\) or \(f\) meets \(c\). Since \(f\) was arbitrary, \(\sigma\subseteq B[c]\). The reverse implication is immediate because every closed radius-one graph ball has pairwise distances at most two. We have proved the **exact equality**

\[
\operatorname{VR}_{\leq2}(L(G))=\mathcal C_2(L(G)).
\]

**2. Elementary collapse of the Čech complex onto the line-graph clique complex.** This step reproduces, for completeness, the unique-connector collapse already established in the cited preceding Čech result. Let \(K=\mathcal C_2(H)\) and \(Y=\operatorname{Cl}(H)\subseteq K\). Every face \(\sigma\in K\setminus Y\) contains two disjoint original edges \(a,b\), by the triangle-free characterization of \(Y\). Since \(\sigma\) lies in a simplex \(\Delta(B[c])\), such a generator \(c\) must connect \(a,b\). The absence of triangles and four-cycles makes it unique; write \(c(\sigma)\). Adding or deleting \(c(\sigma)\) does not eliminate the two disjoint edges \(a,b\), and cannot change this unique generator.

Pair every \(\sigma\in K\setminus Y\) that omits \(c(\sigma)\) with \(\sigma\cup\{c(\sigma)\}\). This partitions every face outside \(Y\) into pairs. Process lower faces in decreasing order of cardinality. To verify that the current lower face \(\sigma\) is free, consider any remaining coface \(\tau\supsetneq\sigma\). Since \(Y\) is a subcomplex, \(\tau\notin Y\); the same disjoint witnesses force \(c(\tau)=c(\sigma)\). If \(\tau\) omits this generator, it was an earlier (strictly larger) lower face and is already gone. If it includes the generator but is not \(\sigma\cup\{c(\sigma)\}\), its paired lower face \(\tau\setminus\{c(\sigma)\}\) was strictly larger than \(\sigma\), so it and \(\tau\) were removed earlier. Therefore the only remaining coface of \(\sigma\) is its matched upper face. This verifies a literal elementary simplicial collapse for each pair. At the end the remaining complex is exactly \(Y\).

**3. Homotopy type and persistence.** The simplices \(\Delta(S_v)\) cover \(Y\). The intersection for two distinct vertices \(u,v\) is the singleton \(\{uv\}\) exactly when \(uv\in E(G)\), and is empty otherwise; triple intersections are empty. Every nonempty intersection is contractible, and the cover nerve is precisely the original graph \(G\). The simplicial nerve lemma gives \(Y\simeq G\). Connected graph topology gives the displayed wedge of \(\lvert E\rvert-\lvert V\rvert+1\) circles. Since \(Y\hookrightarrow K\) is a collapse inverse, its inclusion induces integral homotopy and homology isomorphisms. These arguments cover trees (the zero-fold wedge is a point) and arbitrary branching.

**4. Six-cycle boundary.** If \(G=C_6\), then \(H=L(G)\cong C_6\). In its graph square, all vertex pairs are adjacent except the three antipodal pairs. The clique complex is exactly the join of three two-point sets, namely \(S^0*S^0*S^0\cong\partial\mathcal O_3\simeq S^2\), while \(\operatorname{Cl}(C_6)\cong S^1\). Therefore the claimed scale-one-to-two homotopy preservation fails at girth six, showing that seven is the best possible universal girth threshold.

## Verification

The included standalone `verify.py` uses only the Python standard library. It independently builds line-graph distance-two cliques by exhaustive pairwise adjacency tests, builds the Čech complex from incident-edge balls, and tests **literal equality of their face sets**. It then identifies each outside face's unique Čech generator, builds the complete toggling matching, and executes every ordered elementary collapse after explicitly checking the surviving immediate cofaces of every lower face. It verifies that the remainder equals the scale-one flag complex and that its Euler characteristic equals \(\lvert V(G)\rvert-\lvert E(G)\rvert\). This was done for all labeled trees on two through six vertices (1,441 Prüfer-sequence instances), paths, stars, seven- through twelve-cycles, two multicircuit theta graphs and a two-seven-cycle barbell: 1,467 graph instances overall. A separate direct check shows that for the six-cycle exactly two additional triangular Rips faces are not contained in the radius-one Čech complex and the Rips face vector is \((6,12,8)\).

The script is finite corroboration, **not** the logical justification for the infinite theorem; the arguments in Proof, particularly the six-edge girth argument, establish the general result. The exact program and observed output are embedded in this package and can be run using `python verify.py`.

## Relationship to prior work

Matsushita's 2025 manuscript on closed-neighborhood complexes [1, Definition 1.1 and Theorem 1.5] supplies the general closed-neighborhood framework and studies associated fundamental groups. Its inspected statements neither equate all scale-two Rips faces with closed-neighborhood faces for line graphs of high-girth graphs nor assert the claimed Rips inclusion collapse.

Goyal, Shukla and Singh [2, Corollary 3.4] already prove that the **scale-one** line-graph clique complex has the homotopy type of the original triangle-free graph. This is taken as established and not claimed as original.

A closely related previously indexed finding [4] proves the Čech scale-two collapse for line graphs of graphs of girth at least five. Its complete proof was compared. **That Čech theorem is prior coverage for Step 2, not the new finding:** the nontrivial step proved here is equality of the larger Rips complex with Čech under a sharp girth-seven condition. At girth six the two complexes are provably unequal, so that equality cannot be inferred from the existing Čech collapse merely by substituting terminology. Previously indexed high-girth Rips results for a graph itself cannot be applied directly to a branching line graph, which has many triangles.

The new claimed increment is the high-girth **Rips–Čech coincidence** and hence actual stability of the scale-one-to-two Rips inclusion for arbitrarily branching original graphs, together with its sharp failure at six. No unqualified claim of global bibliographic uniqueness is made.

## Limitations

The uniform statement assumes girth at least seven. It does not classify the scale-two Rips complexes of graphs with shorter cycles, nor give a full filtration at scales larger than two. It concerns the graph metric on the **vertices of the line graph**, not metric points throughout the original geometric graph; using continuous Čech centers is a different convention. The Čech-collapse component and scale-one homotopy type are explicitly prior results; originality concerns the new Rips–Čech identity and its consequence. The literature search and indexed-database comparison are not exhaustive guarantees against unindexed or unpublished equivalent structural statements. The computational verification is limited to finitely many graphs.

## References

[1] T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first publicly posted 2025-11-16; Definition 1.1 and Theorems 1.2, 1.5. https://arxiv.org/html/2511.12608v2

[2] S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first publicly posted 2020-09-25; particularly Corollary 3.4. https://arxiv.org/abs/2009.12130

[3] H. Adams, S. Shukla and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first publicly posted 2022-12-12; graph-radius Čech conventions and Lemma 2.2. https://arxiv.org/abs/2212.05871

[4] *A scale-two Čech collapse theorem for line graphs of girth at least five*, published 2026-10-11, source identifier `2026/10/11/SCOPE-a-scale-two-ech-collapse-theorem-for-line-graphs-of-girth-at-lea--69ae03a7604c`. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-scale-two-ech-collapse-theorem-for-line-graphs-of-girth-at-lea--69ae03a7604c
