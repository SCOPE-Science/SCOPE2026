# Exact heterogeneous conductance allocation for bouquets of four-cycles

## Finding
Fix an integer \(k\ge2\). Form \(k\) four-cycles that share exactly one vertex \(o\), and otherwise have pairwise disjoint vertices and edges. Denote cycle \(j\) by \(o-a_j-b_j-c_j-o\). Each edge conductance is independently selectable and nonnegative. The two edges incident to \(o\) in cycle \(j\) have unit-conductance price \(P_j>0\); the two other edges have price \(Q_j>0\). Let the total price-weighted conductance budget be \(B>0\), and assign infinite objective to disconnected networks. The objective is the unordered-pair Kirchhoff index \(\mathcal K=\sum_{x<y}R_{xy}\).

Put \(E=3k-2\). For every \(j\), let \(t_j\) be the **unique positive real root** of
\[
H_j(t)=(E+2)P_jt^4+2(E+2)P_jt^3+
\bigl((3E+8)P_j-(5E+6)Q_j\bigr)t^2
-6EQ_jt-3EQ_j.
\]
Define
\[
C_j=\frac{(P_jt_j+Q_j)\bigl((E+2)t_j^2+(6E+8)t_j+3E\bigr)}{t_j(t_j+1)},
\qquad Z=\sum_{j=1}^k\sqrt{C_j}.
\]
Then the **unique global minimizer among all independently selectable edge conductances** has in cycle \(j\) the two hub-incident conductances equal to
\[
u_j^*=\frac{B\sqrt{C_j}}{2Z(P_j+Q_j/t_j)},
\]
and the other two conductances equal to \(v_j^*=u_j^*/t_j\). Its optimum is exactly
\[
\boxed{\mathcal K_*=\frac{Z^2}{B}.}
\]
Every one of the \(4k\) optimal conductances is strictly positive for every finite positive choice of prices; no edge is dropped at a price threshold. The budget spent on cycle \(j\) is \(B\sqrt{C_j}/Z\).

In particular, if the two price classes coincide in each cycle, \(P_j=Q_j\), then **all cycles have the same optimal shape**
\[
\boxed{\frac{u_j^*}{v_j^*}=\sqrt{\frac{3(3k-2)}{3k}}},
\]
regardless of how the common price differs between cycles. This ratio equals \(\sqrt2\) for two cycles and tends to \(\sqrt3\) as their number grows.

## Assumptions and scope
The graph is the one-vertex union of exactly \(k\) simple four-cycles. The hub is shared, but no other vertices or edges are. All \(P_j,Q_j,B\) are positive real numbers. Edge conductances may be independently varied, including zero when the remaining graph is connected. Every edge has precisely its specified linear price, with no upper caps. The Kirchhoff index uses ordinary (not normalized) electrical effective resistance. The result concerns a continuous, static budget allocation; it does not assert an optimal dynamic control policy, arbitrary cycle lengths, or unrelated spectral objectives.

## Proof
Let \(N=3k+1\). On any connected weighted graph, the Kirchhoff index equals \(N\operatorname{tr}(L^\dagger)\), where \(L\) is the weighted Laplacian. On the space orthogonal to constants, \(L\) is positive definite. The inverse-trace functional is strictly convex in its positive-definite argument: in any nonzero symmetric direction \(D\), its second derivative is
\[
2\operatorname{tr}\bigl(L^{-1}DL^{-1}DL^{-1}\bigr)>0.
\]
Here inverses and directions are restricted to that orthogonal space. The inequality follows by writing the trace as \(2\operatorname{tr}(S^2L^{-1})\), with \(S=L^{-1/2}DL^{-1/2}\ne0\). Distinct edge-conductance vectors give distinct Laplacians, because the off-diagonal matrix entries recover individual simple-edge weights. Consequently the objective is strictly convex on the connected feasible set. The price-budget simplex is compact; approaching any disconnected allocation makes at least one positive Laplacian eigenvalue tend to zero and the index diverge. Thus an optimum exists and is unique.

Reflection of each four-cycle fixing the hub preserves both the objective and that cycle's two price classes. Uniqueness forces the two hub-adjacent edge rates to coincide, say \(u_j\), and the other two rates to coincide, say \(v_j\). If either were zero, the reflected graph would be disconnected: two missing hub edges isolate the cycle, while two missing distal edges isolate \(b_j\). Hence \(u_j,v_j>0\). This symmetry argument is valid in the unrestricted edge optimization.

For one such cycle, write \(x=1/u\) and \(y=1/v\). Series-parallel reduction yields
\[
R_{oa}=R_{oc}=\frac{x(x+2y)}{2(x+y)},\qquad
R_{ob}=\frac{x+y}{2},
\]
\[
R_{ab}=R_{bc}=\frac{y(2x+y)}{2(x+y)},\qquad
R_{ac}=\frac{2xy}{x+y}.
\]
Therefore the sum of effective resistances among the three nonhub vertices is \(y(4x+y)/(x+y)\), and their sum of resistances to the hub is \(x(x+2y)/(x+y)+(x+y)/2\).

