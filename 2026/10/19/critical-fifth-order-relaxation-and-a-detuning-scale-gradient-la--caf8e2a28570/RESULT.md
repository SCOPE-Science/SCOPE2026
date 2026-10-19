# Critical fifth-order relaxation and a detuning-scale gradient law for a walking-droplet map

## Finding

The two-harmonic wave-particle recurrence introduced by Gilet has an exceptional wave shape at which its origin is nonhyperbolic but locally attracting with an exact inverse-fourth-power relaxation coefficient. On either side of that shape, a square-root spatial scaling and inverse-square detuning time scaling resolve a three-well/one-well transition through an explicit one-dimensional gradient equation.

Fix real constants \(0<\mu<1\) and \(0<C\leq1\). Define
\[
\Psi_\beta(x)=\frac{\cos\beta\sin(3x)+\sin\beta\sin(5x)}{\sqrt\pi},\qquad
w_{n+1}=\mu\bigl(w_n+\Psi_\beta(x_n)\bigr),\quad
x_{n+1}=x_n-Cw_n\Psi_\beta'(x_n).
\]
The critical shape is
\[
\beta_*=\pi-\arctan(3/5),\qquad
\Psi_{\beta_*}(x)=\frac{-40\sin^3x+48\sin^5x}{\sqrt{34\pi}}.
\]

**Critical relaxation.** At \(\beta=\beta_*\), the fixed point \((x,w)=(0,0)\) is locally asymptotically stable despite having multipliers \(1\) and \(\mu\). Every sufficiently near orbit with \(x_0\ne0\) obeys
\[
\lim_{n\to\infty}\frac{1}{n\,x_n^4}=
\frac{9600C\mu}{17\pi(1-\mu)}.
\]
The invariant line \(x_0=0\) is the exceptional strong-stable set: there \(w_n=\mu^n w_0\) and \(x_n=0\).

**Shape detuning.** Let \(\varepsilon>0\) tend to zero and \(\sigma\in\{-1,+1\}\); set \(\beta=\beta_*+\sigma\varepsilon\). There is a fixed neighborhood of \(x=0\) for which, for all sufficiently small \(\varepsilon\), the \(\sigma=+1\) map has only the origin as a fixed point (a hyperbolic sink). The \(\sigma=-1\) map has exactly five fixed points: three hyperbolic sinks (the origin and two wave zeros with positions \(x=\pm\sqrt{17/20}\,\sqrt\varepsilon+O(\varepsilon^{3/2})\)) and two saddles (wave extrema at \(x=\pm\sqrt{17/60}\,\sqrt\varepsilon+O(\varepsilon^{3/2})\)). All fixed-point counts are local, not global statements about the periodic wave.

**Universal crossover.** For fixed \(X_0\in\mathbb R\), assume \(x_0^\varepsilon/\sqrt\varepsilon\to X_0\) and \(w_0^\varepsilon=O(\varepsilon^{3/2})\). Write
\[
A_\sigma(X)=-\frac{34\sigma X+40X^3}{\sqrt{34\pi}},\qquad
\kappa=\frac{C\mu}{1-\mu}.
\]
For each finite \(T>0\), with \(s\in[0,T]\), the rescaled walker coordinate satisfies
\[
\sup_{0\le s\le T}\left|
\frac{x^\varepsilon_{\lfloor s/\varepsilon^2\rfloor}}{\sqrt\varepsilon}-X_\sigma(s)
\right|\longrightarrow0,
\qquad
\frac{dX_\sigma}{ds}=-\kappa A_\sigma(X_\sigma)A_\sigma'(X_\sigma),
\quad X_\sigma(0)=X_0.
\]
For every \(0<s_0<T\), the wave memory has the slaved limit
\[
\sup_{s_0\le s\le T}\left|
\frac{w^\varepsilon_{\lfloor s/\varepsilon^2\rfloor}}{\varepsilon^{3/2}}
-\frac{\mu}{1-\mu}A_\sigma(X_\sigma(s))
\right|\longrightarrow0.
\]
The restriction \(s\ge s_0>0\) permits a fast initial memory transient. The limit flow is gradient descent for \(A_\sigma^2/2\). At positive detuning it has one attracting equilibrium; at negative detuning it has three attracting equilibria separated by two unstable equilibria.

