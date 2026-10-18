# A fivefold asymmetry barrier and center-dimensional transition for \(K_{3,3}\)-minor-free cut polytopes

## Finding
Let \(G\) be any finite simple graph having no \(K_{3,3}\) minor and containing a subgraph isomorphic to \(K_5\). Write \(P(G)\) for its cut polytope in one coordinate per edge. Its Minkowski asymmetry is exactly
\[
 s(P(G))=5,
\]
and the half-edge vector \(\tfrac12\mathbf 1_{E(G)}\) is a minimizing center. **Every** minimizing center has coordinate \(\tfrac12\) on each edge belonging to any \(K_5\) subgraph of \(G\).

There is an exact classification when \(H\) is *edge-maximal* among \(K_{3,3}\)-minor-free simple graphs on its fixed vertex set and contains \(K_5\). Let \(F(H)\) be the union of the edge sets of all \(K_5\) subgraphs. For each triangle \(T\subseteq H\) and each \(W=\varnothing\) or singleton subset of its three vertices, define \(q_T(W)=|\delta_T(W)|\) (hence \(q_T(W)\in\{0,2\}\)) and \(a_{T,W,e}=(-1)^{\mathbf1[e\in\delta_T(W)]}\). The entire set \(\mathcal M(H)\) of minimizing centers is
\[
\left\{c\in\mathbb R^{E(H)}:
  c_e=\tfrac12\ (e\in F(H)),\quad
  \sum_{e\in E(T)}a_{T,W,e}c_e\le\tfrac53-q_T(W)
  \text{ for every }T,W\right\}.
\]
Its affine dimension is
\[
 \dim\operatorname{aff}\mathcal M(H)=|E(H)\setminus F(H)|.
\]
Thus the minimizing center is unique if and only if every edge of \(H\) lies in a \(K_5\) subgraph. These are exact affine-invariant statements, not Euclidean-radius claims.

## Assumptions and scope
For a finite simple graph \(G=(V,E)\), a cut \(\delta_G(S)\), \(S\subseteq V\), consists of edges with exactly one endpoint in \(S\). Define
\[
 P(G)=\operatorname{conv}\{\mathbf1_{\delta_G(S)}:S\subseteq V\}\subseteq\mathbb R^E,
 \qquad
 s(P)=\min\{s\ge1:\exists c,\ -(P-c)\subseteq s(P-c)\}.
\]
The minimizing centers are all \(c\) attaining \(s(P)\). A full-dimensional cut polytope has dimension \(|E|\), including when the graph is disconnected. Isolated vertices do not change \(P(G)\). The first result assumes the **presence of an actual \(K_5\) subgraph**, not just a \(K_5\) minor. The center-dimension formula additionally assumes maximality of \(H\) on its fixed vertex set.

## Proof
**1. A facetwise reflection test.** For a compact full-dimensional polytope and any valid facet \(a\cdot x\le b\), let \(m_a=\min_{x\in P}a\cdot x\). The reflected-containment condition is equivalent to
\[
 (s+1)a\cdot c\le s b+m_a
\]
for every facet. Indeed \(c-(x-c)/s\in P\) for all \(x\in P\) is equivalent to the displayed inequalities. They also force \(c\in P\) by convexity.

**2. Exact pentagon certificate.** Label a copy of \(K_5\) by \([5]\). For each of its sixteen cuts \(\delta(W)\), take the representative with vertex \(5\notin W\), and put \(q(W)=|\delta(W)|\). Switching the pentagonal facet \(\sum_{e\in E(K_5)}x_e\le6\) gives
\[
 a_W\cdot x\le6-q(W),\qquad
 (a_W)_{ij}=(-1)^{\mathbf1[ij\in\delta(W)]},
 \quad\min_{x\in P(K_5)}a_W\cdot x=-q(W).
\]
The last equality follows because switching maps cut indicators bijectively onto cut indicators; their edge counts range from \(0\) to \(6\). Let \(c\) be a putative center at factor \(s\). All sixteen reflection tests imply
\[
 (s+1)a_W\cdot c\le6s-(s+1)q(W).
\]
The exact combinatorial identities
\[
 \sum_W a_W=0,\qquad \sum_W q(W)=80
\]
therefore yield \(0\le96s-80(s+1)=16(s-5)\), forcing \(s\ge5\). At \(s=5\), every one of these inequalities must be equality. Write \(z=c-\tfrac12\mathbf1\); then \(a_W\cdot z=0\) for all \(W\). The characters \((a_W)_{ij}=\sigma_i\sigma_j\) on the sixteen sign vectors with \(\sigma_5=1\) satisfy
\[
 \sum_W(a_W)_{ij}(a_W)_{kl}=16\mathbf1[\{i,j\}=\{k,l\}],
\]
so \(z=0\). Hence **the half-edge vector is the unique factor-five center of \(P(K_5)\)**.

