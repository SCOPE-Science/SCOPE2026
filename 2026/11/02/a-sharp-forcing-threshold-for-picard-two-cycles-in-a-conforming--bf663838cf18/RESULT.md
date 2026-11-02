# A sharp forcing threshold for Picard two-cycles in a conforming Kirchhoff finite element step

## Finding

A genuine one-degree-of-freedom conforming piecewise-linear finite element discretization of a two-dimensional Kirchhoff wave equation has a **unique nonlinear implicit step at every nonnegative forcing amplitude**, but its prescribed undamped Picard solver has a sharp transition from global fixed-point convergence to an attracting period-two orbit.

More precisely, on the mesh and with the data below, the Picard coefficient is
\[
x_{\ell+1}=F_g(x_\ell)=\frac{g+2}{2(1+x_\ell^2)},\qquad x_0=1,\qquad g\ge0.
\]
The nonlinear implicit equation has exactly one real solution, characterized by
\[
x_*+x_*^3=\frac{g+2}{2}.
\]
For \(0\le g\le2\), every nonnegative Picard starting value converges to \(x_*\). For \(g>2\), every nonnegative starting value other than \(x_*\) converges alternately to the unique attracting primitive two-cycle
\[
p_g=\frac{g+2-\sqrt{(g+2)^2-16}}4,\qquad
q_g=\frac{g+2+\sqrt{(g+2)^2-16}}4.
\]
Its two-step multiplier is exactly \(16/(g+2)^2<1\). In particular, the source-prescribed initial guess \(x_0=1\) lies below \(x_*\) when \(g>2\), and hence its even iterates tend to \(p_g\), and its odd iterates to \(q_g\). Neither limit solves the implicit nonlinear equation.

At \(g=4\), the cycle is \(((3-\sqrt5)/2,(3+\sqrt5)/2)\), with two-step multiplier \(4/9\). The half-scaled equation residual \(r(x)=x+x^3-3\) has nonzero alternating limits
\[
r(p_4)=\frac{15-9\sqrt5}{2},\qquad r(q_4)=\frac{15+9\sqrt5}{2}.
\]
Moreover, for \(g\to\infty\), the upper cycle value is asymptotic to \((g+2)/2\) while the genuine implicit solution is asymptotic to \(((g+2)/2)^{1/3}\). Thus the ratio of the spurious upper iterate to the correct solution diverges on the scale \(((g+2)/2)^{2/3}\).

## Assumptions and scope

Let \(\Omega=(0,1)^2\), triangulated by joining its center \((1/2,1/2)\) to each of the four boundary edges. Let \(V_h\subset H^1_0(\Omega)\) be the standard continuous piecewise-linear space on this mesh. It is one-dimensional. Its center hat function \(\psi\) satisfies
\[
\int_\Omega\psi^2=\frac16,\qquad \int_\Omega|\nabla\psi|^2=4.
\]
Consequently \(\phi=\sqrt6\,\psi\) has unit \(L^2\) norm, \(\|\nabla\phi\|_{L^2}^2=24\), and \(\mathcal L_h\phi=24\phi\) for the standard mass-inverted Dirichlet finite element Laplacian.

Use the nonlinear fully discrete step and Picard iteration (3.16), (4.1) of Dörich, Krumbiegel, Rogava, Rupp and Vashakidze [1], at its first interior time level, with \(\tau=1\), \(\theta=\gamma=1/2\), \(\eta=0\), and positive constant material coefficients
\[
\alpha=\frac1{12},\qquad \beta=\frac1{72}.
\]
Set preceding discrete displacements \(u_h^0=0\), \(u_h^1=\phi\), and the discrete load \(f_h^{2;0}=g\phi\), where \(g\ge0\). The source-prescribed Picard initial guess is \(u_{h;0}^2=u_h^1=\phi\). For clarity, the claim is about the algebraically specified fully discrete finite element problem; it makes no assertion that these inputs satisfy the small-timestep hypotheses used for the source's convergence theorem.

## Proof

**1. Exact finite element scalar reduction.** Each of the four triangles has area \(1/4\). On each triangle, the center hat is the barycentric center-coordinate. Its squared integral is the area divided by six, and its gradient has squared magnitude four. Summing yields the mass, stiffness and eigenvalue above.

For a trial Picard coefficient \(x\), the Kirchhoff coefficient in (3.16) is
\[
\Gamma_h^{1;1/2}(x\phi)=\alpha+\frac\beta2\|\nabla(x\phi)\|^2
=\frac1{12}+\frac{x^2}{6}.
\]
Because \(\theta=\gamma=1/2\) and \(u_h^0=0\), the right side of the linearized (4.1) is exactly \((g+2)\phi\), and its left-hand scalar coefficient is
\[
1+\tau^2\theta\,24\,\Gamma_h^{1;1/2}(x\phi)=2(1+x^2).
\]
Hence \(x_{\ell+1}=F_g(x_\ell)\) as asserted. Substitution of \(x_{\ell+1}=x_\ell=x\) gives \(x+x^3=(g+2)/2\). Its derivative \(1+3x^2\) is strictly positive, so the implicit equation has exactly one real solution; this solution is positive for \(g\ge0\).