## Assumptions and scope

The map is studied locally in the real plane near the origin, not on its entire periodic domain or in a stochastic fluid model. The parameters \(\mu,C\) remain fixed with \(0<\mu<1\), \(0<C\le1\); constants in neighborhoods and error bounds may depend on them. Detuning always means \(\varepsilon\downarrow0\) with either of the two fixed signs \(\sigma\). For the crossover, the rescaled initial position has a finite limit and the initial memory is of order at most \(\varepsilon^{3/2}\). A prime denotes differentiation with respect to the spatial coordinate; all convergence statements concern exact iterates, not a truncated recurrence.

## Proof

**1. Exact trigonometric reduction and shape threshold.** Put \(u=\sin x\). The identities \(\sin(3x)=3u-4u^3\) and \(\sin(5x)=5u-20u^3+16u^5\) give
\[
\sqrt\pi\,\Psi_\beta(x)
=a_\beta u+b_\beta u^3+d_\beta u^5,
\quad a_\beta=3\cos\beta+5\sin\beta,
\quad b_\beta=-4\cos\beta-20\sin\beta,
\quad d_\beta=16\sin\beta.
\]
At \(\beta_*\), the trigonometric pair is \((\cos\beta_*,\sin\beta_*)=(-5,3)/\sqrt{34}\), hence \(a_{\beta_*}=0\), \(b_{\beta_*}=-40/\sqrt{34}\), and \(d_{\beta_*}=48/\sqrt{34}\). In particular,
\[
\Psi_{\beta_*}(x)=c\,x^3+O(x^5),\qquad c=-\frac{40}{\sqrt{34\pi}},\qquad
\Psi_{\beta_*}'(x)=3c\,x^2+O(x^4).
\]
Also \(a'_{\beta_*}=-\sqrt{34}\). The latter identity determines the sign of the near-critical zero splitting.

**2. Critical center drift and its sharp coefficient.** The Jacobian at the origin for \(\beta=\beta_*\) is \(\operatorname{diag}(1,\mu)\). The local center-manifold theorem provides a smooth one-dimensional invariant graph \(w=h(x)\), tangent to the \(x\)-axis. Its invariance equation is
\[
h\bigl(x-C h(x)\Psi_{\beta_*}'(x)\bigr)
=\mu\bigl(h(x)+\Psi_{\beta_*}(x)\bigr).
\]
Comparison of the cubic coefficients (the lower ones vanish) yields
\[
h(x)=\frac{\mu}{1-\mu}c\,x^3+O(x^5).
\]
The reduced map is therefore
\[
x\longmapsto x-Kx^5+O(x^7),\qquad
K=\frac{3C\mu c^2}{1-\mu}>0.
\]
On either side of zero this map is locally attracting. The stable transverse multiplier \(\mu<1\) and local stable-foliation/center-stability theorems imply that the full fixed point is locally asymptotically stable and that each nearby orbit is exponentially tracked by a center-manifold orbit. The strong-stable manifold is exactly the locally invariant vertical line \(x=0\), since on this line the map reduces to \(w\mapsto\mu w\), and the local strong-stable manifold is unique. For sufficiently small \((x,w)\), the inequality \(|Cw\Psi_{\beta_*}'(x)|<|x|/2\) when \(x\ne0\) prevents a nonzero orbit from landing on that line.

For a nonzero center orbit, \(x_{n+1}=x_n(1-Kx_n^4+O(x_n^6))\), so
\[
|x_{n+1}|^{-4}-|x_n|^{-4}=4K+o(1).
\]
Cesàro averaging gives \(\lim |x_n|^{-4}/n=4K\); exponentially accurate center tracking gives the same result for every nearby orbit off the vertical strong-stable line. Finally \(4K=12C\mu c^2/(1-\mu)=9600C\mu/[17\pi(1-\mu)]\), as asserted.

**3. Exact local fixed-point census.** At a fixed point, the memory relation forces \(w=\mu\Psi_\beta(x)/(1-\mu)\), while the position relation requires \(\Psi_\beta(x)\Psi_\beta'(x)=0\). Within \(|x|<\delta<\pi/2\), the nonzero roots of \(\Psi_\beta\) have \(u^2\) satisfying \(a_\beta+b_\beta u^2+d_\beta u^4=0\); nonzero roots of \(\Psi_\beta'\) satisfy \(a_\beta+3b_\beta u^2+5d_\beta u^4=0\), because \(\cos x\ne0\). For \(\sigma=-1\),
\[
a_{\beta_* -\varepsilon}=\sqrt{34}\,\varepsilon+O(\varepsilon^2),\quad
b_{\beta_* -\varepsilon}=-40/\sqrt{34}+O(\varepsilon).
\]
Both polynomials have exactly one small positive root in \(u^2\) by monotonicity on a fixed small interval and the implicit-function theorem. These satisfy \(u^2=(17/20)\varepsilon+O(\varepsilon^2)\) and \(u^2=(17/60)\varepsilon+O(\varepsilon^2)\) respectively. Passing from \(u=\sin x\) to \(x=\arcsin u\) gives the stated positions. For \(\sigma=+1\), the constant term is negative and the polynomial slopes are negative near zero, leaving only the origin.

At a wave zero with nonzero spatial slope \(p=\Psi_\beta'(x)\), the Jacobian has trace \(1+\mu\) and determinant \(\mu(1+Cp^2)\). Its Schur quantities are \(\mu Cp^2>0\), \(2+2\mu+\mu Cp^2>0\), and \(1-\mu(1+Cp^2)>0\) for sufficiently small \(\varepsilon\). Hence the origin and the split wave zeros are hyperbolic sinks. At a nonzero wave extremum, the Jacobian eigenvalues are \(\mu\) and \(1-\frac{C\mu}{1-\mu}\Psi_\beta(x)\Psi_\beta''(x)\). The local extrema have \(\Psi_\beta\Psi_\beta''<0\), so the second eigenvalue exceeds one: they are hyperbolic saddles.

**4. Uniform detuning-scale convergence.** On bounded \(X\)-sets, Taylor expansion in \(\varepsilon\) gives uniformly
\[
\Psi_{\beta_*+\sigma\varepsilon}(\sqrt\varepsilon X)
=\varepsilon^{3/2}[A_\sigma(X)+O(\varepsilon)],\qquad
\Psi_{\beta_*+\sigma\varepsilon}'(\sqrt\varepsilon X)
=\varepsilon[A_\sigma'(X)+O(\varepsilon)].
\]
Write \(X_n=x_n/\sqrt\varepsilon\), \(W_n=w_n/\varepsilon^{3/2}\), and \(g(X)=\mu A_\sigma(X)/(1-\mu)\). The exact recurrence becomes, as long as \(X_n\) is bounded,
\[
W_{n+1}=\mu(W_n+A_\sigma(X_n))+O(\varepsilon),\qquad
X_{n+1}=X_n-C\varepsilon^2W_nA_\sigma'(X_n)+O(\varepsilon^3|W_n|).
\]
The contraction \(\mu<1\) bounds \(W_n\) on any bounded \(X\)-set. Consequently \(X_{n+1}-X_n=O(\varepsilon^2)\), and the slaving error \(E_n=W_n-g(X_n)\) obeys
\[
|E_n|\le\mu^n|E_0|+K_1\varepsilon
\]
for a constant \(K_1\) uniform over these sets. Substitute this estimate into the \(X\) recurrence to obtain
\[
X_{n+1}=X_n-\kappa\varepsilon^2A_\sigma(X_n)A_\sigma'(X_n)
+O(\varepsilon^3)+O(\varepsilon^2\mu^n|E_0|).
\]
The limiting polynomial ODE is globally well-posed: along it, \(A_\sigma(X)^2\) is nonincreasing and \(A_\sigma(X)^2\to\infty\) as \(|X|\to\infty\). On each finite horizon its solution therefore stays within a compact interval. Discrete Euler consistency, a discrete Grönwall estimate, and a compact-interval bootstrap yield uniform \(X\)-convergence for all \(0\le s\le T\); the total contribution of the initial memory transient is \(O(\varepsilon^2|E_0|)\). For \(s\ge s_0>0\), \(\mu^{\lfloor s/\varepsilon^2\rfloor}|E_0|\to0\) uniformly, which proves the memory limit.

Finally, the stable zeros of \(A_\sigma\) and unstable nonzero extrema of \(A_\sigma^2\) give exactly the gradient-flow phase portrait stated in the finding. No global assertion is made for initial positions outside the square-root spatial scaling.

## Verification

Run `python walker_verifier.py` with Python, NumPy, SymPy, and SciPy installed. The checker establishes the exact trigonometric identity and the coefficient algebra symbolically, verifies the local polynomial roots in three detuning tests, compares finite rescaled trajectories to high-accuracy numerical ODE solutions for both detuning signs, and checks the convergence of a long critical orbit toward the exact inverse-fourth coefficient. It returns `VERIFY_OK` when all checks succeed. These finite computations do not independently prove the all-parameter, infinite-time, or vanishing-detuning conclusions: those depend on the arguments above.

## Relationship to prior work

Gilet's original 2014 confined-wave walker paper defines exactly this recurrence and two-sine test family, derives fixed-point families and their hyperbolic stability formula, and plots fixed-point branches as the wave-shape parameter changes. Its plots already convey the qualitative creation and merger of stationary points; the local stationary count alone is not asserted as novel here. Rahman and Blackmore's 2015 preprint establishes Neimark–Sacker bifurcations for the same walker map, with conditions involving nonzero wave slopes at the relevant equilibria. Neither inspected source provides the nonhyperbolic critical relaxation coefficient or the full singular detuning-scale trajectory limit of the present statement.

Related research on other dynamical systems establishes quintic slow relaxation at unrelated critical points. Such exponent-level analogies do not imply this walker-specific shape threshold, coefficient, five-equilibrium split, or polynomial gradient scaling limit. The proof uses standard center-manifold and singular-perturbation techniques, not a new general-purpose theorem about all walker models.

## Limitations

The theorem is local near the origin, with fixed damping and coupling; it does not classify global attractors, fluid dynamics, other shape values, higher-dimensional walker motion, or the high-memory limit \(\mu\uparrow1\). The center reduction requires standard smooth invariant-manifold results, while finite numerical checks are only corroborative. Some older or less-indexed treatments of the exact critical wave shape could remain undiscovered; historical priority is not independently certified. The limiting memory law excludes zero scaled time because the initial fast transient need not satisfy instantaneous slaving.

## References

1. T. Gilet, *Dynamics and statistics of wave-particle interactions in a confined geometry*, Physical Review E **90** (2014), 052917; DOI: 10.1103/PhysRevE.90.052917. Author-archived preprint: https://orbi.uliege.be/bitstream/2268/178755/1/Generic.pdf (model equation (9), test family equation (20), and figure 2).
2. A. Rahman and D. Blackmore, *Neimark–Sacker bifurcation and evidence of chaos in a discrete dynamical model of walkers*, arXiv:1507.08057 (first version 2015); https://arxiv.org/abs/1507.08057 (sections 2–4).
3. J. Carr, *Applications of Centre Manifold Theory*, Springer, 1981 (standard smooth center-manifold and stability-reduction theory).
4. M. W. Hirsch, C. C. Pugh, and M. Shub, *Invariant Manifolds*, Lecture Notes in Mathematics **583**, Springer, 1977 (local stable foliations and exponential tracking).
