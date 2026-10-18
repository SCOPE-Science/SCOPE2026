# Exponential polarized attractors with balanced opposing zealots

## Finding
For every finite undirected persuadable network on \(n\geq 1\) vertices, connect **each** persuadable agent to two fixed zealots holding opinions \(-1\) and \(+1\). In the sigmoidal bounded-confidence differential equation defined below, fixing any squared-distance confidence cutoff \(1<\delta<4\) and taking sufficiently large steepness \(\gamma\) produces **at least \(2^n+1\) pairwise distinct hyperbolically attracting equilibria**. One equilibrium is exactly the central state \(\boldsymbol{0}\), and each of the \(2^n\) sign vectors \(\sigma\in\{-1,+1\}^n\) has an attracting equilibrium converging to it. This lower bound holds even when the persuadable network is complete.

These polarized equilibria admit a network-dependent, first-order displacement formula. Let \(L_{\sigma}\) be the ordinary Laplacian of edges that connect persuadable vertices with the **same** sign in \(\sigma\); let \(d_i^{\mathrm{opp}}(\sigma)\) count persuadable neighbors of \(i\) with the opposite sign, and set \(b_i(\sigma)=\sigma_i(1+d_i^{\mathrm{opp}}(\sigma))\). Then, with \(r_{\gamma}=\exp[-\gamma(4-\delta)]\),
\[
\boldsymbol{x}^{\sigma}(\gamma)=\sigma-2r_{\gamma}(I+L_{\sigma})^{-1}\boldsymbol{b}(\sigma)+o(r_{\gamma}).
\]
The inverse exists for every graph and every sign vector. In particular, the leading displacement depends on both cross-camp degrees and within-camp connectivity, rather than only on the number of agents.

For the smallest case, one persuadable vertex connected to the opposing zealots, **exactly five equilibria** lie in the physical interval \([-1,1]\) for all sufficiently large \(\gamma\): \(0,\pm u_{\gamma},\pm v_{\gamma}\) with \(0<u_{\gamma}<v_{\gamma}<1\). Exactly \(0,\pm v_{\gamma}\) are asymptotically stable; \(\pm u_{\gamma}\) are unstable separatrices, and
\[
 u_{\gamma}=\sqrt{\delta}-1+
 \frac{\log\!\left(2(\sqrt{\delta}-1)/(2-\sqrt{\delta})\right)}{2\sqrt{\delta}\,\gamma}
 +O(\gamma^{-2}),\qquad
 v_{\gamma}=1-2e^{-\gamma(4-\delta)}(1+o(1)).
\]
The central basin is \((-u_{\gamma},u_{\gamma})\); initial opinions above \(u_{\gamma}\), respectively below \(-u_{\gamma}\), converge to the positive, respectively negative, outer attractor. The two basin endpoints themselves remain at the unstable equilibria.

## Assumptions and scope
Let \(H=(V,E)\) be an arbitrary fixed finite simple undirected graph with \(|V|=n\ge1\). Its \(n\) vertices are persuadable. Add exactly two fixed zealots of opinions \(-1\) and \(+1\), adjacent to every persuadable vertex, and keep all edges in \(E\). The zealots do not update. Fix real \(\delta\in(1,4)\) and \(\gamma>0\). For any two opinions \(s,t\), let
\[
 w_{\gamma}(s,t)=\frac{1}{1+\exp\{\gamma[(s-t)^2-\delta]\}}.
\]
The opinion coordinates of persuadable vertices satisfy the **normalized** continuous-time model
\[
 \dot x_i=\frac{N_i(\boldsymbol{x})}{D_i(\boldsymbol{x})},\quad
 N_i=\sum_{j:\{i,j\}\in E}w_{\gamma}(x_i,x_j)(x_j-x_i)
 +w_{\gamma}(x_i,1)(1-x_i)+w_{\gamma}(x_i,-1)(-1-x_i),
\]
\[
 D_i=\sum_{j:\{i,j\}\in E}w_{\gamma}(x_i,x_j)
 +w_{\gamma}(x_i,1)+w_{\gamma}(x_i,-1)>0.
\]
The physical opinion cube \([-1,1]^n\) is forward invariant because at each face the derivative points inward or tangent. All asymptotics fix \(H,\delta\) before sending \(\gamma\to\infty\); no universal finite steepness cutoff independent of graph size is claimed.

