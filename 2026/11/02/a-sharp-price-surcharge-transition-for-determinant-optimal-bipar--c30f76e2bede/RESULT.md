# A sharp price-surcharge transition for determinant-optimal bipartite matchings

## Finding
Let \(m\ge 3\). Form the graph \(K_{m,m}\) with bipartition \(U=\{u_1,\ldots,u_m\}\), \(V=\{v_1,\ldots,v_m\}\), distinguishing the perfect matching \(\{u_iv_i:1\le i\le m\}\). Each matching edge has price \(P>0\) per conductance unit and each of the other \(m(m-1)\) edges has price \(Q>0\). Conductances are independently selectable, nonnegative, and subject to total expenditure \(B>0\). The objective is the weighted spanning-tree enumerator \(\tau\), or, equivalently, the determinant of a reduced weighted Laplacian.

**The unique unrestricted optimum is constant on both edge orbits.** Write \(a_*\) for each matching-edge conductance and \(b_*\) for each other cross-edge conductance. Every nonmatching edge is retained: \(b_*>0\). Set
\[
\rho_c(m)=\frac{m(2m-3)}{(m-2)(2m-1)}
=1+\frac{2(m-1)}{(m-2)(2m-1)}.
\]
Then **the entire matching is deleted if and only if**
\[
\frac{P}{Q}\ge\rho_c(m).
\]
At and above this boundary,
\[
a_*=0,\qquad b_*=\frac{B}{m(m-1)Q}.
\]
For \(P/Q<\rho_c(m)\), let \(q=Q/P\),
\[
A_m=4(m-1)-2mq,\qquad
C_m=(m-2)(2m-1)-m(2m-3)q<0,
\]
and
\[
t_*=\frac{\sqrt{A_m^2-8C_m}-A_m}{4}>0.
\]
The unique optimum is
\[
b_*=\frac{B}{m(Pt_*+(m-1)Q)},\qquad a_*=t_*b_*.
\]
At equal prices, \(a_*=b_*=B/(m^2P)\), so the whole price response is anchored at the standard uniform design.

The critical surcharge shrinks inversely with network size. For any fixed real \(\gamma\), if \(P/Q=1+\gamma/m\) (for sufficiently large \(m\) to keep prices positive), then
\[
\lim_{m\to\infty}\frac{a_*}{b_*}=\max\{0,1-\gamma\}.
\]
Moreover, for each fixed \(m\), as \(\rho=P/Q\uparrow\rho_c(m)\) from below,
\[
\frac{a_*}{b_*}=\frac{(m-2)^2(2m-1)^2}{2m(2m^2-5m+4)}\bigl(\rho_c(m)-\rho\bigr)
+O_m\!\left((\rho_c(m)-\rho)^2\right).
\]

## Assumptions and scope
The graph is finite, simple, and connected before conductance choice, with \(m\ge3\). The allowed budget allocations may be asymmetric across individual edges and may assign zero conductance to some edges. There are no capacities, fixed baseline conductances, or discrete edge-selection constraints. Prices and the budget are strictly positive; they are not required to be rational. A zero conductance removes an edge from the effective network. The objective is zero on disconnected effective networks. The case \(m=2\), where deleting the designated matching disconnects the graph, is deliberately excluded.

## Proof
**1. Unrestricted uniqueness and symmetry.** Ground any vertex and write the reduced Laplacian as \(L_0(w)=\sum_e w_ez_ez_e^{\mathsf T}\), where \(z_e\) is the corresponding reduced incidence vector. The map \(w\mapsto L_0(w)\) is injective for a simple graph: entries off the diagonal recover weights of non-ground edges, and then the diagonal entries recover weights incident to ground. Therefore \(\log\det L_0(w)\) is strictly concave on its positive-definite domain, and the feasible budget simplex is compact. A strictly positive feasible allocation exists and has positive determinant; disconnected allocations have determinant zero, so there exists exactly one global maximizer. Simultaneously permuting paired labels and interchanging the two sides acts transitively on the matching edges and on their complement, preserving prices and the objective. Uniqueness forces constant weights \(a,b\) within these classes.

**2. Exact weighted tree polynomial.** Every vertex has weighted degree \(d=a+(m-1)b\), and the off-diagonal adjacency block is \(bJ+(a-b)I\). The Laplacian has eigenvalues \(0\) (once), \(2d\) (once), \(mb\) (multiplicity \(m-1\)), and \(2a+(m-2)b\) (multiplicity \(m-1\)). Matrix–Tree gives
\[
\tau_m(a,b)=\frac{d}{m}(mb)^{m-1}\bigl(2a+(m-2)b\bigr)^{m-1}.
\]
For \(m\ge3\), \(a=0,b>0\) remains connected, but \(b=0\) disconnects the graph into \(m\) pairs. Hence \(b_*>0\) in every optimum.

