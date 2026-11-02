# Matched predator–prey equilibrium profiles yield a global entropy obstruction to heterogeneous Hopf dynamics

## Finding
For the heterogeneous Lotka–Volterra predator–prey system below, a **spatially constant matching ratio between the opposing trophic couplings at a positive equilibrium** suffices for global attraction to that equilibrium. This quantitative obstruction holds with independently nonconstant equilibrium profiles and for arbitrary positive diffusion rates. In particular, it precludes the strictly positive time-periodic solutions that can otherwise arise through heterogeneous Hopf bifurcation.

Let \(h(s)=s-1-\log s\) for \(s>0\). When \(\alpha bU=\beta cV\) holds pointwise for positive constants \(\alpha,\beta\), the functional
\[
\mathcal E(t)=\int_\Omega\left[\alpha U^2 h(u/U)+\beta V^2 h(v/V)\right]dx
\]
is strictly dissipative away from the positive equilibrium. Its exact derivative is
\[
\begin{aligned}
\frac{d\mathcal E}{dt}={}&-\alpha d\int_\Omega U^2|\nabla\log(u/U)|^2dx
-\beta D\int_\Omega V^2|\nabla\log(v/V)|^2dx\\
&-\int_\Omega\left[\alpha aU^3(u/U-1)^2+\beta eV^3(v/V-1)^2\right]dx.
\end{aligned}
\]
Every solution with strictly positive continuous initial values converges uniformly to \((U,V)\) as time tends to infinity. Hence no other positive stationary state or strictly positive nonconstant periodic trajectory is possible.

## Assumptions and scope
Let \(\Omega\subset\mathbb R^n\), \(n\ge1\), be a bounded connected domain with smooth boundary. Consider
\[
\begin{aligned}
\partial_tu&=d\Delta u+u\bigl(r(x)-a(x)u-b(x)v\bigr),\\
\partial_tv&=D\Delta v+v\bigl(m(x)+c(x)u-e(x)v\bigr),\\
\partial_\nu u&=\partial_\nu v=0\quad\text{on }\partial\Omega.
\end{aligned}
\]
Here \(d,D>0\) are spatially constant, \(r,m\in C^\alpha(\overline\Omega;\mathbb R)\), and \(a,b,c,e\in C^\alpha(\overline\Omega)\) have strictly positive minima, for some Hölder exponent \(0<\alpha<1\). To avoid notational collision, let the *constant entropy weights* be denoted \(A,B>0\), and require a strictly positive classical Neumann equilibrium \((U,V)\), with sufficient regularity for the displayed computations, satisfying
\[
A b(x)U(x)=B c(x)V(x)\qquad(x\in\overline\Omega).
\]
The initial functions are arbitrary \(u_0,v_0\in C(\overline\Omega)\) with strictly positive minima. No relation is required between \(d\) and \(D\), and the intrinsic predator growth \(m\) may have either sign, including being negative everywhere.

## Proof
**Step 1 (positive global trajectories).** The parabolic maximum principle preserves strict positivity at every finite time. Since \(a\) has a positive minimum, \(u\) is bounded above by a scalar logistic supersolution whose reaction is \(u(\max r-\min a\,u)\). With this bound, \(v\) is bounded above by a scalar logistic supersolution with growth constant \(\max m+\max c\,\sup u\) and quadratic loss \(\min e\,v^2\). Standard continuation yields a global bounded classical solution.

**Step 2 (ground-state transform).** Set \(p=u/U\), \(q=v/V\). Subtracting the two stationary equations from the corresponding evolution equations and using the product rule yields
\[
\begin{aligned}
\partial_t p&=dU^{-2}\operatorname{div}(U^2\nabla p)-p\bigl(aU(p-1)+bV(q-1)\bigr),\\
\partial_t q&=DV^{-2}\operatorname{div}(V^2\nabla q)+q\bigl(cU(p-1)-eV(q-1)\bigr).
\end{aligned}
\]
The Neumann data for \(u,v,U,V\) imply \(\partial_\nu p=\partial_\nu q=0\).