## Proof
**1. Strict confidence margins.** Fix a sign pattern \(\sigma\). At \(\boldsymbol{x}=\sigma\), same-sign persuadable edges and each vertex's matching zealot have squared opinion distance zero; opposite-sign edges and each vertex's opposing zealot have squared distance four. Since \(1<\delta<4\), all these distances have a positive margin from the switching surface \((s-t)^2=\delta\). Therefore on a sufficiently small fixed neighborhood \(U_{\sigma}\) of \(\sigma\), the sigmoid vector field and its first derivatives converge uniformly, exponentially in \(\gamma\), to the vector field which retains precisely same-sign edges and the matching zealot. The limiting field is
\[
 F_{\sigma,i}(\boldsymbol{x})=
 \frac{\sum_{j:\{i,j\}\in E,\,\sigma_j=\sigma_i}(x_j-x_i)+(\sigma_i-x_i)}{1+d_i^{\mathrm{same}}(\sigma)}.
\]
Its unique equilibrium is \(\sigma\). Its Jacobian is \(-D_{\sigma}^{-1}(I+L_{\sigma})\), where \(D_{\sigma}=\operatorname{diag}(1+d_i^{\mathrm{same}}(\sigma))\). As \(I+L_{\sigma}\) is symmetric positive definite, this Jacobian is similar to a symmetric negative-definite matrix; every eigenvalue is real and strictly negative. Standard local persistence of hyperbolic zeros (the inverse-function theorem, or a contraction argument after fixing neighborhoods) gives, for all sufficiently large \(\gamma\), exactly one equilibrium \(\boldsymbol{x}^{\sigma}(\gamma)\in U_{\sigma}\), approaching \(\sigma\), with the same hyperbolic attracting type. Neighborhoods of the finite set of sign vectors can be chosen mutually disjoint.

**2. First-order polarized displacement.** Put \(r=e^{-\gamma(4-\delta)}\). At \(\boldsymbol{x}=\sigma\), each opposite-sign edge or opposing zealot has weight \(r/(1+r)=r+O(r^2)\) and opinion difference \(-2\sigma_i\), while the same-sign contributions vanish. Hence
\[
 N_i(\sigma)=-2r\sigma_i(1+d_i^{\mathrm{opp}})+O(r^2).
\]
The derivative of the numerator at \(\sigma\) tends to \(-(I+L_{\sigma})\). Moreover, the derivative discrepancy tends to zero at least as fast as a constant times \(\gamma e^{-c\gamma}\) for some \(c>0\), and the established equilibrium displacement is \(O(r)\) by local inverse-function bounds. Taylor's formula yields
\[
 0=N(\boldsymbol{x}^{\sigma})=-2r\boldsymbol{b}-(I+L_{\sigma})(\boldsymbol{x}^{\sigma}-\sigma)+o(r),
\]
which gives the stated expansion. The same-sign Laplacian is positive semidefinite, so \(I+L_{\sigma}\) is invertible. The inverse also maps each fixed-sign connected component's nonnegative input to nonnegative output, showing the leading correction points toward the interior of the physical cube.

**3. Central attractor.** At \(\boldsymbol{x}=\boldsymbol{0}\) all persuadable-to-persuadable differences vanish, and the two zealot forces cancel identically, so it is an exact equilibrium for every \(\gamma\). Because \(\delta>1\), every edge and both zealot interactions have strictly subthreshold squared distances at zero. Differentiating the normalized field gives, as \(\gamma\to\infty\),
\[
 J_{\gamma}(\boldsymbol{0})\longrightarrow
 -\operatorname{diag}(d_i(H)+2)^{-1}(L_H+2I),
\]
where \(L_H\) is the persuadable graph Laplacian. The limit is similar to a negative-definite symmetric matrix. Thus \(\boldsymbol{0}\) is a hyperbolic attractor for all sufficiently large \(\gamma\). Its neighborhood can be chosen disjoint from every \(U_{\sigma}\), proving the \(2^n+1\) lower bound.

**4. Complete three-agent basin classification.** With one persuadable opinion \(x\), the sign of \(\dot x\) is that of
\[
 G_{\gamma}(x)=(1-x)W_{+}(x)-(1+x)W_{-}(x),\qquad
 W_{\pm}(x)=\frac1{1+e^{\gamma[(x\mp1)^2-\delta]}}.
\]
This is odd; \(G_{\gamma}(0)=0\). Write \(a=\sqrt\delta-1\in(0,1)\). On every compact subinterval of \((0,a)\), \(G_{\gamma}\to-2x\) in \(C^1\); on every compact subinterval of \((a,1)\), \(G_{\gamma}\to1-x\) in \(C^1\). Near zero, \(G'_{\gamma}\to-2\) uniformly; near one, \(G'_{\gamma}\to-1\) uniformly. Therefore for large \(\gamma\) there is no positive root except possibly in neighborhoods of \(a\) and \(1\), with exactly one root in the latter by derivative monotonicity and endpoint signs.

