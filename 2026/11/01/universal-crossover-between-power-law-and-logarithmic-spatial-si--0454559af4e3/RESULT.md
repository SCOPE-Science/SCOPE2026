# Universal crossover between power-law and logarithmic spatial singularities under velocity-resampling resets

## Finding

A one-dimensional inertial Langevin particle undergoes simultaneous position resetting to zero and independent Gaussian velocity resampling, at Poisson rate \(r>0\). The resampled velocity has variance \(\varepsilon^2\). As \(\varepsilon\) decreases to zero, the two different known singularity types of the stationary position density are connected by an exact **parameter-free crossover profile** on the spatial scale \(\varepsilon^3/c\), where \(c=2D_v/3\).

For \(y\ne0\), put \(x_\varepsilon(y)=\varepsilon^3 y/c\). Then

\[
\lim_{\varepsilon\downarrow0}\frac{\varepsilon}{r}\,p_\varepsilon(x_\varepsilon(y))=\mathcal F(y),\qquad
\mathcal F(y)=\frac1{\sqrt{2\pi}}\int_0^\infty \frac{\exp[-y^2/(2u^2(1+u))]}{u\sqrt{1+u}}\,du.
\]

The limit is uniform on every compact subset of \(\mathbb R\setminus\{0\}\); \(\mathcal F\) is even and strictly positive. Its two asymptotic edges are

\[
\mathcal F(y)=\frac1{\sqrt{2\pi}}\left[\log\frac1{|y|}+\log4+\frac{\log2-\gamma_{\rm E}}2+o(1)\right]\quad (y\to0),
\]
\[
\mathcal F(y)\sim \frac{2^{1/6}\Gamma(1/6)}{3\sqrt{2\pi}}\,|y|^{-1/3}\quad (|y|\to\infty).
\]

For fixed positive velocity-reset standard deviation, the density diverges logarithmically at the reset position; for an exactly zero velocity reset, it diverges with exponent \(-1/3\). The profile determines the singular crossover scale and its explicit constants; it does **not** identify a crossover at finite reset variance outside the stated small-variance limit.

## Assumptions and scope

Fix \(r,\gamma,D_v>0\). Between successive reset events the position and velocity solve

\[
dX_t=V_t\,dt,\qquad dV_t=-\gamma V_t\,dt+\sqrt{2D_v}\,dB_t.
\]

At each event of an independent homogeneous Poisson process of rate \(r\), set \(X=0\) and independently redraw \(V\) from \(N(0,\varepsilon^2)\), with \(\varepsilon\ge0\). Brownian noise is independent across nonoverlapping time segments. There is no spatial force, no reset-position dispersion, and no dependence of reset velocities on the pre-reset state. Let \(p_\varepsilon\) denote the stationary position density for \(x\ne0\), and define \(c=2D_v/3\) and \(h(t)=(1-e^{-\gamma t})/\gamma\).

The exact age-mixture representation is

\[
 p_\varepsilon(x)=r\int_0^\infty \frac{e^{-rt}}{\sqrt{2\pi W_\varepsilon(t)}}\exp\left[-\frac{x^2}{2W_\varepsilon(t)}\right]dt,\qquad
 W_\varepsilon(t)=\varepsilon^2h(t)^2+2D_v\int_0^t h(s)^2\,ds.
\]

For every fixed \(\varepsilon>0\) and any fixed reference length \(L>0\),

\[
p_\varepsilon(x)=\frac{r}{\varepsilon\sqrt{2\pi}}\log\frac L{|x|}+O(1)\quad (x\to0).
\]

For \(\varepsilon=0\),

\[
p_0(x)\sim r c^{-1/3}\frac{2^{1/6}\Gamma(1/6)}{3\sqrt{2\pi}}|x|^{-1/3}\quad(x\to0).
\]

The error bound implicit in the first display can depend on \(\varepsilon,r,\gamma,D_v,L\). These are spatial-density asymptotics, not statements about the joint position–velocity density or first-passage laws.

## Proof

**1. Regenerative stationary law.** The independent resetting events create identically distributed cycles. At an observation time in the stationary process, the backward time since the last reset is exponential with rate \(r\). Conditional on an age \(t>0\), the position is a centered Gaussian sum of the contribution \(h(t)V_0\) from the redrawn velocity and the stochastic convolution \(\sqrt{2D_v}\int_0^t h(t-s)\,dB_s\). Its variance is exactly \(W_\varepsilon(t)\); averaging its Gaussian density over the exponential age yields the stated formula. This renewal construction also supplies the unique stationary law of the reset process.

**2. Short-time variance.** Taylor expansion of \(h\) at zero gives \(h(t)=t+O(t^2)\) and \(2D_v\int_0^th(s)^2ds=c t^3+O(t^4)\). In particular

\[
 W_\varepsilon(t)=\varepsilon^2t^2(1+O(t))+ct^3(1+O(t))
\]

uniformly for \(\varepsilon\) in bounded intervals and sufficiently small \(t\). There exist fixed positive bounds, independent of sufficiently small \(\varepsilon\), comparing \(W_\varepsilon(t)\) to \(\varepsilon^2t^2+ct^3\) for \(t\) in a common small interval.

**3. Scaling and domination.** Set \(t=\varepsilon^2u/c\), \(x=\varepsilon^3y/c\). For every fixed \(u>0\),

