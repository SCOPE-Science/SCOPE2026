# Sharp degree-controlled spoke deletion in determinant-optimal tree cones

## Finding
Let \(T=(V,E)\) be any finite simple tree on \(n\ge3\) vertices, and let \(G=K_1\vee T\) be its cone: a new hub \(o\) is joined to each vertex of \(T\). Let \(d_v\) be the degree of \(v\) in \(T\), and let \(\Delta=\max_v d_v\). Allocate independent nonnegative conductances \(a_v\) to the hub spokes and \(x_e\) to the tree edges. With budget \(B>0\) and relative cost \(t>0\), require
\[
 \sum_{v\in V}a_v+t\sum_{e\in E}x_e=B.
\]
Maximize the weighted spanning-tree enumerator \(\mathscr T_G(a,x)=\sum_{S\text{ spanning tree of }G}\prod_{e\in S}w_e\), with the product using these conductances. The maximizer is unique over **all** individual asymmetric assignments.

Define the degree threshold
\[
 t_0(T)=\begin{cases}0,&\Delta\le2,\\[2pt]
 \dfrac{2(\Delta-2)}{\Delta-1},&\Delta\ge3.
 \end{cases}
\]
For \(t_0(T)\le t\le2\), put \(\rho=1-t/2\). The unique maximizer is
\[
 \boxed{a_v^*=\frac Bn\frac{1-(d_v-1)\rho}{1+\rho},\qquad
 x_e^*=\frac Bn\frac{\rho}{1-\rho^2}\quad(e\in E).}
\]
Here \(t>0\), so \(0\le\rho<1\) throughout the stated interval. For \(t\ge2\), the unique maximizer is \(a_v^*=B/n\) for every spoke and \(x_e^*=0\) for every tree edge. In the explicitly solved range,
\[
 \boxed{\mathscr T_{G,\max}=\begin{cases}
 (B/n)^n\bigl[t(4-t)/4\bigr]^{-(n-1)},&t_0(T)\le t\le2,\\[3pt]
 (B/n)^n,&t\ge2.
 \end{cases}}
\]
The optimum value in this range is **independent of the shape of \(T\)**: it depends only on \(n\), \(B\), and \(t\).

The spoke-support threshold is sharp **over the entire domain \(t>0\)**: the unique optimizer has positive conductance on every spoke if and only if \(t>t_0(T)\). At \(t=t_0(T)>0\), exactly the spokes at vertices of degree \(\Delta\) vanish; at \(0<t<t_0(T)\), at least one spoke vanishes (the remaining optimal weights are not classified here). For all \(t_0(T)\le t<2\), every tree edge is strictly positive; at \(t\ge2\), every tree edge vanishes. In particular, when \(T\) is a path, the explicit formulas and optimal value hold for every \(t>0\).

## Assumptions and scope
The tree is finite, connected, simple and unweighted as a *support graph*; its edge conductances are decision variables. The hub-spoke cost is one per unit conductance and the cost of each tree-edge conductance is \(t\). Conductances are continuous, nonnegative and may be chosen independently. The zero-weight convention allows an edge to be present in the support graph but unused in the weighted network. There are no upper bounds or integrality constraints on conductances. The objective counts weighted spanning trees, not minimum spanning trees and not the sum of effective resistances. All statements concern the reduced *unnormalized* weighted graph Laplacian with the hub grounded.

## Proof
**1. Strictly concave determinant design.** Ground the hub. If \(b_{uv}=e_u-e_v\), the reduced Laplacian is
\[
 M(a,x)=\operatorname{Diag}(a_v)+\sum_{\{u,v\}\in E}x_{uv}b_{uv}b_{uv}^{\mathsf T}.
\]
By the weighted matrix-tree theorem, \(\mathscr T_G(a,x)=\det M(a,x)\). The feasible budget simplex is compact and contains positive-definite designs (uniform positive spokes). Hence a positive-determinant optimum exists. On the positive-definite locus, \(\log\det M\) is strictly concave in the edge weights: distinct tree-edge weights are read from the off-diagonal entries \(M_{uv}=-x_{uv}\), and then distinct spokes are read from the diagonals. Thus the affine map from all available edge weights to \(M\) is injective. The maximizer is unique.

