# Sharp clique-factor dominance and limiting norms for canonical graph Hodge projections

## Finding
Let \(H\) be any finite connected simple graph with at least two vertices, and let \(G_m=H\square K_m\) be its Cartesian product with the unweighted \(m\)-vertex clique. On the real coordinate edge space \(\ell_1(E(G_m))\), let \(Q_m\) denote the Euclidean orthogonal cut-space projector and \(C_m=I-Q_m\) the cycle-space projector. For every integer \(m\ge4\),
\[
\boxed{\|C_m\|_{1\to1}-\|Q_m\|_{1\to1}\ge\frac{m-4}{m+2}.}
\]
The bound is **sharp for every \(m\ge4\)**, and equality holds **if and only if \(H=K_2\)**. In particular, the cycle projector dominates strictly for all \(m\ge5\) and for \(m=4\) unless \(H=K_2\). The clique size four is the least size with universal nonnegative dominance: for \(H=K_2\) and \(m=3\), the norm difference is \(-2/15\).

In addition, write \(Q_H\) for the canonical orthogonal cut projector on the edge space of \(H\). Then, with \(H\) fixed and \(m\to\infty\),
\[
\boxed{\lim_{m\to\infty}\|Q_m\|_{1\to1}=2+\|Q_H\|_{1\to1},\qquad
\lim_{m\to\infty}\|C_m\|_{1\to1}=3+\|Q_H\|_{1\to1}.}
\]
By matrix symmetry, every endpoint norm here is also the \(\ell_\infty\)-operator norm. The statements concern canonical orthogonal projectors, not minimum norms over all projections onto the same subspaces.

## Assumptions and scope
Every graph is finite, simple, connected, and unweighted. All edge-coordinate spaces are real, with an arbitrary fixed orientation. For a graph \(X\), write \(D_X\) for its vertex-edge incidence matrix, \(L_X=D_XD_X^{\mathsf T}\), and \(Q_X=D_X^{\mathsf T}L_X^+D_X\). Thus \(Q_X\) is the orthogonal projector onto \(\operatorname{im}(D_X^{\mathsf T})\); \(C_X=I-Q_X\) projects onto \(\ker D_X\). All matrix inverses below are ordinary inverses of positive-definite matrices, while \(L_X^+\) denotes the Moore--Penrose inverse.

## Proof
**1. Product Laplacian and diagonal bounds.** Let \(n=|V(H)|\), \(L=L_H\), \(P_0=J_m/m\), and \(P_1=I_m-P_0\). Because \(L_{K_m}=mP_1\), the product Laplacian and its pseudoinverse satisfy
\[
L_{G_m}=L\otimes I_m+I_n\otimes mP_1,\qquad
L_{G_m}^{+}=L^{+}\otimes P_0+(L+mI_n)^{-1}\otimes P_1.
\]
Set \(S_m=(L+mI_n)^{-1}\). For a horizontal edge \((u,a)(v,a)\), set \(b=e_u-e_v\). The projector diagonal, equivalently the unit-resistance effective resistance across that edge, is
\[
R_{\mathrm{hor}}=\frac{b^{\mathsf T}L^+b}{m}+\frac{m-1}{m}\,b^{\mathsf T}S_mb.
\]
Since \(Q_H\) is an orthogonal projection, \(0<b^{\mathsf T}L^+b\le1\). Since \(L=\sum_{f\in E(H)}b_fb_f^{\mathsf T}\succeq bb^{\mathsf T}\), inversion reverses the positive-definite order and Sherman--Morrison gives
\[
b^{\mathsf T}S_mb\le b^{\mathsf T}(mI_n+bb^{\mathsf T})^{-1}b=\frac2{m+2}.
\]
Consequently \(R_{\mathrm{hor}}\le3/(m+2)\). If \(H\ne K_2\), there is another edge incident to an endpoint of \(uv\). The inverse comparison is then strict on \(b\), so \(R_{\mathrm{hor}}<3/(m+2)\).

For a vertical clique edge \((x,a)(x,b)\), the product pseudoinverse instead yields \(R_{\mathrm{vert}}=2(S_m)_{xx}\). The inequality \(S_m\preceq I_n/m\) gives \(R_{\mathrm{vert}}\le2/m\), strictly for every connected \(H\) with at least two vertices. At \(m\ge4\), \(2/m\le3/(m+2)\). Therefore every product edge \(e\) satisfies
\[
0\le(Q_m)_{ee}\le\frac3{m+2},
\]
with the upper bound strict at all edges when \(H\ne K_2\).

**2. Endpoint norm dominance.** For any orthogonal projection matrix \(Q\), write \(C=I-Q\), so \(0\le Q_{ee}\le1\). In the \(e\)-th coordinate column, the off-diagonal entries of \(C\) equal the negatives of those of \(Q\), while the diagonal entry is \(1-Q_{ee}\ge0\). Hence, exactly,
\[
\|C\delta_e\|_1=\|Q\delta_e\|_1+1-2Q_{ee}.
\]
The previous step implies, for all \(m\ge4\) and all \(e\in E(G_m)\),
\[
\|C_m\delta_e\|_1\ge\|Q_m\delta_e\|_1+\frac{m-4}{m+2}.
\]
Taking maxima over the finite edge-coordinate basis proves the displayed sharp inequality. For \(H\ne K_2\), every column inequality is strict; taking maxima preserves strictness because the edge set is finite.

