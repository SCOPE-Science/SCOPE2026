# A universal Beta disk and two distinct memory layers for independently reset active particles

## Finding

In a harmonically trapped planar active Brownian particle, independent position resetting and orientation resetting produce two different stationary memory scales in the strong-trap limit. When the position-reset rate grows proportionally to trap stiffness, the normalized stationary position has an **independent Beta radial variable and a nonuniform angular reset-diffusion variable**. The two-time position correlation retains a fast radial relaxation at scale \(k^{-1}\) and a separate angular relaxation at fixed physical times. In particular, the strong-trap and zero-lag limits of the correlation do not commute.

For \(c>0\), \(h>0\), \(D_R>0\), put \(m=h/(h+D_R)\), \(\mu=(1+c)^{-1}\) and \(\nu=c/((1+c)^2(2+c))\). The stationary normalized position \(Y_k=kX/v\), with position-reset rate \(r=ck\), obeys
\[
Y_k(0)\ \Longrightarrow\ R U_0,\qquad R\sim\mathrm{Beta}(1,c),\quad R\perp U_0,
\]
where \(U_0=e^{i\Theta_0}\) follows the stationary angular-reset diffusion. Moreover, for each \(s\ge0\),
\[
\lim_{k\to\infty}\mathbb E[Y_k(0)\overline{Y_k(s/k)}]
=\mu^2+\nu e^{-(1+c)s},
\]
whereas for each **fixed** \(t>0\),
\[
\lim_{k\to\infty}\mathbb E[Y_k(0)\overline{Y_k(t)}]
=\mu^2\{m^2+(1-m^2)e^{-(h+D_R)t}\}.
\]
The first expression at \(s=0\) is \(\mu^2+\nu\), while the second expression as \(t\downarrow0\) is \(\mu^2\): the finite gap \(\nu>0\) is a sharp, unresolved-by-fixed-lag memory layer.

## Assumptions and scope

Identify the physical plane with \(\mathbb C\). Fix independent constants \(v,k,D_R,h,c>0\), and write \(r=ck\). Let \(\Theta_t\in\mathbb R/(2\pi\mathbb Z)\) be a circular Brownian motion with generator \(D_R\partial_\theta^2\), independently reset to angle zero at Poisson rate \(h\). Set \(U_t=e^{i\Theta_t}\). Independently, a Poisson clock of rate \(r\) resets the physical position \(X_t\) to zero **without changing the current orientation**. Between those resets,
\[
\frac{dX_t}{dt}=-kX_t+vU_t.
\]
All statements refer to the unique jointly stationary process driven by the two independent clocks and the angular Brownian motion. There is no translational thermal noise. The limit \(k\to\infty\) keeps \(c,D_R,h,v\) fixed. These assumptions differ from simultaneous resetting of position and orientation.

The orientation law at stationarity has density on \([-\pi,\pi]\)
\[
q_h(\theta)=\frac{\kappa\cosh(\kappa(\pi-|\theta|))}{2\sinh(\pi\kappa)},\qquad \kappa=\sqrt{h/D_R},
\]
and Fourier coefficients \(\mathbb E[U_0^j]=h/(h+D_Rj^2)\) for all integer \(j\). For \(0<\rho<1\), \(-\pi<\theta<\pi\), the limiting polar measure is
\[
\mathbb P(R\in d\rho,\Theta_0\in d\theta)=c(1-\rho)^{c-1}q_h(\theta)\,d\rho\,d\theta.
\]
The planar area density is \(c(1-\rho)^{c-1}q_h(\theta)/\rho\), exhibiting a central integrable singularity and an edge whose density diverges, stays finite, or vanishes as \(c<1\), \(c=1\), or \(c>1\), respectively. For any nonnegative integers \(p,q\),
\[
\mathbb E[(RU_0)^p(\overline{RU_0})^q]
=\frac{\Gamma(p+q+1)\Gamma(c+1)}{\Gamma(p+q+c+1)}
\frac{h}{h+D_R(p-q)^2}.
\]

## Proof