For \(\Sigma=M^{-1}\), the partial derivatives of \(\log\det M\) are
\[
 \frac{\partial\log\det M}{\partial a_v}=\Sigma_{vv},\qquad
 \frac{\partial\log\det M}{\partial x_{uv}}
 =\Sigma_{uu}+\Sigma_{vv}-2\Sigma_{uv}.
\]
At any optimum the budget multiplier is \(\lambda=n/B\): multiplying the first-order conditions for positive variables by their weights and summing uses \(\sum_e w_e\partial\log\det M/\partial w_e=\operatorname{tr}(M^{-1}M)=n\) and the budget equality. Therefore global optimality is equivalent to derivative \(\lambda\) for every positive spoke, at most \(\lambda\) for a zero spoke, and derivative \(t\lambda\) for every positive tree edge, at most \(t\lambda\) for a zero tree edge. These are the usual sufficiency conditions for a concave differentiable objective.

**2. Tree correlation lemma.** For \(0\le\rho<1\), define the \(n\)-by-\(n\) matrix
\[
 C_\rho(u,v)=\rho^{\operatorname{dist}_T(u,v)},\qquad \rho^0=1.
\]
Choose any root of \(T\). Let \(X_{\rm root}\) have unit variance, and for each child \(v\) of \(u\) set \(X_v=\rho X_u+\sqrt{1-\rho^2}\,\varepsilon_v\), with independent standard normal innovations. This constructs the covariance \(C_\rho\), proves positive definiteness, and gives
\[
 \det C_\rho=(1-\rho^2)^{n-1}.
\]
The joint Gaussian negative log-density is the root square plus \(\sum_{u\to v}(X_v-\rho X_u)^2/(1-\rho^2)\). Expanding the quadratic gives
\[
 (C_\rho^{-1})_{uv}=\begin{cases}
 \dfrac{1+(d_v-1)\rho^2}{1-\rho^2},&u=v,\\[5pt]
 -\dfrac{\rho}{1-\rho^2},&\{u,v\}\in E,\\[5pt]
 0,&\text{otherwise.}
 \end{cases}
\]
(The diagonal expression uses \(d_v\), so the cases are disjoint.)

**3. Candidate, feasibility and first-order sufficiency.** Set \(\rho=1-t/2\) and \(M_*=(B/n)C_\rho^{-1}\). Comparing its off-diagonal entries with those of the grounded Laplacian forces
\[
 x_e^*=(B/n)\rho/(1-\rho^2),
\]
and then comparing diagonals yields
\[
 a_v^*=(B/n)\frac{1-(d_v-1)\rho}{1+\rho}.
\]
Since \(\sum_v d_v=2(n-1)\) and \(t=2(1-\rho)\), direct substitution yields the exact budget \(\sum a_v^*+t\sum x_e^*=B\). The spokes are nonnegative precisely when \(\rho\le1/(\Delta-1)\) for \(\Delta\ge3\); for \(\Delta\le2\) they are positive for every \(0\le\rho<1\). This is exactly \(t\ge t_0(T)\).

At the candidate \(\Sigma_*=(n/B)C_\rho\), every spoke derivative is \(n/B\), and every tree-edge derivative is \((2n/B)(1-\rho)=tn/B\). Therefore all positive/zero edge first-order inequalities hold, even when maximal-degree spokes vanish at the lower boundary. Strict concavity proves unique global optimality. The determinant identity follows from the preceding formula for \(\det C_\rho\). For \(t\ge2\), the star-only design has \(M_*=(B/n)I\): spoke derivatives equal \(n/B\), and every unused tree-edge derivative is \(2n/B\le tn/B\). This proves the high-cost branch.

**4. Necessity of vanishing spokes below the threshold.** Suppose \(\Delta\ge3\), \(0<t<t_0(T)<2\), and an optimal design had every spoke strictly positive. Then each diagonal of its inverse \(\Sigma\) would equal \(n/B\). If some tree edge \(\{u,v\}\) had zero weight, removing that edge would partition the tree support and make the grounded Laplacian block diagonal. Consequently \(\Sigma_{uv}=0\), so its unused-edge derivative would be \(2n/B>tn/B\), contradicting optimality. Hence every tree edge is positive.

