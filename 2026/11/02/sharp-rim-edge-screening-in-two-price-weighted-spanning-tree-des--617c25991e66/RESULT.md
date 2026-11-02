# Sharp rim-edge screening in two-price weighted spanning-tree design on wheel networks

## Finding
For every integer \(m\ge3\), consider the wheel \(W_m=K_1\vee C_m\), whose hub connects to all \(m\) vertices of the rim cycle. Give every spoke a cost \(P>0\) per unit of conductance, every rim edge a cost \(Q>0\), and permit each edge to be assigned its own arbitrary nonnegative conductance under budget \(B>0\). Let \(r=Q/P\). The unique allocation maximizing the weighted spanning-tree enumerator is uniform within the spoke orbit and within the rim orbit, even when no symmetry is imposed on feasible allocations.

**Sharp deletion boundary.** Every rim edge has zero conductance in the unique optimum if and only if \(r\ge2\). In that regime, the spoke conductances are \(s_*=B/(mP)\), the rim conductances are \(c_*=0\), and the optimum weighted spanning-tree enumerator is
\[
\mathcal T_* =\left(\frac{B}{mP}\right)^m.
\]

**Interior regime.** For \(0<r<2\), let \(a=1-r/2\), and define the unique \(u_m\in(0,a)\) solving
\[
\frac{u_m+u_m^{m-1}}{1+u_m^m}=a.
\]
Then the unique optimum has
\[
t_m=\frac{u_m}{(1-u_m)^2},\qquad
s_* = \frac{B}{mP(1+rt_m)},\qquad c_*=t_m s_*>0,
\]
with optimal tree count
\[
\mathcal T_* = \left(\frac{B}{mP}\right)^m
\frac{(1-u_m^m)^2}{\bigl[(1-u_m)^2+ru_m\bigr]^m}.
\]

**Finite-size scaling.** At each fixed \(0<r<2\), the rim-to-spoke optimum ratio approaches its explicit limit exponentially:
\[
\lim_{m\to\infty} t_m=\frac{2(2-r)}{r^2},\qquad
\lim_{m\to\infty}\frac{\frac{2(2-r)}{r^2}-t_m}{(1-r/2)^{m-1}}
=\left(\frac{4-r}{r}\right)^2.
\]
The equal-price specialization \(r=1\), including the limiting correction \(2-t_m\sim18\,2^{-m}\), is **already known** in the literature and is not claimed as original here. The claimed additional finding is the complete arbitrary-positive-price allocation, sharp \(r=2\) edge screening and price-dependent exponential law.

## Assumptions and scope
The wheel is the simple graph with one hub and one cycle of length \(m\ge3\). Every nonnegative real edge conductance is allowed, without upper bounds; all prices are fixed positive real numbers. The budget is imposed as \(P\sum_{i=1}^m s_i+Q\sum_{i=1}^m c_i\le B\), with positive budget. The weighted spanning-tree enumerator is \(\mathcal T(w)=\sum_T\prod_{e\in T}w_e\), summed over spanning trees, and by the matrix-tree theorem equals the determinant of the Laplacian grounded at the hub. A disconnected network has enumerator zero. This is a continuous-conductance, not integer edge-selection, problem.

## Proof
**1. Reduction without a symmetry assumption.** Ground at the hub. The grounded Laplacian is the positive-definite matrix \(L=\operatorname{diag}(s_1,\ldots,s_m)+L(C_m;c_1,\ldots,c_m)\) for connected feasible designs. Its off-diagonal entries uniquely identify all rim conductances, and its diagonals then uniquely identify all spokes, so the linear mapping from edge weights to \(L\) is injective. Because \(\log\det\) is strictly concave on positive-definite matrices, \(\log\mathcal T\) is strictly concave in edge conductances throughout connected feasible designs. The compact budget simplex contains a positive spanning-tree allocation, so it has a unique maximizer; monotonicity and positive homogeneity of the tree polynomial ensure the budget is tight. Every rim rotation or reflection preserves feasibility and the objective, and uniqueness therefore forces identical spokes \(s\) and identical rim conductances \(c\). This proves global, not merely symmetric-subproblem, uniqueness.

**2. Spectral product.** With common spoke and rim conductances, the hub-grounded Laplacian has Fourier eigenvalues \(s+4c\sin^2(\pi k/m)\), \(0\le k<m\). Thus
\[
\mathcal T(s,c)=\prod_{k=0}^{m-1}\left(s+4c\sin^2\frac{\pi k}{m}\right),\qquad
m(Ps+Qc)=B.
\]
Put \(t=c/s\ge0\) and set \(t=u/(1-u)^2\) with \(0\le u<1\). By factoring the cycle determinant over the \(m\)th roots of unity, or using \(1+4t\sin^2(\theta/2)=(1-2u\cos\theta+u^2)/(1-u)^2\), one gets
\[
\prod_{k=0}^{m-1}\left(1+4t\sin^2\frac{\pi k}{m}\right)
=\frac{(1-u^m)^2}{(1-u)^{2m}}.
\]
Combining with \(s=B/[mP(1+rt)]\) gives the exact one-variable objective
\[
\mathcal T(u)=\left(\frac{B}{mP}\right)^m
\frac{(1-u^m)^2}{D(u)^m},\qquad
D(u)=(1-u)^2+ru.
\]
Its value tends to zero as \(u\uparrow1\), so no boundary optimizer is missed.

