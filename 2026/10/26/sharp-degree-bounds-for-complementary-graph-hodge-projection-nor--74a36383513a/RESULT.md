# Sharp degree bounds for complementary graph Hodge projection norms

## Finding
Let \(G\) be any finite connected simple graph with at least one edge, with unit edge conductances and maximum vertex degree \(\Delta\geq1\). Let \(Q\) be the Euclidean orthogonal projector from the real edge-coordinate space onto its cut (gradient) space, and let \(C=I-Q\) be the complementary cycle-space projector. In the unweighted coordinate \(\ell_1\) and \(\ell_\infty\) operator norms,
\[
\boxed{\|Q\|_{1\to1}-\|C\|_{1\to1}\geq\frac{3-\Delta}{\Delta+1},\qquad
\|Q\|_{\infty\to\infty}-\|C\|_{\infty\to\infty}\geq\frac{3-\Delta}{\Delta+1}.}
\]
The constant is best possible for **every** integer \(\Delta\geq1\), with equality for the complete graph \(K_{\Delta+1}\). Consequently, every graph of maximum degree at most three has \(\|Q\|\geq\|C\|\) at both endpoints. Degree four is the first possible reversal: \(K_5\) has \(\|Q\|=8/5\) and \(\|C\|=9/5\).

A sharper local statement uses the two endpoint degrees. For an edge \(e=uv\), write \(p=\deg(u)\), \(q=\deg(v)\), \(R_e\) for the unit-resistance effective resistance of its endpoints, and \(q_e=\|Q\mathbf e_e\|_1\), \(c_e=\|C\mathbf e_e\|_1\). Then
\[
\boxed{q_e-c_e=2R_e-1.}
\]
For \((p,q)\ne(1,1)\), the previously known degree lower bound for effective resistance yields
\[
q_e-c_e\geq\frac{1-(p-2)(q-2)}{pq-1}.
\]
Thus if every edge satisfies \((p-2)(q-2)\leq1\), cut-projection dominance holds globally, even if the graph has vertices of arbitrarily high degree. When both endpoint degrees are at least two, equality in this local degree bound occurs **exactly** when the endpoints are adjacent true twins: they have the same degree and the same neighbors outside each other. If either endpoint has degree one, the edge is a bridge and the local bound is also an equality. The degree resistance inequality itself is not claimed as new; the contribution is its sharp translation into complementary projection-norm dominance and its local saturation criterion.

## Assumptions and scope
The graph is finite, connected, simple, undirected, and unweighted, with at least two vertices. Fix any orientation of its edges, let \(B\) be its signed vertex-by-edge incidence matrix, and let \(L=BB^{\mathsf T}\) be the combinatorial Laplacian. Then \(Q=B^{\mathsf T}L^{+}B\), where \(L^+\) is the Moore–Penrose inverse, and \(C=I-Q\). All norms are for operators on the full real edge-coordinate space equipped with its ordinary \(\ell_1\) or \(\ell_\infty\) norm; no assertion is made about optimality among nonorthogonal projectors. Changing edge orientation only conjugates the projectors by coordinate signs and changes none of their norms.

## Proof
**1. Exact complementary-column relation.** The projector \(Q\) is real symmetric and idempotent. For each coordinate edge \(e\), set \(r=Q_{ee}\). Standard electrical network identities give \(r=R_e\in(0,1]\). Since \(C=I-Q\), for all \(f\ne e\), \(C_{fe}=-Q_{fe}\), while \(C_{ee}=1-r\geq0\). Consequently,
\[
\|Q\mathbf e_e\|_1=r+\sum_{f\ne e}|Q_{fe}|,\qquad
\|C\mathbf e_e\|_1=1-r+\sum_{f\ne e}|Q_{fe}|.
\]
Subtracting establishes \(q_e-c_e=2R_e-1\) without any assumption of edge transitivity or regularity. Since induced \(\ell_1\) norms are maximum absolute column sums,
\[
\|Q\|_{1\to1}-\|C\|_{1\to1}
=\max_e q_e-\max_e c_e\geq\min_e(q_e-c_e)=2\min_eR_e-1.
\]
Both projectors are symmetric, so their induced \(\ell_\infty\) norms equal their induced \(\ell_1\) norms.

**2. Sharp degree-only resistance estimate.** Fix \(e=uv\), put \(p=\deg(u)\), \(q=\deg(v)\), and impose electrical potentials \(\phi(u)=1\), \(\phi(v)=0\). The Dirichlet principle states that the effective conductance \(R_e^{-1}\) is the minimum of \(\sum_{xy\in E(G)}(\phi(x)-\phi(y))^2\) among such functions. The trial function taking value \(1/2\) at every other vertex has energy exactly \(1+(p+q-2)/4=(p+q+2)/4\). Therefore
\[
R_e\geq\frac4{p+q+2}\geq\frac2{\Delta+1}.
\]
This proves both global inequalities. The first bound in this display, as well as the sharper degree-pair estimate below, also appears in De Loera–Eddy–Robertson–Samper, Theorem 3.9; it is used here, not asserted to be a new electrical result.

