# Exact optimal resistance allocation on trees of gateway cliques

## Finding

Let \(T\) be any finite tree with \(k\ge2\) vertices. Replace vertex \(i\) by a complete graph \(K_{n_i}\), \(n_i\ge2\), choosing one distinguished gateway \(g_i\). For every edge \(ij\) of \(T\), add exactly one edge \(g_i g_j\), and add no other edges between cliques. All conductances are independently adjustable and nonnegative, with total conductance budget \(B>0\). Write \(N=\sum_i n_i\). For a bridge \(e\) in \(T\), let \(s_e\) be the sum of the clique sizes on either side, so \(s_e(N-s_e)\) is well-defined regardless of which side is chosen.

Minimize the *unordered-pair total effective resistance*
\[
\mathcal R(w)=\sum_{u<v}R_{uv}(w),
\]
with \(\mathcal R=+\infty\) for disconnected nonnegative-conductance networks. Define
\[
H=\sum_{i=1}^k\left[\sqrt{\frac{n_i(N-n_i+1)}2}+(n_i-2)\sqrt{\frac N2}\right]+\sum_{e\in E(T)}\sqrt{s_e(N-s_e)}.
\]
Then the exact minimum and its **unique optimizer among all individually adjustable conductances** are
\[
\boxed{\mathcal R_{\min}=\frac{H^2}{B}}.
\]
For each clique \(i\), put \(c=B/H\), and define
\[
b_i=c\sqrt{\frac{2(N-n_i+1)}{n_i}},\qquad
\lambda_i=c\sqrt{2N},\qquad
a_i=\frac{\lambda_i-b_i}{n_i-1}.
\]
Every gateway-to-peripheral edge of clique \(i\) has conductance \(b_i\), and every edge between two peripheral vertices has conductance \(a_i\). When \(n_i=2\) there are no peripheral-to-peripheral edges, and \(a_i\) is immaterial. Every inter-clique bridge \(e\) has conductance
\[
\boxed{\beta_e=c\sqrt{s_e(N-s_e)}}.
\]
All present edges have strictly positive optimal conductance. In particular, for every clique of size at least three, the peripheral-contrast Laplacian eigenvalue
\[
\boxed{b_i+(n_i-1)a_i=c\sqrt{2N}}
\]
is **the same for every clique**, despite their different sizes and positions in the tree.

## Assumptions and scope

The graph is simple and undirected. Every bridge incident to clique \(i\) meets the *same* gateway vertex \(g_i\). No extra inter-clique edges, no separate gateway vertices within a clique, no vertex-dependent noises, and no unequal construction costs are allowed. The edge budget is the sum of conductances rather than a sum of resistances. The objective sums the electrical effective resistances over unordered pairs; it equals \(N\operatorname{tr}(L^+)\), with \(L^+\) the Laplacian pseudoinverse. The claimed optimizer is unrestricted across individual graph edges; within-clique symmetry is a conclusion, not a constraint.

## Proof

**1. Strict convexity and symmetry.** On the connected domain, \(\mathcal R=N\operatorname{tr}(L^+)\) is strictly convex in the independent conductances: restricting \(L\) to the orthocomplement of the constants yields a positive definite matrix, the trace of whose inverse is strictly convex in that matrix, and the map from distinct edge conductances to a simple graph Laplacian is injective. This remains true on a line segment between two connected nonnegative assignments. Consequently a global minimizer is unique. Permutations of the \(n_i-1\) peripheral vertices in each clique preserve the graph, budget, and objective, forcing their incident gateway edges to have a common conductance \(b_i\) and their peripheral-peripheral edges (if present) to have a common conductance \(a_i\). The bridges have independent conductances \(\beta_e\). We may therefore derive the unique global optimum in these variables.

**2. Series decomposition over the bridge tree.** Electrical effective resistance between vertices in two distinct cliques is the sum of their resistances to the corresponding gateways, plus the resistances of all bridges on the unique intervening tree path. Dangling other cliques cannot affect these pairwise resistances. Thus each bridge \(e\) of conductance \(\beta_e\) contributes exactly \(s_e(N-s_e)/\beta_e\) to \(\mathcal R\). A clique of size \(n\) contributes its own total pairwise resistance plus \(N-n\) times the sum of the resistances from its gateway to all its vertices.

