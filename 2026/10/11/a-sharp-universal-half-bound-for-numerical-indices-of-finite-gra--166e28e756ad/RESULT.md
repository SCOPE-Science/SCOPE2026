# A sharp universal half bound for numerical indices of finite graph free spaces

## Finding
Let \(G=(V,E)\) be any finite connected simple graph with at least two vertices, equipped with its unit-edge shortest-path metric. For its **real** Lipschitz-free Banach space \(X=\mathcal F(V)\), the numerical index satisfies the dimension-independent bound
\[
\boxed{\frac12\le n(X)\le1.}
\]
Equivalently, every bounded linear operator \(T:X\to X\) satisfies the sharp estimate
\[
\boxed{\|T\|\le2v(T),}
\]
where \(v(T)\) is the numerical radius. The coefficient \(2\) cannot be reduced uniformly, because the unit-edge triangle \(K_3\) has numerical index \(1/2\).

## Assumptions and scope
All spaces and operators are over the real scalars. Give each graph edge length \(1\) and let \(d\) be the graph distance. Choose a base vertex \(o\). The finite-dimensional free space \(X\) is spanned by evaluations \(\delta_u\) with \(\delta_o=0\); its dual identifies isometrically with the space of functions \(h:V\to\mathbb R\) satisfying \(h(o)=0\), with norm
\[
\|h\|_{\mathrm{Lip}}=\max_{uv\in E}|h(u)-h(v)|.
\]
For an oriented edge \((a,b)\), put \(m_{ab}=\delta_a-\delta_b\). This unit molecule has \(\|m_{ab}\|=1\).

For an operator \(T\), define
\[
v(T)=\sup\{|x^*(Tx)|:x\in S_X,\ x^*\in S_{X^*},\ x^*(x)=1\},
\qquad n(X)=\inf_{\|T\|=1}v(T).
\]
No assumption of bipartiteness, planarity, regularity, or bounded vertex degree is made.

## Proof
**1. Edge molecules norm every operator.** The free-space unit ball is the convex hull of the signed normalized molecules \((\delta_u-\delta_v)/d(u,v)\) for distinct vertices. If \(u=v_0,v_1,\ldots,v_k=v\) is any shortest path, with \(k=d(u,v)\), then
\[
\frac{\delta_u-\delta_v}{d(u,v)}=\frac1k\sum_{j=1}^{k}(\delta_{v_{j-1}}-\delta_{v_j}).
\]
Consequently \(B_X=\operatorname{conv}\{m_{ab}:ab\in E\text{ oriented}\}\), and every \(T\) satisfies \(\|T\|=\max_{ab\in E}\|Tm_{ab}\|\).

**2. Extreme dual potentials are integral.** The dual unit ball is the finite polytope
\[
P=\{h:V\to\mathbb R:h(o)=0,\ |h(u)-h(v)|\le1\text{ for }uv\in E\}.
\]
Call an edge tight when its difference has absolute value \(1\). If the tight-edge spanning subgraph of a point \(h\in P\) were disconnected, a tight component not containing \(o\) could be shifted by a sufficiently small positive or negative constant. Each crossing edge has strict slack, so both shifts remain in \(P\), expressing \(h\) as their nontrivial midpoint. Thus a vertex \(h\) of \(P\) has a connected tight-edge spanning subgraph. Along its tight edges \(h\) changes by \(+1\) or \(-1\); connectivity and \(h(o)=0\) force \(h(v)\in\mathbb Z\) for every \(v\in V\).

**3. A two-functional decomposition at any neutral edge.** Let \(h\in P\) be *any integer-valued* \(1\)-Lipschitz potential, and let \(ab\in E\) satisfy \(h(a)=h(b)\). Give each graph edge its two orientations. Define the nonnegative integer cost of the arc \(s\to t\) by
\[
c(s,t)=1+\min\{0,h(t)-h(s)\}\in\{0,1\}.
\]
Let \(g(z)\) be the minimum total cost of a directed path from \(b\) to \(z\); these distances are finite. The direct arc \(b\to a\) costs \(1\), while every cost-zero arc strictly decreases \(h\) by \(1\). Since \(h(a)=h(b)\), no all-zero-cost path connects \(b\) to \(a\). Hence \(g(b)=0\) and \(g(a)=1\).

For every oriented edge \(s\to t\), the directed triangle inequality gives
\[
g(t)-g(s)\le c(s,t)=1+\min\{0,h(t)-h(s)\}.
\]
Apply the same inequality in reverse. With \(\Delta=h(t)-h(s)\in\{-1,0,1\}\), the resulting interval is
\[
-1+\max\{0,\Delta\}\le g(t)-g(s)
\le1+\min\{0,\Delta\}.
\]
Case inspection for the three integer values of \(\Delta\) shows simultaneously that \(|g(t)-g(s)|\le1\) and \(|(h-g)(t)-(h-g)(s)|\le1\). It follows that both \(g\) and \(h-g\) are \(1\)-Lipschitz on the entire graph metric. Normalize
\[
h_1=g-g(o),\qquad h_2=h-g+g(o).
\]
Then \(h=h_1+h_2\), both belong to \(P\), and
\[
h_1(m_{ab})=1,\qquad h_2(m_{ab})=-1.
\]
In particular, both have Lipschitz norm exactly \(1\) and each, with an appropriate sign, norms the selected edge molecule.