**3. Optimal center of every maximal minor-free extension.** Theorem 3.3 of Chimani–Juhnke-Kubitzke–Nover–Römer gives a complete facet list for an edge-maximal \(K_{3,3}\)-minor-free graph \(H\): the four switched metric inequalities on each triangle and the sixteen switched pentagonal inequalities on each \(K_5\). At \(c_0=\tfrac12\mathbf1_{E(H)}\), a switched pentagon with \(q\in\{0,4,6\}\) has right support \(6-q\), center value \(5-q\), and left support \(-q\). Its reflection ratio is therefore precisely \(5\). A switched triangle has the corresponding values \(2-q\), \(\tfrac32-q\), and \(-q\), giving ratio \(3\). Consequently **all** facet tests hold at factor \(5\), with strict slack on every triangle test. Thus \(s(P(H))\le5\).

Every \(K_5\) subgraph induces a coordinate projection of \(P(H)\) onto \(P(K_5)\); projecting a reflected containment cannot increase asymmetry. Step 2 therefore yields \(s(P(H))\ge5\). If \(c\) is any factor-five center, its projection to every \(K_5\) is the unique half-edge center by Step 2. This proves the coordinate constraints on \(F(H)\). Conversely these constraints make every pentagonal test an equality; the remaining triangle tests at \(s=5\) are exactly \(a_{T,W}\cdot c\le\tfrac53-q_T(W)\). This proves the asserted complete center polytope.

The affine space fixed by \(c_e=1/2\) for \(e\in F(H)\) has dimension \(|E(H)\setminus F(H)|\). At \(c_0\), each triangle inequality has strict slack
\[
 (\tfrac53-q)-(\tfrac32-q)=\tfrac16.
\]
Thus a sufficiently small relative open ball about \(c_0\) in that affine space satisfies every triangle test, proving the dimension formula and uniqueness criterion.

**4. All nonmaximal minor-free graphs containing a clique.** Let \(G\) satisfy the first claim, and extend its edge set on the same vertex set to an edge-maximal \(K_{3,3}\)-minor-free graph \(H\). Coordinate projection maps \(P(H)\) *onto* \(P(G)\), so the factor-five containment centered at \(c_0(H)\) projects to factor-five containment centered at \(c_0(G)\). Conversely, coordinate projection from \(P(G)\) onto any subgraph \(K_5\) gives \(s(P(G))\ge s(P(K_5))=5\). Every minimizing center projects to a minimizing center of that \(K_5\), pinning its ten edge coordinates. Taking the union of all such copies proves the general statement.

## Verification
A pure-Python exact checker (`verify_cut_symmetry.py`) enumerates all sixteen \(K_5\) cuts, their sixteen switched pentagonal support ranges, all forty switched triangle support ranges, the Walsh Gram identities, and a strict two-clique-sum example. It uses rational arithmetic and asserts the values \(\sum_Wq(W)=80\), the symmetry bound \(5\), and the positive-dimensional center example; it terminates with two `VERIFY_OK` lines. The infinite-graph assertion is proved by the preceding facet-classification and projection arguments, not by finite enumeration.

In the explicit strict two-clique-sum of \(K_5\) and \(K_3\) along one edge, the ten clique-edge coordinates are fixed at \(1/2\). If \(u,v\) are the other two triangle-edge center coordinates, then
\[
 \tfrac56\le u+v\le\tfrac76,\qquad |u-v|\le\tfrac16.
\]
This is a genuinely two-dimensional family of optimal centers; the same graph is not edge-transitive. Larger collections of attached triangles produce arbitrarily large center dimensions.

## Relationship to prior work
Chimani, Juhnke-Kubitzke, Nover, and Römer (arXiv:1903.01817, first posted 2019-03-05) prove the exact facet classification for \(K_{3,3}\)-minor-free cut polytopes (Theorem 3.3) and their projection description (Corollary 3.4). Barahona and Mahjoub (1986) established foundational facet and switching results. Neither inspected primary text identifies the resulting factor-five Minkowski asymmetry or the full optimal-center polytope and affine-dimension classification.

The exact \(K_5\) base case is already known from an edge-transitive-graph cut-polytope asymmetry theorem; it is not independently claimed novel here. Another prior result identifies asymmetry of \(K_5\)-minor-free cut polytopes through odd girth and has a disjoint hypothesis. The present result instead characterizes a non-edge-transitive infinite class **containing a \(K_5\)**, including its entire maximizing-center geometry for maximal graphs. Equality and rigidity use the complete pentagon Walsh certificates; the global extension uses the minor-free facet theorem and projection.

## Limitations
The asserted value \(5\) requires an actual \(K_5\) subgraph and exclusion of a \(K_{3,3}\) minor; it is **not** claimed for every graph with a \(K_5\) minor. The center-dimension and full center-halfspace formulas are proved for edge-maximal graphs; for arbitrary nonmaximal graphs only half-center optimality and coordinate pinning on existing \(K_5\) subgraphs are asserted. Independently established facet classification is an explicit premise of the argument. The literature checks do not establish absolute bibliographic uniqueness, and no independent mathematical audit is claimed.

## References
1. M. Chimani, M. Juhnke-Kubitzke, A. Nover, and T. Römer, *Cut Polytopes of Minor-free Graphs*, arXiv:1903.01817v1, 2019-03-05, especially Theorem 3.3 and Corollary 3.4. https://arxiv.org/html/1903.01817v1
2. F. Barahona and A. R. Mahjoub, *On the cut polytope*, Mathematical Programming 36 (1986), 157–173, especially Section 2. https://www.lamsade.dauphine.fr/~mahjoub/Papers/BM86.pdf