**3. Reduction and exact threshold.** With \(t=a/b\ge0\), the budget \(mPa+m(m-1)Qb=B\) gives \(b=B/[m(Pt+(m-1)Q)]\). Omitting a positive factor independent of \(t\), the determinant becomes
\[
F_m(t)=\frac{(t+m-1)(2t+m-2)^{m-1}}{(Pt+(m-1)Q)^{2m-1}}.
\]
A direct derivative calculation yields
\[
\frac{d}{dt}\log F_m(t)
=\frac{1}{t+m-1}+\frac{2(m-1)}{2t+m-2}
-\frac{(2m-1)P}{Pt+(m-1)Q}.
\]
Multiplication by the positive denominator \((t+m-1)(2t+m-2)(Pt+(m-1)Q)\) shows that the derivative has the opposite sign to
\[
2t^2+A_mt+C_m.
\]
Here \(C_m\ge0\) precisely if \(P/Q\ge\rho_c(m)\), and \(A_m>0\) whenever \(C_m\ge0\) (because \(A_m\) is then at least its strictly positive value at \(\rho_c(m)\)). Thus the derivative is nonpositive for all \(t\ge0\) above the threshold, with equality only at \(t=0\) in the boundary case. If \(C_m<0\), the quadratic has exactly one positive root, given by the displayed radical. The derivative is positive before and negative after this root. This independently confirms the unique scalar maximum, hence the unrestricted optimum already established in step 1.

**4. Scaling and boundary law.** In the window \(\rho=1+\gamma/m\), the derivative quadratic satisfies \(A_m=2m+O_\gamma(1)\), \(C_m=2m(\gamma-1)+O_\gamma(1)\). For \(\gamma<1\), the unique positive root converges to \(1-\gamma\); for \(\gamma>1\), the exact price threshold eventually forces \(t_*=0\); and for \(\gamma=1\), the positive root (if present) converges to zero. For fixed \(m\), write \(\rho_c=\rho_c(m)\). Since \(C_m(\rho_c)=0\), \(C_m'(\rho_c)=m(2m-3)/\rho_c^2\), and \(A_m(\rho_c)=2(2m^2-5m+4)/(2m-3)>0\), the implicit function theorem at the simple root \(t=0\) gives the displayed linear coefficient and quadratic remainder.

## Verification
The standalone file `verify.py` recomputes the reduced-Laplacian determinant, the exact spectral product, the threshold polynomial and the budget, compares unrestricted asymmetric feasible allocations, solves sample unconstrained-by-symmetry numerical optimizations, and checks the critical window. Run `python3 verify.py` with Python 3, NumPy and SciPy. In the recorded execution it passed 8 exact rational determinants, 175 direct numerical determinants, 175 optimality-polynomial and budget checks, 2,100 independent asymmetric feasible-allocation comparisons, 18 unrestricted numerical optimizations, and 18 critical-window tests. These finite checks corroborate, but do not replace, the analytical proof above.

## Relationship to prior work
Weighted spanning-tree determinants are classical via the Matrix–Tree theorem. General graph-Laplacian eigenvalue optimization and semidefinite design methods are described by Boyd; the 2016 work of Khosoussi, Sukhatme, Huang and Dissanayake develops weighted spanning-tree optimization for fixed-weight edge selection and related convex relaxations. Those frameworks support the chosen objective but do not supply the explicit two-price perfect-matching deletion threshold or its vanishing-surcharge scaling in their inspected statements. The crown graph \(K_{m,m}\setminus M\) is classical; identifying it as the unique optimal support is the price-sensitive conclusion here. A claim of exhaustive historical publication priority is not made.

## Limitations
Only a complete balanced bipartite graph with one distinguished perfect matching, two homogeneous price classes, and independent continuous conductances is treated. General unbalanced bipartite graphs, multiple exceptional matchings, edge capacities, discrete edge selection, and robustness to arbitrary price perturbations are outside the theorem. The verification program uses finite experiments only; it does not establish any infinite claim. The possible existence of an overlooked specialized earlier theorem remains a research-literature risk. Independent external mathematical validation has not been performed.

## References
1. K. Khosoussi, G. S. Sukhatme, S. Huang and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, arXiv:1604.01116, first posted 2016-04-05, https://arxiv.org/abs/1604.01116.
2. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, https://web.stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf, especially Section 3 (continuous-time mixing and algebraic connectivity).
3. Matrix–Tree theorem (classical), as recalled in Reference 1, Section 2.2.