\[
\frac{c^2}{\varepsilon^6}W_\varepsilon(\varepsilon^2u/c)\longrightarrow u^2(1+u),\qquad e^{-r\varepsilon^2u/c}\longrightarrow1.
\]

After changing variables in the mixture, the integrand of \(\varepsilon p_\varepsilon(x_\varepsilon(y))/r\) converges pointwise to the displayed integrand defining \(\mathcal F(y)\). On the common small-time interval the comparison in step 2 bounds the integrand by a constant multiple of \(u^{-1}(1+u)^{-1/2}\exp[-a y^2/(u^2(1+u))]\) for some \(a>0\). This is integrable at zero for \(y\ne0\) and at infinity. The part of the age integral with \(t\) above that interval contributes \(O(\varepsilon)\) to the rescaled density, since its variance has a positive lower bound and the exponential reset-age law is integrable. Dominated convergence proves the limit and, using the smallest absolute \(y\) in a compact set, its local uniformity away from zero.

**4. Small-argument constant.** For \(y>0\) split the integral defining \(\mathcal F\) at a small fixed \(\delta>0\). On \((0,\delta)\), the leading integral is \(\frac12 E_1(y^2/(2\delta^2))\), where \(E_1(z)=\int_z^\infty e^{-s}ds/s\), and it equals \(\log(\delta/y)+(\log2-\gamma_{\rm E})/2+o(1)\) as \(y\downarrow0\) at fixed \(\delta\). The difference caused by replacing \((1+u)^{-1/2}\) and \(u^2(1+u)\) with their small-\(u\) approximations vanishes as \(\delta\downarrow0\). On \((\delta,\infty)\) dominated convergence gives

\[
 \int_\delta^\infty\frac{du}{u\sqrt{1+u}}=\log\frac{\sqrt{1+\delta}+1}{\sqrt{1+\delta}-1}=\log\frac4\delta+o(1).
\]

Combining and then sending \(\delta\downarrow0\) gives the exact constant. Evenness gives the negative side.

**5. Large-argument power law.** Put \(u=|y|^{2/3}v\). After multiplying by \(|y|^{1/3}\), dominated convergence (with separate bounds for \(v\le1\) and \(v\ge1\)) reduces the limit to

\[
 \frac1{\sqrt{2\pi}}\int_0^\infty v^{-3/2}e^{-1/(2v^3)}dv
 =\frac{2^{1/6}\Gamma(1/6)}{3\sqrt{2\pi}}.
\]

This is the stated large-argument constant.

**6. Two endpoint singularities.** For fixed \(\varepsilon>0\), use \(W_\varepsilon(t)=\varepsilon^2t^2(1+O(t))\) to isolate the local \(t^{-1}\) integral in the mixture. Its effective cutoff is \(t\asymp |x|/\varepsilon\), giving coefficient \(r/(\varepsilon\sqrt{2\pi})\) in front of \(\log(L/|x|)\), while the remainder is bounded. For \(\varepsilon=0\), use \(W_0(t)=ct^3(1+O(t))\) and substitute \(t=(|x|/\sqrt c)^{2/3}v\); the same gamma integral from step 5 gives the specified \(|x|^{-1/3}\) coefficient. These two fixed-parameter limits do not commute with the small-\(\varepsilon\) scaling limit.

## Verification

Run `python checks.py` with NumPy and SciPy. The program checks the profile against the exact regenerative integral across three distinct choices of \((\gamma,D_v,r)\), tests evenness, and verifies both limiting constants numerically. In the package the verifier passes 47 deterministic quadrature and consistency checks. Numerical quadrature is finite evidence only: the renewal formula, dominated-convergence arguments, and integral asymptotics above prove the limits.

## Relationship to prior work

Franke and Sokolov (2026) establish and discuss the distinct stationary spatial singularities for zero-velocity and thermal-equilibrium Gaussian velocity resetting in one-dimensional underdamped Brownian motion. Their full accessible article was inspected for the same reset object and singular exponents. The present result treats a continuous family of arbitrarily small *velocity reset variances* and evaluates the nontrivial crossover profile, exact scaling width, normalization, and both matching constants. It does not claim the two endpoint exponents as new.

Singh (2020) studies random acceleration under stochastic resetting, including fixed zero-velocity protocols; Gupta (2018/2019) considers an underdamped process with a different reset rule affecting position rather than fully resampling velocity. Neither checked source was identified as establishing the stated small-variance crossover. The construction uses standard regenerative Gaussian-mixture analysis and asymptotic integration; claims of global priority or independent certification are not made.

## Limitations

The theorem assumes a single freely moving one-dimensional Gaussian inertial particle, an independent Poisson reset clock, full position reset and independently sampled centered Gaussian reset velocities. It does not cover position-only resets, state-dependent rates, non-Gaussian velocity reset laws, external forces, or finite-\(\varepsilon\) uniform error bounds as \(y\) approaches zero or infinity. The accessible literature comparison does not establish absolute novelty; stronger general renewal-mixture asymptotics may encompass some statements.

## References

1. H. Franke and I. M. Sokolov, “Resetting of underdamped Brownian motion,” *Physical Review E* **113**, 064125 (2026), DOI: 10.1103/qyl8-6q9h. Public article dated 11 June 2026.
2. P. Singh, “Random acceleration process under stochastic resetting,” arXiv:2007.05576v1 (10 July 2020).
3. D. Gupta, “Stochastic resetting in underdamped Brownian motion,” arXiv:1812.07227v1 (2018); journal publication in 2019.
