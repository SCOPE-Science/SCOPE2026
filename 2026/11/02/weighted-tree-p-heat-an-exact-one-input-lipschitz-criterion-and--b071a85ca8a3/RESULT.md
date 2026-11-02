# Weighted-tree \(p\)-heat: an exact one-input Lipschitz criterion and universal two-input rigidity

## Finding

For every finite tree with positive vertex masses, edge conductances and edge metric lengths, the one-input Lipschitz contractivity of nonlinear \(p\)-heat is exactly characterized by one inequality per edge. A Perron–Frobenius test characterizes whether suitable edge lengths can make the evolution contractive. In contrast, the corresponding **two-input** Lipschitz nonexpansivity is impossible on every tree with at least two edges whenever \(p\ne2\), even if the one-input estimate holds. The latter rigidity is already sharp on the three-vertex path.

Specifically, with the quantities defined below, the one-input estimate for every initial function \(u\) and all \(t\ge0\) holds precisely when
\[
A_e\le D_e\qquad(e\in E).
\]
The exact maximal instantaneous upper derivative over \(\operatorname{Lip}_{\ell}(u)=1\) is
\[
\max_{e\in E}\frac{A_e-D_e}{\ell_e}.
\]
Two-input nonexpansivity for all pairs of initial functions holds precisely in either of two cases: \(|E|=1\) (any \(p>1\)), or \(p=2\) and the displayed edge inequalities hold.

## Assumptions and scope

Let \(T=(V,E)\) be a finite undirected tree with at least one edge. Assume \(m_v>0\), \(c_e>0\), and \(\ell_e>0\), with an independent positive mass at each vertex and positive conductance and metric length at each edge; the metric is the shortest-path length metric. Fix \(1<p<\infty\). The mass-weighted nonlinear heat equation is
\[
m_v\dot u_v(t)=\sum_{w\sim v}c_{vw}\,|u_w(t)-u_v(t)|^{p-2}(u_w(t)-u_v(t)).
\]
Write its solution operator as \(S_t\). Its unique global flow follows, for example, from monotonicity of the gradient of the convex \(p\)-Dirichlet energy in the weighted Euclidean space. The Lipschitz seminorm of a vertex function is
\[
\operatorname{Lip}_{\ell}(u)=\max_{e=vw\in E}\frac{|u_v-u_w|}{\ell_e}.
\]
For \(e=uv\), define
\[
D_e=c_e\left(\frac1{m_u}+\frac1{m_v}\right)\ell_e^{p-1},\quad
A_e=\sum_{\substack{f\ne e\\f\ni u}}\frac{c_f\ell_f^{p-1}}{m_u}
+\sum_{\substack{f\ne e\\f\ni v}}\frac{c_f\ell_f^{p-1}}{m_v}.
\]
The two-input assertion concerns the same Lipschitz seminorm of the *difference between two solutions*, not vertexwise maximum-norm contraction or decay of the total edge variation.

## Proof

**1. Independent tree edge coordinates.** Fix an arbitrary orientation for all edges and let \(g_e=u_v-u_u\) for the oriented edge \(e=u\to v\). Since the graph is a tree, every vector of edge differences \(g\in\mathbb R^E\) is realized by some vertex function uniquely modulo constants. Let \(\phi_p(s)=|s|^{p-2}s\). Subtracting the two endpoint equations gives, for each oriented edge \(e=u\to v\),
\[
\dot g_e=-c_e\left(\frac1{m_u}+\frac1{m_v}\right)\phi_p(g_e)
+\sum_{\substack{f\ne e\\f\ni u\text{ or }v}}\sigma_{ef}\frac{c_f}{m_{e\cap f}}\phi_p(g_f),
\]
where \(m_{e\cap f}\) is the mass at the common endpoint and each \(\sigma_{ef}\in\{-1,1\}\) is a fixed incidence sign. The line graph of a tree records precisely the nonzero off-diagonal terms.

**2. Sharp boundary test.** On the compact gradient box \(|g_f|\le r\ell_f\) for \(r>0\), at a face \(g_e=\pm r\ell_e\) the maximal possible outward velocity is exactly
\[
r^{p-1}(A_e-D_e).
\]
The upper bound is the triangle inequality. It is attained: the tree-gradient coordinates are independent, so assign each neighboring gradient its allowed endpoint and the sign making its contribution outward; other gradients can be chosen arbitrarily inside their intervals. Thus the box has nonpositive outward velocity on every face exactly when all \(A_e\le D_e\). The tangent-cone invariance criterion for this finite-dimensional continuous, uniquely solvable monotone ODE (or a first-exit argument via a vanishing outer inflation of the box) proves the forward implication. A positive outward derivative at a chosen face disproves contractivity when an inequality fails. Divide by \(\ell_e\) to obtain the exact unit-seminorm instantaneous gain. The argument is valid even when \(1<p<2\), since no derivative of \(\phi_p\) at zero is needed for this step.

