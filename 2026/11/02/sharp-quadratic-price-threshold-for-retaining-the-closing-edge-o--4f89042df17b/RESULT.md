# Sharp quadratic price threshold for retaining the closing edge of an optimally weighted cycle

## Finding

Let \(n\ge3\) be an integer. Consider the undirected cycle with vertices \(1,\ldots,n\), ordinary edges \(e_k=\{k,k+1\}\) for \(1\le k<n\), and the distinguished closing edge \(e_0=\{n,1\}\). Choose a nonnegative conductance independently on every edge. The ordinary edges have unit conductance price; the closing edge has relative price \(r>0\); and the total budget is \(B>0\). Among connected conductance allocations satisfying
\[
\sum_{k=1}^{n-1}w_k+r w_0\le B,
\]
minimize the Kirchhoff index \(\mathcal K(w)=\sum_{1\le u<v\le n}R_{uv}(w)\), the sum of all unordered-pair effective resistances.

Put
\[
a_k=\frac{1}{\sqrt{k(n-k)}},\quad
S_n=\sum_{k=1}^{n-1}\sqrt{k(n-k)},\quad
T_j=\sum_{k=1}^{j-1}a_k,\quad
\overline T=\frac1n\sum_{j=1}^nT_j.
\]
The **exact critical relative price** is
\[
\boxed{r_c(n)=n\sum_{j=1}^{n}(T_j-\overline T)^2.}
\]
The unique globally optimal allocation has **every ordinary edge strictly positive for every \(r>0\)**. Its closing edge is deleted exactly when \(r\ge r_c(n)\). Thus for \(0<r<r_c(n)\), all \(n\) cycle edges are strictly positive; for \(r\ge r_c(n)\), exactly the closing edge has zero conductance. In the latter regime the entire optimizer and optimum are
\[
\boxed{w_0^*=0,\qquad w_k^*=\frac{B\sqrt{k(n-k)}}{S_n}\quad(1\le k<n),\qquad \mathcal K_*=\frac{S_n^2}{B}.}
\]
At the transition equality \(r=r_c(n)\), deletion remains uniquely optimal. At smaller prices the unique all-positive optimizer is characterized as the minimizer of the original strictly convex finite-dimensional objective; no closed form for its individual conductances is claimed.

The critical price grows **quadratically** with the cycle size:
\[
\boxed{\lim_{n\to\infty}\frac{r_c(n)}{n^2}=\frac{\pi^2}{4}-2\approx0.4674011002723395.}
\]
In particular \(r_c(3)=3\), and \(r_c(4)=11/3+4/\sqrt3\).

## Assumptions and scope

The graph is a simple undirected cycle, including the triangle when \(n=3\). Conductances are allowed to vanish provided the resulting graph remains connected; disconnected allocations have infinite objective. Every ordinary edge costs one unit per conductance, the single distinguished edge costs \(r>0\) units, and no individual conductance upper bound is imposed. Effective resistances are computed using the weighted combinatorial Laplacian (not a degree-normalized Laplacian). The comparison is over all individually selected conductances, not just reflection-symmetric proposals. The constant \(B>0\) scales the optimum but does not change the critical price.

## Proof

**1. Existence, strict convexity, and symmetry.** For a connected allocation let \(L=\sum_e w_e b_e b_e^{\mathsf T}\), where \(b_e\) is an oriented edge incidence vector, let \(J=\mathbf1\mathbf1^{\mathsf T}\), and set \(Q=L+J/n\). Then \(Q\) is positive definite and
\[
\mathcal K=n\,\mathrm{tr}(Q^{-1})-n,\qquad
\frac{\partial\mathcal K}{\partial w_e}=-n\|Q^{-1}b_e\|_2^2.
\]
For a nonzero real perturbation \(h\), put \(H=\sum_eh_e b_e b_e^{\mathsf T}\). Because the graph is simple, its distinct off-diagonal entries force \(H\ne0\). The second directional derivative is
\[
2n\,\mathrm{tr}(Q^{-1}H Q^{-1}H Q^{-1})>0.
\]
Thus the objective is strictly convex on the connected positive-semidefinite domain. The feasible budget simplex is compact and approaching disconnection makes the objective diverge; a minimizer exists, is unique, and spends the full budget by positive homogeneity. Reflection fixing \(e_0\) preserves costs and the objective, so uniqueness implies \(w_k=w_{n-k}\) for all ordinary edges.

