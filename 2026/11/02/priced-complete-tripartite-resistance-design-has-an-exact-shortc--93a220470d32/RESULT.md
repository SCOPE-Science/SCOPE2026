# Priced complete-tripartite resistance design: exact edge deletion and the critical \(1/m\) price window

## Finding
For every integer \(m\ge2\), the unrestricted conductance-budget problem on the balanced tripartite network \(K_{m,m,m}\) has a unique global optimum. Label its three parts \(A,B,C\), with \(m\) nodes in each. Conductance on edges connecting \(A\) to \(B\), or \(B\) to \(C\), costs \(Q>0\) per unit; direct \(A\)-to-\(C\) conductance costs \(P>0\). Write \(r=P/Q\). In the optimal network all cheaper-orbit edges have common positive conductance \(x\), and all direct-orbit edges have common conductance \(y\ge0\). The direct links are all deleted **if and only if**
\[
r\ge r_c(m):=\frac{24m}{15m-7}.
\]
For \(0<r<r_c(m)\), the uniquely optimal ratio \(t_m(r)=y/x>0\) is the unique positive solution of
\[
\frac{r(3m-1)}2+\frac{6(m-1)(r-2)}{(1+t)^2}+\frac{3(r-4)}{(1+2t)^2}=0.
\]
For \(r\ge r_c(m)\), put \(t_m(r)=0\). If the total budget is \(B_0>0\), the unique edge values are
\[
x=\frac{B_0}{m^2Q(2+rt_m(r))},\qquad y=t_m(r)x.
\]
The minimized Kirchhoff index, defined as the sum of effective resistances over all unordered vertex pairs, is
\[
\mathcal K_* =\frac{m^2 Q}{B_0}(2+rt_m(r))
\left[\frac{3m-1}{2}+\frac{6(m-1)}{1+t_m(r)}+\frac3{1+2t_m(r)}\right].
\]
In particular, when direct edges are deleted, \(\mathcal K_*=m^2Q(15m-7)/B_0\).

There is a size-dependent price boundary: \(r_c(m)\searrow8/5\). For fixed \(0<r<8/5\),
\[
t_m(r)\longrightarrow 2\sqrt{\frac{2-r}{r}}-1.
\]
For fixed \(r>8/5\), direct edges are all absent for sufficiently large \(m\). In the critical window \(r_m=8/5+\kappa/m\) with any fixed \(\kappa\in\mathbb R\),
\[
\lim_{m\to\infty}m t_m(r_m)=\max\left\{0,\frac76-\frac{25\kappa}{16}\right\}.
\]
At \(r=2\), there is a small-size exception: \(m=2\) gives \(t_2(2)=(\sqrt{6/5}-1)/2>0\), whereas every \(m\ge3\) gives \(t_m(2)=0\).

## Assumptions and scope
The graph is simple and undirected, with three labeled parts of exactly \(m\ge2\) vertices each; edges exist between every pair of vertices in different parts and not within parts. Each individual edge is free to carry a different nonnegative real conductance, subject to the total price-weighted budget not exceeding \(B_0>0\). Positive prices are \(Q\) for edges in \(AB\cup BC\) and \(P\) for edges in \(AC\). A disconnected positive-conductance support is assigned infinite objective. For a connected conductance assignment \(w\), let \(L(w)\) be the ordinary combinatorial conductance Laplacian and \(\mathcal K(w)=\sum_{i<j}(e_i-e_j)^\mathsf T L(w)^+(e_i-e_j)=3m\,\operatorname{tr}(L(w)^+)\). The claim is for this exact Kirchhoff-index objective and the linear conductance budget, not for an imposed sparsity penalty or a nonlinear cost.

## Proof
**1. Existence, exact budget, unrestricted uniqueness, and symmetry.** Any connected feasible conductance assignment gives a positive-definite matrix \(H(w)=L(w)+\mathbf1\mathbf1^\mathsf T/(3m)\), with
\[
\mathcal K(w)=3m\left(\operatorname{tr}(H(w)^{-1})-1\right).
\]
The edge weights determine \(L(w)\) injectively because every off-diagonal edge entry is minus its weight. Along a nonconstant affine segment of connected assignments the second derivative of \(\operatorname{tr}(H^{-1})\) is strictly positive: with \(\Delta H\ne0\) symmetric, it equals \(2\operatorname{tr}(H^{-1}\Delta H H^{-1}\Delta H H^{-1})>0\). This follows, for instance, by conjugating \(\Delta H\) with \(H^{-1/2}\) and expressing the trace as a positively weighted square. The connected region is convex. Existence follows by compactness of the budget simplex, lower-semicontinuity with divergence as the smallest nontrivial Laplacian eigenvalue tends to zero, and the existence of an interior connected allocation. The entire budget is used since common positive scaling reduces all resistances.

Independently permuting vertices within each part and exchanging \(A\) and \(C\) preserves graph, prices and objective. Uniqueness forces the minimizer to be fixed by this group. There are exactly two edge orbits, \(AB\cup BC\) and \(AC\), so the unrestricted optimizer has conductances \(x\) and \(y\) as stated. Connectivity forces \(x>0\); \(y\ge0\) is allowed because \(AB\cup BC\) is connected.