**3. One clique's exact local terms.** In a clique of size \(n\), give the \(n-1\) gateway spokes conductance \(b>0\) and the \(\binom{n-1}{2}\) peripheral edges conductance \(a\ge0\). Put \(\ell=b+(n-1)a\). Its nonzero Laplacian eigenvalues are \(nb\) once and \(\ell\) with multiplicity \(n-2\). The internal pairwise resistance sum and the sum of gateway-to-vertex resistances are respectively
\[
\frac1b+\frac{n(n-2)}\ell,
\qquad
\frac1b+\frac{n-2}\ell.
\]
The latter follows also by projecting \(e_{g}-e_v\) onto the one-dimensional hub contrast and the \(n-2\)-dimensional peripheral-contrast space. Hence clique \(i\) contributes
\[
\frac{N-n_i+1}{b_i}+\frac{N(n_i-2)}{\ell_i}.
\]
Its edge-budget consumption is
\[
(n_i-1)b_i+\binom{n_i-1}{2}a_i
=\frac{n_i}{2}b_i+\frac{n_i-2}{2}\ell_i.
\]
The change of variables requires \(\ell_i\ge b_i>0\) for \(n_i\ge3\). For \(n_i=2\), only the \(b_i\) term is present.

**4. Sharp Cauchy–Schwarz allocation.** The complete reduced objective is a sum \(\sum_j d_j/x_j\) with positive coefficients \(d_j\), and the budget is \(\sum_j c_jx_j=B\). There are variables \(b_i\) with \((d,c)=(N-n_i+1,n_i/2)\), variables \(\ell_i\) for \(n_i\ge3\) with \((d,c)=(N(n_i-2),(n_i-2)/2)\), and bridge variables \(\beta_e\) with \((d,c)=(s_e(N-s_e),1)\). Cauchy–Schwarz yields
\[
\left(\sum_j\frac{d_j}{x_j}\right)\left(\sum_jc_jx_j\right)
\ge\left(\sum_j\sqrt{c_jd_j}\right)^2=H^2,
\]
with equality exactly when \(x_j=(B/H)\sqrt{d_j/c_j}\). These are precisely the displayed values.

**5. Feasibility and global uniqueness.** For every \(n_i\ge3\),
\[
\frac{\ell_i}{b_i}=\sqrt{\frac{Nn_i}{N-n_i+1}}>1,
\]
because \(Nn_i>N-n_i+1\) when \(N\ge n_i\ge2\). Hence all derived \(a_i\) are strictly positive. For \(n_i=2\), no \(a_i\) variable is needed. Every bridge and spoke is positive, all constraints hold, and equality in Cauchy–Schwarz is attained. Strict convexity from step 1 makes this optimum unique even for arbitrary non-symmetric edge allocations. The assertion follows.

## Verification

The included `verify.py` constructs the full conductance Laplacian and calculates total effective resistance from the inverse of a grounded Laplacian, rather than using the decomposed objective. On five nonisomorphic or size-heterogeneous examples it checks the closed form against direct matrix inversion, tests 250 independently perturbed feasible allocations, and compares five unrestricted all-edge numerical optimizations using SLSQP. All checks passed. Run `python verify.py` with Python, NumPy, and SciPy. The theorem for arbitrary clique sizes and arbitrary tree structure is proved analytically; finite numerical tests are not used as infinite certificates.

## Relationship to prior work

Ghosh, Boyd and Saberi established strict convexity of total-resistance conductance design, a square-root allocation law for **trees**, and a closed-form solution for the **equal-size two-clique barbell**. These are credited and included as known special cases. The statement here covers an arbitrary *tree of heterogeneous gateway cliques* with one port per clique, determines every conductance in closed form, and reveals a size-independent optimal peripheral-contrast eigenvalue for every clique. A generic convex-programming formulation does not itself state these explicit all-tree formulas. No claim of novelty is made for the generic Cauchy–Schwarz inequality, the equal barbell, the all-two-vertex-clique tree case, or the known strict-convexity principle.

## Limitations

The one-gateway-per-clique hypothesis is essential to the simple resistance decomposition. Multiple attachment gateways, extra inter-clique links, nonlinear prices, directed networks, and optimizing graph topology are not covered. Priority relative to specialized graph-resistance design literature remains subject to independent verification; no exhaustive uniqueness-of-publication claim is made. No independent audit has been performed.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, proceedings of MTNS 2006, Kyoto, July 24–28, 2006, author-hosted proceedings paper, https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf.
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66, DOI:10.1137/050645452. Relevant material: sections 2.7 (strict convexity), 5.1 (trees), 5.2 (symmetry and equal-size barbells).
