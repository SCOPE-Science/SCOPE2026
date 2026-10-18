# Fractional coloring determines the Minkowski-center space of every stable-set polytope

## Finding

**Theorem.** Let \(G=(V,E)\) be any finite simple graph on \(n\ge1\) vertices. Its stable-set polytope is
\[
P_G=\operatorname{conv}\{\mathbf1_I:I\subseteq V\text{ is an independent set}\}\subset\mathbb R^V.
\]
Let \(\chi_f(G)\) be the fractional chromatic number, and set \(\lambda=\chi_f(G)\). For every compact full-dimensional convex body \(K\) define its *Minkowski asymmetry* and its set of *Minkowski centers* by
\[
s(K)=\inf_{c\in\mathbb R^n}\inf\{r\ge1:-(K-c)\subseteq r(K-c)\},\qquad
\mathcal M(K)=\{c:-(K-c)\subseteq s(K)(K-c)\}.
\]
Then
\[
\boxed{s(P_G)=\chi_f(G)},\qquad
\boxed{\mathcal M(P_G)=\frac{\lambda P_G\cap[1,\infty)^V}{\lambda+1}}.
\]
Define the fractional-coloring dual polytope and its optimal-support union by
\[
D_G=\left\{y\in\mathbb R^V_{\ge0}:\sum_{i\in I}y_i\le1\quad\text{for every independent }I\right\},
\]
\[
T_G=\left\{i\in V:\exists y\in D_G,\ \sum_{j\in V}y_j=\lambda,\ y_i>0\right\}.
\]
The Minkowski-center space satisfies
\[
\boxed{\dim\operatorname{aff}\mathcal M(P_G)=n-|T_G|}.
\]
More precisely, every center has coordinate \(1/(\lambda+1)\) at each vertex in \(T_G\). At every vertex outside \(T_G\), the coordinate can be increased by a sufficiently small positive amount, *simultaneously and independently*, starting from the constant center \(\mathbf1/(\lambda+1)\). Thus the center is unique exactly when \(T_G=V\).

For a perfect graph, \(\lambda=\omega(G)\) and \(T_G\) is precisely the union of its maximum cliques. Hence the center-space dimension is the number of graph vertices lying in no maximum clique. For every vertex-transitive graph, the center is unique (the uniform average of an optimal dual solution is strictly positive).

## Assumptions and scope

The graph is finite, simple, undirected, and nonempty. Isolated vertices, disconnected graphs, and the edgeless graph are permitted. Geometric dimension is the full coordinate dimension \(n\), since the origin and all standard basis vectors belong to \(P_G\). The fractional chromatic number is the optimal value
\[
\chi_f(G)=\min\left\{\sum_I w_I:w_I\ge0,\ \sum_{I\ni i}w_I\ge1\ \text{for every }i\in V\right\},
\]
where \(I\) ranges over all independent sets. No integrality or perfectness hypothesis is required except for the stated specialization to perfect graphs.

## Proof

**1. Downward closure.** If \(x\in P_G\) and \(0\le z\le x\) coordinatewise, then \(z\in P_G\). To see this, represent \(x\) as the expectation of a random independent-set indicator. Conditional on the selected independent set, independently retain a selected vertex \(i\) with probability \(z_i/x_i\) when \(x_i>0\), and retain it with probability zero when \(x_i=0\). The thinned set remains independent and has inclusion marginals \(z_i\). Also \(P_G\subseteq[0,1]^V\).

**2. Exact feasibility criterion.** For any \(r\ge1\), the condition that \(c\) be a center with containment factor \(r\) is
\[
(1+r)c-x\in rP_G\quad\text{for every }x\in P_G.
\]
Put \(q=(1+r)c\). Taking \(x=0\) shows \(q\in rP_G\). Taking \(x=e_i\) and using nonnegativity of \(rP_G\) shows \(q_i\ge1\) for every coordinate. Conversely, if \(q\in rP_G\) with \(q_i\ge1\) for all \(i\), then for any \(x\in P_G\) we have \(0\le q-x\le q\); downward closure gives \(q-x\in rP_G\). Hence
\[
\boxed{r\text{ is feasible }\Longleftrightarrow rP_G\cap[1,\infty)^V\ne\varnothing},
\]
and at the optimal factor the centers are exactly the points displayed in the theorem.

**3. Fractional-coloring equivalence.** Suppose \(q=\sum_I w_I\mathbf1_I\in rP_G\), with \(w_I\ge0\) and \(\sum_I w_I=r\), where the empty independent set may carry slack weight. If \(q\ge\mathbf1\), then the \(w_I\)'s give a fractional coloring of total weight \(r\). Conversely, if a fractional coloring has total weight \(r\), its weighted incidence-vector sum belongs to \(rP_G\) and dominates \(\mathbf1\). If its cost is below a prescribed \(r\), add slack weight to the empty independent set. Consequently the minimum feasible geometric factor equals \(\lambda=\chi_f(G)\). In particular \(\mathbf1\in\lambda P_G\): by downward closure, a fractional coloring of optimal cost yields this exact point. The constant vector \(\mathbf1/(\lambda+1)\) is therefore a minimizing center.

