# An equal-conductance plateau in worst-outage resistance design of alternating-price cycles

## Finding

For every integer \(m\ge2\), budget \(B>0\), and relative conductance price \(t>0\), consider an even cycle \(C_{2m}\) with independent edge conductances. A complete outage of any one edge leaves a path. We minimize the **worst**, over all possible single-edge outages, sum of effective resistances between unordered vertex pairs in that residual network.

Define
\[
U_m=\frac{m(2m^2+1)}{3},\qquad
V_m=\frac{2m(m^2-1)}{3},\qquad
t_- =\frac{V_m}{U_m}=\frac{2(m^2-1)}{2m^2+1},\qquad
t_+=\frac{U_m}{V_m}=\frac{2m^2+1}{2(m^2-1)}.
\]
Then \(0<t_-<1<t_+\). There is exactly one optimal conductance vector, even among all independently selected asymmetric edge weights. Every edge has positive optimal conductance. Writing \(a\) for conductance on each even-indexed edge and \(b\) on each odd-indexed edge, the optimal ratio is
\[
r=\frac ab=
\begin{cases}
\sqrt{U_m t/V_m},&0<t<t_-,\\
1,&t_-\le t\le t_+,\\
\sqrt{V_m t/U_m},&t>t_+.
\end{cases}
\]
The exact allocation is
\[
b=\frac{B}{m(r+t)},\qquad a=\frac{Br}{m(r+t)}.
\]
The minimum worst-outage Kirchhoff index is
\[
\mathcal R_*=
\begin{cases}
\dfrac{m}{B}(\sqrt{U_m}+\sqrt{V_m t})^2,&0<t<t_-,\\[5pt]
\dfrac{m}{B}(1+t)(U_m+V_m),&t_-\le t\le t_+,\\[5pt]
\dfrac{m}{B}(\sqrt{V_m}+\sqrt{U_m t})^2,&t>t_+.
\end{cases}
\]
The formulas agree at both endpoints, where the unique optimum still has \(a=b\).

In particular, a nonempty interval of *unequal per-unit prices* nevertheless has exactly equal optimal edge conductances. Its width obeys
\[
t_+-t_-=\frac{3}{2m^2-2}+\frac{3}{2m^2+1},\qquad
\lim_{m\to\infty}m^2(t_+-t_-)=3.
\]
By contrast, with the same budget and no outage, a fully equal conductance allocation can minimize the ordinary Kirchhoff index only when \(t=1\). Thus the robust plateau is not inherited from nominal cycle symmetry.

## Assumptions and scope

Label the vertices by integers modulo \(N=2m\), and the undirected edges by \(e_j=\{j,j+1\}\), \(0\le j<N\). The conductance on \(e_j\) is an independent variable \(w_j\ge0\). All even-indexed edges have cost per conductance \(1\), all odd-indexed edges cost \(t\). The *exact* budget is
\[
\sum_{j\,\mathrm{even}}w_j+t\sum_{j\,\mathrm{odd}}w_j=B.
\]
For any index \(f\), let \(C_{2m}\setminus e_f\) denote the network after setting the conductance of edge \(e_f\) to zero without reallocating its cost. Let \(\mathcal K_f(w)\) be the sum over all \(\binom{N}{2}\) unordered vertex pairs of the effective resistance in that post-outage network; set \(\mathcal K_f=+\infty\) if the network is disconnected. The objective is \(\mathcal R(w)=\max_f\mathcal K_f(w)\). There are no upper or lower conductance bounds besides nonnegativity, and failures are deterministic worst cases rather than random events.

## Proof

**1. Post-failure resistance is a separable reciprocal sum.** After deletion of \(e_f\), the residual path starts with \(e_{f+1}\), then \(e_{f+2}\), and so on, with indices taken modulo \(N\). The edge at distance \(d\) separates \(d\) from \(N-d\) path vertices, hence occurs in precisely \(d(N-d)\) unordered vertex-to-vertex routes. Summing series resistances over those routes gives, for positive conductances,
\[
\mathcal K_f(w)=\sum_{d=1}^{N-1}\frac{d(N-d)}{w_{f+d}}.
\tag{1}
\]
If any edge has zero conductance, deleting a different edge disconnects the cycle, so \(\mathcal R=+\infty\). A feasible constant positive allocation has finite objective; consequently every optimizer is strictly positive.

**2. The unrestricted minimizer exists and is unique.** On the compact nonnegative budget simplex the extended objective is lower semicontinuous, and equation (1) diverges at its boundary. Thus a finite interior minimizer exists. Each \(\mathcal K_f\) is convex, and is strictly convex along any segment on which any variable other than \(w_f\) changes. Two distinct points of the exact-budget hyperplane differ in *at least two* coordinates because every cost is positive. Therefore every \(\mathcal K_f\) is strictly convex on such a segment. As there are only finitely many possible failures, their maximum \(\mathcal R\) is strictly convex on the feasible budget hyperplane. This proves global uniqueness without assuming symmetry.

**3. Invariance enforces only two conductance values.** Rotation of the cycle by two vertices and reflection of vertex \(j\) to vertex \(1-j\) preserve edge-price parity, the budget, and the set of all possible failed edges. They act transitively on even-indexed edges and transitively on odd-indexed edges. The unique minimizer is fixed by this group, so it has constant values \(a>0\) and \(b>0\) on the respective classes, subject to \(m(a+tb)=B\).

