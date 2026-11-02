# Noise-robust single-snapshot direction inference and its fast-tumbling crossover in a planar active trap

## Finding

Consider a stationary planar run-and-tumble particle with four possible instantaneous propulsion headings (east, north, west, south). The hidden heading executes independent clockwise and counterclockwise quarter-turns, each at rate \(\gamma>0\). In a harmonic trap with translational thermal noise, the exact optimal **one-position** heading classifier is the same for all tumbling rates and thermal noise strengths:

\[
\widehat\sigma(x,y)=
\begin{cases}
E,&x>|y|,\\
N,&y>|x|,\\
W,&-x>|y|,\\
S,&-y>|x|.
\end{cases}
\]

The equal-probability boundaries have zero stationary position probability and may be broken arbitrarily. The classifier also survives independent symmetric strictly unimodal measurement noise on the two rotated coordinates; an exact classification-accuracy formula and a sharp fast-tumbling/noise crossover are given below. These are inference statements, not new positional stationary-density formulas.

With \(\beta=\gamma/\mu\), \(\delta=\sqrt{\mu D}/v_0\), and \(Z\) distributed according to the known density

\[
f_\beta(z)=\frac{(1-z^2)^{\beta-1}}{B(1/2,\beta)}\mathbf1_{\{|z|<1\}},
\]

the optimal one-coordinate sign success probability and four-heading success probability are exactly

\[
p(\beta,\delta)=\frac12+\frac12\mathbb E\left[Z\,\operatorname{erf}\left(\frac{Z}{\sqrt2\delta}\right)\right],\qquad
\mathcal A(\beta,\delta)=p(\beta,\delta)^2,\quad\delta>0.
\]

At \(\delta=0\), interpret the error function as the sign function, yielding

\[
p(\beta,0)=\frac12+\frac{\Gamma(\beta+1/2)}{2\sqrt\pi\,\Gamma(\beta+1)}.
\]

For fixed \(\delta\ge0\), \(p\) is strictly decreasing in \(\beta>0\); for fixed \(\beta>0\), it is strictly decreasing in \(\delta\ge0\). If \(\delta>0\) stays fixed while \(\beta\to\infty\), then

\[
p(\beta,\delta)=\frac12+\frac1{(2\beta+1)\sqrt{2\pi}\delta}+O_\delta(\beta^{-2}).
\]

At strictly zero thermal noise the rate is instead \(p(\beta,0)=1/2+(2\sqrt{\pi\beta})^{-1}+o(\beta^{-1/2})\). The exact crossover between these different exponents is

\[
\boxed{\lim_{\beta\to\infty}\sqrt\beta\left[p(\beta,\delta_\beta)-\frac12\right]
=\frac1{2\sqrt{\pi(1+\lambda^2)}}}
\qquad\text{if}\quad\sqrt{2\beta}\delta_\beta\to\lambda\in[0,\infty).
\]

For example, at \(\beta=1\) and \(\delta=0\) the four-heading Bayes success probability is exactly \(9/16\), whereas at \(\beta=1\), \(\delta=0.3\) it is approximately \(0.5293088050\).

## Assumptions and scope

Let \(\mu,v_0,\gamma>0\) and \(D\ge0\). Work with the unique stationary law of

\[
d\mathbf r_t=\left(-\mu\mathbf r_t+\sqrt2v_0\boldsymbol\sigma_t\right)dt+\sqrt{2D}\,d\mathbf W_t,
\]

where \(\boldsymbol\sigma_t\in\{\pm\mathbf e_x,\pm\mathbf e_y\}\), and each of the two possible ninety-degree turns occurs at rate \(\gamma\). Brownian motion is independent of heading changes. The observed snapshot is the exact current physical position, not a trajectory. With the orthogonal coordinates \(u=(x+y)/\sqrt2\), \(v=(x-y)/\sqrt2\), normalize \(X=\mu u/v_0\), \(Y=\mu v/v_0\). Set \(\beta=\gamma/\mu\), \(\delta^2=\mu D/v_0^2\).

The further sensor-noise assertion has a separate scope: instead of (or in addition to) the physical thermal noise, each normalized rotated coordinate may be observed with independent additive noise having a positive, even density \(g_i\) strictly decreasing as \(|z|\) increases. This assertion concerns the optimal *classifier only*; its Gaussian-accuracy formulas apply only when the total independent coordinate noise is Gaussian with standard deviation \(\delta\). In the zero-noise case position support is the rotated square \(|X|<1\), \(|Y|<1\). All tie sets have probability zero.

