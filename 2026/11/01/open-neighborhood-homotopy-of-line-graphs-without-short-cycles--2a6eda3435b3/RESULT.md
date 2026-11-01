# Open-neighborhood homotopy of line graphs without short cycles

## Finding
Let \(G\) be any finite connected simple graph of girth at least five and minimum vertex degree at least three. Write \(n=|V(G)|\), \(m=|E(G)|\), and \(b=m-n+1\). Let \(L(G)\) be its line graph, and let \(\mathcal N(L(G))\) be the **open** Lovász neighborhood complex: its simplices are the collections of edges of \(G\) all adjacent, as vertices of \(L(G)\), to some other edge of \(G\). (An edge is not adjacent to itself.) Then, with all multiplicities included,
\[
\boxed{\mathcal N(L(G))\simeq\bigvee^{m+b}S^1\ \vee\ \bigvee_{v\in V(G)}S^{\deg_G(v)-2}.}
\]
In particular all integral homology is torsion-free. A degree-three vertex contributes an additional circle; for any \(k\ge2\), the reduced integral \(k\)-homology has one canonical local generator for every vertex of degree \(k+2\):
\[
\widetilde H_k(\mathcal N(L(G));\mathbb Z)\cong\bigoplus_{\substack{v\in V(G)\\\deg_G(v)=k+2}}\mathbb Z.
\]
This isomorphism is natural under graph automorphisms when the summands are regarded as **orientation lines** of the incidence-edge sets: an automorphism sends the generator of the oriented boundary on the edges incident to \(v\) to the corresponding generator at its image, times the sign of the induced ordering permutation. We do not assert a canonical decomposition of the full first-homology representation.

As an incidence-geometric consequence, for the Levi graph \(G_\Pi\) of *any* finite projective plane \(\Pi\) of order \(q\ge2\), set \(s=q^2+q+1\). Then
\[
\mathcal N(L(G_\Pi))\simeq \bigvee^{2qs+1}S^1\ \vee\ \bigvee^{2s}S^{q-1}.
\]
For order \(q=3\), this is \(\bigvee^{79}S^1\vee\bigvee^{26}S^2\). For \(q=2\), the two circle contributions combine to \(\bigvee^{43}S^1\).

## Assumptions and scope
All graphs are finite, loopless, undirected and simple. Girth at least five means that neither triangles nor quadrilaterals exist, even as non-induced subgraphs. No regularity, bipartiteness, or absence of bridges is assumed. Minimum degree three ensures each vertex-star boundary is connected and every open-neighborhood attachment has two nonempty, distinct ends. The wedge is an ordinary nonequivariant homotopy equivalence; the higher-homology signed-permutation description is an additional canonical statement, not an equivariant wedge splitting. A zero-fold wedge has its usual basepoint interpretation.

For \(v\in V(G)\), let \(S_v=\{e\in E(G):v\in e\}\). For a set \(T\) of edges, write \(\Delta(T)\) for the simplex on those edge-vertices. The line graph has vertex set \(E(G)\); its open neighborhood at \(e=uv\) is \((S_u\cup S_v)\setminus\{e\}\).

## Proof
**Step 1: A canonical subcomplex consisting of local spheres.** For each original vertex \(v\), put \(A_v=\partial\Delta(S_v)\), the full proper-face boundary of the \((\deg(v)-1)\)-simplex. Every proper subset \(F\subsetneq S_v\) has a common open line-graph neighbor: choose an edge \(e\in S_v\setminus F\), which is adjacent to every edge of \(F\). The whole \(S_v\) is not a face of \(\mathcal N(L(G))\): a candidate witnessing edge incident to \(v\) would itself lie in \(S_v\) and fail self-adjacency, while an edge outside \(S_v\) has only two endpoints and can meet at most two distinct edges incident to \(v\). Thus \(A_v\cong S^{\deg(v)-2}\) is embedded as the induced local boundary.

