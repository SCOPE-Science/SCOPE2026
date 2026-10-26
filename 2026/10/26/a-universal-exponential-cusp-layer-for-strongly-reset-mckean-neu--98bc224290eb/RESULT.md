# A universal exponential cusp layer for strongly reset McKean neurons

## Finding

Consider the adiabatically frozen fast voltage of a stochastic McKean neuron, with Gaussian diffusivity \(D>0\) and independent Poisson resetting at rate \(r\). When the reset voltage approaches either kink \(b\in\{-a,a\}\) on the Brownian scale \(v_r=b+\xi/\sqrt r\), the stationary voltage mean differs from its deterministic reset-drift approximation by an explicit, nonanalytic term:

\[
\mu_r(w;v_r)=v_r+\frac{f(v_r)+I_0-w}{r}
 +\frac{\Delta_b\sqrt D}{2r^{3/2}}e^{-|\xi|/\sqrt D}
 +O_K(r^{-2}),
\]

uniformly for the frozen recovery parameter \(w\) and the detuning \(\xi\) in arbitrary fixed compact sets. Here \(\Delta_b=f'_+(b)-f'_-(b)\) is the jump in voltage-drift slope. Thus the first stochastic correction caused by a kink has exponent \(3/2\), a universal exponential crossover shape, and a width of order \(r^{-1/2}\) in reset location. At any fixed reset location strictly inside a linear segment, the corresponding correction is instead \(O(r^{-2})\).

For all sufficiently large \(r\), the averaged slow equation has exactly one globally attracting fixed point, which has the matching expansion

\[
 w_r^*=\frac{v_r}{\gamma}
 +\frac{f(v_r)+I_0-v_r/\gamma}{\gamma r}
 +\frac{\Delta_b\sqrt D}{2\gamma r^{3/2}}e^{-|\xi|/\sqrt D}
 +O_K(r^{-2}).
\]

Both assertions are for fixed \(D>0\), fixed McKean parameters, and bounded \(\xi\); there is no claim that the expansion is uniform as \(D\downarrow0\) or across arbitrary detunings.

## Assumptions and scope

Fix \(a>0\), \(D>0\), \(\gamma>0\), \(I_0\in\mathbb R\), and slopes \(m_-<0\), \(m_+<0\), \(m_0>0\). The continuous, piecewise-affine McKean nonlinearity is

\[
 f(v)=\begin{cases}
 m_-v-a(m_0-m_-),&v<-a,\\
 m_0v,&-a\le v\le a,\\
 m_+v+a(m_0-m_+),&v>a.
 \end{cases}
\]

Let \(L=\max\{|m_-|,|m_0|,|m_+|\}\). For frozen \(w\in\mathbb R\), a voltage process starts at \(v_r\), evolves between resets according to

\[
 dV_t=[f(V_t)+I_0-w]dt+\sqrt{2D}\,dB_t,
\]

and is reset to \(v_r\) by an independent Poisson process of rate \(r\). Define \(\mu_r(w;v_r)\) as the mean of its unique regenerative stationary law. Write \(\Delta_{-a}=m_0-m_-\) and \(\Delta_a=m_+-m_0\). The principal assertions hold as \(r\to\infty\) for each choice of \(b\in\{-a,a\}\), \(v_r=b+\xi r^{-1/2}\), and any compact \(K\subset\mathbb R^2\) for \((w,\xi)\). The averaged recovery dynamics is \(dw/d\tau=\mu_r(w;v_r)-\gamma w\), which is a singular-timescale model rather than a statement about the finite-timescale full two-dimensional system.

## Proof

**1. Renewal representation and moment identity.** For each frozen \(w\), let \(X_t\) solve the no-reset SDE from \(X_0=v_r\), and let \(T_r\sim\operatorname{Exp}(r)\) be independent. Regeneration gives the stationary law \(V_{\mathrm{st}}\stackrel d=X_{T_r}\). In particular,

\[
\mu_r(w;v_r)=r\int_0^\infty e^{-rt}\mathbb E X_t\,dt.
\]

Because \(f\) is globally \(L\)-Lipschitz and has at most linear growth, the expectations are finite for \(r>L\). Integrating the SDE up to \(T_r\), or integrating by parts in the resolvent, gives the *exact* identity

\[
\mu_r(w;v_r)-v_r=\frac{\mathbb E f(X_{T_r})+I_0-w}{r}. \tag{1}
\]

**2. Universal Brownian profile at the kink.** Synchronous comparison of the no-reset path and pure Brownian motion yields

\[
X_{T_r}=v_r+\sqrt{2D}B_{T_r}+R_r,
\qquad \mathbb E|R_r|=O_K(r^{-1}),
\]

uniformly on the specified compacts, for all sufficiently large \(r\). Indeed \(R_r=\int_0^{T_r}[f(X_s)+I_0-w]ds\); global linear growth and standard SDE first-moment estimates give a uniform bound \(\mathbb E|f(X_s)+I_0-w|\le C_K e^{Ls}(1+\sqrt s)\), which integrates to \(O_K(r^{-1})\) under the exponential time law.

The random variable \(Y_r=\sqrt{2D}B_{T_r}\) has characteristic function

\[
\mathbb E[e^{itY_r}]=\frac r{r+Dt^2},
\]

so \(\sqrt rY_r\) is *exactly* a centered Laplace random variable \(Y\) of scale \(\sqrt D\), with density \(e^{-|y|/\sqrt D}/(2\sqrt D)\). For every real \(\xi\), direct integration gives

\[
\mathbb E[(\xi+Y)_+]-\xi_+=\frac{\sqrt D}{2}e^{-|\xi|/\sqrt D}. \tag{2}
\]

Near a kink \(b\), on a neighborhood that excludes the other kink, the nonlinearity is exactly an affine function plus \(\Delta_b(v-b)_+\). The Lipschitz bound on \(f\) permits replacing \(X_{T_r}\) by \(v_r+Y_r\) with \(O_K(r^{-1})\) expectation error. Contributions from the other kink are exponentially small in \(\sqrt r\), since the distance to it is at least \(a\) for bounded detunings and the Brownian-at-exponential-time law is Laplace. The affine part has zero Brownian mean. Consequently (2) yields

\[
\mathbb E f(X_{T_r})=f(v_r)
 +\frac{\Delta_b\sqrt D}{2\sqrt r}e^{-|\xi|/\sqrt D}
 +O_K(r^{-1}). \tag{3}
\]

Inserting (3) into (1) proves the stationary-mean formula with \(O_K(r^{-2})\) remainder. If \(v_r\) is held a fixed positive distance from both kinks, the Laplace probability of crossing a kink is exponentially small in \(\sqrt r\); then (3) has no \(r^{-1/2}\) term, proving the interior comparison.

**3. Unique averaged equilibrium and its expansion.** Couple two no-reset diffusions with the same Brownian motion and reset value but different frozen parameters \(w,w'\). By global Lipschitzness, their difference is bounded pathwise by

\[
|X_t^w-X_t^{w'}|\le |w-w'|\frac{e^{Lt}-1}{L}.
\]

Integrating against the exponential age law gives, for \(r>L\),

\[
|\mu_r(w;v_r)-\mu_r(w';v_r)|\le\frac{|w-w'|}{r-L}. \tag{4}
\]

For \(r>L+\gamma^{-1}\), the map \(w\mapsto\mu_r(w;v_r)/\gamma\) is a strict contraction on the complete real line. Hence it has exactly one fixed point \(w_r^*\). Its scalar averaged flow is globally exponentially attracted to this point: one-dimensional SDE comparison implies \(\mu_r\) is nonincreasing in \(w\), so \((w-w_r^*)[\mu_r(w)-\mu_r(w_r^*)-\gamma(w-w_r^*)]\le-\gamma(w-w_r^*)^2\). The contraction bound and the expansion of \(\mu_r\) show \(w_r^*=v_r/\gamma+O_K(r^{-1})\). Substituting this into the stationary-mean expansion and using (4) to control the dependence on \(w\) gives the displayed slow-equilibrium formula, with the same \(O_K(r^{-2})\) remainder.

## Verification

A finite-volume independent calculation solves \((rI-Q^{\mathsf T})\pi=r\delta_{v_r}\) for a nearest-neighbor diffusion discretization whose drift is the exact piecewise-affine McKean drift. At \(a=0.35\), \(m_0=1.14\), \(m_\pm=-2\), \(D=0.5\), \(I_0=0\), and \(w=0.35\), the scaled correction at the right kink approaches \(-3.14\sqrt{0.5}/2\approx-1.11015765\). Independently, for detunings \(\xi=\pm1\) the predicted coefficient is multiplied by \(e^{-1/\sqrt{0.5}}\). The bundled `verify.py` checks the Laplace transform and hinge integral numerically, and compares nine finite-volume computations at \(r\in\{64,256,625\}\), \(\xi\in\{-1,0,1\}\), against the exact asymptotic profile. All recorded numerical checks passed. These finite calculations are corroboration, not proof of the uniform limit.

## Relationship to prior work

Swaby and Bressloff, arXiv:2609.31153v1 (2026), introduce precisely this diffusion-plus-Poisson-reset McKean model. They derive its piecewise parabolic-cylinder stationary densities and an averaged recovery equation; their reported asymptotic analysis treats *vanishing diffusion at fixed resetting parameters* rather than the strong-reset kink layer. Those stationary formulas, the model, and the averaged equation are prior work. Bressloff, arXiv:2503.07585v1 (2025), gives the precursor averaged slow-fast theory without Brownian diffusion and with a smooth cubic fast nonlinearity. The contribution here is the explicit \(r^{-3/2}\) slope-jump correction with its full \(r^{-1/2}\) reset-detuning profile and the induced high-rate slow-equilibrium shift, not the existence of the stationary measure or the original model. The exact Laplace law of Brownian motion at an exponential time is elementary established probability theory and is used, not claimed as new.

## Limitations

The theorem applies to the singular adiabatic averaged equation and a frozen-parameter stochastic fast process; it does not show finite-\(\varepsilon\) approximation errors for the original two-dimensional dynamics. The expansion takes fixed positive diffusivity, fixed McKean slopes, \(r\to\infty\), and bounded scaled detuning \(\xi\). It does not provide a uniform joint limit as noise vanishes, extend beyond Lipschitz piecewise-affine drift, or describe arbitrary reset laws. The originality assessment is literature-bounded; a broad resolvent boundary-layer theorem may imply this specialization without using the same notation.

## References

1. J. Swaby and P. C. Bressloff, *Slow–fast dynamics of the McKean model with stochastic resetting and diffusion*, arXiv:2609.31153v1 (first public September 25, 2026). https://arxiv.org/abs/2609.31153
2. P. C. Bressloff, *Slow-fast systems with stochastic resetting*, arXiv:2503.07585v1 (first public March 10, 2025). https://arxiv.org/abs/2503.07585
3. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Physical Review Letters **106**, 160601 (2011). DOI: 10.1103/PhysRevLett.106.160601.
