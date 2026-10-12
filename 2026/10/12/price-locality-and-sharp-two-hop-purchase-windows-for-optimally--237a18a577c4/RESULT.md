# Price-locality and sharp two-hop purchase windows for optimally weighted trees

## Finding

**Theorem (one optional shortcut under a shared conductance budget).** Let \(T=(V,E)\) be any finite simple tree with \(N\ge3\) vertices. Each old edge \(e\) has an arbitrary positive unit-conductance price \(c_e\). Fix distinct nonadjacent vertices \(u,v\) and an optional shortcut \(f=uv\) with positive price \(\tau\). Minimize the Kirchhoff index \(K=\sum_{\{a,b\}\subset V}R_{ab}\) over nonnegative conductances \(g_e,z\) satisfying

\[
\sum_{e\in E}c_eg_e+\tau z=1,
\]

with \(K=+\infty\) for disconnected positive-conductance support. The minimizing allocation is unique. It assigns \(z^*=0\) if and only if \(\tau\ge\Theta_T(u,v)\), with strict \(z^*>0\) for \(0<\tau<\Theta_T(u,v)\), where the following formula uses only cut sizes and prices along the tree path.

Orient the unique path from \(u\) to \(v\), and enumerate its \(\ell\ge2\) edges as \(e_1,\ldots,e_\ell\). Let \(s_i\) be the size of the component containing \(u\) after deleting \(e_i\); then \(1\le s_1<\cdots<s_\ell\le N-1\). Put \(c_i=c_{e_i}\). The exact critical price is

\[
\boxed{\displaystyle
\Theta_T(u,v)=\sum_{i=1}^{\ell}c_i+
2\sum_{1\le i<j\le\ell}\sqrt{c_ic_j}
\sqrt{\frac{s_i(N-s_j)}{s_j(N-s_i)}}.}
\]

In particular, modifying **any** old-edge price outside the path leaves the purchase decision unchanged, even though it changes the optimal old-edge conductances. The threshold satisfies the strict universal bounds

\[
\sum_{i=1}^{\ell}c_i<\Theta_T(u,v)<
\left(\sum_{i=1}^{\ell}\sqrt{c_i}\right)^2.
\]

For each fixed path length and its positive prices, the upper bound is sharp as a supremum over trees: adding equally many leaves at the two endpoints and letting their number grow makes the threshold approach the upper bound.

**Sharp finite-size two-hop classification.** If \(u-w-v\) is a path of length two in an \(N\)-vertex tree and its two edge prices are \(c_1,c_2\), set

\[
R_N=\begin{cases}
\frac{N-1}{N+1},&N\text{ odd},\\
\sqrt{\frac{N-2}{N+2}},&N\text{ even}.
\end{cases}
\]

Across **all** \(N\)-vertex trees containing such a two-hop path, with arbitrary positive prices on the other edges, the exact attainable extreme critical prices are

\[
\boxed{\displaystyle
c_1+c_2+\frac{2\sqrt{c_1c_2}}{N-1}
\ \le\ \Theta_T(u,v)\ \le\
c_1+c_2+2R_N\sqrt{c_1c_2}.}
\]

Both endpoints are attained. The lower extreme occurs exactly when the two selected endpoints are leaves. For the upper extreme, deleting the two path edges must leave the middle component consisting only of \(w\), while the two endpoint components have sizes \(\lfloor(N-1)/2\rfloor\) and \(\lceil(N-1)/2\rceil\). These characterize all maximizing and minimizing component-size profiles; branching within an endpoint component is arbitrary.

For example, with \(N=6\) and \(c_1=c_2=1\), the critical price ranges sharply from \(12/5\) to \(2+\sqrt2\). A star with the shortcut between two leaves attains the lower extreme; a tree with endpoint-component sizes three and two, separated by a degree-two middle vertex, attains the upper extreme.

## Assumptions and scope

All graphs are finite, simple, undirected. Conductances are nonnegative and **all** original edges may be reweighted, subject to one linear budget shared with the optional edge. All old-edge prices and the shortcut price are strictly positive. The shortcut is not a pre-existing edge. Effective resistance is computed after reallocating conductances; a disconnected network has infinite Kirchhoff index. The conclusion is a purchase criterion and a unique global optimizer, not a closed formula for the positive shortcut weight when it is installed. No fixed-base-weight or unit-price assumption is imposed.