**2. Exact spectral reduction.** For common edge weights \(x>0,y\ge0\), the nonzero eigenvalues of \(L\) consist of
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
m(x+y)&2(m-1)\\
2mx&m-1\\
m(x+2y)&1\\
3mx&1
\end{array}.
\]
The first two eigenvalue families arise from within-part zero-sum vectors; in the three-dimensional part-constant subspace, the two nonzero eigenvectors are proportional to \((1,0,-1)\) and \((1,-2,1)\). Hence
\[
\mathcal K(x,y)=\frac{6(m-1)}{x+y}+\frac{3m-1}{2x}+\frac3{x+2y}.
\]
There are \(2m^2\) edges of conductance \(x\) and \(m^2\) edges of conductance \(y\). Exact budget use means \(m^2(2Qx+Py)=B_0\). Put \(t=y/x\) and \(r=P/Q\), giving \(x=B_0/[m^2Q(2+rt)]\) and \(\mathcal K=(m^2Q/B_0)F_m(t)\), where
\[
F_m(t)=(2+rt)\left[\frac{3m-1}{2}+\frac{6(m-1)}{1+t}+\frac3{1+2t}\right],\qquad t\ge0.
\]
Direct differentiation simplifies to
\[
F_m'(t)=\frac{r(3m-1)}2+\frac{6(m-1)(r-2)}{(1+t)^2}+\frac{3(r-4)}{(1+2t)^2}.
\]
At \(t=0\), this is \(r(15m-7)/2-12m\). Since \(F_m\) is the strictly convex conductance objective along the budget line, expressed through the increasing parameter \(t\), the derivative sign at the boundary completely determines whether the unique minimizer lies at \(t=0\) or at the unique positive stationary point. Because \(F_m(t)\to\infty\) as \(t\to\infty\), no minimum is lost at infinity. This proves the exact threshold, optimizer, and minimum formula, including equality at the threshold.

**3. Critical scaling.** The threshold obeys
\[
r_c(m)=\frac85+\frac{56}{75m}+O(m^{-2}).
\]
For any fixed \(0<r<8/5\), the stationary equation divided by \(m\), together with boundedness of its positive root, gives in the limit
\[
\frac{3r}{2}+\frac{6(r-2)}{(1+t)^2}=0,
\]
whose unique nonnegative root is \(2\sqrt{(2-r)/r}-1\). For fixed \(r>8/5\), the exact support criterion gives eventual deletion. For \(r_m=8/5+\kappa/m\), Taylor expansion of \(F_m'\) at zero yields
\[
F_m'(0)=\frac{15\kappa}{2}-\frac{28}{5}+O(m^{-1}),\qquad
F_m''(0)=\frac{24}{5}m+O(1).
\]
When \(\kappa<56/75\), the unique positive root is \(O(m^{-1})\), and Taylor's theorem then gives \(m t_m(r_m)\to 7/6-25\kappa/16\). When \(\kappa>56/75\), the exact threshold sets \(t_m(r_m)=0\) eventually; at equality its ratio is \(o(m^{-1})\), so the limiting formula holds there too. Finally, setting \(r=2\) and \(m=2\) gives \(F_2'(t)=5-6/(1+2t)^2\), while the threshold for \(m\ge3\) lies strictly below \(2\). These establish the last assertion.

## Verification
The standalone script `verify.py` uses symbolic differentiation to check the derivative and threshold identities, constructs full matrices on multiple finite tripartite graphs, checks all eigenvalues and the independent pairwise-resistance sum against the formula, compares the scalar optimum with an unrestricted full-edge nonlinear solver started from nonsymmetric allocations, and checks the critical scaling numerically. It prints its assertion count and PASS status when run with Python, NumPy, SymPy and SciPy. Computation is corroboration only; the proof of the infinite statements is above.

## Relationship to prior work
Ghosh, Boyd and Saberi established the general convex framework for minimizing total resistance and illustrated analytical symmetry reduction for trees, wheels and barbell networks. Johnson and Chertkov adapted conductance-budget methods to priced network design and numerically examined sparsity, but did not give this balanced three-community threshold. Gervacio treated unit-resistor complete multipartite networks; the independently known unweighted value \(\mathcal K(K_{m,m,m})=(9m-5)/2\) agrees with the displayed formula at \(x=y=1\). Kooij and Achterberg used precisely this unweighted three-part value in a graph-augmentation complexity proof. The present theorem fixes the graph topology, varies every conductance independently under heterogeneous prices, and identifies both the global deletion frontier and its \(1/m\) transition law. No claim is made that convexity or the equal-weight Kirchhoff index is new.

## Limitations
The support theorem is specific to three **equal** vertex classes, one expensive class-to-class link orbit, a linear per-conductance price, and the sum-of-pairwise-resistances objective. The costly links are optional, while the cheap links must maintain connectivity. No assertion is made about arbitrary tripartite sizes, fixed per-link installation charges, other resistance functionals, or physical alternating-current grid safety. Specialized earlier treatment of this exact priced network may exist. A full PDF of Gervacio's 2012 work was not accessible in the consulted route, so comparison with it relied on its published abstract and corroborating unweighted formulas, not a claimed full-document negative search.

## References
- A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66. Original conference version: MTNS (July 2006). https://stanford.edu/~boyd/papers/pdf/eff_res.pdf
- S. Gervacio, *Resistance distance in complete n-partite graphs*, Mindanawan Journal of Mathematics 3 (2012), 1–19. Public record dated 2012-05-01: https://journals.msuiit.edu.ph/tmjm/article/view/26
- J. K. Johnson and M. Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks*, arXiv:1004.2285 (first version 2010-04-13). https://arxiv.org/abs/1004.2285
- R. E. Kooij and M. A. Achterberg, *Minimizing the effective graph resistance by adding links is NP-hard*, Operations Research Letters 51 (2023), 601–604. https://doi.org/10.1016/j.orl.2023.10.002