**2. Complete phase portrait.** Put \(a=(g+2)/2>0\), so \(F_g(x)=a/(1+x^2)\). On the nonnegative half-line this map is continuous, strictly decreasing except at the origin, and takes values in \((0,a]\). Its second iterate is increasing and obeys the exact factorization
\[
F_g^2(x)-x
=-\frac{(x^3+x-a)(x^2-ax+1)}{(1+x^2)^2+a^2}.
\]
The cubic has exactly one positive zero \(x_*\). If \(a\le2\), the quadratic factor is nonnegative for every real \(x\). Thus \(F_g^2(x)-x\) points toward \(x_*\). Iterating the increasing map \(F_g^2\) yields a bounded monotone even subsequence converging to \(x_*\), including the equality case \(a=2\); continuity gives the same limit for the odd subsequence.

If \(a>2\), the quadratic has two distinct positive roots \(p=(a-\sqrt{a^2-4})/2\) and \(q=(a+\sqrt{a^2-4})/2\), satisfying \(p+q=a\) and \(pq=1\). Consequently \(F_g(p)=q\), \(F_g(q)=p\). Because \(p<1<q\), the cubic sign places \(p<x_*<q\). The displayed factorization shows that the second iterate moves toward \(p\) on \([0,x_*)\), and toward \(q\) on \((x_*,\infty)\). By monotonicity and boundedness, all non-fixed nonnegative orbits converge to this cycle in the corresponding phase; the exceptional initial value \(x_*\) is fixed. Direct differentiation gives the two-step multiplier
\[
F'_g(p)F'_g(q)=\frac{4}{a^2}=\frac{16}{(g+2)^2},
\]
which is strictly below one when \(g>2\). These are the only nonnegative fixed points of \(F_g^2\), so no other nonnegative periodic orbit is possible.

**3. Prescribed start and severity.** When \(g>2\), \(a>2\) and \(1+1^3=2<a\); hence \(x_0=1<x_*\) and the phase is even-to-\(p_g\), odd-to-\(q_g\). At \(g=4\), exact substitution gives the listed residuals. For \(a\to\infty\), the exact cycle formula gives \(q=a+O(a^{-1})\) and \(p=a^{-1}+O(a^{-3})\), whereas \(x_*^3+x_*=a\) yields \(x_*\sim a^{1/3}\). Therefore \(q/x_*\sim a^{2/3}\), proving arbitrarily large relative overshoot along the spurious high phase.

## Verification

The accompanying `checker.py` computes the four triangle areas exactly, verifies the mass and stiffness values, reduces the source iteration symbolically, factors the second-iterate displacement, checks the two-cycle identities and multiplier, verifies both exact residual limits, and checks multiple rational sample parameters. Run `python checker.py` with SymPy installed. The analytical monotone-map argument, not finite tests, proves the all-parameter assertions.

## Relationship to prior work

Dörich et al. [1] formulate the exact finite element nonlinear Picard map and prove conditional convergence for sufficiently small time steps (Lemma 4.1), with experiments in that regime. Their Sections 3–5 and appendix do not establish this sharp forcing threshold or an attracting incorrect Picard two-cycle. The companion paper [2] develops the corresponding time-discrete scheme and likewise reports small-step convergence; its complete text could not be accessed for this comparison, leaving a historical-overlap risk.

Classical scalar rational iteration already contains the elementary factorization and period-two mechanism. Their abstract dynamical properties are **not claimed as new**. The contribution claimed here is the exact conforming two-dimensional finite element realization of that mechanism in the specified Kirchhoff Picard solver, the complete forcing boundary for its valid discrete inputs, and the unbounded upper-phase error despite uniqueness of the nonlinear stage. The source convergence theorem assumes a sufficiently small timestep and is neither contradicted nor strengthened outside its stated domain.

## Limitations

The construction uses a deliberately minimal one-dimensional finite element space, an externally forced step, an undamped Picard iteration, positive constant material coefficients, and exact arithmetic. Energy conservation in the underlying method holds for appropriately solved unforced problems and is **not** claimed for this forced step or for nonconverged iterates. It is not a statement about higher-dimensional spatial approximation errors, Newton or damped solvers, floating-point runs, or violation of the source's local small-step theorem. The dynamical portion of the argument is classical; exhaustive priority of its exact finite element specialization is not independently established.

## References

[1] B. Dörich, F. Krumbiegel, J. Rogava, A. Rupp, Z. Vashakidze, *Conservative Finite Element Methods for Kirchhoff-Type Equations*, arXiv:2610.31487v1, first submitted 22 October 2026. https://arxiv.org/html/2610.31487v1

[2] F. Krumbiegel, J. Rogava, A. Rupp, Z. Vashakidze, *Conservative Three-Layer Schemes for Kirchhoff-Type Equations*, arXiv:2609.27707, first submitted 23 September 2026. https://arxiv.org/abs/2609.27707
