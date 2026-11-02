# Exact mixed-support conductance design for heterogeneous clique bouquets

## Finding

Let \(k\ge2\), let \(m_1,\ldots,m_k\ge2\) be integers, and join \(k\) complete graphs of orders \(m_j+1\) at one common vertex, with no other overlap. Let \(M=\sum_{j=1}^k m_j\) and \(N=M+1\). In blade \(j\), every hub-to-peripheral edge has a positive unit-conductance price \(P_j\), and every peripheral-to-peripheral edge has a positive price \(Q_j\). Independently assign nonnegative conductances to **every** edge under total linear cost at most \(B>0\); disconnected allocations have infinite total pairwise effective resistance.

There is exactly one global minimizer of the Kirchhoff index \(\mathcal K=\sum_{u<v}R_{uv}\), and its nonzero conductances are constant on each of the two edge classes in each blade. Set

\[
A_j=N-m_j,\quad C_j=N(m_j-1),\quad
 a_j=m_jP_j,\quad b_j=\frac{m_j-1}{2}Q_j.
\]

The optimal within-blade spectral ratio is

\[
t_j=\begin{cases}
1,&Q_j/P_j\ge 2N/M,\\
\displaystyle\sqrt{\frac{(a_j-b_j)C_j}{b_jA_j}},&Q_j/P_j<2N/M.
\end{cases}
\]

Define \(F_j=[a_j+b_j(t_j-1)](A_j+C_j/t_j)\) and \(Z=\sum_j\sqrt{F_j}\). With \(E_j=B\sqrt{F_j}/Z\), the unique optimal conductance of each spoke of blade \(j\) is

\[x_j=\frac{E_j}{a_j+b_j(t_j-1)},\]

and the unique optimal conductance of every peripheral edge of that blade is

\[y_j=\frac{x_j(t_j-1)}{m_j}.\]

The exact globally minimum Kirchhoff index is

\[\boxed{\mathcal K_*=\frac{Z^2}{B}.}\]

Consequently, **the entire peripheral clique of blade \(j\) is retained with positive conductance exactly when \(Q_j/P_j<2(M+1)/M\)**. This threshold depends only on the total peripheral-vertex count \(M\), not on \(m_j\), the other blades' prices, or \(B\). Any prescribed subset of blades can be active by choosing their price ratios on the corresponding sides of the threshold; all hub-to-peripheral edges remain positive.

## Assumptions and scope

All graphs are finite simple undirected graphs. Each blade has \(m_j\ge2\) labeled peripheral vertices; different blades meet only at the hub. The conductance of each edge is a separate decision variable. Edge prices are strictly positive, classwise constant within a blade but otherwise unrestricted across blades. The objective is the **unnormalized** sum of resistances over unordered vertex pairs, not the maximal pair resistance, effective conductance of a chosen terminal pair, or a Markov-chain spectral gap. A zero-conductance edge is allowed, but a disconnected positive-support graph has objective \(+\infty\). The formula remains valid at the exact activation boundary, where the peripheral edges of the affected blade have conductance zero. No optimization over new candidate edges or over a nonlinear cost law is asserted.

## Proof

**1. Unrestricted uniqueness and symmetry.** For a connected allocation write \(L=\sum_e w_e d_ed_e^{\mathsf T}\), with incidence vectors \(d_e\), and \(H=L+\mathbf1\mathbf1^{\mathsf T}/N\). Then \(H\) is positive definite and

\[\mathcal K=N\operatorname{tr}(H^{-1})-N.\]

Along any nonzero edge-weight perturbation \(\Delta L\), its second directional derivative is

\[2N\operatorname{tr}(H^{-1}\Delta L H^{-1}\Delta L H^{-1})>0.\]

Indeed, \(Y=H^{-1/2}\Delta LH^{-1/2}\) is nonzero symmetric, and the displayed trace equals \(2N\operatorname{tr}(Y^2H^{-1})>0\). Distinct edges of a simple graph have distinct off-diagonal Laplacian entries, so a nonzero edge-weight perturbation gives \(\Delta L\ne0\). Thus the objective is strictly convex on connected allocations. It decreases when any edge weight is increased, hence the available budget is exhausted. A connected allocation exists, the feasible box is bounded by positive prices, and the objective diverges when connectedness is lost, so the optimum exists and is unique. Independent permutations of the peripheral vertices within each blade preserve both costs and the objective. By uniqueness, every spoke in blade \(j\) receives a common value \(x_j>0\), and every peripheral edge receives a common \(y_j\ge0\).

**2. Exact pairwise resistance decomposition.** For a single blade of size \(m\), with spoke conductance \(x>0\) and peripheral conductance \(y\ge0\), the grounded Laplacian (hub removed) is \((x+my)I-y\mathbf1\mathbf1^{\mathsf T}\). Its eigenvalues are \(x\) in the constant direction and \(x+my\) in the \(m-1\) orthogonal directions. Therefore each hub-to-peripheral resistance equals

\[r_h=\frac1{mx}+\frac{m-1}{m(x+my)},\]

and each distinct peripheral pair has resistance \(2/(x+my)\). The hub is an articulation vertex; the resistance between peripheral vertices in two different blades equals the sum of their respective hub resistances. The coefficient of \(r_h\) contributed by blade \(j\) is \(m_j(N-m_j)\), and the within-blade peripheral pairs contribute \(m_j(m_j-1)/(x_j+m_jy_j)\). Collecting terms yields the identity

\[\boxed{\mathcal K=\sum_{j=1}^{k}\left(\frac{N-m_j}{x_j}+\frac{N(m_j-1)}{x_j+m_jy_j}\right).}\]

It holds also when one or more peripheral edge classes have zero conductance.

**3. Shape optimization within each blade.** The budget spent in blade \(j\) is \(E_j=a_jx_j+b_jm_jy_j\). Set \(t=(x_j+m_jy_j)/x_j\ge1\). Then \(E_j=x_j[a_j+b_j(t-1)]\) and that blade's resistance contribution is \(f_j(t)/E_j\), where

\[f_j(t)=[a_j+b_j(t-1)](A_j+C_j/t).\]

For \(t>0\),

\[f_j'(t)=b_jA_j-\frac{(a_j-b_j)C_j}{t^2}.\]

If \((a_j-b_j)C_j\le b_jA_j\), the unique minimizer on \([1,\infty)\) is \(t=1\). Otherwise the derivative changes sign once, at the stated square root greater than one, which is the unique minimizer. The sign condition reduces exactly as follows:

\[
(a_j-b_j)C_j>b_jA_j
\iff a_jC_j>b_j(A_j+C_j)
\iff \frac{Q_j}{P_j}<\frac{2N}{M},
\]

because \(A_j+C_j=m_jM\). In particular, \(a_j>b_j\) automatically in the positive-edge regime. This also settles equality and rules out an unproved interior candidate.

**4. Allocation of the common budget.** After optimizing shape, the objective is \(\sum_jF_j/E_j\) with \(E_j>0\) and \(\sum_jE_j=B\). Cauchy–Schwarz gives

\[\sum_j\frac{F_j}{E_j}\ge\frac{(\sum_j\sqrt{F_j})^2}{B},\]

with equality **only** when \(E_j\) is proportional to \(\sqrt{F_j}\). Substitution yields the stated \(E_j,x_j,y_j\). Uniqueness in steps 1, 3 and 4 proves that these are the global optimum among all individually adjustable edge weights, not merely among classwise symmetric trial weights.

## Verification

The standalone Python program `verify.py` executes 480 assertions. It computes exact rational inverses of full grounded Laplacians for 96 heterogeneous conductance configurations, compares their Kirchhoff indices against the closed formula, checks phase inequalities, and independently tests stationarity and complementary slackness across five heterogeneous budget examples. All tests passed. The numerical example with three blades \((m_1,m_2,m_3)=(2,3,4)\), unit spoke prices, peripheral prices \((1,3,2)\), and budget \(B=10\) has positive peripheral edges precisely in blades 1 and 3, and gives \(\mathcal K_*\approx70.9502722896\). This is a mixed-support case absent from equal-price windmill symmetry. Exact finite tests are corroboration; global validity and uniqueness are established by the preceding analytical steps.

## Relationship to prior work

Ghosh, Boyd and Saberi established the convex effective-resistance network design problem, strict convexity and edge-orbit symmetrization, and gave exact examples for trees, wheels and barbells, but not the present heterogeneous clique-bouquet optimum. Nikseresht and Sepasdar established block-decomposition identities for Kirchhoff indices, from which the resistance-separation step follows; they did not solve this positive-cost allocation problem. Tovar and coauthors discussed the general price-dependent edge-closure criterion and explicitly identified the three-vertex triangle threshold at price ratio three; that is the one-blade, two-peripheral-vertex special case, not the heterogeneous mixed-support result. An earlier equal-size, common-price clique-windmill result already gives the uniform-blade threshold and is **not** being re-claimed. The contribution here is the complete heterogeneous per-blade optimum, independently selectable peripheral supports and exact coupled square-root budget split. A later windmill-index paper based on unweighted resistance computations was found at abstract level; its full text remained inaccessible, so overlap cannot be excluded absolutely.

## Limitations

The result requires one shared hub, complete peripheral subgraphs, price constancy within each blade's two edge orbits, a linear conductance budget, and the sum-of-all-pairs resistance objective. It does not assert anything about multiple articulation vertices, arbitrary individual prices, nonlinear construction costs, fixed nonzero lower bounds on each edge, or alternative control/mixing objectives. The originality judgment is literature-bounded, and no independent mathematical audit has been performed.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, DOI: 10.1137/050645452, https://stanford.edu/~boyd/papers/pdf/eff_res.pdf (2008 publication; earlier 2006 conference version noted).
2. A. Nikseresht and Z. Sepasdar, *On the Kirchhoff and the Wiener Indices of Graphs and Block Decomposition*, Electronic Journal of Combinatorics 21 (2014), P1.25, DOI: 10.37236/3508, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i1p25/pdf/ (first public 2014-02-07).
3. H. Tovar et al., *Cost convexity controls the architecture of resistance-optimal networks*, arXiv:2610.03627 (2026), https://arxiv.org/abs/2610.03627 (Sections II–IV, especially the triangle closure example).
4. M. S. Sardar and S.-J. Xu, *Resistance Distance and Kirchhoff Index in Windmill Graphs*, Current Organic Synthesis 22 (2025), 159–168, DOI: 10.2174/0115701794299562240606054510 (published online 2024-07-04; abstract consulted only).