**4. Dual support and center rigidity.** The polytope \(D_G\) is compact because the singleton independent sets imply \(0\le y_i\le1\). Finite-dimensional linear programming duality gives
\[
\lambda=\max_{y\in D_G}\sum_{i\in V}y_i.
\]
Antiblocking (or direct separating-hyperplane duality for downward-closed convex sets) gives
\[
\lambda P_G=\{z\ge0:y\cdot z\le\lambda\ \text{for all }y\in D_G\}.
\]
Indeed, any violated separating inequality for nonnegative \(z\) can be chosen with nonnegative normal by downward closure, then scaled to the unit-support bound defining \(D_G\). Let \(q\in\lambda P_G\cap[1,\infty)^V\). If \(y\in D_G\) is optimal, then
\[
0\le\sum_i y_i(q_i-1)=y\cdot q-\lambda\le0.
\]
Every term is nonnegative, so \(q_i=1\) whenever some optimal \(y\) has \(y_i>0\); precisely the coordinates in \(T_G\) are fixed.

For the converse, let \(i\notin T_G\). Every vertex \(y\) of the finite polytope \(D_G\) satisfies either \(y_i=0\) or \(\sum_j y_j<\lambda\). Thus a sufficiently small positive \(\varepsilon_i\) satisfies
\[
y\cdot(\mathbf1+\varepsilon_i e_i)\le\lambda\quad\text{for every vertex }y\text{ of }D_G,
\]
and hence \(\mathbf1+\varepsilon_i e_i\in\lambda P_G\). Choosing still smaller perturbations in all free coordinate directions simultaneously preserves every finitely many strict vertex inequalities; the resulting feasible orthant box has dimension \(n-|T_G|\). All other coordinates are fixed, proving the affine-dimension formula.

**5. Perfect graphs.** For a perfect graph \(G\), its complement is perfect, and the clique-inequality description of the stable-set polytope gives \(D_G=\operatorname{STAB}(\overline G)\), the convex hull of clique indicators of \(G\). Maximizing \(\sum_i y_i\) selects maximum-clique indicators; therefore \(\lambda=\omega(G)\) and the support union equals the union of maximum cliques. This establishes the claimed specialization. For a vertex-transitive graph, average any optimal dual vector over automorphisms; its sum remains \(\lambda>0\) and all its coordinates are equal and positive, proving uniqueness.

## Verification

A self-contained exact-rational checker is included as `verify.py`. It enumerates independent sets and vertices of \(D_G\), solves their active inequalities over rational numbers, identifies the exact optimal dual face and free-coordinate directions, and verifies positive feasible perturbations. It reproduces the following cases: an edgeless graph on three vertices (factor \(1\), unique center), a triangle (factor \(3\), unique), a three-vertex path (factor \(2\), unique), one edge plus an isolated vertex (factor \(2\), center-space dimension \(1\)), a five-cycle (factor \(5/2\), unique), and a four-clique plus an isolate (factor \(4\), center-space dimension \(1\)). The verifier is finite corroboration; Steps 1--5 prove the universal theorem.

## Relationship to prior work

Classical stable-set-polytope antiblocking and the fractional-coloring linear program establish the two geometric ingredients independently; see de Carli Silva--Tunçel (2014), in particular its equations (1.4c), (7.5)--(7.7), and appendix on antiblocking. Brandenberg--von Dichter--González Merino (2021), especially its Introduction and symmetrization sections, studies the Minkowski asymmetry of general convex bodies but does not evaluate it for stable-set polytopes. Beck--Schymura (2023), especially Sections 1--2 and the zonotope applications, studies asymmetry for lattice zonotopes rather than this graph-based family. Rezaei's chapter on graph entropy and fractional chromatic numbers in *Mathematical Foundations and Applications of Graph Entropy* (2016), Section 4.9, records the fractional-coloring point \(\mathbf1/\chi_f\) in the stable-set polytope and analyzes coordinates improvable above it, but does not identify the complete Minkowski-center space or prove the affine-dimension formula stated here. The present result uses known LP/antiblocking ingredients but adds the global asymmetry interpretation and a complete support-sensitive rigidity classification. No claim is made that fractional coloring, antiblocking duality, or Minkowski asymmetry itself is newly defined here.

## Limitations

The equivalence is specific to polytopes generated by zero-one incidence vectors of a hereditary independence system containing all singletons; the explicit graph-theoretic simplifications use graph structure. The center-space dimension is computed by a (potentially exponentially sized) exact fractional-coloring dual, not claimed polynomial-time for arbitrary graphs. This is a self-review and finite exact-rational verification, not independent validation. Equivalent statements under different antiblocking or graph-entropy terminology remain a literature risk; no absolute priority or certification claim is made.

## References

1. R. Brandenberg, K. von Dichter, B. González Merino, *Tightening and reversing the arithmetic-harmonic mean inequality for symmetrizations of convex sets*, arXiv:2112.13590v1 (first publicly posted 2021-12-27), https://arxiv.org/html/2112.13590v1.
2. M. Beck and M. Schymura, *Deep lattice points in zonotopes, lonely runners, and lonely rabbits*, arXiv:2301.12182v1 (first publicly posted 2023-01-28), https://arxiv.org/html/2301.12182v1.
3. M. K. de Carli Silva and L. Tunçel, *An Axiomatic Duality Framework for the Theta Body and Related Convex Corners*, arXiv:1412.2103v1 (2014), https://arxiv.org/html/1412.2103v1.
4. S. S. C. Rezaei, *Entropy, Counting, and Fractional Chromatic Number*, Chapter 4 in *Mathematical Foundations and Applications of Graph Entropy* (2016), especially Section 4.9.