**2. Every ordinary edge is active.** If \(w_k=0\) for an ordinary edge not fixed by reflection, its distinct mirror edge is also zero. This disconnects a simple cycle, a contradiction. An ordinary edge fixed by the reflection exists only for even \(n\): the edge opposite \(e_0\). Suppose this edge were zero. The other \(n-1\) edges then form a path, whose two terminal edges both have price one. Enumerate the path edges in order, with positive prices \(d_i\), \(1\le i<n\), and let \(b_i=i(n-i)\) and \(S=\sum_i\sqrt{b_i d_i}\). Every connected feasible allocation on this path has Kirchhoff index \(\sum_i b_i/w_i\). By Cauchy–Schwarz, the unique path optimum has
\[
w_i=\frac{B\sqrt{b_i/d_i}}{S},\qquad \mathcal K=\frac{S^2}{B},\qquad
-\frac{\partial\mathcal K}{\partial w_i}=\frac{S^2}{B^2}d_i.
\]
Set \(a_i'=\sqrt{d_i/b_i}\), \(U_j=\sum_{i<j}a_i'\), and \(\overline U=n^{-1}\sum_j U_j\). The centered electrical potential produced by a unit current between the two missing-edge endpoints equals, up to sign, \((S/B)(U_j-\overline U)\). Consequently the ratio of the benefit from adding the missing edge to the path's budget multiplier \(\mu=S^2/B^2\) is
\[
\frac{-\partial\mathcal K/\partial w_{\mathrm{missing}}}{\mu}
=n\sum_{j=1}^n(U_j-\overline U)^2.
\]
The two terminal path edges have \(d_1=d_{n-1}=1\), and hence
\[
U_n-U_1=\sum_{i=1}^{n-1}\sqrt{d_i/b_i}\ge\frac{2}{\sqrt{n-1}}.
\]
For any real \(U_1,\ldots,U_n\), the sum of squared deviations from their mean is at least \((U_n-U_1)^2/2\). Therefore
\[
\frac{-\partial\mathcal K/\partial w_{\mathrm{missing}}}{\mu}
\ge\frac{2n}{n-1}>1.
\]
But the missing ordinary edge has unit price, and its nonnegative-boundary first-order optimality condition would require that ratio to be at most one. This contradiction proves every ordinary edge has positive conductance at the global optimum.

**3. The closing-edge transition.** Restrict temporarily to allocations with \(w_0=0\), when all ordinary edges must remain positive. The path calculation with \(d_i=1\) gives the sole optimum on that face:
\[
w_k^P=B\sqrt{k(n-k)}/S_n,\qquad \mathcal K_P=S_n^2/B.
\]
Its budget multiplier is \(\mu=S_n^2/B^2\). Applying the same centered-potential calculation to the omitted closing edge, whose endpoints are the path endpoints, gives
\[
-\left.\frac{\partial\mathcal K}{\partial w_0}\right|_{w^P}
=\mu\, n\sum_{j=1}^n(T_j-\overline T)^2=\mu r_c(n).
\]
The Karush–Kuhn–Tucker condition for this zero edge is precisely \(-\partial\mathcal K/\partial w_0\le\mu r\), equivalently \(r\ge r_c(n)\). Since the problem is convex, this condition and the active-edge equalities are sufficient for global optimality; strict convexity makes it unique. For \(r<r_c(n)\), a feasible perturbation allocating a small positive conductance to the closing edge, compensated by reducing ordinary conductances proportionally, has negative first derivative \(\mu(r-r_c(n))\). The path-face optimizer is therefore not globally optimal. By step 2 every ordinary edge is active, and since the only closing-zero candidate has been excluded, the unique optimum has all edges active. This proves the exact support classification, including equality.