An articulation-point resistance identity gives \(R_{z,z'}=R_{z,o}+R_{o,z'}\) whenever \(z,z'\) are in distinct petals. Each nonhub vertex is paired with the hub and the \(3(k-1)\) vertices of other petals, so its hub resistance occurs with coefficient \(E=1+3(k-1)\). Accordingly,
\[
\mathcal K=\sum_{j=1}^k
\left[\frac{y_j(4x_j+y_j)}{x_j+y_j}
+E\left(\frac{x_j(x_j+2y_j)}{x_j+y_j}+\frac{x_j+y_j}{2}\right)\right].
\]
For cycle \(j\), let its spent budget be \(b_j=2P_ju_j+2Q_jv_j>0\), and set \(t_j=y_j/x_j=u_j/v_j>0\). Substitution gives the exact separation
\[
\mathcal K=\sum_j\frac{C_j(t_j)}{b_j},\qquad
C_j(t)=\frac{(P_jt+Q_j)\bigl((E+2)t^2+(6E+8)t+3E\bigr)}{t(t+1)}.
\]
The derivative is
\[
C_j'(t)=\frac{H_j(t)}{t^2(t+1)^2}.
\]
The coefficients of \(H_j\) in descending powers have signs \(+,+,\pm,-,-\), with the middle coefficient permitted to vanish, hence exactly one sign change. Descartes' sign rule bounds its number of positive roots by one, counted with multiplicity. Since \(H_j(0)=-3EQ_j<0\) and \(H_j(t)\to+\infty\) as \(t\to\infty\), it has exactly one positive, simple root. Also \(C_j(t)\to\infty\) at both endpoints \(t\downarrow0\) and \(t\to\infty\). Thus that root is the unique minimizing shape.

Finally, for fixed minimized shape costs \(C_j>0\), the sharp Cauchy--Schwarz inequality gives
\[
\left(\sum_j\frac{C_j}{b_j}\right)
\left(\sum_jb_j\right)\ge\left(\sum_j\sqrt{C_j}\right)^2.
\]
Equality under \(\sum_jb_j=B\) holds uniquely for \(b_j=B\sqrt{C_j}/Z\). Solving \(b_j=2u_j(P_j+Q_j/t_j)\) proves all stated rate formulas and the optimum. When \(P_j=Q_j\), the quartic factorizes as
\[
H_j(t)=P_j(t+1)^2\bigl((E+2)t^2-3E\bigr),
\]
which yields the equal-price shape formula.

## Verification
The accompanying `verify.py` implements exact-rational Laplacian inverses independently of the articulation-point decomposition, checks the symbolic derivative and equal-price factorization, and tests full-matrix cost-stationarity under independent perturbations of all edge weights. It passed 1,078 exact and numerical assertion groups in the recorded execution. It includes 52 rational graph tests with up to four cycles, and 84 randomized positive-price allocation tests. These finite tests corroborate, but do not replace, the all-parameter analytic proof.

For example, with two cycles, \(B=12\), and price pairs \((P_1,Q_1)=(1,4)\), \((P_2,Q_2)=(4,1)\), the optimal shape ratios are approximately \(3.497610998306\) and \(0.535750315287\), the cycle budgets are approximately \(5.661201610529\) and \(6.338798389471\), and the optimal index is approximately \(35.213708634842\). An independently inverted seven-vertex weighted Laplacian reproduces this value.

Run the independent-inversion and formula checks with `python verify.py`; Python 3, SymPy and NumPy are required.

## Relationship to prior work
Ghosh, Boyd and Saberi (2006) establish general convex optimization for total effective resistance, uniqueness, numerical algorithms, and a distinct explicit solution for barbell graphs. Their general method covers the optimization *framework* but neither states the heterogeneously priced quadrilateral-bouquet optimum nor its scalar quartic and cycle-level budget law. Sardar and Xu (public online 2024) study resistance distances and Kirchhoff indices for windmill graphs with unit-resistor interpretations; the accessible abstract does not establish variable-conductance budget optimization. Its full text was not available for comparison, so coverage of details remains a residual risk. The superficially related clique-bouquet problem has triangles or cliques rather than four-cycles and different edge-support behavior; it does not imply this precise square-cycle formula by relabeling. Likewise cactus spanning-tree maximization is a different determinant objective rather than inverse-Laplacian trace minimization.

## Limitations
No claim is made for cycles of length other than four, nonuniform individual prices within an edge orbit, cross-cycle edges, nonlinear prices, or multiple hub vertices. The quartic root is implicit but unique and computable by scalar bisection; its existence is proved for all positive parameters. The historical originality comparison is evidence-based, not an exhaustive literature theorem. In particular, the full 2024 Sardar--Xu windmill study could not be inspected. No independent mathematical validation has been performed.

## References
1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, Mathematical Theory of Networks and Systems, Kyoto, July 24--28, 2006. https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
2. M. S. Sardar and S.-J. Xu, *Resistance Distance and Kirchhoff Index in Windmill Graphs*, online July 5, 2024, DOI: 10.2174/0115701794299562240606054510. https://www.benthamscience.com/article/141453
3. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37--66. https://doi.org/10.1137/050645452