**3. Refined local bound and saturation.** If \(p+q>2\), use instead the trial potential taking the common value \(t\) on all vertices other than \(u,v\). Its energy is
\[
E(t)=1+(p-1)(1-t)^2+(q-1)t^2.
\]
Its minimum occurs at \(t=(p-1)/(p+q-2)\), giving \(E_{\min}=(pq-1)/(p+q-2)\). Hence
\[
R_e\geq\frac{p+q-2}{pq-1},\qquad
2R_e-1\geq\frac{1-(p-2)(q-2)}{pq-1}.
\]
For \(p,q\geq2\), equality in the resistance estimate is equivalent to this trial function being the genuine harmonic Dirichlet minimizer. At an exterior vertex \(w\), its Laplacian is
\[
(L\phi)(w)=\frac{-(q-1)\mathbf1_{w\sim u}+(p-1)\mathbf1_{w\sim v}}{p+q-2}.
\]
Harmonicity forces each exterior vertex to be adjacent to both or neither endpoints; because each endpoint has another neighbor, at least one common neighbor exists, and harmonicity there forces \(p=q\). Conversely, adjacent true twins with equal degree make the displayed Laplacian zero at every exterior vertex, so equality holds. When \(p=1\) or \(q=1\), the edge is a bridge, \(R_e=1\), and the refined bound is an equality; when \(p=q=1\), the entire graph is \(K_2\) and the exact column identity still holds. Finally, \((p-2)(q-2)\leq1\) makes every relevant column difference nonnegative and therefore makes the global norm difference nonnegative.

**4. Sharpness in each degree.** On \(K_{\Delta+1}\), every edge has resistance \(2/(\Delta+1)\), and edge transitivity makes the column sums constant. For its cut projector, a fixed edge column has diagonal absolute value \(2/(\Delta+1)\), value \(1/(\Delta+1)\) on each of the \(2(\Delta-1)\) incident other edges, and zero on disjoint edges. Therefore
\[
\|Q\|_{1\to1}=\frac{2\Delta}{\Delta+1},\qquad
\|C\|_{1\to1}=\frac{3(\Delta-1)}{\Delta+1},\qquad
\|Q\|-\|C\|=\frac{3-\Delta}{\Delta+1}.
\]
This includes \(\Delta=1\) (the single edge, for which \(C=0\)). All inequalities are attained as stated.

## Verification
The accompanying standalone `verify_degree_projection.py` implements rational Gaussian elimination on the reduced graph Laplacian, constructs the complete edge-projector matrix for connected sample graphs, and checks projector identities, exact column differences, both degree bounds, saturation at adjacent true twins, and sharpness on complete graphs. Its recorded successful execution tested 74 graph configurations and 635 edge columns, including complete graphs, cycles, trees, stars, book graphs, generalized Petersen graphs, and reproducibly seeded connected random graphs. These checks are finite sanity tests only; the universal claims follow from the Dirichlet and column-norm identities above.

To reproduce, execute `python3 verify_degree_projection.py` from the same directory. Python 3 standard library suffices.

## Relationship to prior work
Dilworth–Kutzarova–Ostrovskii (2023), *Cycle spaces: invariant projections and applications to transportation cost* (arXiv:2305.12582), supplies the relevant cycle/cut Banach-space framework and exact calculations for symmetric families. Its general framework and existing family formulas do not state the sharp maximum-degree comparison for arbitrary finite graphs.

De Loera–Eddy–Robertson–Samper (2025), *Discrete Curvatures and Convex Polytopes* (arXiv:2510.11894, Theorem 3.9), **already proves both displayed degree-only resistance lower bounds**. The present statement does not repackage those resistance estimates as original; it addresses a different graph-derived Banach-space invariant: the sharp difference between the operator norms of two complementary Hodge projections, including the universal subcubic threshold and an exact equality criterion for the refined column comparison. Standard effective-resistance/transfer-current identities are also not new.

## Limitations
The statement is for connected simple graphs with unit conductances and canonical Euclidean **orthogonal** projections; arbitrary conductances or minimum projection constants are not treated. Sharpness asserts that the lower bound is attained by complete graphs, not that these are the only global equality cases. The literature comparison did not establish absolute bibliographic uniqueness; equivalently phrased results in electrical-network or Banach-space literature remain possible. Independent review has not been performed.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, first posted 2023-05-21, https://arxiv.org/html/2305.12582v1 .
2. J. A. De Loera, J. Eddy, S. J. Robertson, J. A. Samper, *Discrete Curvatures and Convex Polytopes*, arXiv:2510.11894v1, Theorem 3.9, first posted 2025-10-13, https://arxiv.org/html/2510.11894v1 .
3. D. Cai, X. Chen, P. Peng, *Effective Resistances in Non-Expander Graphs*, arXiv:2307.01218, https://arxiv.org/abs/2307.01218 .