## Proof

**1. Reduction to two independent stationary sign drives.** Write \(S_1=\sigma_x+\sigma_y\) and \(S_2=\sigma_x-\sigma_y\). Both take values \(\pm1\). Each physical ninety-degree turn flips exactly one of them, so the two signs independently flip at rate \(\gamma\). Their joint stationary law is uniform on four pairs. The normalized stationary coordinate is

\[
X=\mu\int_{-\infty}^0 e^{\mu s}S_1(s)\,ds+\delta G_1=Z_1+\delta G_1,
\]

with an identical independent representation for \(Y\), and \(G_i\) independent standard Gaussians. In the athermal subsystem the stationary state-resolved Fokker–Planck equations give the zero-current relation \(P_+(z)-P_-(z)=z[P_+(z)+P_-(z)]\). Their normalized solution is

\[
P_\pm(z)=\frac12(1\pm z)f_\beta(z),\qquad
f_\beta(z)=\frac{(1-z^2)^{\beta-1}}{B(1/2,\beta)}\quad(-1<z<1).
\]

This is a *known* athermal stationary conditional law, not the novel part of the finding. It implies \(\mathbb E[S_i\mid Z_i=z]=z\).

**2. Exact posterior and universal decision sectors.** For a generic even, positive, strictly decreasing-in-absolute-value independent measurement kernel \(g\), Bayes' formula yields

\[
\mathbb E[S\mid X=x]=\frac{\int_{-1}^1 z f_\beta(z)g(x-z)\,dz}{\int_{-1}^1 f_\beta(z)g(x-z)\,dz}.
\]

For \(x>0\) the numerator is

\[
\int_0^1 z f_\beta(z)\big[g(x-z)-g(x+z)\big]dz>0,
\]

because \(|x-z|<|x+z|\). It is strictly negative for \(x<0\), by symmetry. At zero noise, the posterior mean is exactly \(x\) on \((-1,1)\). Therefore the unique Bayes sign decision is \(\operatorname{sgn}x\) for every permitted rate and noise, and the two independent conditional posteriors factorize. The sign pair \((+,+)\) maps to east, \((+,-)\) north, \((-,-)\) west and \((-,+)\) south. Translating the two sign inequalities into physical coordinates proves the four sector conditions.

For Gaussian noise the exact state posterior is also reconstructible directly from the known stationary *position-only* density \(F_{\beta,\delta}=f_\beta*\varphi_\delta\):

\[
\Pr(S=+\mid X=x)=\frac12\left(1+x+\delta^2\frac{d}{dx}\log F_{\beta,\delta}(x)\right).
\]

This follows by differentiating the Gaussian convolution. Moreover its conditional mean has strictly positive derivative \(\operatorname{Var}(Z\mid X=x)/\delta^2\). The score representation is a convenient way to infer the hidden motor state from marginal-position measurements without reconstructing a separate state-conditioned density.

**3. Exact optimal accuracy.** Since \(S\in\{-1,+1\}\) and the optimal decision is \(\operatorname{sgn}X\),

\[
\Pr(\widehat S=S)=\frac12+\frac12\mathbb E[S\operatorname{sgn}(Z+\delta G)]
=\frac12+\frac12\mathbb E\left[Z\operatorname{erf}\left(\frac{Z}{\sqrt2\delta}\right)\right].
\]

At zero noise this becomes \(1/2+\mathbb E|Z|/2\), and evaluation of the beta integral gives the displayed gamma ratio. Both sign decisions succeed independently, so their product is the exact optimal heading-classification probability. For example, the uniform \(Z\) distribution at \(\beta=1\) gives \(p(1,0)=3/4\), hence \(\mathcal A(1,0)=9/16\).

**4. Strict monotonicity.** The variable \(Z^2\) has \(\operatorname{Beta}(1/2,\beta)\) distribution. Increasing \(\beta\) strictly shifts it downward in monotone likelihood-ratio order because the ratio of two densities is proportional to \((1-t)^{\beta_2-\beta_1}\). The function \(z\mapsto z\operatorname{erf}(z/(\sqrt2\delta))\) is even and strictly increasing on \(z>0\), so accuracy strictly decreases with \(\beta\), also at zero noise by the absolute-value formula. Increasing \(\delta\) strictly decreases the error function at every positive \(z\), proving the second monotonicity assertion.

**5. Sharp fast-switching crossover.** The exact even moments are