**4. The two adversarial failure classes.** The odd distances \(d=1,3,\ldots,2m-1\) in equation (1) have total coefficient
\[
\sum_{\substack{1\le d<2m\\d\ \mathrm{odd}}}d(2m-d)
=\frac{m(2m^2+1)}3=U_m.
\]
The even distances \(d=2,4,\ldots,2m-2\) have coefficient sum
\[
\sum_{\substack{1\le d<2m\\d\ \mathrm{even}}}d(2m-d)
=\frac{2m(m^2-1)}3=V_m.
\]
In particular \(U_m-V_m=m>0\). Deleting an even edge yields \(U_m/b+V_m/a\); deleting an odd edge yields \(U_m/a+V_m/b\). Therefore
\[
\mathcal R(a,b)=\max\left\{\frac{V_m}{a}+\frac{U_m}{b},
\frac{U_m}{a}+\frac{V_m}{b}\right\}.
\tag{2}
\]
When \(a>b\) the first branch is larger; when \(a<b\) the second branch is larger; and both tie at \(a=b\).

**5. Exact minimax solution and both thresholds.** Write \(r=a/b>0\). The budget gives \(b=B/[m(r+t)]\), and equation (2) becomes
\[
\mathcal R(r)=\frac{m(r+t)}{B}
\begin{cases}
U_m/r+V_m,&0<r\le1,\\
V_m/r+U_m,&r\ge1.
\end{cases}
\tag{3}
\]
On \(0<r\le1\), the derivative has the sign of \(V_m-U_m t/r^2\). The only unconstrained minimum is at \(r=\sqrt{U_m t/V_m}\), which lies below \(1\) exactly if \(t<t_-=V_m/U_m\); otherwise that branch is minimized at the endpoint \(r=1\). On \(r\ge1\), the derivative has the sign of \(U_m-V_m t/r^2\). Its unconstrained minimum is at \(r=\sqrt{V_m t/U_m}\), which lies above \(1\) exactly if \(t>t_+=U_m/V_m\); otherwise that branch is minimized at \(r=1\). Strict convexity proved in step 2 excludes any additional minimizer. Substitution in equation (3) gives the displayed three-part optimal value and conductances. The reciprocal thresholds follow from the explicit coefficient sums.

**6. Comparison with nominal design.** At a uniform positive allocation on the unfailed cycle, the ordinary Kirchhoff-index objective is differentiable and has the same partial derivative with respect to every edge conductance, because the underlying (unpriced) cycle is edge-transitive. These common derivatives are nonzero (scaling all conductances strictly decreases the Kirchhoff index). With a linear exact budget whose marginal costs are \(1\) and \(t\), the Lagrange necessary condition for an interior optimum requires equal marginal derivative-to-price ratios. At uniform weights this forces \(t=1\). Conversely, at \(t=1\), symmetry and strict convexity of the nominal objective give uniform optimal weights. This establishes the claimed contrast to the robust plateau.

## Verification

The standalone reproducibility program `verify_robust_cycle.py` constructs every possible single-edge-loss coefficient, verifies the two parity sums symbolically, and checks the three formula regimes on rational and floating-point parameter grids. It independently constructs weighted Laplacians after edge failures and compares the exact path-resistance expression with \(N\operatorname{tr}L^+\) obtained from matrix eigenvalues. It also tests asymmetric feasible competitor vectors and numerical optimization over all \(2m\) unrestricted edge variables. Executing the program using Python with NumPy, SciPy, and SymPy completed **2,478 assertions** without failures. These are finite cross-checks; the all-parameter conclusions come from the analytic proof.

The exact differentiation and asymptotic identities were checked separately using symbolic algebra, in addition to the program. See `VERIFICATION.md` for replay instructions and limits.

## Relationship to prior work

Ghosh, Boyd, and Saberi, *Minimizing Effective Resistance of a Graph* (2008), establish convex total-effective-resistance conductance allocation and analyze unfailed trees, wheels, and other graphs. Their cycle observation applies to equal-cost, **no-failure** allocations; it does not give the present worst-outage three-regime formula.

Johnson and Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks* (first publicly posted 13 April 2010, arXiv:1004.2285), Section V, already propose the **general idea of worst-case power loss after prescribed line failures**. That broad formulation is prior work, not a new contribution here. The present result instead provides an exact, unrestricted, all-size closed-form minimizer, uniqueness proof, and positive-width equal-allocation plateau for a specific priced family; the paper's general numerical/smoothed procedure does not state these values or a comparison to nominal design.

Boyd, Vandenberghe, El Gamal, and Yun, *Design of Robust Global Power and Ground Networks* (ISPD 2001), optimize networks against varying currents, rather than optimizing the same worst-single-line-removal Kirchhoff objective. These distinctions are based on inspection of the primary sources, not solely search-result titles.

## Limitations

The theorem applies to even simple cycles with two strictly positive alternating edge prices and a single complete outage. It does not characterize arbitrary price vectors, multiple simultaneous failures, stochastic failure probabilities, or networks with parallel edges. The cost budget is fixed at design time and is not reallocated after failure. The exact spectral computations in the accompanying program cover finite test cases only. A published general convex programming formulation for edge failures predates this result; no new general optimization framework is claimed.

## References

1. J. K. Johnson and M. Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks*, arXiv:1004.2285, initial public version 2010-04-13; especially Section V. https://arxiv.org/abs/1004.2285
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66. DOI:10.1137/050645452. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. S. Boyd, L. Vandenberghe, A. El Gamal, and S. Yun, *Design of Robust Global Power and Ground Networks*, ISPD (2001), 60–65. https://cecs.uci.edu/~papers/compendium94-03/papers/2001/ispd01/pdffiles/p060.pdf
