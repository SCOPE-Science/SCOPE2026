# Sharp peripheral-link price threshold for resistance-optimal barbell networks

## Finding

For every integer \(m\ge2\), every conductance budget \(B>0\), and every peripheral-edge price \(t>0\), there is a **unique globally optimal conductance assignment** minimizing total pairwise effective resistance on two copies of \(K_{m+1}\) joined by a single bridge. Each clique has a distinguished bridge endpoint (hub). Hub--peripheral edges (spokes) and the bridge cost one unit per unit conductance; edges between two peripheral vertices within either clique cost \(t\) per unit conductance. Every allowed edge may independently receive any nonnegative conductance.

Write \(a\) for the conductance on every spoke, \(b\) for that on every peripheral--peripheral edge, and \(c\) for the bridge conductance. The optimum has precisely this symmetric form even when symmetry is not imposed on competitors. Define

\[
 t_c(m)=\frac{4(m+1)}{2m+1}=2+\frac2{2m+1},
 \qquad S_0(m)=(m+1)+2m\sqrt{2m+1}.
\]

**Lower-price regime, \(0<t<t_c(m)\).** Put

\[
 w=2m-t(m-1),\qquad v=t(m-1),
\]
\[
 S=(m+1)+\sqrt{2(m+2)w}+2(m-1)\sqrt{(m+1)t}.
\]

Then \(w>0\) and the globally optimal assignment is

\[
 a_*=\frac{B}{S}\sqrt{\frac{2(m+2)}{w}},\qquad
 u_*=\frac{2B}{S}\sqrt{\frac{m+1}{t}},
\]
\[
 b_*=\frac{u_*-a_*}{m}>0,\qquad
 c_*=\frac{B(m+1)}S,
 \qquad \boxed{K_*=\frac{S^2}{B}}.
\]

**At and above the threshold, \(t\ge t_c(m)\),** the unique optimal assignment instead has

\[
 \boxed{b_*=0},\quad
 a_*=\frac{B\sqrt{2m+1}}{S_0(m)},\quad
 c_*=\frac{B(m+1)}{S_0(m)},\quad
 \boxed{K_*=\frac{S_0(m)^2}{B}}.
\]

Thus an entire orbit of \(m(m-1)\) possible peripheral edges disappears **simultaneously** at an exact finite price. For any subsequent price increase, both the optimum conductance assignment and the minimum resistance stay fixed. For example, the threshold is \(12/5\) for two triangles joined by a bridge, and it decreases strictly toward \(2\) as \(m\) grows.

## Assumptions and scope

The underlying undirected simple graph contains \(N=2(m+1)\) labeled vertices and all edges in the two cliques plus their single hub-to-hub bridge. For every edge \(e\), select \(g_e\ge0\) and pay \(p_e g_e\), where \(p_e=t\) on peripheral--peripheral edges and \(p_e=1\) on all other edges. Require \(\sum_e p_e g_e=B\) and that the subgraph on positive-conductance edges is connected. A disconnected support has infinite objective. Effective resistance \(R_{ij}\) is defined by the weighted Laplacian pseudoinverse as \(R_{ij}=(e_i-e_j)^T L^+(e_i-e_j)\). The objective is the **unordered-pair Kirchhoff index** \(K=\sum_{i<j}R_{ij}\), with no arbitrary normalization. The result does not concern the fastest discrete-time mixing eigenvalue modulus or maximal/minimal individual-pair resistance.

## Proof

**1. Global symmetry and uniqueness.** Write \(J=\mathbf1\mathbf1^T/N\). On every connected positive-conductance support, \(X=L+J\) is positive definite and

\[
 K=N\operatorname{tr}(X^{-1})-N.
\]

The map \(X\mapsto\operatorname{tr}(X^{-1})\) is strictly convex on positive-definite matrices; along any nonzero symmetric direction \(H\), its second derivative is \(2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0\). For a simple graph, different conductance vectors produce different Laplacians (the off-diagonal entries recover individual conductances). Therefore \(K\) is strictly convex on connected feasible allocations. Averaging any allocation under independent permutations of the \(m\) peripheral vertices of each clique and interchange of the two cliques preserves budget and connectivity, and cannot increase \(K\). Strict convexity then shows that the unique unrestricted optimum is invariant, with the three weights \(a,b,c\). All optimum weights displayed above give connected supports, so existence also follows from their feasibility and the global lower bound below.

**2. Exact effective-resistance reduction.** Set \(u=a+mb\). For one weighted clique, the resistance from its hub to each peripheral vertex is \((a+b)/(au)\), and between distinct peripheral vertices it is \(2/u\); this follows by diagonalizing the peripheral difference subspace, or by inverting the grounded clique Laplacian \(uI-b\mathbf1\mathbf1^T\). Consequently the within-clique resistance sum is \(1/a+(m+1)(m-1)/u\), and the sum of its hub-to-peripheral resistances is \(1/a+(m-1)/u\). Every resistance between opposite cliques is the sum of its two within-clique hub resistances and \(1/c\), because the bridge is a cut edge. Hence