The KKT equalities then force \(\Sigma_{uv}=(n/B)(1-t/2)\) along every tree edge. Because \(M=\Sigma^{-1}\) has no off-diagonal entries outside the tree edges, its centered Gaussian law is Markov on \(T\): for three vertices where \(v\) separates \(u\) and \(w\), conditional independence gives \(\Sigma_{uw}=\Sigma_{uv}\Sigma_{vw}/\Sigma_{vv}\). Iterating this identity along paths shows \(\Sigma=(n/B)C_\rho\), \(\rho=1-t/2\). Step 2 then forces a spoke at any vertex of degree \(\Delta\) to be
\[
 a_v=(B/n)\frac{1-(\Delta-1)\rho}{1+\rho}<0,
\]
a contradiction. Thus at least one spoke must vanish. At \(t=t_0(T)>0\) the explicit candidate has exactly the maximum-degree spokes zero; at larger costs its spokes are strictly positive. This establishes the sharp spoke-support classification.

## Verification
A standalone script checks the tree covariance inverse, exact budget, derivative conditions, and closed-form determinant on paths, stars, and randomly generated trees. It also compares many randomly chosen feasible allocations against the explicit optimum and checks selected instances using exact rational arithmetic. The recorded execution reports 836 candidate matrix/budget/KKT/determinant checks, 3,344 feasible competitor comparisons, nine exact-rational identities, and 232 infeasible continuations below the explicit regime. Execute `python verify.py` with Python 3, NumPy, and SymPy. The mathematical proof above is independent of finite tests.

## Relationship to prior work
The weighted matrix-tree theorem and general log-determinant optimal-design viewpoint are classical. Khosoussi, Sukhatme, Huang and Dissanayake (arXiv:1604.01116, first posted 2016-04-05) develop general spanning-tree network-design algorithms and determinant relaxations, not this tree-cone allocation with a priced internal tree, its sharp degree threshold, or its shape-independent optimized determinant. Malioutov, Johnson and Willsky (JMLR 7, 2006) analyze Gaussian graphical models and belief propagation on trees; the Gaussian Markov covariance mechanism used above belongs to that established theory, but their objective is inference, not budgeted weighted spanning-tree maximization. Cheng (1981) studies maximizing numbers of spanning trees under fixed vertex/edge-count constraints and design-theoretic connections rather than independently priced edge conductances; only bibliographic descriptions, not complete text, were available for this comparison. An earlier exact design for a direct edge and several internally disjoint terminal paths covers genuine subcases: when \(T\) itself is a star and all edge costs are one, its cone is such a theta network; likewise the three-vertex path cone has that form. That earlier classification does not determine the arbitrary-tree degree threshold, arbitrary relative tree-edge price, full high-price weight formulas, or the tree-shape-independent maximum. These already-covered special cases are not presented as independent novelty. The originality claim is restricted to the combined, exact design and support theorem above, not the determinant concavity or Gaussian-tree ingredients.

## Limitations
For \(0<t<t_0(T)\) with \(\Delta\ge3\), only the necessity of at least one zero spoke is proved; the complete optimal conductance vector and determinant are not claimed there. This is a deterministic continuous-weight design problem, not a probabilistic failure model, a constrained edge-count selection problem, or a statement about arbitrary non-tree internal graphs. Finite checks do not establish the infinite-family result. A specialized historical source could have treated the same exact priced tree-cone design without appearing in the inspected literature; independent mathematical validation has not been performed.

## References
1. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, arXiv:1604.01116, first posted 2016-04-05. https://arxiv.org/abs/1604.01116
2. D. M. Malioutov, J. K. Johnson, and A. S. Willsky, *Walk-Sums and Belief Propagation in Gaussian Graphical Models*, Journal of Machine Learning Research 7 (2006), 2031–2064. https://jmlr.org/papers/volume7/malioutov06a/malioutov06a.pdf
3. C.-S. Cheng, *Maximizing the Total Number of Spanning Trees in a Graph: Two Related Problems in Graph Theory and Optimum Design Theory*, Journal of Combinatorial Theory, Series B 31 (1981), 240–248, DOI:10.1016/S0095-8956(81)80028-7 (bibliographic/abstract comparison only).
