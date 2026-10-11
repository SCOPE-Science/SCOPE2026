# A sharp one-half numerical-index bound for finite unweighted graph metrics
## Finding
Let \(G=(V,E)\) be any finite, connected, simple undirected graph with at least two vertices. Give \(V\) the shortest-path metric in which each edge has length \(1\). For its real Lipschitz-free (transportation-cost) space \(X=\mathcal F(V)\), the numerical index satisfies the dimension-free sharp bound
\[
\boxed{n(X)\ge\frac12.}
\]
Equality is attained by the three-vertex complete graph. Equivalently, every real-linear operator \(T:X\to X\) satisfies the sharp uniform estimate
\[
\boxed{\|T\|\le2v(T),}
\]
where \(v(T)\) is the numerical radius. This is a lower bound valid for **all** finite unweighted graph metrics, not an exact computation of the index of every individual graph.

## Assumptions and scope
Choose a root \(o\in V\), and identify \(X^*\) with the real space \(\operatorname{Lip}_0(V)\) of functions vanishing at \(o\), with norm \(\|h\|_{\mathrm{Lip}}=\max_{uv\in E}|h(u)-h(v)|\). Denote the canonical evaluation vector at \(z\) by \(\delta_z\), with \(\delta_o=0\). Every oriented graph edge \(uv\) defines a unit molecule \(m_{uv}=\delta_u-\delta_v\), and \(m_{vu}=-m_{uv}\). For each real-linear operator \(T\) on \(X\), define
\[
v(T)=\sup\big\{|h(Tx)|:\|x\|=\|h\|=1,\ h(x)=1\big\},\qquad n(X)=\inf_{\|T\|=1}v(T).
\]
All quantities are real. The number of vertices may be arbitrarily large but finite. Simplicity and unit edge lengths are essential to the proof below.

## Proof
**Step 1: edge molecules determine the norm.** The unit ball of a finite free space is the convex hull of its normalized point-pair molecules. If distinct \(a,b\in V\) have graph distance \(k\), a shortest path \(a=v_0,v_1,\ldots,v_k=b\) gives
\[
\frac{\delta_a-\delta_b}{d(a,b)}=\frac1k\sum_{j=0}^{k-1}(\delta_{v_j}-\delta_{v_{j+1}}).
\]
Thus \(B_X\) is the convex hull of the oriented edge molecules. In particular, every operator satisfies
\[
\|T\|=\max_{uv\in E}\|Tm_{uv}\|=\max_{uv\in E}\max_{h\in\operatorname{ext}B_{X^*}}|h(Tm_{uv})|.
\]
We may maximize numerical radius over norming pairs consisting of an oriented edge molecule and an extreme point of the dual ball. Indeed, a norming \(x\in S_X\) is a convex combination of oriented edge molecules; if \(h(x)=1\), each molecule with positive coefficient must also satisfy \(h(m)=1\). For a fixed molecule, the face of dual functionals satisfying \(h(m)=1\) is compact and convex, so the maximum of a linear evaluation on this face occurs at a dual-ball extreme point. Therefore
\[
v(T)=\max\big\{|h(Tm_{uv})|:uv\in E\text{ oriented},\ h\in\operatorname{ext}B_{X^*},\ h(m_{uv})=1\big\}.
\]

**Step 2: every extreme dual height is integral.** Let \(h\) be a vertex of the Lipschitz unit ball. Call an edge \(ab\) *tight* when \(|h(a)-h(b)|=1\). Its tight-edge subgraph must be connected: otherwise choose a tight-edge component not containing \(o\). All edges crossing from this component to its complement have positive slack. Since the graph is finite, adding or subtracting the same sufficiently small positive constant on that component leaves every edge constraint valid and leaves \(h(o)=0\), contradicting extremality. Thus the tight-edge subgraph is connected. Starting at \(h(o)=0\) and following tight edges shows that \(h(z)\in\mathbb Z\) for every vertex \(z\). In particular, along every edge \(uv\),
\[
h(m_{uv})=h(u)-h(v)\in\{-1,0,1\}.
\]

**Step 3: a zero edge slope is the difference of two norming functionals.** Fix an oriented edge \(uv\) and an extreme dual \(h\) with \(h(u)=h(v)\). Give each edge \(ab\) a new positive length
\[
w_{ab}=1-\frac12|h(a)-h(b)|\in\left\{\frac12,1\right\}.
\]
The selected edge \(uv\) has new length \(1\). Every alternative simple path from \(u\) to \(v\) uses at least two edges (simplicity excludes parallel edges), and each has new length at least \(1/2\). Consequently the shortest-path distance \(d_w(u,v)\) in the reweighted graph equals exactly \(1\).

Set \(k(z)=d_w(v,z)-d_w(v,o)\). Then \(k(o)=0\), and on each edge \(ab\) we have \(|k(a)-k(b)|\le w_{ab}\). Define
\[
g_+(z)=k(z)+\frac12h(z),\qquad g_-(z)=k(z)-\frac12h(z).
\]
Both are rooted and \(1\)-Lipschitz for the **original**, unweighted graph metric because
\[
|g_\pm(a)-g_\pm(b)|\le w_{ab}+\frac12|h(a)-h(b)|=1
\]
on each edge. Moreover \(k(u)-k(v)=1\), while \(h(u)-h(v)=0\), so \(g_+(m_{uv})=g_-(m_{uv})=1\). Thus each \(g_\pm\) is a dual unit norming functional for \(m_{uv}\), and \(h=g_+-g_-\) exactly.

