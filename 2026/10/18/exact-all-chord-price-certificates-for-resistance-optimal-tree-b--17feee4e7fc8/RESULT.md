# Exact all-chord price certificates for resistance-optimal tree backbones

## Finding

Consider any tree \(T=(V,E)\) on \(n\ge4\) labeled vertices and any finite set \(F\) of additional simple edges not in \(E\). Each tree edge has a positive linear price \(c_e\), and each possible chord \(uv\in F\) has a positive price \(p_{uv}\). Conductances are chosen independently and nonnegatively with exact expenditure \(B>0\). The criterion below characterizes exactly when *every* available chord receives zero conductance in the unique minimizer of \(J=\operatorname{tr}(L^+)\).

Delete a tree edge \(e\) and let \(k_e\) be either component size; define
\[
b_e=k_e(n-k_e),\qquad S=\sum_{e\in E}\sqrt{b_ec_e}.
\]
For a candidate chord \(uv\), list tree-path edges \(e_1,\ldots,e_\ell\) in order from \(u\) to \(v\). Upon deleting \(e_i\), let \(s_i\) be the size of the component containing \(u\); then \(s_1<\cdots<s_\ell\). Define the explicit price threshold
\[
\Theta_{uv}=\sum_{i=1}^{\ell}c_{e_i}
+2\sum_{1\le i<j\le\ell}
\sqrt{\frac{s_i(n-s_j)}{s_j(n-s_i)}}\sqrt{c_{e_i}c_{e_j}}.
\]
**The tree-backbone theorem:** The unique global optimum over all admissible graph edges has every chord zero **if and only if**
\[
p_{uv}\ge\Theta_{uv}\quad\text{for every }uv\in F.
\]
In that regime, all tree edges are positive, with the uniquely optimal allocation and value
\[
g_e^*=\frac{B}{S}\sqrt{\frac{b_e}{c_e}},\qquad
J^*=\frac{S^2}{nB}.
\]
If *any* price is strictly below its threshold, the tree-only allocation is strictly improvable and every global optimum invests positive conductance in at least one available chord; the claim does not determine which chords then enter. Equality \(p_{uv}=\Theta_{uv}\) is included in the sparse regime. Every threshold is independent of the scale \(B\), and simultaneous candidate chords need no extra pairwise interaction tests for deciding whether the original tree stays optimal.

For a star on \(m\ge3\) leaves, with spoke prices \(c_i\), the criterion becomes
\[
p_{ij}\ge c_i+c_j+\frac2m\sqrt{c_ic_j}
\]
for all offered leaf-to-leaf edges. Uniform spoke prices give the sharp threshold \(2+2/m\). The familiar three-vertex triangle threshold \(3\) is previously known and is not claimed as a new discovery. For the four-vertex path with unit tree prices, the end-to-end chord threshold is \(11/3+4/\sqrt3\).

## Assumptions and scope

The base \(T\) is an undirected simple tree on \(n\ge4\) vertices. Offered extra edges form a subset of the missing edges of the complete graph on the same vertices. Costs \(c_e,p_{uv}\) and total budget \(B\) are strictly positive reals. Each conductance \(g_e\ge0\) incurs its own listed price times its conductance, with total cost exactly \(B\). The weighted Laplacian is \(L(g)=\sum_e g_e(e_a-e_b)(e_a-e_b)^\mathsf T\). A disconnected positive-conductance support is assigned infinite cost; for connected designs \(J(g)=\operatorname{tr}(L(g)^+)\), one \(n\)-th of the total unordered-pair effective resistance. The theorem has no assertion about the full active set outside the tree-support region.

## Proof

**1. Exact tree optimum.** Each unordered vertex pair uses a unique tree path. A tree edge \(e\) lies on exactly \(b_e=k_e(n-k_e)\) such paths, so
\[
J_T(g)=\frac1n\sum_{e\in E}\frac{b_e}{g_e}.
\]
Cauchy–Schwarz and \(\sum_E c_eg_e=B\) imply
\[
\left(\sum_E\frac{b_e}{g_e}\right)B\ge
\left(\sum_E\sqrt{b_ec_e}\right)^2=S^2.
\]
Equality is unique, forcing the positive tree weights \(g_e^*=(B/S)\sqrt{b_e/c_e}\), and gives \(J_T^*=S^2/(nB)\). Write \(\lambda=S^2/(nB^2)\); differentiation at these weights gives \(-\partial J/\partial g_e=\lambda c_e\) for every tree edge.

**2. Chord derivative as a tree-path cut sum.** For any edge-incidence vector \(d=e_u-e_v\), the resolvent/pseudoinverse derivative is
\[
-\frac{\partial J}{\partial g_{uv}}=\|L^+d\|_2^2.
\]
Let \(C_i\) be the component containing \(u\) after deleting path edge \(e_i\), with size \(s_i\). These sets are nested in increasing order. The unit-current potential from \(u\) to \(v\), centered to have mean zero, is exactly
\[
L^+d=\sum_{i=1}^{\ell}\frac1{g_{e_i}}
\left(\mathbf1_{C_i}-\frac{s_i}{n}\mathbf1\right).
\]
Indeed, the Laplacian of each cut indicator produces current only across the unique deleted tree edge; summing these unit currents telescopes to \(e_u-e_v\). For nested cuts,
\[
\left\langle\mathbf1_{C_i}-\frac{s_i}{n}\mathbf1,
\mathbf1_{C_j}-\frac{s_j}{n}\mathbf1\right\rangle
=\frac{\min(s_i,s_j)\bigl(n-\max(s_i,s_j)\bigr)}n.
\]
Thus, at the tree-only optimizer,
\[
\|L^+d\|_2^2
=\frac{S^2}{nB^2}
\sum_{i,j=1}^{\ell}\frac{\min(s_i,s_j)\bigl(n-\max(s_i,s_j)\bigr)}{\sqrt{s_i(n-s_i)s_j(n-s_j)}}\sqrt{c_{e_i}c_{e_j}}
=\lambda\Theta_{uv}.
\]
The diagonal terms equal \(c_{e_i}\); each off-diagonal pair combines into the displayed explicit threshold.