**4. Quadratic large-cycle scaling.** The symmetry \(a_k=a_{n-k}\) gives \(\overline T=\tfrac12\sum_{k=1}^{n-1}a_k\). Write \(f(x)=[x(1-x)]^{-1/2}\). The cumulative sums \(T_j=n^{-1}\sum_{k<j}f(k/n)\) converge uniformly in \(j\) to \(g((j-1)/n)\), where \(g(x)=\int_0^x f(t)\,dt=2\arcsin\sqrt x\). To justify uniformity despite the endpoint singularities, split the sum into \([0,\varepsilon]\), \([\varepsilon,1-\varepsilon]\), and \([1-\varepsilon,1]\): both endpoint tails are bounded uniformly by a constant times \(\sqrt\varepsilon\), while ordinary Riemann-sum convergence is uniform on the central interval. Hence
\[
\lim_{n\to\infty}\frac{r_c(n)}{n^2}
=\int_0^1\left(g(x)-\frac{\pi}{2}\right)^2dx
=\frac12\int_0^{\pi}(t-\pi/2)^2\sin t\,dt
=\frac{\pi^2}{4}-2.
\]

## Verification

The standalone script `verify_cycle.py` requires Python 3, NumPy, SciPy, and SymPy and can be run as `python verify_cycle.py`. It verifies the exact small-order expressions symbolically, compares pseudoinverse derivatives with the stated critical-price formula, independently recomputes pairwise effective resistances using series/parallel arc reduction, and compares selected full-dimensional numerical solutions on both sides of the transition. The output of an actual run is in `VERIFICATION_OUTPUT.txt`. Numerical optimizations and finite checks corroborate, but cannot establish, the all-size strict-convexity and support arguments or the asymptotic result.

## Relationship to prior work

Ghosh, Boyd, and Saberi (2006 conference version; 2008 journal version) establish convex optimization of total effective resistance, general edgewise optimality conditions, and the square-root edge allocation for trees. These are used explicitly as methodological starting points. Their inspected treatment gives uniform-price cycles by symmetry and discusses weighted trees and barbell examples, but does not give a heterogeneous single-price cycle support classification, the proof that no ordinary edge can be deleted, or the size-dependent sharp threshold with a quadratic scaling constant. The present statement is a specialization of the general problem but requires a coupled deletion-face and endpoint-voltage calculation plus a separate all-support proof; it is not presented as a new general convexity or KKT theorem.

Bhoite, Dhuli, Werner, and Kansanen (2026) analyze cost-aware graph augmentation of an existing weighted network using selection variables and semidefinite relaxations. Their cost-normalized marginal-benefit criterion overlaps the general first-order machinery but not the particular freely reallocated cycle model or its analytic global support boundary. Existing unicyclic D-optimal design concerns a determinant objective, not the Kirchhoff-index objective here. Literature search cannot rule out an equivalent specialized earlier derivation.

## Limitations

The interior \(0<r<r_c(n)\) conductances are proved uniquely positive but are not expressed in closed form. The result presumes one distinguished edge price and otherwise uniform prices; it does not classify arbitrary cost vectors, multiple exceptional edges, different objectives, or disconnected candidates. The asymptotic is a limit without a claimed finite-size error bound. Novelty is a best-knowledge scientific comparison rather than proof of publication priority, and the work has not undergone independent mathematical validation.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, Kyoto, Japan, July 24–28, 2006; open conference copy: https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf.
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1), 37–66 (2008), doi:10.1137/050645452; full author-hosted text: https://www.arpitaghosh.com/papers/eff_res.pdf.
3. O. Bhoite, V. S. Dhuli, S. Werner, and K. Kansanen, *Budget-Constrained Graph Augmentation for Robust Network Design via Kirchhoff Index Minimization*, arXiv:2609.29790 (2026), https://arxiv.org/html/2609.29790v1.
4. H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107(2), 330–339 (2007), doi:10.1002/qua.21068 (published online September 5, 2006).