**Step 4: operator norm versus numerical radius.** For any oriented edge \(uv\) and any extreme dual \(h\), there are only two cases. If \(|h(m_{uv})|=1\), changing sign if necessary makes it a norming pair, whence \(|h(Tm_{uv})|\le v(T)\). If \(h(m_{uv})=0\), the construction above gives
\[
|h(Tm_{uv})|\le|g_+(Tm_{uv})|+|g_-(Tm_{uv})|\le2v(T).
\]
Taking the maximum over all extreme dual potentials and all edges in Step 1 gives \(\|T\|\le2v(T)\) for every \(T\). Hence \(n(X)\ge1/2\).

**Step 5: sharpness.** Let the graph be a triangle with root \(o\) and other vertices \(a,b\). In the basis \((\delta_a,\delta_b)\) the free-space norm is
\[
\|(s,t)\|=\max\{|s|,|t|,|s+t|\}.
\]
Define \(T\) by the matrix
\[
\begin{pmatrix}-1/2&0\\1&1/2\end{pmatrix}.
\]
The three unoriented edge molecules are \((1,0)\), \((0,1)\), and \((1,-1)\). Their images have respective norms \(1\), \(1/2\), and \(1/2\), so \(\|T\|=1\). The six extreme dual functions are the sign pairs of \((1,0)\), \((0,1)\), and \((1,1)\). For every extreme dual functional norming an oriented edge molecule, direct substitution gives absolute evaluation \(1/2\) on its image under \(T\). The finite extreme-norming-pair reduction of Step 1 yields \(v(T)=1/2\). This realizes equality and proves that the universal bound is sharp.

## Verification
The proof is symbolic for every finite connected simple unit-edge graph. An accompanying standalone Python 3 verifier uses exact rational arithmetic to check all connected labeled simple graphs with two, three, or four vertices, and five additional five-vertex graphs (a cycle, a wheel, a complete graph, a path, and a complete bipartite graph). It tests the tight-edge extremality criterion, the reweighted distance identity, both dual norming functions, their exact difference, and the triangle sharpness witness. Successful replay reports `VERIFY_OK graphs=48 zero-edge_face_checks=556 triangle_norm=1 triangle_radius=1/2`. Finite experiments do **not** substitute for Steps 1–5.

## Relationship to prior work
A. Godard (2009, arXiv:0904.3178v1) develops the geometry of Lipschitz-free spaces over tree metrics and the basic free-space/dual-Lipschitz pairing; it does not study numerical indices of arbitrary finite graphs. Cobollo, Guirao, and Montesinos (2023, arXiv:2304.13183v1) determine the numerical index of every **two-dimensional** free space, in particular \(1/2\) for the equilateral triangle. Their theorem does not yield a dimension-free statement for all finite unit-edge graph metrics.

A published graph-metric classification of **numerical index one** establishes that \(n(\mathcal F(V))=1\) exactly for bipartite graphs, but explicitly does not determine the index of nonbipartite graphs. Related published exact evaluations of numerical index \(1/2\) for equilateral spaces of all finite cardinalities and for the five-vertex wheel furnish matching examples, not a universal lower bound for arbitrary graphs. The present theorem supplies that missing uniform inequality by expressing a zero-slope extreme dual potential as the difference of two norming Lipschitz functions. Neither an exact single-graph calculation nor a characterization of the **upper** endpoint implies this inequality.

## Limitations
Only real scalars, finite connected simple unweighted graph metrics, and the standard Lipschitz-free norm are covered. There is no claim for arbitrary finite metrics, edge-weighted graphs, multigraphs, complex numerical indices, or infinite graphs. The theorem gives a sharp universal lower bound, not the numerical index of each nonbipartite graph. The originality comparison included open-access primary manuscripts and closely related published research records; an equivalent historical result under Arens–Eells, polyhedral, or numerical-radius language cannot be entirely excluded. No independent mathematical audit has been performed.

## References
1. A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178v1 (first posted 21 April 2009); Proceedings of the American Mathematical Society 138 (2010), 4311–4320, DOI 10.1090/S0002-9939-2010-10421-5.
2. Ch. Cobollo, A. J. Guirao, and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1 (first posted 25 April 2023); Journal of Mathematical Analysis and Applications 538 (2024), 128333.
3. *Bipartiteness exactly characterizes numerical index one for finite graph metrics*, publicly available mathematical manuscript (2026), record 1ca1185831c4.
4. *Numerical index one half for every finite equilateral Lipschitz-free space*, publicly available mathematical manuscript (2026), record cc7060df7211.
5. *A five-point non-equilateral Lipschitz-free space with numerical index one half*, publicly available mathematical manuscript (2026), record 9265557f0f91.