\[
\mathbb E Z^2=\frac1{2\beta+1},\qquad
\mathbb E Z^4=\frac3{(2\beta+1)(2\beta+3)}.
\]

For each fixed positive \(\delta\), Taylor's theorem for the error function, uniformly in \(|Z|\le1\), gives

\[
p-\frac12=\frac{\mathbb E Z^2}{\sqrt{2\pi}\delta}+O_\delta(\mathbb E Z^4),
\]

establishing the order \(\beta^{-1}\) with its sharp coefficient. At zero noise, the gamma-ratio asymptotic yields the distinct \(\beta^{-1/2}\) law. Finally set \(Y_\beta=\sqrt{2\beta}Z\). The beta central-limit scaling yields \(Y_\beta\Rightarrow G\sim N(0,1)\), and \(\mathbb E Y_\beta^2=2\beta/(2\beta+1)\le1\) gives uniform integrability of the linear-growth integrand. If \(\sqrt{2\beta}\delta_\beta\to\lambda\ge0\), dominated-convergence and Gaussian integration lead to

\[
\mathbb E\left[G\operatorname{erf}\left(\frac{G}{\sqrt2\lambda}\right)\right]
=\sqrt{\frac2\pi}\frac1{\sqrt{1+\lambda^2}},
\]

with \(\lambda=0\) interpreted using the sign function. Substitution gives the claimed crossover limit. No finite numerical experiment is used to justify an infinite-parameter statement.

## Verification

The standalone checker `verify.py` uses Python 3 with NumPy, SciPy and SymPy and can be run with `python verify.py`. It verifies the stationary state-resolved Fokker–Planck residuals symbolically, beta moment identities symbolically, the sector correspondence over an angular grid, the Bayes accuracy against a second independent quadrature identity, monotonicity samples, the fast-switching and crossover asymptotics at finite parameters, and independent stationary-state Monte Carlo tests. It reports `PASS 899 reproducible analytic/numerical diagnostics` on the specified environment. These diagnostics are corroboration; the proof above establishes the universal quantifiers.

## Relationship to prior work

Smith, Le Doussal, Majumdar and Schehr (2022, arXiv:2207.10445) introduced and solved the four-heading planar harmonic trap, proved the rotated-coordinate factorization and treated translational diffusion. Frydel (2022, arXiv:2207.08695) analyzed related beta-plus-Gaussian trapped-particle distributions. Garcia-Millan and Pruessner (2020, arXiv:2012.02900) derived exact observables for one-dimensional thermal run-and-tumble motion in harmonic confinement. Sun, Ye and Chen (2026, arXiv:2610.24961) explicitly provide one-dimensional athermal state-conditioned stationary densities. Accordingly, none of the model, positional law, scalar beta law, Gaussian convolution, or athermal one-dimensional conditional law is claimed to be new here.

The assessed extension is the full **four-state Bayes optimality** result, its noise-kernel-invariant decision sectors, the marginal-density score reconstruction, the sharp two-regime accuracy laws, and their uniform crossover. Originality is a best-knowledge comparison of statements and implications, not an independent priority certificate. Known exact state-resolved propagators may make portions deducible from more general formulae; the mathematical contribution is the derived complete classifier and its quantified singular accuracy transition.

## Limitations

The optimality assertion assumes the four-state orthogonal-quarter-turn model, uniform stationary prior, isotropic harmonic confinement, instantaneous position observation, and independent symmetric strictly decreasing observation kernels (or independent isotropic thermal Brownian noise). It does not hold automatically under correlated, biased, or asymmetric observation noise, anisotropic confinement, chiral turning, arbitrary heading-reset mechanisms, or conditioning on entire trajectories. The formula for \(\mathcal A\) and crossover assumes Gaussian total coordinate noise. The conclusions do not infer physical torque, entropy production or trajectory-wide motor-state decoding. Independent mathematical validation and publication-priority assessment have not been performed.

## References

1. N. R. Smith, P. Le Doussal, S. N. Majumdar and G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445v1 (first public 2022-07-21), https://arxiv.org/abs/2207.10445 .
2. D. Frydel, *Positing the problem of stationary distributions of active particles as third-order differential equation*, arXiv:2207.08695v1 (2022-07-18), https://arxiv.org/abs/2207.08695 .
3. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion: field theory and entropy production*, arXiv:2012.02900v1 (2020-12-04), https://arxiv.org/abs/2012.02900 .
4. A. Sun, F. Ye and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961v1 (2026-10-18), https://arxiv.org/abs/2610.24961 .