## Proof

**1. Exact optimum without the shortcut.** For an old edge \(e\), let \(a_e\) be the size of one component of \(T-e\) and \(b_e=a_e(N-a_e)>0\). On a tree, the series-resistance identity gives

\[
K_T(g)=\sum_{e\in E}\frac{b_e}{g_e}.
\]

Cauchy–Schwarz, using the budget with \(z=0\), gives \(K_T(g)\ge S^2\) where

\[
S=\sum_{e\in E}\sqrt{b_ec_e}.
\]

The unique equality case is \(g_e^0=\sqrt{b_e/c_e}/S\), with \(K_T(g^0)=S^2\). Every old edge is positive. Differentiation at this point gives

\[
\frac{\partial K}{\partial g_e}(g^0,0)=-S^2c_e.
\]

**2. Derivative in the new-link direction.** Let \(L_0\) denote the weighted tree Laplacian at \(g^0\), and put \(\beta={\bf e}_u-{\bf e}_v\). On any connected network, \(K=N\operatorname{tr}L^+\), and the rank-one perturbation \(L(z)=L_0+z\beta\beta^{\mathsf T}\) satisfies

\[
\left.\frac{\partial K}{\partial z}\right|_{(g^0,0)}
=-N\|L_0^+\beta\|_2^2.
\]

Indeed, write \(M=L+{\bf1}{\bf1}^{\mathsf T}/N\), use \(K=N(\operatorname{tr}M^{-1}-1)\), differentiate the inverse, and note \(M^{-1}\beta=L^+\beta\). The unique unit current from \(u\) to \(v\) travels on their tree path. Let \(U_i\) be the component containing \(u\) after deleting \(e_i\), and put \(h(x)=\sum_{i=1}^{\ell}\sqrt{c_i/b_{e_i}}\,\mathbf1_{U_i}(x)\). The unit-current potential is \(Sh\) up to a common additive constant, because the resistance of \(e_i\) under \(g^0\) is \(S\sqrt{c_i/b_{e_i}}\). Thus, with \(\bar h=N^{-1}\sum_xh(x)\),

\[
\left.\frac{\partial K}{\partial z}\right|_{(g^0,0)}
=-S^2\underbrace{N\sum_{x\in V}(h(x)-\bar h)^2}_{\Theta_T(u,v)}.
\]

**3. The cut-correlation identity.** The sets \(U_1\subsetneq U_2\subsetneq\cdots\subsetneq U_\ell\) are nested, with \(|U_i|=s_i\). The centered indicator of each \(U_i\) has squared norm \(s_i(N-s_i)/N\), and, for \(i<j\), the centered inner product is \(s_i(N-s_j)/N\). Expanding the variance yields exactly the displayed formula for \(\Theta_T(u,v)\). In particular \(S\) and every off-path price cancel. The off-diagonal coefficients are positive and strictly smaller than one: their squares equal \(s_i(N-s_j)/(s_j(N-s_i))\), and the strict inequalities follow from \(0<s_i<s_j<N\). Hence the strict bounds hold. If \(M\) new leaves are attached to each endpoint of a fixed length-\(\ell\) path, its cut sizes are \(s_i=M+i\) and \(N=2M+\ell+1\). Every off-diagonal coefficient tends to one as \(M\to\infty\), proving sharpness of the upper bound.

**4. Global threshold and uniqueness.** On the connected region, \(K=N(\operatorname{tr}M^{-1}-1)\) is strictly convex in the complete conductance vector. Indeed, \(A\mapsto\operatorname{tr}A^{-1}\) has a strictly positive second directional derivative for every nonzero symmetric direction at \(A\succ0\); distinct edge weights induce distinct Laplacians because the underlying graph is simple and off-diagonal Laplacian entries recover individual conductances. Disconnected boundaries have \(K=+\infty\), so a unique global minimizer exists under the compact budget simplex. At \((g^0,0)\), the first-order condition for every old edge is zero after adding the budget multiplier \(S^2\); for the nonnegative shortcut it is \(S^2(\tau-\Theta_T(u,v))\). Convexity proves global optimality with \(z=0\) precisely for \(\tau\ge\Theta_T(u,v)\). If the inequality fails, increasing \(z\) by \(\varepsilon\) and multiplying all old weights by \(1-\tau\varepsilon\) is feasible for sufficiently small positive \(\varepsilon\) and decreases the objective to first order by \(S^2(\Theta_T(u,v)-\tau)\varepsilon\). Hence every optimum has \(z>0\). Strict convexity ensures uniqueness including at equality.