**Stationary construction and quantitative approximation.** Use the stationary angular process on the full time axis and the independent stationary position-reset Poisson process. Let \(A_k(t)\) be the age of the last position reset at time \(t\); at each fixed time \(A_k\sim\mathrm{Exp}(ck)\) and is independent of the entire orientation path. Variation of constants since the last reset gives the exact identity
\[
Y_k(t)=k\int_0^{A_k(t)}e^{-ks}U_{t-s}\,ds,\qquad |Y_k(t)|\le1.
\]
Set \(Z_k(t)=U_t(1-e^{-kA_k(t)})\). Conditional Jensen with the subprobability measure \(ke^{-ks}\mathbf1_{s\le A_k(t)}ds\) gives
\[
\mathbb E|Y_k(t)-Z_k(t)|^2\le\int_0^\infty ke^{-ks}\mathbb E|U_{t-s}-U_t|^2ds.
\]
For the angular reset diffusion, \(\mathbb E|U_{t-s}-U_t|^2\le(2D_R+4h)s\): without an intervening reset the Brownian chord bound is \(2D_Rs\), and the probability of at least one reset is at most \(hs\) with squared chord at most four. Consequently,
\[
\mathbb E|Y_k(t)-Z_k(t)|^2\le\frac{2D_R+4h}{k}.
\]
This bound is uniform in \(c\) and \(t\). With \(E=kA_k\sim\mathrm{Exp}(c)\), the variable \(1-e^{-E}\) has cumulative distribution \(1-(1-\rho)^c\), exactly the \(\mathrm{Beta}(1,c)\) law, and it is independent of \(U_t\). The bound proves convergence in quadratic Wasserstein distance at rate at most \(\sqrt{(2D_R+4h)/k}\), and thus convergence of all finite polynomial moments on the closed unit disk. The stationary angular density solves \(D_Rq''-hq+h\delta_0=0\) on the circle. Direct solution with periodic boundary conditions yields \(q_h\), whose Fourier coefficients follow from the angular generator. Radial independence gives the displayed joint moments.

**Fast memory layer.** In time \(t=s/k\), the angular process is constant in probability as \(k\to\infty\). The rescaled last-reset age becomes the age of a rate-\(c\) Poisson process in time \(s\). Thus finite-dimensional distributions of the normalized position converge to \(U_0R_s\), where \(R_s\) is the stationary piecewise-deterministic process \(\dot R_s=1-R_s\) with independent resetting \(R\mapsto0\) at rate \(c\). Its stationary mean and variance are, respectively, \(\mu=1/(1+c)\) and \(\nu=c/((1+c)^2(2+c))\). Its generator gives
\[
\mathbb E[R_s\mid R_0]=\mu+(R_0-\mu)e^{-(1+c)s},
\]
hence \(\mathbb E[R_0R_s]=\mu^2+\nu e^{-(1+c)s}\). Boundedness allows passage from distributional convergence to correlations.

**Slow memory layer.** For distinct fixed physical times \(t_1<\dots<t_n\), with probability tending to one each last-position-reset age is shorter than half the minimum spacing. The corresponding ages depend on disjoint Poisson increments and therefore converge jointly to independent scaled exponential ages, also independent of the orientation path. The above quantitative approximation shows that the joint normalized position converges to \((R_jU_{t_j})_{j=1}^n\), where the \(R_j\) are independent \(\mathrm{Beta}(1,c)\) variables, independent of the correlated stationary orientations. The first orientation harmonic obeys
\[
\mathbb E[U_t\mid U_0]=m+(U_0-m)e^{-(h+D_R)t},\qquad m=\frac{h}{h+D_R}.
\]
Taking the product with \(\overline{U_0}\) and using \(|U_0|=1\) gives \(\mathbb E[U_t\overline{U_0}]=m^2+(1-m^2)e^{-(h+D_R)t}\), proving the second formula. The limiting zero-lag discrepancy equals the strictly positive \(\nu\) and is not a nonzero persistent long-lag covariance.

