# A reset-rate phase reversal in variance-constrained critical habitat design

## Finding

Consider independent organisms diffusing with diffusivity \(D>0\) inside a hostile-boundary habitat \((-L,L)\), growing at spatially constant first-moment rate \(g>0\), and returning at Poisson rate \(r>0\) to independent locations \(LZ\). The resampled fractional reset coordinate has law \(\nu\) supported on \([-c,c]\), where \(0<\sigma<c<1\), \(\mathbb E_\nu Z=0\), and \(\mathbb E_\nu Z^2=\sigma^2\). Its law does not change as the habitat halfwidth \(L\) varies. Boundary killing is immediate. Let \(L_c(\nu)\) be the unique positive halfwidth at which the principal population mean-growth exponent is zero.

Define the symmetric *two-site shell* and *center-and-edge* laws
\[
\nu_{\rm sh}=\tfrac12(\delta_{-\sigma}+\delta_{\sigma}),\qquad
\nu_{\rm ec}=\left(1-\frac{\sigma^2}{c^2}\right)\delta_0
+\frac{\sigma^2}{2c^2}(\delta_{-c}+\delta_c).
\]
Then the following are sharp, with uniqueness among **all**, not just symmetric, admissible reset laws:
\[
\begin{array}{ll}
0<r<g:& L_c(\nu_{\rm ec})\le L_c(\nu)\le L_c(\nu_{\rm sh});\\
r>g:& L_c(\nu_{\rm sh})\le L_c(\nu)\le L_c(\nu_{\rm ec}).
\end{array}
\]
For either strict-rate case, equality in an endpoint inequality holds precisely at the corresponding displayed law. At the exact resonance \(r=g\), all admissible laws have the **same** critical halfwidth:
\[
L_c(\nu)=\sqrt{\frac{2D}{g(1-\sigma^2)}}.
\]
Thus the reset law which best minimizes habitat requirements changes discontinuously between two explicitly characterized laws as the reset rate crosses the population growth rate; at the crossing the optimization objective is law-independent.

## Assumptions and scope

The diffusion generator is \(D\partial_x^2\), not \((D/2)\partial_x^2\). At \(\pm L\) particles are killed. Between killing and births, reset events replace the position by an independently drawn point \(LZ\), without dependence on the pre-reset location. Growth adds \(+g\) to the first-moment generator; any linear branching system having that mean-generator interpretation is allowed. The statement concerns the **principal eigenvalue and mean population threshold**; it does not assert almost-sure eternal survival of a finite branching population.

The class of admissible probability laws includes atomic, nonsymmetric and mixed measures satisfying the fixed support, first and second moment constraints. \(c\), \(\sigma\), \(g\), \(r\) and \(D\) remain fixed as \(L\) varies, so support and variance in physical units scale with the halfwidth. All inequalities are for \(L_c\), rather than for the mean first-passage time of one searcher.

## Proof

**1. Positive rank-one spectral reduction.** The killed, reset and growth backward generator on functions vanishing at the endpoints is
\[
\mathcal G_{L,\nu}f(x)=Df''(x)+(g-r)f(x)
+r\int_{-c}^{c}f(Lz)\,\nu(dz).
\]
The Dirichlet diffusion semigroup is positivity improving in the interval. The reset operator is positive and rank one. For real \(\lambda>g-r-D\pi^2/(4L^2)\), define \(s=\lambda+r-g\) and let
\[
F_s^{(L)}(y)=\int_0^\infty e^{-st}\Pr_y\{\tau_L>t\}\,dt,
\]
where \(\tau_L\) is the first hitting time of either endpoint. In this spectral region \(F_s^{(L)}\) is the positive Dirichlet solution of \(D F''-sF=-1\). A positive eigenfunction of eigenvalue \(\lambda\) must be a positive scalar multiple of \(F_s^{(L)}\), because rearrangement of the eigenvalue equation gives \((s-D\partial_x^2)f=r\int f(Lz)\nu(dz)\cdot1\). The corresponding characteristic equation is
\[
1=r\int F_{\lambda+r-g}^{(L)}(Lz)\nu(dz).
\]
Its right-hand side decreases strictly with \(\lambda\), tends to zero as \(\lambda\to\infty\), and tends to infinity as \(\lambda\downarrow g-r-D\pi^2/(4L^2)\), since the ground-state sine/cosine coefficient is strictly positive. It therefore has exactly one real solution in this region, with a strictly positive eigenfunction, which is the principal eigenvalue. Its sign changes at the equation with \(s=r-g\).

**2. Explicit threshold resolvent.** Put \(s=r-g\) and abbreviate \(F_s(Lz)=F_s^{(L)}(Lz)\). When \(s>0\), solving the Dirichlet ODE yields
\[
F_s(Lz)=\frac{1-\cosh(Lz\sqrt{s/D})/\cosh(L\sqrt{s/D})}{s}.
\]
At \(s=0\), the solution is
\[
F_0(Lz)=\frac{L^2(1-z^2)}{2D}.
\]
For \(s=-p<0\), on the positive-resolvent branch \(0<L<\frac\pi2\sqrt{D/p}\), it is
\[
F_{-p}(Lz)=\frac{\cos(Lz\sqrt{p/D})/\cos(L\sqrt{p/D})-1}{p}.
\]
For fixed \(|z|<1\), \(F_s^{(L)}(Lz)\) increases strictly with \(L\): equivalently, Brownian exit time from \((-L,L)\) started at fractional position \(z\) scales as \(L^2\tau_1/D\), and its exponential potential is an increasing function of the lifetime wherever defined. Consequently
\[
\mathcal R_\nu(L):=r\int F_{r-g}^{(L)}(Lz)\,\nu(dz)
\]
increases strictly from zero with \(L\). For \(r>g\) its limit is \(r/(r-g)>1\); for \(r=g\) it grows quadratically; for \(r<g\) it diverges as the first Dirichlet pole is approached, since all \(|z|\le c<1\). Hence there is exactly one critical root \(\mathcal R_\nu(L_c)=1\), with negative and positive mean growth below and above that root.

**3. Exact convex-order comparison.** Introduce \(W=Z^2\in[0,c^2]\), which always has mean \(\sigma^2\). At any fixed admissible \(L\), the map \(w\mapsto F_{r-g}^{(L)}(L\sqrt w)\) is strictly concave when \(r>g\), strictly convex when \(r<g\) and affine when \(r=g\). To verify the signs, write \(u=L\sqrt{|r-g|w/D}\):
\[
\frac{d^2}{dw^2}\cosh(L\sqrt{(r-g)w/D})>0
\quad(r>g),
\]
because \(u\cosh u-\sinh u>0\) for \(u>0\). The hyperbolic contribution enters \(F_{r-g}\) with a negative sign. When \(r<g\),
\[
\frac{d^2}{dw^2}\cos(L\sqrt{(g-r)w/D})>0
\]
because \(\sin u-u\cos u>0\) for \(0<u<\pi/2\). Here the cosine contribution enters \(F_{r-g}\) with a positive sign. At \(w=0\) the derivatives extend by continuity. Both inequalities are strict on the entire compact interval of \(w\) in the appropriate branch.

For every convex function \(H:[0,c^2]\to\mathbb R\), Jensen and its endpoint chord give
\[
H(\sigma^2)\le\mathbb E H(W)
\le\left(1-\frac{\sigma^2}{c^2}\right)H(0)
+\frac{\sigma^2}{c^2}H(c^2).
\]
For strictly convex \(H\), the first equality requires \(W=\sigma^2\) almost surely; the second requires \(W\in\{0,c^2\}\) almost surely. Strict concavity reverses both inequalities and leaves the same equality conditions. Because \(\mathbb E Z=0\), the first equality forces the unique law \(\nu_{\rm sh}\); the second forces the unique law \(\nu_{\rm ec}\). For \(r<g\), the convex comparison therefore makes \(\mathcal R_{\rm ec}(L)\) maximal and \(\mathcal R_{\rm sh}(L)\) minimal. The relations reverse for \(r>g\).

**4. Convert potentials to critical lengths.** Each \(\mathcal R_\nu(L)\) is strictly increasing through one. A pointwise higher potential reaches one at a (strictly) smaller halfwidth. This proves the two strict-regime comparisons, all equality conditions, and their reversal. At \(r=g\), the second-moment constraint gives \(\mathcal R_\nu(L)=g L^2(1-\sigma^2)/(2D)\) for every law, proving the common threshold. No spectral or numerical extrapolation is needed.

## Verification

The accompanying `verify.py` is standalone Python 3 standard library code. Run `python3 verify.py`. It checks normalization and moment constraints, strict optimizer reversal for 13 reset rates, the common resonant halfwidth, strict bounds for 19 intermediate mixtures at each rate, numerical Dirichlet-resolvent roots, independent tridiagonal finite-difference solutions and scaling relations. It also evaluates the moment-kernel curvature on finite meshes. The verifier prints `PASS 846 deterministic checks` on success; these tests are corroboration, not an infinite proof.

As a numerical illustration with \(D=g=1\), \(c=0.9\) and \(\sigma=0.5\): at \(r=0.3\), the shell/edge-center critical halfwidths are \(1.592919475973\) and \(1.585985384767\); at \(r=1\), both are \(\sqrt{8/3}=1.632993161855\); at \(r=3\), they are \(1.668723954174\) and \(1.882542994956\), respectively.

## Relationship to prior work

Menon, de Castro and Anteneodo (2025) studied the critical-habitat problem under resetting to a **fixed** location, including fully hostile absorbing boundaries and finite external mortality. Their 2025 preprint explicitly suggests a distribution of reset positions as an extension (Section V). The present classification concerns independently resampled reset *laws*, fixed mean and variance, sharp extremizers among arbitrary such laws, and a rate-controlled reversal not stated for fixed-site resetting.

Méndez, Flaquer-Galmés and Campos (2024) derived distributed-reset first-passage formulas for searchers with a target in an unbounded setting. Julián-Salgado, Dagdug and Boyer (2025) studied optimization of the *reset rate* for distributed resetting on an unbounded domain. These broader renewal tools are compatible with the rank-one calculation but do not, in the inspected results, imply a sharp variance-constrained comparison of the principal population-growth threshold on a bounded absorbing patch. The convex-order argument is elementary once the relevant killed resolvent is written, and independent priority verification beyond the cited sources has not been undertaken.

## Limitations

The result is for one spatial dimension, Dirichlet killing, constant linear growth, independent memoryless resets, a common location law scaled with the habitat halfwidth, and an imposed first and second moment plus bounded support. The result does not cover continuously coupled exterior mortality, fixed physical resetting coordinates as habitat width changes, higher-dimensional geometry, nonlinear crowding, or almost-sure nonextinction of a finite stochastic population. Bounds are for the critical *mean-growth* threshold; they do not compare complete survival distributions. Broader convex-order resetting theorems might subsume the underlying method and remain a literature-priority risk.

## References

1. L. Menon Jr., P. de Castro and C. Anteneodo, *Critical habitat size of organisms diffusing with stochastic resetting*, arXiv:2505.03727v1 (first public 2025-05-06), https://arxiv.org/abs/2505.03727.
2. P. Julián-Salgado, L. Dagdug and D. Boyer, *Abrupt transitions in the optimization of diffusion with distributed resetting*, arXiv:2507.14483 (first public 2025-07-19), https://arxiv.org/abs/2507.14483.
3. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (2024), https://arxiv.org/abs/2401.01125.