**4. Numerical-radius estimate.** Take any \(T\) with \(\|T\|=1\). By step 1, choose an oriented edge \((a,b)\) with \(\|Tm_{ab}\|=1\). Because \(P\) is a finite polytope, some vertex \(h\in P\) satisfies
\[
|h(Tm_{ab})|=\|Tm_{ab}\|=1.
\]
By step 2, \(h\) is integer valued, and \(h(m_{ab})\in\{-1,0,1\}\). If \(|h(m_{ab})|=1\), one of \(h\) or \(-h\) norms \(m_{ab}\), whence \(v(T)\ge |h(Tm_{ab})|=1\). If \(h(m_{ab})=0\), step 3 writes \(h=h_1+h_2\), where both \(h_1\) and \(-h_2\) norm \(m_{ab}\). Thus
\[
1=|h(Tm_{ab})|\le|h_1(Tm_{ab})|+|h_2(Tm_{ab})|\le2v(T).
\]
This proves \(v(T)\ge1/2\) for every norm-one \(T\), and scaling proves the operator inequality. Finally, the unit-edge triangle is equilateral; its exact numerical index is \(1/2\), by Corollary 5.3 of Cobollo–Guirao–Montesinos [1]. Therefore the lower bound is sharp within the stated family.

## Verification
The infinite family follows from the four analytic steps, not from finite enumeration. The standalone standard-library checker `artifacts/verify.py` independently enumerates all \(771\) connected labeled simple graphs of orders \(2\) through \(5\), all \(41{,}463\) normalized integer-valued \(1\)-Lipschitz potentials in their complete allowable range, and \(88{,}156\) incidences of edges with equal potential values. For each incidence it computes the shortest-path potential by exact integer relaxations, tests the prescribed edge difference, and checks both resulting Lipschitz functions on every edge. Its output is:

`VERIFY_OK connected_labeled_graphs= 771 integer_potentials= 41463 equal_edge_decompositions= 88156 n=2..5`

Reproduce with `python3 artifacts/verify.py`. The finite checker tests the novel graph-potential lemma only. It is not an exhaustive check of infinite graph orders or of all operators; the analytic proof provides those quantifiers.

## Relationship to prior work
Cobollo, Guirao, and Montesinos [1] introduced the exact numerical-index theory of two-dimensional Lipschitz-free spaces and proved that the equilateral three-point space has index \(1/2\). Their higher-dimensional application concerns two-dimensional subspaces, not a uniform lower bound on the *ambient* numerical index for graph metrics. The published finite-unit-edge graph theorem [2] characterizes precisely when the index equals \(1\), via bipartiteness, but leaves nonbipartite numerical-index values undetermined. The published complete-equilateral classification [3], wheel example [4], and cycle calculations [5] provide special values only; none implies a graph-uniform lower bound. The present argument instead uses a universal **integral-potential splitting** at every neutral graph edge, giving a single sharp inequality for all finite connected unweighted graphs.

## Limitations
The result concerns **real**, **finite**, **connected**, **unit-edge shortest-path graph metrics**. No claim is made for arbitrary positively weighted graphs, complex scalars, infinite graphs, or general finite metric spaces. It provides a sharp common lower bound, not the exact numerical index of each nonbipartite graph; in particular, different nonbipartite examples may have distinct indices. The bibliographic comparison cannot rule out an unpublished or unindexed equivalent argument under root-polytope, Arens–Eells, transportation-cost, or numerical-radius terminology.

## References
1. Ch. Cobollo, A. J. Guirao, and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1 (public 2023-04-25), later *J. Math. Anal. Appl.* **538** (2024), 128333, DOI 10.1016/j.jmaa.2024.128333; see Theorem 5.1 and Corollary 5.3. https://arxiv.org/pdf/2304.13183.
2. *Bipartiteness exactly characterizes numerical index one for finite graph metrics*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-bipartiteness-exactly-characterizes-numerical-index-one-for-fini--1ca1185831c4.
3. *Numerical index one half for every finite equilateral Lipschitz-free space*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-numerical-index-one-half-for-every-finite-equilateral-lipschitz--cc7060df7211.
4. *A five-point non-equilateral Lipschitz-free space with numerical index one half*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-five-point-non-equilateral-lipschitz-free-space-with-numerical--9265557f0f91.
5. *Numerical-index parity law for Lipschitz-free spaces over cycles*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-numerical-index-parity-law-for-lipschitz-free-spaces-over-cycles--06885f9d5f05.