Let \(A=\bigcup_v A_v\). For two different vertices \(u,v\), the sets \(S_u,S_v\) intersect in precisely the single edge \(uv\) if it exists, and otherwise not at all. Consequently \(A_u\cap A_v\) is exactly that one vertex (when \(uv\in E(G)\)); triple intersections are empty. Each \(A_v\) is path-connected because \(\deg(v)\ge3\). A connected graph-of-spaces made from connected spheres identified only at distinct marked points, with underlying incidence graph the barycentric subdivision of \(G\), has the homotopy type of the wedge of its vertex spheres and the underlying graph. This follows by choosing a spanning tree among the point-identification edges, collapsing its contractible connecting spine and retaining one extra loop per graph edge outside the tree. Therefore
\[
A\simeq\left(\bigvee^b S^1\right)\vee\bigvee_{v\in V(G)}S^{\deg(v)-2}.
\]
This argument uses homotopy equivalence of a graph of connected CW spaces with point-edge spaces, not a claim that each original sphere can be collapsed to a point.

**Step 2: The additional open-neighborhood simplices.** For an original edge \(e=uv\), put \(X_e=S_u\setminus\{e\}\), \(Y_e=S_v\setminus\{e\}\), and \(B_e=\Delta(X_e\cup Y_e)\). Both \(X_e\) and \(Y_e\) have at least two vertices and are disjoint. By the definition of the open neighborhood,
\[
\mathcal N(L(G))=A\cup\bigcup_{e\in E(G)}B_e,
\]
where including \(A\) is redundant for covering but essential for the attachment analysis.

A face of \(B_e\) that lies in \(A\) cannot use both an edge \(x\in X_e\) and an edge \(y\in Y_e\). Indeed, if \(x\) and \(y\) shared an endpoint other than \(u,v\), then \(e,x,y\) would form a triangle in \(G\); they cannot share either \(u\) or \(v\) because \(x\ne e\ne y\) and the graph is simple. Hence
\[
A\cap B_e=\Delta(X_e)\ \sqcup\ \Delta(Y_e),
\]
a disjoint union of two nonempty contractible simplices.

**Step 3: Distinct new simplices have no extra intersections.** Let \(e\ne f\) be edges of \(G\). If they meet at a vertex \(v\), their sets of common line-graph neighbors equal \(S_v\setminus\{e,f\}\): any additional shared neighbor would join their two other endpoints, making a triangle. Hence \(B_e\cap B_f\subseteq A_v\subseteq A\). If \(e,f\) are disjoint, a common line-graph neighbor is an edge joining one endpoint of \(e\) to one endpoint of \(f\). Two different such connectors create either a triangle or a four-cycle. Thus there is at most one, and \(B_e\cap B_f\) is empty or a single vertex lying in \(A\). This proves for every ordering of the original edges that the intersection of each newly attached \(B_e\) with all previously constructed material is *exactly* \(A\cap B_e\), the same two disjoint simplices.

**Step 4: One loop per original edge.** Attaching a contractible simplex along two disjoint contractible sub-simplices of its boundary to an already path-connected CW complex is homotopy equivalent to attaching a single interval with both endpoints in that complex. It therefore adds precisely one wedge summand \(S^1\) and changes no higher integral homology. The simplicial inclusions here are cofibrations, so the homotopy-pushout argument applies. The complex \(A\) is connected, and Step 3 permits all \(m\) attachments independently. Therefore
\[
\mathcal N(L(G))\simeq A\vee\bigvee^m S^1
\simeq\bigvee^{m+b}S^1\vee\bigvee_{v\in V(G)}S^{\deg(v)-2}.
\]
This proves the integral homotopy classification and torsion-freeness. In degrees \(k\ge2\), every attachment adds only an interval up to homotopy, and the inclusions \(A_v\hookrightarrow A\hookrightarrow\mathcal N(L(G))\) induce the stated direct-sum homology isomorphism. A graph automorphism carries \(S_v\) bijectively to \(S_{g(v)}\) and acts on the oriented boundary of its simplex with the sign of the incidence-edge permutation. This proves the asserted canonical higher-homology action.

**Step 5: Projective planes.** A finite projective plane of order \(q\) has \(s=q^2+q+1\) points and as many lines, with \(q+1\) incidences at each point or line. Its Levi graph has \(n=2s\) vertices, \(m=(q+1)s\) edges, girth at least six by bipartiteness and uniqueness of the line through any two points, and minimum degree \(q+1\ge3\). The formula gives \(m+b=2qs+1\) circles and \(2s\) spheres of dimension \(q-1\), including the cases \(q=2,3\).