**3. Exact global phase separation.** Differentiating yields
\[
\frac{d}{du}\log\mathcal T(u)
=\frac{m\big[(2-r)(1+u^m)-2(u+u^{m-1})\big]}
{D(u)(1-u^m)}.
\]
The denominator is positive for \(0\le u<1\). When \(r\ge2\), the numerator is negative for every \(u>0\), hence the sole optimum is \(u=0\), or \(c=0\). When \(0<r<2\), define \(a=1-r/2\in(0,1)\) and \(\phi_m(u)=(u+u^{m-1})/(1+u^m)\). Direct differentiation gives
\[
\phi_m'(u)=\frac{1-u^{2m-2}+(m-1)u^{m-2}(1-u^2)}{(1+u^m)^2}>0
\quad(0<u<1).
\]
Also \(\phi_m(0)=0\), \(\phi_m(1)=1\), and \(\phi_m(a)>a\). The derivative of \(\mathcal T\) therefore changes from positive to negative exactly once, at the unique \(u_m\in(0,a)\) solving \(\phi_m(u_m)=a\). Substitution yields the stated conductances and objective.

**4. Sharp price-dependent size law.** The scalar root equation rearranges *exactly* to
\[
a-u_m=\frac{u_m^{m-1}(1-u_m^2)}{1+u_m^m}.
\]
Since \(u_m<a<1\), the right-hand side lies in \((0,a^{m-1})\), so \(u_m\to a\) and division by \(a^{m-1}\) proves
\[
\lim_{m\to\infty}\frac{a-u_m}{a^{m-1}}=1-a^2.
\]
The map \(h(u)=u/(1-u)^2\) has \(h'(u)=(1+u)/(1-u)^3\). The mean-value theorem consequently gives
\[
\lim_{m\to\infty}\frac{h(a)-h(u_m)}{a^{m-1}}
=(1-a^2)h'(a)=\frac{(1+a)^2}{(1-a)^2}
=\left(\frac{4-r}{r}\right)^2,
\]
while \(h(a)=2(2-r)/r^2\). All quantifiers and endpoints follow; the asymptotic is for fixed positive \(r<2\), not a uniform joint limit with \(r\to0\) or \(r\to2\).

## Verification
The standard-library Python source `verify.py` constructs grounded Laplacians and computes exact-rational determinants, checks rational polynomial identities, performs numerical root and asymptotic checks and compares against independently perturbed feasible asymmetric designs. It completes with `VERIFY_OK exact=2725 analytic_numerical=292 asymmetric=1800 total=4817`. These finite checks support the claimed formulas and implementation; the proof for all \(m\), all real prices and all feasible conductances is the analytic argument above.

## Relationship to prior work
Khosoussi, Sukhatme, Huang and Dissanayake (arXiv:1604.01116v1, April 5, 2016) motivate weighted spanning-tree connectivity optimization and give algorithms for discrete edge selection. It does not present the present continuous two-price wheel classification in its inspected public text. General graph-Laplacian D-optimality and effective-resistance KKT theory already supply the abstract optimization framework; that framework and ordinary Fourier diagonalization are not claimed as new.

Crucially, the published result *The exact Löwner ellipsoid and exponential edge-weight stabilization for wheel symmetric edge polytopes* (published-finding corpus, October 11, 2026, identifier `2026/10/11/SCOPE-the-exact-l-wner-ellipsoid-and-exponential-edge-weight-stabiliza--39d62ea47ea0`) **does solve the equal-price wheel case** in a D-optimal-equivalent formulation, including the \(18\,2^{-m}\) correction. This prior case is explicitly excluded from the originality assertion. That result does not assign arbitrary distinct positive spoke/rim prices or identify the all-price sharp deletion phase at \(Q/P=2\). Other price-sensitive wheel designs with spectral-gap or total-effective-resistance objectives also do not imply the weighted-spanning-tree determinant solution, since the objectives differ. A relevant earlier all-price D-optimal wheel calculation may exist and remains an explicit overlap risk.

## Limitations
The graph must be a wheel and each of its two edge orbits must have a constant positive price, although edge conductances are unrestricted individually. The result is not a solution for arbitrary edge prices, constrained positive lower edge bounds, directed networks, or integer edge selection. The asymptotic holds at fixed \(0<r<2\). The equal-price case and general D-optimality principles are prior knowledge, not original discoveries. No independent validation or priority certification has occurred.

## References
1. K. Khosoussi, G. S. Sukhatme, S. Huang and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116v1, publicly posted April 5, 2016. https://arxiv.org/abs/1604.01116
2. *The exact Löwner ellipsoid and exponential edge-weight stabilization for wheel symmetric edge polytopes*, published-finding corpus research record, October 11, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-exact-l-wner-ellipsoid-and-exponential-edge-weight-stabiliza--39d62ea47ea0
3. A. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966v1, publicly posted February 12, 2023. https://arxiv.org/abs/2302.05966
4. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, ICM proceedings, 2006. https://web.stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf
