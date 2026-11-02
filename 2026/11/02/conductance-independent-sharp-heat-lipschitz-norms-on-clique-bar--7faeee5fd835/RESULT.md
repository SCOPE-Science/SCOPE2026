# Conductance-independent sharp heat-Lipschitz norms on clique barbells

## Finding
For every integer \(m\geq2\), join two vertex-disjoint copies of \(K_m\) by one edge between distinguished vertices \(a\) and \(b\). Give the bridge and each edge incident with a distinguished vertex conductance one. On each of the two sets of \(m-1\) remaining vertices, choose arbitrary symmetric internal conductances \(c_{ij}\geq1\), independently of one another, without any uniform upper bound. Give every graph edge **metric length one**, regardless of its conductance. Set \(L_cf(x)=\sum_{y\sim x}c_{xy}(f(x)-f(y))\), \(H_t=\exp(-tL_c)\), and \(\operatorname{Lip}(f)=\max_{xy\in E}|f(x)-f(y)|\). The norm on the quotient by constants is
\[
\Lambda_m(t)=\sup_{\operatorname{Lip}(f)>0}\frac{\operatorname{Lip}(H_tf)}{\operatorname{Lip}(f)}
=A_m e^{-\alpha_m t}-B_m e^{-\beta_m t}\qquad(t\geq0),
\]
where
\[
\Delta_m=\sqrt{(m+2)^2-8},\quad
\alpha_m=\frac{m+2-\Delta_m}{2},\quad
\beta_m=\frac{m+2+\Delta_m}{2},\quad
A_m=\frac{3m-2-\alpha_m}{\Delta_m},\quad
B_m=\frac{3m-2-\beta_m}{\Delta_m}>0.
\]
In particular, this is completely **independent of all internal clique conductances**. For every \(t>0\), the unique maximizing edge is the bridge; all real nonconstant extremizers, up to nonzero scalar multiplication and addition of a constant, are the function equal to \(2\) on left peripheral vertices, \(1\) at \(a\), \(0\) at \(b\), and \(-1\) on right peripheral vertices.

For \(m=2\), \(\Lambda_m(t)<1\) at every \(t>0\). For every \(m\geq3\), the profile strictly rises above one, has a unique maximum at
\[
t_m^*=\frac{1}{\Delta_m}\log\left(\frac{\beta_m B_m}{\alpha_m A_m}\right)>0,
\qquad
\Lambda_m(t_m^*)=A_m\left(1-\frac{\alpha_m}{\beta_m}\right)e^{-\alpha_m t_m^*},
\]
and then strictly decreases. Furthermore,
\[
t_m^*=\frac{2\log m-\log3}{m}+O\!\left(\frac{\log m}{m^2}\right),\qquad
\Lambda_m(t_m^*)=3-\frac8m+O\!\left(\frac{\log m}{m^2}\right).
\]
Consequently the sharp supremum over these graphs, all admissible internal conductances, and all times is \(3\), although no finite graph and time attain it.

## Assumptions and scope
The graph has exactly \(2m\) vertices, and its two cliques have equal order. The bridge and hub-spoke heat conductances are exactly one. Internal peripheral-peripheral heat conductances are arbitrary real values at least one; they need not be symmetric between the cliques or constant within either clique. The Laplacian is the **unnormalized** symmetric conductance Laplacian. The Lipschitz seminorm uses the **unweighted graph metric**, equivalently unit edge-length constraints. All functions are real. The semigroup is positive, conservative, and acts on the complete finite vertex set.

## Proof
Write the left peripheral vertices as \(u_1,\ldots,u_{m-1}\) and the right as \(v_1,\ldots,v_{m-1}\). For any time-evolved function \(f_t=H_tf\), introduce oriented gradients
\[
g_i(t)=f_t(u_i)-f_t(a),\quad h_j(t)=f_t(b)-f_t(v_j),\quad z(t)=f_t(a)-f_t(b).
\]
A direct subtraction of the heat equations, without assuming any peripheral symmetry, gives
\[
\begin{aligned}
g_i'&=-mg_i+z+\sum_{\ell\ne i}(c^L_{i\ell}-1)(g_\ell-g_i),\\
h_j'&=-mh_j+z+\sum_{\ell\ne j}(c^R_{j\ell}-1)(h_\ell-h_j),\\
z'&=\sum_{i=1}^{m-1}g_i+\sum_{j=1}^{m-1}h_j-2z.
\end{aligned}
\tag{1}
\]
All off-diagonal entries of this \((2m-1)\)-dimensional system are nonnegative, since \(c_{ij}-1\geq0\). Its directed coupling graph is strongly connected through \(z\), so its matrix exponential has **strictly positive entries** at each positive time (shift the diagonal to obtain an irreducible nonnegative matrix and use its exponential series).

The constant-gradient ansatz \(g_i=h_j=a(t)\), \(z=b(t)\) is invariant for every choice of internal conductances. Its solution with \(a(0)=b(0)=1\) obeys
\[
a'=-ma+b,\qquad b'=2(m-1)a-2b.\tag{2}
\]
Both coordinates are strictly positive. Because the system (1) has a positive exponential, the coordinatewise order interval with initial \(|g_i(0)|,|h_j(0)|,|z(0)|\leq L\) is propagated into
\[
|g_i(t)|,|h_j(t)|\leq La(t),\qquad |z(t)|\leq Lb(t),\tag{3}
\]
for \(L=\operatorname{Lip}(f)\). For \(w=b-a\), (2) yields
\[
w'=(3m-5)a-3w,\qquad w(0)=0.
\]
Since \(m\geq2\) and \(a(t)>0\), one has \(b(t)>a(t)\) whenever \(t>0\).