**Step 3 (exact weighted entropy).** Define
\[
\mathcal E(t)=\int_\Omega\left[A U^2h(p)+B V^2h(q)\right]dx,
\qquad h(s)=s-1-\log s.
\]
Because \(h'(s)=1-s^{-1}\), \(h''(s)=s^{-2}\), integration by parts gives the two diffusion dissipations \(-Ad\int U^2|\nabla\log p|^2\) and \(-BD\int V^2|\nabla\log q|^2\). The reaction contribution is
\[
-\int_\Omega\bigl[AaU^3(p-1)^2+BeV^3(q-1)^2\bigr]dx
+\int_\Omega UV\bigl(BcV-AbU\bigr)(p-1)(q-1)dx.
\]
The last integral vanishes *identically* by the pointwise matching assumption. Thus the derivative of \(\mathcal E\) equals the strictly negative four-term formula in the Finding section. Since \(h\ge0\), the entropy is nonnegative, finite initially, and nonincreasing. Positivity of the reaction coefficients and profiles implies
\[
\int_0^\infty\bigl(\|p(t)-1\|_{L^2(\Omega)}^2+\|q(t)-1\|_{L^2(\Omega)}^2\bigr)\,dt<\infty.
\]

**Step 4 (convergence for every positive datum).** The uniform upper bounds and classical semilinear parabolic regularization give uniform Hölder bounds, and in particular a uniform bound on \(\|\partial_tu\|_{L^2}+\|\partial_tv\|_{L^2}\), for times bounded away from zero. As \(U,V\) are fixed and uniformly positive, the function \(t\mapsto\|p-1\|_2^2+\|q-1\|_2^2\) is uniformly continuous on \([1,\infty)\). A nonnegative uniformly continuous integrable function tends to zero, proving convergence in \(L^2\). Uniform spatial Hölder estimates and interpolation on the bounded smooth domain upgrade this to uniform convergence. Consequently a second positive equilibrium or strictly positive nonconstant periodic trajectory would contradict convergence to \((U,V)\).

**Step 5 (a genuinely heterogeneous example).** On \(\Omega=(0,1)\), put
\[
\begin{gathered}
U(x)=1+\tfrac1{10}\cos(\pi x),\qquad
V(x)=1+\tfrac1{20}\cos(2\pi x),\\
d=D=\tfrac1{10},\quad a=1,\quad e=\tfrac15,\quad c=2,\quad b(x)=2V(x)/U(x),\quad A=B=1,\\
r(x)=aU+bV-dU''/U,\qquad m(x)=eV-cU-DV''/V.
\end{gathered}
\]
Both profiles are positive and *not proportional*, both have zero endpoint derivatives, and \(bU=cV\) holds identically. The defining expressions make \((U,V)\) an exact equilibrium. Using \(9/10\le U\le11/10\), \(19/20\le V\le21/20\), and \(\pi^2<10\), one obtains
\[
\begin{aligned}
r(x)&>\tfrac9{10}+2\frac{(19/20)^2}{11/10}-\frac{1/10}{9/10}>0,\\
m(x)&<\tfrac15\cdot\tfrac{21}{20}-2\cdot\tfrac9{10}+\frac{1/5}{19/20}<0.
\end{aligned}
\]
Thus the example has heterogeneous coefficients and an everywhere *negative* intrinsic predator growth rate but is globally attracted to its nonconstant coexistence profile for all positive initial states.

## Verification
Run \(`python CHECK.py`\) with SymPy. The executable recomputes the exact cross-term cancellation, the weighted-divergence transform, Neumann endpoint identities, both stationary substitutions, and strict parameter bounds of the constructed example. The identities constitute exact symbolic checks; they do not replace the parabolic existence and convergence arguments in Steps 1 and 4.

## Relationship to prior work
Lou and Xin (2026, arXiv:2610.02630) give heterogeneous Neumann predator–prey systems with a unique positive equilibrium undergoing Hopf bifurcation; their Section 1 and Theorems 1.1–1.2 establish that positivity and uniqueness alone cannot preclude oscillation. The pointwise matched equilibrium-coupling condition here identifies an explicit nonoscillatory subfamily rather than contradicting those examples. Ni, Shi, and Wang (2019, arXiv:1909.00537) develop weighted Lyapunov functionals for **competition–diffusion systems** with both off-diagonal interactions suppressive; the present cancellation instead uses **oppositely signed predator–prey interactions** and the condition \(AbU=BcV\). Li, Wu, and Dong (2019, DOI:10.1007/s00526-019-1558-4) consider a different saturating Crowley–Martin functional response with strong predator competition sufficient for stability, not this unrestricted-diffusion matched-profile criterion. Related classical Lyapunov methods motivate the construction; the claim is the specified structural theorem, not priority over relative-entropy methods in general.

## Limitations
Existence of a strictly positive stationary pair and the pointwise matching identity are assumptions, not universal consequences of heterogeneous predator–prey coefficients. The theorem does not apply to generic heterogeneous systems or to boundary initial conditions in which a species is identically absent. No uniform-in-initial-data exponential decay rate is claimed. Historical priority beyond the inspected literature is not independently certified; the 2019 Crowley–Martin article was examined via published abstract and available excerpts, not its complete primary text.

## References
1. Y. Lou and M.-Z. Xin, *Hopf bifurcation in a predator-prey model with diffusion and spatial heterogeneity* (2026), arXiv:2610.02630, https://arxiv.org/abs/2610.02630 (first public October 2, 2026).
2. W. Ni, J. Shi, and M. Wang, *Global stability of nonhomogeneous equilibrium solution for the diffusive Lotka-Volterra competition model* (2019), arXiv:1909.00537, https://arxiv.org/abs/1909.00537.
3. S. Li, J. Wu, and Y. Dong, *Uniqueness and stability of positive solutions for a diffusive predator–prey model in heterogeneous environment*, Calculus of Variations and Partial Differential Equations **58** (2019), 110, DOI:10.1007/s00526-019-1558-4.
4. E. Beretta and Y. Takeuchi, *Global asymptotic stability of Lotka–Volterra diffusion models with continuous time delay*, SIAM Journal on Applied Mathematics **48** (1988), 627–651, DOI:10.1137/0148035 (patch-diffusion and delay setting).