At any root sufficiently near \(a\), the root equation gives \(W_-=(1-x)W_+/(1+x)\). As \(W_+\to1\), the root's \(W_-\) stays uniformly bounded away from both zero and one. Direct differentiation then yields, **at such roots**,
\[
 G'_{\gamma}(x)=-W_+-W_-+
 2\gamma(1-x)^2W_+(1-W_+)+
 2\gamma(1+x)^2W_-(1-W_-)>0
\]
for sufficiently large \(\gamma\). Continuity and the opposite signs at the endpoints of the neighborhood give at least one such root; two distinct upward-crossing roots are impossible without an additional non-upward-crossing root, so the root is unique. Its position \(u_{\gamma}\) tends to \(a\), and the identity for \(W_-\) gives
\[
 \gamma[(1+u_{\gamma})^2-\delta]
 =\log\!\left(\frac{2a}{1-a}\right)+O(\gamma^{-1}),
\]
which, by expanding the square, gives the claimed \(u_{\gamma}\) expansion. At the outer root \(v_{\gamma}\to1\), its root equation and \(W_+\to1\) give \(1-v_{\gamma}=2e^{-\gamma(4-\delta)}(1+o(1))\). The derivative signs at \(0,u_{\gamma},v_{\gamma}\), odd symmetry, and inward-pointing boundaries complete the exhaustive list of five roots, their types and their one-dimensional basins.

## Verification
`verify_sbc.py` builds the actual normalized vector field and analytically differentiates it, then uses independent numerical root solving on graphs with one through four persuadable vertices (empty, path, complete, and one mixed example) at several steepness/cutoff choices. All \(324\) tested signed/central graph equilibrium configurations had negligible residual and negative Jacobian spectral abscissa, and finite-\(\gamma\) displacements were compared against the explicit graph-Laplacian coefficient. The program also checks scalar roots and their types over fifteen double-precision cases and independently uses arbitrary-precision bisection for twelve further scalar cases, including the exponential outer-root and reciprocal-steepness inner-root asymptotics. Run `python verify_sbc.py` with NumPy, SciPy and mpmath. The finite tests do **not** prove the infinite-family result; the argument above does.

## Relationship to prior work
Brooks, Chodrow and Porter's sigmoidal bounded-confidence model introduces this logistic confidence weight, zealots, finite-steepness stability analysis, and its large-steepness relation to a modified Hegselmann–Krause model. Their Theorem 3 provides a limiting implication for equilibria; their Conjecture 1 asks for reverse approximations; their Section 5 examines paths and a balanced-exposure setting, including stability of the central equilibrium. Those observations are not claimed as new here. The present result gives a **constructive large-steepness persistence theorem for every binary assignment on every arbitrary persuadable graph with universal balanced zealot exposure**, an exponential stable-equilibrium lower bound, an explicit first nonzero network correction and an exact minimal-case basin classification. This proves a concrete family of the reverse-approximation patterns contemplated in that work, but not its general conjecture. Earlier work on nonlinear graph consensus and tunable-sensitivity opinion dynamics studies related multistability in distinct interaction equations and does not directly yield this precise result.

## Limitations
The stable-state count is a **lower bound**, not a global classification for arbitrary \(n\ge2\); additional equilibria may exist. Both zealots must connect to every persuadable agent and have opinions exactly \(\pm1\); persuadable edges must be fixed, undirected and unweighted; \(1<\delta<4\) stays fixed. The theorem is deterministic and local in its multidimensional stability assertions; it supplies the complete basins only for the single-persuadable case. The threshold on \(\gamma\) may depend strongly on the graph and on \(\delta\). High steepness is a modeling limit rather than an empirical estimate, and multistability is not evidence about the frequency of real social opinions. As with any literature search, an unindexed equivalent construction cannot be excluded solely by the searches performed.

## References
1. H. Z. Brooks, P. S. Chodrow and M. A. Porter, *Emergence of polarization in a sigmoidal bounded-confidence model of opinion dynamics*, arXiv:2209.07004, first submitted 2022-09-15. https://arxiv.org/html/2209.07004v2 (Sections 2, 4, 5 and 6; Theorems 3 and 6, Conjecture 1).
2. M. Homs-Dones, K. Devriendt and R. Lambiotte, *Nonlinear consensus on networks: equilibria, effective resistance and trees of motifs*, arXiv:2008.12022 (2020). https://arxiv.org/abs/2008.12022 .
3. A. Bizyaeva, A. Franci and N. E. Leonard, *Nonlinear Opinion Dynamics with Tunable Sensitivity*, arXiv:2009.04332 (2020). https://arxiv.org/abs/2009.04332 .