It remains essential to bound the edges **inside** the cliques, which are not included in the hub gradients as individual norm constraints. In vector notation, for the left peripheral gradients, (1) reads \(g'=(-mI+Q_L)g+z\mathbf1\), where \(Q_L\) is the Markov generator with symmetric off-diagonal rates \(c^L_{ij}-1\) and row sums zero. Since \(Q_L\mathbf1=0\), the forcing contributes the same scalar to every coordinate. Thus
\[
\max_{i,j}|g_i(t)-g_j(t)|\leq e^{-mt}\max_{i,j}|g_i(0)-g_j(0)|\leq e^{-mt}L,\tag{4}
\]
because \(e^{tQ_L}\) is a stochastic matrix and therefore contracts oscillation. The same holds on the right. The last inequality uses the fact that each peripheral set is a clique of unit **metric** edge lengths. From \(b'=2(m-1)a-2b>-2b\), \(b(t)>e^{-2t}\geq e^{-mt}\) for \(t>0\). Together with (3) and \(b>a\), this proves that **all edges** have heat gradient at most \(Lb(t)\), with strict improvement on every nonbridge edge for positive time.

For the explicit function \(f_*=2\) on the left periphery, \(f_*(a)=1\), \(f_*(b)=0\), \(f_*=-1\) on the right periphery, all gradients \(g_i(0),h_j(0),z(0)\) equal one and \(\operatorname{Lip}(f_*)=1\). Its evolved gradients solve (2), so the bridge gradient equals \(b(t)\); equality in the upper bound is attained. Conversely, for \(t>0\), a norm-attaining input must attain equality in the bridge bound (3). Strict positivity of every entry in the bridge row of the gradient propagator forces **all** initial oriented gradients to have modulus \(L\) and the same sign. These edge differences uniquely determine \(f\) modulo constants, giving precisely the stated extremizers.

The characteristic polynomial of the negative of the system matrix in (2) is \(\xi^2-(m+2)\xi+2\). Solving for \(b(0)=1\), \(b'(0)=2m-4\) gives the displayed two-exponential formula. In particular \(A_m-B_m=1\). The ratio \(\beta_m B_m/(\alpha_m A_m)\) exceeds one exactly when \(m>2\), since \(b'(0)=2m-4\); differentiation of the exponential formula shows one strict maximum for \(m\geq3\) and monotone decrease for \(m=2\).

For large \(m\), algebraic expansion yields \(\alpha_m=2/m+O(m^{-2})\), \(\beta_m=m+2+O(m^{-1})\), \(A_m=3-8/m+O(m^{-2})\), \(B_m=2-8/m+O(m^{-2})\). Inserting these into the exact peak-time identity gives the stated asymptotics. Finally, the graph diameter is three, hence \(\operatorname{osc}(f)\leq3\operatorname{Lip}(f)\) and \(\operatorname{Lip}(H_tf)\leq\operatorname{osc}(H_tf)\leq\operatorname{osc}(f)\), providing the universal bound of three. It is strict at positive time for any fixed finite graph because all heat-kernel entries are positive and \(\operatorname{osc}(H_tf)<\operatorname{osc}(f)\) for nonconstant \(f\); the asymptotic peaks approach three, proving sharpness without attainment.

## Verification
The standalone file `verify_weighted_barbell.py` verifies (1) **exactly over rational arithmetic**, on every coordinate basis vector for 15 independently heterogeneous weighted graphs with sizes \(m=2,3,4,5,6\). It separately computes the full vertex heat evolution by nonnegative uniformization, checks the two-exponential bridge formula and compares all edge gradients for three positive times per graph. It also checks five peak cases. Execution result: `CHECK_OK exact_gradient_intertwining_basis=120 weighted_graphs=15 independent_heat_edge_comparisons=45 root_asymptotic_cases=5`. Finite checks are corroboration, not a proof for all conductances, orders, or times; the proof is analytic above.

## Relationship to prior work
Ollivier's transport curvature framework relates graph-metric Wasserstein transport and contraction. Chafaï–Joulin develop gradient intertwining for birth-death semigroups, and Münch–Wojciechowski establish general graph heat-gradient/transport equivalences. The present theorem uses a direct finite gradient system but adds **exact global norm, arbitrary heterogeneous clique-interior conductance invariance, complete equality cases, unique temporal amplification peak, and sharp limiting factor three** for the two-clique bridge family. A numerically identical two-mode scalar law can occur on sparse double-star graphs; the new statement is not that scalar identity in isolation, but its persistence under a family of independently adjustable **extra heat edges that are also metric edges**, with a full Lipschitz and uniqueness proof. No priority claim is made beyond the specific comparisons reported in the review.

## Limitations
The conductance lower bound \(c_{ij}\geq1\), unit hub and bridge conductances, unit graph metric, equal clique orders, real functions, and unnormalized Laplacian are essential hypotheses of the stated result. No extension to arbitrary weights, unequal clique sizes, normalized generators, or different metric lengths has been established. General heat/transport frameworks may contain unindexed equivalent specializations; this self-review analysis is not independent publication-priority certification.

## References
1. Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, first public arXiv version 2007-01-30, `arXiv:math/0701886v1`, https://arxiv.org/abs/math/0701886.
2. Djalil Chafaï and Aldéric Joulin, *Intertwining and commutation relations for birth-death processes*, first public arXiv version 2010-11-10, `arXiv:1011.2331v1`, https://arxiv.org/abs/1011.2331.
3. Florentin Münch and Radosław K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: heat equation, Laplacian comparison, non-explosion*, first public arXiv version 2017-12-04, `arXiv:1712.00875v1`, https://arxiv.org/abs/1712.00875.