## Verification
The included standalone `verify.py` enumerates, for four independent admissible finite examples, all simplices of the actual open-neighborhood complex \(\mathcal N(L(G))\). It verifies the no-triangle/no-quadrilateral hypotheses, the precise intersection identities of Step 3, and the ranks of the simplicial boundary matrices over \(\mathbb F_2\) computed directly from face incidence. The examples are the Fano-plane incidence graph, the order-three projective-plane incidence graph, the Petersen graph, and two Petersen graphs joined by a bridge. The recorded output in `verification_output.txt` is reproducible with `python3 verify.py`.

The mod-two reduced Betti ranks are respectively \(43\) in degree one; \(79\) in degree one and \(26\) in degree two; \(31\) in degree one; and \(61\) in degree one and \(2\) in degree two. In the order-three plane example the exact face counts by dimensions zero through five are \((52,624,1040,780,312,52)\), and the boundary ranks are \((0,51,494,520,260,52,0)\). The finite checks corroborate the cell construction; they do not substitute for the general homotopy proof. The checker does not calculate full integral Smith normal forms or all automorphism actions.

## Relationship to prior work
Lovász introduced neighborhood complexes in topological graph coloring. Kozlov (2005) proved the simple-homotopy equivalence between neighborhood complexes and graph-Hom complexes; this does not supply the present line-graph classification. Kamibeppu (2008, Theorems 3–4) obtains graph-like box-complex behavior when the **graph fed to the neighborhood construction** has no four-cycles. Here that graph is \(L(G)\), which contains overlapping four-cycles whenever \(G\) has a vertex of degree at least four. Thus Kamibeppu's theorem cannot yield the higher-dimensional sphere summands; the degree-three special subcase is not claimed as new by itself. Matsushita (2012) describes neighborhood-complex fundamental groups, but does not calculate the higher homotopy and integral homology of these line graphs.

The published block-graph neighborhood theorem (2026) covers line graphs of *trees* and their clique-block sphere boundaries; a connected original graph of minimum degree at least three is never a tree, and its line graph generally has cyclic, non-clique blocks. The published square-cycle-disjoint neighborhood theorem (2026) does not apply to line graphs of degree-four or higher graphs because their vertex cliques contain overlapping four-cycles. A separate line-graph Čech theorem (2026) concerns **closed** radius-one neighborhoods, which collapse to the original graph, not the **open** neighborhood complex here. In the order-three plane example the latter has \(26\) independent two-sphere generators, providing a concrete obstruction to identifying the two statements. These are comparisons of implications and object definitions, not merely titles. Search and access limitations are detailed in `REVIEW.md` and `AUDIT.json`.

## Limitations
The theorem does not cover graphs containing triangles or four-cycles, vertices of degree below three, disconnected graphs, or the closed-neighborhood/Čech construction. It does not assert that the displayed non-equivariant wedge decomposition is an equivariant one, nor give the full first-homology representation. No uniform classification under weakened girth or degree hypotheses is claimed. The originality assessment is based on accessible documents and searches; an unindexed equivalent formula cannot be ruled out. Independent mathematical validation has not been performed.

## References
1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613 (first posted 2005-03-28), https://arxiv.org/abs/math/0503613.
2. A. Kamibeppu, *Homotopy type of the box complexes of graphs without 4-cycles*, RIMS Kôkyûroku 1578 (2008), pp. 67–70, https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1578-13.pdf.
3. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (first posted 2012-10-10), https://arxiv.org/abs/1210.2803.
4. *Blockwise sphere bouquets in neighborhood complexes of block graphs*, published published-finding corpus record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-blockwise-sphere-bouquets-in-neighborhood-complexes-of-block-gra--2a7bb737f35c.
5. *Graph-like neighborhood complexes with edge-disjoint four-cycles*, published published-finding corpus record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-graph-like-neighborhood-complexes-with-edge-disjoint-four-cycles--d8f86495e49d.
6. *A scale-two Čech collapse theorem for line graphs of girth at least five*, published published-finding corpus record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-scale-two-ech-collapse-theorem-for-line-graphs-of-girth-at-lea--69ae03a7604c.