**5. Exact two-hop extremes.** If the three components after deleting the two path edges have orders \(a,k,b\) in path order, then \(a,b,k\) are positive integers with \(a+b+k=N\), and the general formula reduces to

\[
\Theta=c_1+c_2+2\sqrt{c_1c_2}\sqrt{\frac{ab}{(N-a)(N-b)}}.
\]

The last factor increases strictly in each of \(a,b\), so its minimum is at \(a=b=1\), where it equals \(1/(N-1)\). Its maximum has \(k=1\), hence \(a+b=N-1\). For fixed sum, the product \(a(N-1-a)/[(N-a)(a+1)]\) is maximal at the two integers nearest \((N-1)/2\); this follows either from the symmetry and monotonicity of its successive ratio, or by setting \(x=a(N-1-a)\) and rewriting the product as \(x/(x+N)\). Substitution gives the stated odd/even values of \(R_N\). Each component profile is realized by attaching finite trees at \(u,w,v\), so both bounds are genuinely attained.

## Verification

The companion `verify.py` uses only the Python standard library. It constructs finite trees with exact-rational edge prices chosen to make the optimal old conductances rational, independently computes \(K\) from the inverse of \(L+{\bf1}{\bf1}^{\mathsf T}/N\), computes the exact new-edge derivative from the inverse squared, and compares this with the cut-correlation and potential-variance formulas. It also checks strict cut bounds and every internal split inequality for the tested paths. It checks the two-hop extrema by exact arithmetic for every integer \(3\le N\le49\). The reproduced result is `VERIFY_OK 154 exact tree/chord KKT tests; 47 finite two-hop extremal checks`. The infinite-domain assertions are established by the proof, not by finite sampling.

## Relationship to prior work

Ghosh, Boyd, and Saberi established convex conductance allocation, derivative and optimality conditions for the Kirchhoff index, and the unpriced optimum for trees. Those general ingredients are acknowledged. The classification here concerns an **optional new edge sharing an arbitrary-price budget with all reweighted tree edges**, the exact nested-cut correlation law, independence from off-path prices, a sharp general price bound, and a complete finite-order classification for two-hop shortcuts. Path-only unit-price specializations are not the distinct contribution here. Predari and collaborators study greedy edge insertion with fixed underlying weights and algorithmic approximation, not this joint continuous reallocation threshold. Broader historical coverage remains possible.

## Limitations

The theorem covers one optional shortcut and Kirchhoff-index minimization, not selecting several new links simultaneously or objectives such as spectral gap or maximum pairwise resistance. It classifies whether the shortcut is installed, not the complete positive optimum below its price threshold. There is no independent audit. The prior-art comparison is not a proof that no equivalent earlier specialization exists. The earliest primary source used for the historical anchor has an explicitly verified online publication date; an earlier conference version is known only to month precision in the inspected material.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, DOI: 10.1137/050645452. Public full text: https://stanford.edu/~boyd/papers/pdf/eff_res.pdf. Sections 2.3, 4.2, 5.1; online publication dated 2008-02-01.
2. M. Predari, L. Berner, R. Kooij, and H. Meyerhenke, *Greedy Optimization of Resistance-based Graph Robustness with Global and Local Edge Insertions*, arXiv:2309.08271v1, https://arxiv.org/html/2309.08271v1 (2023); Sections 1–4 and 7.
3. R. E. Kooij and M. A. Achterberg, *Minimizing the Effective Graph Resistance by Adding Links Is NP-hard*, Operations Research Letters 51 (2023), 601–604, DOI: 10.1016/j.orl.2023.10.002. Studies discrete fixed-weight augmentation, a different design problem.