\[
 \boxed{K(a,b,c)=\frac{(m+1)^2}{c}
 +\frac{2(m+2)}a+\frac{4(m+1)(m-1)}{a+mb}}.
\]

The budget is \(2ma+t\,m(m-1)b+c=B\). Here \(a,c>0\) and \(b\ge0\); the objective would diverge if either \(a\) or \(c\) vanished.

**3. Interior solution and its feasibility.** Let \(A=(m+1)^2\), \(C=2(m+2)\), and \(D=4(m+1)(m-1)\). Substitute \(u=a+mb\) to obtain

\[
 K=\frac A c+\frac C a+\frac D u,
 \quad wa+vu+c=B,\quad u\ge a>0,
\]

where \(w=2m-t(m-1)\), \(v=t(m-1)\). For \(0<t<t_c(m)\) we have \(w,v>0\). The three-term Cauchy--Schwarz inequality gives

\[
 K B\ge \big(\sqrt A+\sqrt{Cw}+\sqrt{Dv}\big)^2=S^2,
\]

with equality precisely when

\[
 (a,u,c)=\frac B S
 \left(\sqrt{C/w},\sqrt{D/v},\sqrt A\right).
\]

The condition \(u\ge a\) holds exactly when

\[
 \frac{D}{v}\ge\frac Cw
 \quad\Longleftrightarrow\quad t\le \frac{4(m+1)}{2m+1}.
\]

It is strict below the threshold, proving the first branch globally and its strict use of peripheral edges. At equality the same formula gives \(u=a\) and coincides with the boundary branch.

**4. Boundary solution and global KKT certificate.** On \(b=0\), the exact objective and budget reduce to

\[
 K=\frac A c+\frac{2m(2m+1)}a,\qquad 2ma+c=B.
\]

Cauchy--Schwarz gives the stated unique boundary optimum and value \(S_0^2/B\). It is also globally optimal over \(b\ge0\) whenever \(t\ge t_c\): at the boundary optimum put \(\Lambda=A/c_*^2=(2m+1)/a_*^2\). Then the Lagrangian gradients for the two strictly positive coordinates vanish, while the one-sided derivative on the forbidden \(b<0\) side obeys

\[
 \left.\frac{\partial K}{\partial b}\right|_{b=0}
 +\Lambda\,t m(m-1)
 =\frac{m(m-1)}{a_*^2}
 \big((2m+1)t-4(m+1)\big)\ge0.
\]

These are sufficient KKT conditions by convexity on the positive-definite Laplacian domain; strict convexity proves unrestricted uniqueness, including exactly at equality. Conversely this derivative is negative below the threshold, so the boundary allocation cannot be optimal there. This completes all parameters and all boundary cases.

## Verification

Run the bundled `verify.py` with Python and SymPy. It reconstructs weighted Laplacians and computes \(N\operatorname{tr}[(L+J)^{-1}-J]\) exactly for four small clique sizes with positive or zero peripheral-edge weights, independently checking the resistance formula. Further exact radical/rational checks verify budget equality, optimal values, stationarity, complementary-slackness inequality, and agreement of the branches at their boundary over a finite grid of sizes and costs. These are corroborating tests; the universal proof is the analytic derivation in the preceding section.

## Relationship to prior work

Ghosh, Boyd and Saberi introduced the total-effective-resistance minimization framework and explicitly solved the **equal-unit-price** balanced barbell problem. Their 2006 proceedings article, Section V, equation (33), and longer 2008 paper, equation (39), give a three-weight spectral reduction and an optimum at the fixed price \(t=1\). The present result instead analyzes a **variable nonhub-edge price** for every \(t>0\), classifies exactly when the optimal topology drops those edges, proves global unrestricted uniqueness throughout that phase change, and gives complete cost and conductance formulas. The original case \(t=1\) is included as a previously known special case and is not claimed as new.

Johnson and Chertkov analyzed more general power-network design with linear and nonconvex line costs; their model and algorithms do not explicitly establish this all-size barbell price threshold in the inspected material. More recent general resource-allocation and augmentation studies likewise motivate cost-dependent sparsification but are not identified as containing this exact closed-form theorem. A general convex algorithm that could numerically evaluate each instance is not equivalent to an explicit all-parameter classification.

## Limitations

The result assumes identical clique sizes, an identical price on all peripheral--peripheral edges, unit prices on spokes and bridge, and a linear conductance budget. It does not classify unequal-clique cases or nonuniform within-orbit prices. Since the primary equal-price barbell result is explicit, the variable-price extension must be understood as a sharp sensitivity/support theorem, not a claim to have discovered the underlying graph or the original resistance decomposition. Although relevant sources were compared, unindexed specialized literature or implicit consequences not recognized in those sources remain possible. The verification script performs finite checks and is not a proof for arbitrary \(m\).

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, 2006, pp. 1185--1196, Section V. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1), 37--66 (2008), Section 5; doi:10.1137/050645452. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. J. K. Johnson and M. Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks* (2010), arXiv:1004.2285. https://arxiv.org/abs/1004.2285
4. H. Tovar et al., *Cost convexity controls the architecture of resistance-optimal networks* (2026), arXiv:2610.03627. https://arxiv.org/abs/2610.03627
