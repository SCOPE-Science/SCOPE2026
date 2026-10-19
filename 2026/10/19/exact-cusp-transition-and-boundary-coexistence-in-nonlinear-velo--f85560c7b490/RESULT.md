# Exact cusp transition and boundary coexistence in nonlinear velocity resetting

## Finding

A telegraph-driven inertial particle whose **velocity**, but not its active orientation, is reset at Poisson times has an exactly located local-density transition. The central one-sided slope depends on the nonlinear drag only through its slope at zero. A complementary no-tumble argument forces divergent densities at both terminal velocities over an explicit open region. These two mechanisms can coexist, producing a central cusp maximum separated by two interior minima from two singular boundary peaks. In particular, an arbitrarily small positive reset rate can create the central cusp even when the reset-free density has a strict central minimum.

Precisely, let \(\sigma_t\in\{-1,+1\}\) flip sign at rate \(\lambda>0\), and between resets let
\[
\dot V_t=\Sigma\sigma_t-g(V_t),\qquad \Sigma>0.
\]
At independent Poisson times of rate \(r>0\), set \(V_t=0\) without changing \(\sigma_t\). Under the assumptions below the unique stationary velocity density \(p_r\) is even, has finite one-sided derivatives at zero, and satisfies
\[
\boxed{\quad p_r'(0+)=\frac{r\,[c_0-r-2\lambda]}{2\Sigma^2},\quad c_0=g'(0)>0.\quad}
\]
Thus zero is a strict cusp maximum exactly when \(r+2\lambda>c_0\), and a strict local minimum if \(r+2\lambda<c_0\). At equality it remains a local minimum, with the sharper exact identity
\[
\boxed{\quad p_r''(0+)=\frac{2c_0\lambda}{\Sigma^2}p_r(0)>0.\quad}
\]
If \(v_*>0\) is the terminal speed defined by \(g(v_*)=\Sigma\), and \(c_*=g'(v_*)>0\), then
\[
\boxed{\quad r+\lambda<c_*\ \Longrightarrow\ \lim_{v\uparrow v_*}p_r(v)=+\infty.\quad}
\]
The same divergence occurs as \(v\downarrow-v_*\). Therefore the **explicit open coexistence region**
\[
\boxed{\quad r+2\lambda>c_0,\qquad r+\lambda<c_*\quad}
\]
forces a central strict cusp maximum, two divergent terminal peaks, and at least one intervening local minimum on each side. This is an existence assertion, not a proof that these are the only extrema.

For the shear-thickening drag \(g(v)=\tan v\), the inequalities are \(r+2\lambda>1\) and \(r+\lambda<1+\Sigma^2\), and are simultaneously attainable for every \(\Sigma>0\). For the shear-thinning drag \(g(v)=\tanh v\), with \(0<\Sigma<1\), the inequalities are \(r+2\lambda>1\) and \(r+\lambda<1-\Sigma^2\).

In the reset-free system \(r=0\), the stationary density satisfies
\[
\boxed{\quad p_0''(0)=\frac{2c_0(c_0-\lambda)}{\Sigma^2}p_0(0).\quad}
\]
Thus, for \(c_0/2<\lambda<c_0\), the reset-free origin is a strict minimum but every \(r>0\) sufficiently small has a strict cusp maximum there. For \(g(v)=\tan v\), those arbitrarily weak resets simultaneously retain divergent endpoint peaks. The local type change is singular at zero reset rate; no claim is made about a discontinuity of the probability law itself.

## Assumptions and scope

Assume \(g\) is odd and \(C^3\) on an open neighborhood of \([-v_*,v_*]\), strictly increasing there, and has \(g(0)=0\), \(g'(0)=c_0>0\), \(g(v_*)=\Sigma\), and \(g'(v_*)=c_*>0\). The speed interval \((-v_*,v_*)\) is forward invariant. The flip chain is symmetric, its rate \(\lambda\) is per orientation change (so its correlation rate is \(2\lambda\)), and velocity resetting preserves orientation. All claimed statements concern fixed positive \(r,\lambda,\Sigma\), except the explicitly stated comparison with \(r=0\). The initial state is immaterial for the invariant distribution.

The generator acting on smooth test functions \(h(v,s)\), for \(s=\pm1\), is
\[
\mathcal Lh=(\Sigma s-g(v))\partial_vh+\lambda[h(v,-s)-h(v,s)]+r[h(0,s)-h(v,s)].
\]
The compact-speed process has a stationary distribution; resetting couples initial velocities and the irreducible two-state flip chain couples initial orientations, yielding uniqueness. The marginal orientation law at stationarity is \((1/2,1/2)\). Its velocity marginal has a locally smooth density on each side of zero, obtained from first-order transport equations; the only interior coefficient singularity introduced by resetting is at the source point \(v=0\). In particular \(0<p_r(0)<\infty\).

## Proof

**1. Stationary transport and the central source.** Let \(p_+(v)\) and \(p_-(v)\) be joint stationary densities, normalized so that \(p=p_++p_-\). Distributionally,
\[
\frac d{dv}\bigl[(\Sigma-g)p_+\bigr]=-(r+\lambda)p_++\lambda p_-+\frac r2\delta_0,
\]
\[
\frac d{dv}\bigl[(-\Sigma-g)p_-\bigr]=-(r+\lambda)p_-+\lambda p_++\frac r2\delta_0.
\]
The source weights are \(r/2\), not \(r\), because the orientation is retained and the symmetric flip chain is fair in stationarity. Symmetry under \((v,s)\mapsto(-v,-s)\) gives \(p(v)=p(-v)\).

Write \(q=p_+-p_-\), \(J=\Sigma q-gp\), and \(K=\Sigma p-gq\). For \(v>0\), adding and subtracting the transport equations gives
\[
J'(v)=-rp(v),\qquad K'(v)=-(r+2\lambda)q(v).
\]
No flux can cross \(v_*\): \(J(v_*{-})=0\). Integrating over the positive half interval and using symmetry therefore gives \(J(0+)=r/2\). Equivalently, the source jump at zero directly gives \(\Sigma q(0+)=r/2\). Eliminating \(q=(J+gp)/\Sigma\) from \(K\) gives the exact interior identity
\[
\bigl(\Sigma^2-g(v)^2\bigr)p'(v)
=\bigl(g'(v)-r-2\lambda\bigr)J(v)
+2g(v)\bigl(g'(v)-r-\lambda\bigr)p(v),\qquad v>0.
\tag{1}
\]
The transport ODE has smooth nonvanishing coefficients near \(0+\), so its one-sided derivatives are well defined. Substituting \(g(0)=0\), \(g'(0)=c_0\), and \(J(0+)=r/2\) into (1) gives exactly
\[
p'(0+)=\frac{r(c_0-r-2\lambda)}{2\Sigma^2}.
\]
When this is negative, evenness makes zero a strict cusp maximum; when positive, it makes zero a strict local minimum. At \(r+2\lambda=c_0\), differentiate (1). The assumptions of oddness give \(g''(0)=0\). All terms vanish at \(0+\) except \(2c_0(c_0-r-\lambda)p(0)=2c_0\lambda p(0)\), hence \(\Sigma^2p''(0+)=2c_0\lambda p(0)>0\). The equality case is therefore a quadratic local minimum, not a cusp maximum.

**2. Terminal-velocity divergence from a positive trajectory subpopulation.** Consider stationary trajectories for which the most recent resetting event occurred \(t\) time units ago, the orientation was \(+1\) at that event, and no flip occurred subsequently. Such histories have unnormalized age density \((r/2)e^{-(r+\lambda)t}\,dt\), even though other histories contribute to the full stationary law. Their velocity follows the strictly increasing solution \(\phi_+(t)\) of \(\dot v=\Sigma-g(v)\), \(v(0)=0\). At \(v\in(0,v_*)\), invert this flow using
\[
T(v)=\int_0^v\frac{du}{\Sigma-g(u)}.
\]
This positive subpopulation has exact velocity density
\[
h_r(v)=\frac r2\frac{e^{-(r+\lambda)T(v)}}{\Sigma-g(v)},\qquad 0<v<v_*.
\tag{2}
\]
Therefore \(p(v)\ge h_r(v)\). Taylor expansion of the drag at the terminal point yields \(\Sigma-g(v)=c_*(v_*-v)+O((v_*-v)^2)\). Integration yields
\[
T(v)=-\frac1{c_*}\log(v_*-v)+O(1),
\]
and, because \(g\) is \(C^3\), the finite constant in the remainder has a limit. Thus for some \(C_r>0\),
\[
h_r(v)\sim C_r(v_*-v)^{(r+\lambda)/c_*-1}.
\tag{3}
\]
When \(r+\lambda<c_*\), (3) diverges. The full stationary density must diverge at least as strongly; its **complete** leading coefficient is not determined by this argument. Symmetry gives the analogous conclusion at \(-v_*\).

**3. Forced coexistence.** If \(r+2\lambda>c_0\), the first step makes \(p\) strictly decreasing immediately to the right of zero. If also \(r+\lambda<c_*\), the second step makes \(p(v)\to+\infty\) as \(v\uparrow v_*\). Continuity of \(p\) on \((0,v_*)\) then forces at least one interior local minimum; reflection forces another one on the negative half interval. The central maximum and divergent terminal peaks therefore coexist on precisely the displayed sufficient open region. No unimodality of the interior derivative is assumed.

**4. Singular zero-reset comparison.** At \(r=0\), the stationary current is identically zero and (1) becomes
\[
\frac{p_0'(v)}{p_0(v)}=\frac{2g(v)[g'(v)-\lambda]}{\Sigma^2-g(v)^2}.
\tag{4}
\]
Differentiating at zero gives \(p_0''(0)=2c_0(c_0-\lambda)p_0(0)/\Sigma^2\). Hence \(c_0/2<\lambda<c_0\) produces a smooth reset-free minimum, while for every sufficiently small \(r>0\), the exact cusp formula has \(r+2\lambda>c_0\), producing a cusp maximum. If also \(\lambda<c_*\), sufficiently small positive rates lie in the coexistence regime. For \(\tan v\), \(c_0=1\), \(c_*=1+\Sigma^2\); therefore every \(\lambda\in(1/2,1)\) has this simultaneous weak-reset behavior.

## Verification

`verify.py` is a standalone, finite-volume check of the stationary forward generator, implemented independently of the analytic elimination leading to (1). It uses a two-orientation upwind continuous-time Markov chain with explicit Poisson resets and solves its normalized stationary equations using NumPy/SciPy. The center grid cell contains the delta-source, so numerical one-sided slopes are calculated from the first and second cells strictly to the right of that source cell. Run with `python verify.py` after installing NumPy and SciPy.

With \(g(v)=\tan v\), \(\Sigma=2\), \(\lambda=0.2\), and \(r=0.4\), the predicted positive origin slope is \(0.0100000\); the 4,001-cell discretization gives \(0.0100242\). For \(r=0.7\), the predicted negative slope is \(-0.0087500\), and the discretization gives \(-0.0087331\). A separate linear-drag computation gives \(-0.0087201\) against the same \(-0.0087500\) prediction. At \(r=0.6\), the predicted quadratic curvature from the local stationary density is \(0.0223072\) and the 8,001-cell discretization gives \(0.0223878\). The endpoint density estimate increases as the mesh resolves the analytically divergent region. Five checks pass. Numerical agreement supports the formulas but does not replace the stationary transport and no-flip proofs.

## Relationship to prior work

Howlader, Mondal, and Das (arXiv:2606.00560, first publicly submitted May 30, 2026) study **this same velocity-reset and orientation-preserving model** with the nonlinear choices \(\tan v\) and \(\tanh v\). Their stationary Fokker–Planck equations agree with the starting equations here; their numerical figures describe the appearance of a cusp at the resetting point and competing side peaks. Those equations, figures, and the qualitative existence of resetting-induced cusps **are not claimed as new**. The narrower contribution here is the exact all-parameter local transition line, the positive critical quadratic derivative, a rigorously sufficient edge-coexistence window from a no-flip subpopulation, and the singular immediate cusp onset for arbitrarily weak resetting. The main source does not state these quantitative classifications or the no-flip divergence criterion.

Olsen and Löwen (arXiv:2401.12685, 2024) develop partial velocity-resetting transport coefficients for coupled systems; their stated results concern spatial diffusion and drift rather than the stationary-velocity cusp and terminal-speed coexistence of the telegraph-driven nonlinear-drag system. The reset-free nonlinear-drag stationary densities reported in earlier 2025 work are also acknowledged, and formula (4) is consistent with their central curvature behavior. These works motivate, but do not directly state, the joint classification above.

## Limitations

The coexistence condition is sufficient rather than necessary. The proof does not count all stationary-density extrema, and the outer singularities are boundary peaks rather than necessarily interior maxima. Equation (3) is the asymptotic of a **positive no-flip subpopulation**, not an asserted sharp asymptotic formula for the full density. No claim about the complete edge coefficient, small-reset minimum separation, first-passage behavior, transport diffusivity, or the uniqueness of peaks is made. General published piecewise-deterministic Markov-process theory might implicitly yield the local slope identity; novelty is assessed for the explicit coupled local and boundary classification, not for the underlying forward equations. Independent validation has not been performed.

## References

1. S. Howlader, S. Mondal, and P. Das, *Velocity Resetting of Inertial Run-and-Tumble Particles in Non-Newtonian Media: Velocity Distribution, Diffusion and First-Passage Time*, arXiv:2606.00560v1 (first submitted 2026-05-30). https://arxiv.org/abs/2606.00560
2. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (2024). https://arxiv.org/abs/2401.12685
3. S. Howlader, S. Mondal, and P. Das, *Physical Review E* **112**, 025403 (2025), as cited for reset-free shear-thickening stationary densities in reference 1.
4. S. Mondal and P. Das, *Physics of Fluids* **37**, 057114 (2025), as cited for reset-free shear-thinning stationary densities in reference 1.