**3. Global optimization certificate and sharpness.** On any connected weighted support set
\[
J(g)=\operatorname{tr}\left(L(g)+\frac1n\mathbf1\mathbf1^\mathsf T\right)^{-1}-1.
\]
The inverse trace is convex in its positive-definite matrix argument. Moreover, for a nonzero change in edge conductances, the Laplacian change \(H\) is nonzero (different simple edges have unique off-diagonal entries), and the second directional derivative is
\[
2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0,
\qquad X=L(g)+\mathbf1\mathbf1^\mathsf T/n.
\]
Positivity follows by diagonalizing \(X\) and writing the trace as a strictly positive sum of squared entries of \(H\), each multiplied by positive eigenvalue denominators. Therefore \(J\) is strictly convex on every connected feasible line segment, and the global minimizer, whose existence follows from the compact budget simplex and divergence at disconnection, is unique.

At the candidate tree optimum, the gradient equals \(-\lambda c_e\) on each positive tree edge and \(-\lambda\Theta_{uv}\) on each inactive chord. The Karush–Kuhn–Tucker conditions with exact budget require \(-\lambda\Theta_{uv}+\lambda p_{uv}\ge0\) for every inactive chord, precisely \(p_{uv}\ge\Theta_{uv}\). By convexity these conditions are sufficient for global optimality; by strict convexity no distinct optimum exists, including at equality. If some \(p_{uv}<\Theta_{uv}\), add a small conductance \(\delta\) on that chord and multiply every tree conductance by \(1-p_{uv}\delta/B\). The budget stays exact, while the first derivative of \(J\) at zero is \(\lambda(p_{uv}-\Theta_{uv})<0\), establishing strict improvement. If every chord were still zero, the unique optimum would be the tree-only one, contradiction.

**4. Specializations.** On a star with \(m\) leaves, each length-two path has cut sizes \(1,m\), so the mixed coefficient is \(1/m\), giving \(\Theta_{ij}=c_i+c_j+2\sqrt{c_ic_j}/m\). On the four-vertex path, the ordered cut sizes are \(1,2,3\), giving \(\Theta=3+2(1/\sqrt3+1/3+1/\sqrt3)=11/3+4/\sqrt3\) when all three prices are one.

## Verification

Run \(\texttt{python3 verify_tree.py}\) with Python 3 (standard library only). The program constructs path, star and seeded Prüfer trees for each order \(4\) through \(8\); chooses integer costs giving rational tree-optimal weights; computes exact rational Laplacian pseudoinverses, verifies all tree gradients and full chord derivatives against the cut formula, checks the exact budget, and constructs strict improvements for subthreshold chord prices. Executed output: \(\texttt{VERIFY_OK exact_rational_assertions= 1900}\). These finitely many exact checks are independent confirmations, **not** an infinite proof; universality rests on Steps 1–3.

## Relationship to prior work

Ghosh, Boyd and Saberi establish convex optimization of total effective resistance, graph-Laplacian derivatives and closed-form tree conductances for **uniform conductance prices** (2006 conference version; 2008 journal version). Those are foundational premises, not claimed new here. The later study *Cost convexity controls the architecture of resistance-optimal networks* explicitly gives heterogeneous-edge-price marginal/KKT closure and the exact three-vertex triangle threshold \(3\); this theorem neither reclaims that threshold nor claims to invent the general KKT test. The distinct result is an **explicit, necessary-and-sufficient, all-chord combinatorial price region for any tree with arbitrary positive tree prices**: cut sizes, nested-path mixed terms, and unique global support at every threshold equality. This also gives a nonuniform-star formula and multi-edge path interactions. Exact prior-equivalence remains a research risk because the result is derived from existing general sensitivity theory.

## Limitations

The result determines exactly when the original tree remains the unique global optimum, not the optimal active graph or conductances after that region is left. Price is linear in assigned conductance; nonlinear costs, mandatory lower bounds, directed edges, and disconnected base graphs are excluded. This is self-reviewed only; there has been no independent audit. The possibility of an equivalent specialization in unindexed literature is not ruled out by search.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006; SIAM Review 50 (2008), 37–66. DOI: 10.1137/050645452. https://web.stanford.edu/~boyd/papers/eff_res.html
2. *Cost convexity controls the architecture of resistance-optimal networks*, preprint, first public version 2 October 2026, arXiv:2610.03627. https://arxiv.org/abs/2610.03627
3. Y. Yi, L. Shan, H. Li, Z. Zhang, *Biharmonic Distance Related Centrality for Edges in Weighted Networks*, IJCAI 2018. https://www.ijcai.org/proceedings/2018/503