**Other positional-reset scales.** More generally, if \(r_k/k\to0\), the same coupling and \(kA_k\to\infty\) show \(Y_k(0)\Rightarrow U_0\) (a ring). If \(r_k/k\to\infty\), then \(kA_k\to0\), so \(Y_k(0)\Rightarrow0\). For \(r_k/k\to c\in(0,\infty)\), the preceding Beta-disk conclusion applies. These three cases form the complete trichotomy for positive deterministic reset rates under the stated fixed angular dynamics.

## Verification

The standalone standard-library program `checker.py` checks angular Fourier coefficients and normalization by quadrature; Beta moments and radial density; finite-stiffness stationary generator equations at rational parameters; exact algebraic moment identities; and both two-time scaling laws against exact finite-stiffness two-time correlations. Its final output is `PASS 640 total deterministic checks including time-covariance limits`. These numerical and finite-parameter checks are reproducibility tests, not substitutes for the analytic proofs above.

An independent derivation uses the stationary moment equations for physical complex position \(z=X/v\). Set \(\alpha=k+r\), \(\beta=h+D_R\), \(m=h/\beta\). Then
\[
\mathbb Ez=\frac m\alpha,\quad
\mathbb E[z\overline U]=\frac{1+h\mathbb Ez}{\alpha+\beta},\quad
\mathbb E|z|^2=\frac{2\mathbb E[z\overline U]}{2k+r}.
\]
The exact normalized complex two-time correlation is
\[
\begin{aligned}
\mathbb E[Y_k(0)\overline{Y_k(t)}]
=k^2\bigg[&e^{-\alpha t}\mathbb E|z|^2
+\frac{m\mathbb Ez}{\alpha}(1-e^{-\alpha t})\\
&+(\mathbb E[z\overline U]-m\mathbb Ez)
\frac{e^{-\beta t}-e^{-\alpha t}}{\alpha-\beta}\bigg],
\end{aligned}
\]
with the quotient interpreted as \(te^{-\alpha t}\) when \(\alpha=\beta\). Direct limits reproduce the two memory expressions.

## Relationship to prior work

Shee (arXiv:2409.06920v1, first public 2024-09-11) studies an active Brownian particle in a harmonic trap with stochastic position and orientation resetting **at the same events**, and obtains moment and kurtosis formulas. Kumar, Sadekar, and Basu (arXiv:2008.03294) distinguish position-only and orientation-only resetting for free active Brownian motion; no harmonic-trap strong-coupling comparison occurs there. Chaudhuri and Dhar (2020) study the harmonic active Brownian particle without resets, and derive exact moments. Basu et al. (arXiv:1910.10083) and Frydel (arXiv:2309.12537) describe Beta-type stationary laws for run-and-tumble particles in traps, so the mere appearance of a Beta distribution is **not** claimed to be new. The present statement instead concerns **two independent reset clocks** and the resulting independent polar law, quantitative trap limit, and **distinct noncommuting fast and slow correlation layers**. These comparisons do not establish a universal priority claim; relevant generic switching-process limit theorems may imply special portions of the result.

## Limitations

The theorem excludes translational Brownian noise, nonlinear traps, velocity inertia, correlated reset clocks, and simultaneous position-orientation resetting. Angular resetting is to one specified heading and not to a uniformly chosen heading. The two correlations have different time scalings and must not be conflated. The edge singularity is a stationary spatial-density property, not a thermodynamic phase transition. No finite-data parameter recovery or universal novelty claim is made. The bibliographic comparison is limited to the cited material; other equivalent formulations may exist.

## References

1. S. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920v1 (first public 2024-09-11), https://arxiv.org/abs/2409.06920.
2. S. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294 (2020), https://arxiv.org/abs/2008.03294.
3. D. Chaudhuri and A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv preprint (2020), https://arxiv.org/search/?query=Active+Brownian+particle+in+harmonic+trap%3A+exact+computation+of+moments&searchtype=all.
4. U. Basu et al., *Stationary states of an active Brownian particle in a harmonic trap*, arXiv:1910.10083 (2019), https://arxiv.org/abs/1910.10083.
5. D. Frydel, *Stationary distributions for harmonically trapped active particles*, arXiv:2309.12537 (2023), https://arxiv.org/abs/2309.12537.