**3. Sharpness and the critical dimension.** If \(H=K_2\), then \(L=\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\). The horizontal and vertical \(\ell_1\) column norms of \(Q_m\) are, respectively,
\[
\frac{3m}{m+2},\qquad 2-\frac4{m(m+2)},
\]
and those of \(C_m\) are
\[
\frac{4(m-1)}{m+2},\qquad3-\frac4m.
\]
Direct subtraction shows that the horizontal columns dominate for both projectors when \(m\ge4\). Thus
\[
\|Q_m\|_{1\to1}=\frac{3m}{m+2},\qquad
\|C_m\|_{1\to1}=\frac{4(m-1)}{m+2},
\]
and their difference is exactly \((m-4)/(m+2)\). At \(m=3\), the horizontal cut column gives \(\|Q_3\|=9/5\), while the vertical cycle column gives \(\|C_3\|=5/3\), producing the negative difference \(-2/15\).

**4. Complete transfer-current formula and limiting norms.** Orient the base edges and write their incidence vectors as \(b_e\). Let \(T=Q_H\), \(h_{fe}=b_f^{\mathsf T}S_mb_e\), and \(p_{xe}=(S_mb_e)_x\). For a horizontal product edge of base type \(e\), the absolute column sum of \(Q_m\), obtained from the two fiber eigenspaces, is exactly
\[
A_e(m)=\sum_{f\in E(H)}\left|\frac{T_{fe}}m+\frac{m-1}{m}h_{fe}\right|
+\frac{m-1}{m}\sum_{f\in E(H)}|T_{fe}-h_{fe}|
+(m-1)\sum_{x\in V(H)}|p_{xe}|.
\]
For a vertical clique edge in the fiber over \(x\), the corresponding absolute column sum is
\[
V_x(m)=\frac{2(m-1)}m+2\sum_{f\in E(H)}|b_f^{\mathsf T}S_me_x|.
\]
Indeed, \(S_m\) has nonnegative entries and column sums \(1/m\), so the total vertical contribution in the second formula is \(2(m-1)/m\); the remaining terms count horizontal copies. Since \(mS_m\to I_n\), for each base edge \(e\),
\[
A_e(m)\longrightarrow 2+\sum_{f\in E(H)}|T_{fe}|,\qquad V_x(m)\longrightarrow2.
\]
Every product-edge diagonal of \(Q_m\) tends to zero. Applying the exact column identity from step 2 gives cycle-column limits \(3+\sum_f|T_{fe}|\) horizontally and \(3\) vertically. The finite base cut projector is nonzero, so \(\|Q_H\|_{1\to1}\ge1\). Taking maxima of finitely many base types proves both asymptotic claims. Symmetry of \(Q_m\) and \(C_m\) implies equality of their \(\ell_1\) and \(\ell_\infty\) operator norms.

## Verification
The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It computes graph projectors from grounded Kirchhoff systems, independently derives the product columns from a small base-graph resolvent, and compares the resulting exact product operator norms from both constructions. It passed 129 tests over all connected labeled graphs on two, three, and four vertices, 18 full-product versus compressed calculations, every sharp case \(4\le m\le64\) for \(H=K_2\), the \(m=3\) counterexample, and six large-clique rational checks. Finite computations corroborate the algebraic proof but do not substitute for its universal quantifiers or asymptotic limit.

Run `python verify.py` in the directory containing this result and `verify.py`.

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii (2023) introduce and investigate invariant and minimum-norm cycle projections and compute particular Hamming-cube endpoint norms; the elementary complementary-column identity is consistent with their Section 2.7. Their result does not state a sharp universal comparison for arbitrary \(H\square K_m\) or identify the limiting dependence on the base-graph cut norm. Bollobás and Brightwell (1997) study electrical resistances and random walks on products, including a hitting-probability comparison for products with cliques; the available abstract does not establish the present endpoint operator-norm inequalities. The previously studied special product \(K_2\square K_m\) supplies sharpness here, but a single special case cannot imply a uniform all-base-graph inequality or both arbitrary-base limiting formulas.

## Limitations
The new inequalities concern the **canonical Euclidean orthogonal projections** on real, unweighted, finite Cartesian products, not arbitrary norm-minimizing projections. The large-clique limits hold with the base graph fixed; no uniformity in a simultaneously growing base graph is claimed. The exact \(\ell_p\) norms at intermediate exponents are not evaluated. An older electrical-network paper on graph products was available in abstract but not full text, leaving a bibliographic comparison risk; no exhaustive novelty certification is asserted.

## References
1. Stephen J. Dilworth, Denka Kutzarova, and Mikhail I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first posted 2023-05-21), https://arxiv.org/abs/2305.12582. See Sections 1.1, 1.4, 2.6, 2.7 and Corollary 60.
2. Béla Bollobás and Graham Brightwell, *Random walks and electrical resistances in products of graphs*, Discrete Applied Mathematics 73 (1997), 69–79, https://doi.org/10.1016/S0166-218X(96)00002-9. Comparison is limited to the publicly accessible abstract.