**3. Positive-length design.** Put \(x_e=c_e\ell_e^{p-1}\), and define the nonnegative matrix indexed by edges
\[
B_{ef}=\begin{cases}
\dfrac{\mathbf1_{f\ni u}/m_u+\mathbf1_{f\ni v}/m_v}{1/m_u+1/m_v},&f\ne e,\quad e=uv,\\
0,&f=e.
\end{cases}
\]
The inequalities are precisely \(Bx\le x\). If there is more than one edge, the line graph is connected and \(B\) is irreducible. Hence the positive left Perron vector shows that \(Bx\le x\) with \(x>0\) forces \(\rho(B)\le1\). Conversely, for \(\rho(B)<1\), take \(x=(I-B)^{-1}\mathbf1>0\). At \(\rho(B)=1\), the positive Perron eigenvector works, and multiplying the inequality by a positive left eigenvector forces equality in every component. Thus the gauge is unique up to scale at the critical threshold. For a single edge, \(B=0\) and every positive length works. Recover metric lengths as \(\ell_e=(x_e/c_e)^{1/(p-1)}\).

For a star with hub mass \(M\) and leaf masses \(m_i\), the conditions reduce, on putting \(X=\sum_i x_i\), to
\[
\left(2+\frac{M}{m_i}\right)x_i\ge X\quad\text{for each }i.
\]
Summing the resulting lower bounds proves necessity of \(\sum_i(2+M/m_i)^{-1}\le1\), and the converse follows by selecting positive \(x_i\) with total \(X\) satisfying these bounds. This star threshold also arises for a different, edge-total-variation norm; the present theorem does not claim that numerical threshold itself is new.

**4. Two-input rigidity.** A single edge has one scalar edge-difference equation \(\dot g=-\kappa\phi_p(g)\). Since \(\phi_p\) is increasing, two scalar solutions are nonexpansive, proving the one-edge case. When \(p=2\), linearity gives \(S_tu-S_tv=S_t(u-v)\), so the two-input and one-input estimates coincide.

Now let \(|E|\ge2\) and \(p\ne2\). Select adjacent edges \(e,f\). Choose a background gradient vector \(g\) all of whose components are nonzero. The edge-flow vector field is differentiable there. Its Jacobian has diagonal coefficient \(-(p-1)c_e(1/m_u+1/m_v)|g_e|^{p-2}\), whereas its \((e,f)\) entry has nonzero magnitude \((p-1)c_f|g_f|^{p-2}/m_{e\cap f}\). Choose a perturbation \(h\) with \(|h_e|=\ell_e\), \(|h_f|=\ell_f\) and all other edge gradients zero, and choose its signs so the \((e,f)\) entry adds positively to the outward velocity at \(e\). By varying \(|g_f|\), the positive off-diagonal contribution can overwhelm the fixed diagonal loss: send \(|g_f|\to\infty\) for \(p>2\), or \(|g_f|\to0\) through nonzero values for \(1<p<2\). The derivative of the Lipschitz distance of the two flows at this initial perturbation is therefore positive for sufficiently small perturbation scale. More explicitly, the Jacobian has positive outward component at the active face \(e\), and differentiability implies a positive short-time increase for some arbitrarily close initial pairs. Since any edge vector is realized by actual vertex data, the counterexample is genuine on the tree.

On the three-vertex unit path, with edge differences \((a,b)\), the edge ODE is \(\dot a=-2\phi_p(a)+\phi_p(b)\), \(\dot b=\phi_p(a)-2\phi_p(b)\). For \(p\ne2\), choose background \((a,b)=(1,4^{1/(p-2)})\) and perturb in direction \((1,1)\). The first component of the Jacobian times this direction is \(2(p-1)>0\), directly witnessing two-input amplification. The same path nonetheless satisfies one-input contractivity for every \(p>1\).

## Verification

Run `python3 verify_tree_p_heat.py` (Python standard library). It checks the exact face-maximization identity against all endpoint sign choices on six positively weighted trees for exponents \(2,3,4\), verifies the star mass thresholds by rational arithmetic, and independently computes the short-time Jacobian witness on the three-vertex path for exponents \(1.2,1.5,2.5,3,4,5\). The run returned `ALL_TREE_P_HEAT_LIPSCHITZ_CHECKS_OK` with 678 signed faces and all listed Jacobian diagnostics passing. These finite calculations are not proofs of the universally quantified statements above; the preceding analytic arguments supply those proofs.

## Relationship to prior work

Mugnolo's *Parabolic theory of the discrete p-Laplace operator* (arXiv:1207.1996, first posted July 9, 2012) develops the general nonlinear graph evolution framework, including nonlinear semigroup and contractivity properties in vertex-function norms. The examined main text does not evaluate the edge-Lipschitz seminorm criterion, optimal length gauges, or two-input rigidity in the present theorem. Münch and Wojciechowski's *Ollivier Ricci curvature for general graph Laplacians* (arXiv:1712.00875) relates linear heat flow to Lipschitz contraction and curvature, furnishing a different-operator antecedent for the \(p=2\) case. Its examined Lipschitz/curvature equivalence does not cover the nonlinear \(p\ne2\) rigidity. The mass-balance criterion on stars coincides with an earlier *edge-total-variation* gauge threshold, but total variation is a different seminorm and does not imply this tree-wide Lipschitz criterion or its two-input obstruction.

## Limitations

The theorem concerns finite trees, positive vertex masses/conductances/metric lengths, and \(1<p<\infty\). It does not give a complete sharp amplification factor at positive times when contractivity fails; its derivative formula is instantaneous. It does not classify graphs with cycles, nonpower-law diffusion, or nonlocal generators. The finite verification does not replace the proof; prior equivalent or substantially stronger unindexed results remain an originality risk. No independent external review has been performed.

## References

- D. Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, arXiv:1207.1996, first public version July 9, 2012.
- F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, first public version December 4, 2017.
