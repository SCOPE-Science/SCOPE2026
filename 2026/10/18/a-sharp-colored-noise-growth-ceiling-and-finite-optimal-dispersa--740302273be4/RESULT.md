# A sharp colored-noise growth ceiling and finite optimal dispersal in two ecological patches

## Finding

For a symmetric two-patch population with independent Ornstein–Uhlenbeck fluctuations in its local growth rates, a positive migration rate always improves the almost-sure asymptotic logarithmic growth rate over the uncoupled baseline. However, the improvement vanishes in both the zero-migration and infinite-migration limits, so at least one strictly positive, finite optimal migration rate exists. More quantitatively, for all \(M,\lambda,D>0\), the growth enhancement \(g(M)\) satisfies the strict, parameter-explicit inequality

\[
0<g(M)<\frac{\lambda D}{2(M+\lambda)}.
\]

This upper envelope is asymptotically attained to first order in weak environmental noise, and its leading large-migration coefficient is exact:

\[
\lim_{D\downarrow0}\frac{g(M)}D=\frac{\lambda}{2(M+\lambda)},
\qquad
\lim_{M\to\infty}M g(M)=\frac{\lambda D}{2}.
\]

The small-migration limit is quantitative: for every \(R>0\),

\[
g(M)\le \frac M2(\cosh R-1)+\frac DR,
\]

which implies \(\lim_{M\downarrow0}g(M)=0\). These claims concern the **exact colored-noise model**, without reducing the Ornstein–Uhlenbeck forcing to a white-noise approximation.

## Assumptions and scope

Let \(C_1(t),C_2(t)>0\) be the abundances in two patches. Let \(r\in\mathbb R\) be their common baseline growth rate, and let \(M,\lambda,D>0\). The population and environmental processes are defined by

\[
\dot C_i(t)=[r+\eta_i(t)]C_i(t)+\frac M2[C_{3-i}(t)-C_i(t)],\qquad i\in\{1,2\},
\]

\[
d\eta_i=-\lambda\eta_i\,dt+\lambda\sqrt{2D}\,dW_i(t),
\]

where the two Brownian motions are independent, and the environmental processes are taken in their stationary versions. Positive initial abundances are arbitrary. Put

\[
X(t)=\log\frac{C_1(t)}{C_2(t)},\qquad H(t)=\eta_1(t)-\eta_2(t).
\]

Then

\[
\dot X=H-M\sinh X,\qquad
 dH=-\lambda H\,dt+2\lambda\sqrt D\,dW,
\]

where \(W\) is standard Brownian motion and \(\operatorname{Var}(H)=2\lambda D\) at stationarity. For every \(M>0\), write \(\nu_M\) for the unique stationary law of \((X,H)\), and define

\[
g(M)=\lim_{t\to\infty}\frac1t\log\frac{C_1(t)+C_2(t)}{C_1(0)+C_2(0)}-r.
\]

The limit exists almost surely and is deterministic. Expectations below are under \(\nu_M\), written \(\mathbb E_M\). The stated limit as \(D\downarrow0\) fixes \(M,\lambda>0\); the limit as \(M\to\infty\) fixes \(D,\lambda>0\). Existence of an interior maximizer does **not** assert uniqueness or give its location.

## Proof

**1. Stationary dynamics and growth identities.** The scalar random ODE for \(X\) is strictly contracting in its initial state: two solutions driven by the same environmental path obey

\[
|X_1(t)-X_2(t)|\le e^{-Mt}|X_1(0)-X_2(0)|.
\]

Existence and integrability follow from the OU stationary forcing and the restoring drift. For example, the Markov generator of \((X,H)\) is

\[
\mathcal L=(h-M\sinh x)\partial_x-\lambda h\partial_h
 +2\lambda^2D\partial_{hh}.
\]

A Lyapunov function \(\cosh x+a h^2\) with sufficiently large \(a\) controls both \(\sinh^2 x\) and \(h^2\): use \(h\sinh x\le (M/2)\sinh^2x+h^2/(2M)\). Standard truncation then justifies the stationary moment identities below. The strictly contractive pullback dynamics yield a unique stationary law; it is ergodic as a causal function of the ergodic OU path.

The logarithmic geometric mean of the patch abundances has derivative

\[
\frac d{dt}\left[\frac{\log C_1+\log C_2}{2}\right]
=r+\frac{\eta_1+\eta_2}{2}+\frac M2(\cosh X-1).
\]

The difference between the logarithm of the arithmetic mean and that of the geometric mean is \(\log\cosh(X/2)\), a stationary sublinear boundary term at long times. Therefore the ergodic theorem gives

\[
g(M)=\frac M2\mathbb E_M[\cosh X-1].\tag{1}
\]

Alternatively, with \(p_i=C_i/(C_1+C_2)\), observe that \(p_1-p_2=\tanh(X/2)\). Differentiating the logarithm of total abundance gives the second exact identity

\[
g(M)=\frac12\mathbb E_M[H\tanh(X/2)].\tag{2}
\]

Since nondegenerate OU forcing rules out \(X=0\) almost surely, equation (1) proves \(g(M)>0\).

**2. Exact Gaussian-response identity and global upper ceiling.** Take the stationary solution of the random ODE as a causal functional of the past Gaussian path \(H(s)\). A perturbation of the additive forcing at time \(-u\) changes \(X(0)\) by the causal response

\[
R_M(u)=\exp\!\left(-M\int_{-u}^0\cosh X(v)\,dv\right),\qquad u\ge0.
\]

For stationary OU forcing, the covariance function is

\[
\mathbb E[H(0)H(-u)]=2\lambda D e^{-\lambda u}.
\]

Gaussian integration by parts, initially for finite-past functionals and then by dominated convergence, applies to equation (2) and yields the **exact identity**

\[
\boxed{
 g(M)=\frac{\lambda D}{2}\int_0^\infty e^{-\lambda u}\,
 \mathbb E_M\!\left[\operatorname{sech}^2\!\left(\frac{X(0)}2\right)
 R_M(u)\right]du.}
\tag{3}
\]

Indeed, the derivative of \(\tanh(X(0)/2)\) with respect to the forcing at \(-u\) is \(\tfrac12\operatorname{sech}^2(X(0)/2)R_M(u)\). Equation (3) includes the factor \(1/2\) from (2). Since \(\cosh X\ge1\), one has \(0<R_M(u)\le e^{-Mu}\), while \(0<\operatorname{sech}^2(X/2)\le1\). Inserting these inequalities gives

\[
0<g(M)<\frac{\lambda D}{2}\int_0^\infty e^{-(\lambda+M)u}\,du
=\frac{\lambda D}{2(\lambda+M)}.\tag{4}
\]

The inequality is strict for positive noise, because the stationary ratio is not identically zero.

**3. Large migration and weak-noise sharpness.** Stationarity of \(X^2\) and Cauchy–Schwarz imply

\[
M\mathbb E_M[X\sinh X]=\mathbb E_M[XH],\qquad
\mathbb E_M[X^2]\le\frac{2\lambda D}{M^2}.
\tag{5}
\]

Stationarity of \(\cosh X\) also gives

\[
M\mathbb E_M[\sinh^2X]=\mathbb E_M[H\sinh X],
\qquad
\mathbb E_M[\sinh^2X]\le\frac{2\lambda D}{M^2}.\tag{6}
\]

At fixed \(M,\lambda\), equations (5)–(6) imply \(X\to0\) in probability as \(D\downarrow0\); for fixed \(u\), they also imply \(R_M(u)\to e^{-Mu}\). The integrand in (3) is bounded by \(e^{-(\lambda+M)u}\). Dominated convergence proves

\[
\lim_{D\downarrow0}\frac{g(M)}D=\frac{\lambda}{2(\lambda+M)}.
\]

For fixed \(D,\lambda\), substitute \(u=v/M\) in (3). Equations (5)–(6), stationarity, and

\[
0\le\cosh X-1\le\frac12\sinh^2 X
\]

show that the random factor in the new integrand tends in probability to \(e^{-v}\) for each fixed \(v\), while it is dominated by \(e^{-v}\). Hence

\[
\lim_{M\to\infty}M g(M)=\frac{\lambda D}{2}.
\]

**4. Vanishing improvement for weak migration.** Stationarity of \(XH\) and \(\cosh X\) gives the exact relation

\[
\lambda\mathbb E_M[XH]+M^2\mathbb E_M[\sinh^2X]
=\mathbb E[H^2]=2\lambda D.
\]

Combining this with the first identity in (5) yields

\[
M\mathbb E_M[X\sinh X]\le 2D.\tag{7}
\]

For every fixed \(R>0\), split the expectation in (1) into \(|X|\le R\) and \(|X|>R\). Since \(\cosh x-1\le |\sinh x|\) and, on the latter region, \(|\sinh x|\le x\sinh x/R\), equation (7) implies

\[
g(M)\le \frac M2(\cosh R-1)+\frac DR.\tag{8}
\]

For sufficiently small \(M<\lambda\), take \(R=\tfrac12\log(\lambda/M)\) to see \(g(M)\to0\) as \(M\downarrow0\).

**5. Existence of an interior optimum.** On any compact interval of positive migration rates, the stationary laws vary weakly continuously by uniqueness of the invariant law and the uniform bounds in (5)–(6). Those bounds also make \(\cosh X\) uniformly integrable, so (1) shows that \(g(M)\) is continuous. It is strictly positive on \((0,\infty)\), but tends to zero at both endpoints by (4) and (8). Therefore it achieves a positive global maximum at at least one finite \(M_*\in(0,\infty)\).

## Verification

The included `verification.py` independently simulates the **original** coupled OU and log-ratio equations, using exact OU time steps and symmetric drift splitting. It compares the two stationary growth identities (1)–(2), checks the nonperturbative upper envelope, and evaluates the moment-budget identity against \(2\lambda D\). The deterministic algebra is rederived in the proof; these trajectories serve only as sanity checks, not as an infinite-time certificate. Run with `python verification.py` after installing NumPy.

## Relationship to prior work

Henderson and Tiffeau-Mayer (arXiv:2603.02403v1, 2 March 2026) introduce this exact two-patch colored-noise model, derive the stationary growth identity corresponding to (1), and report a **numerically** observed finite optimum of growth as a function of migration. Their supplementary material evaluates the colored-noise case numerically and gives the exact Bessel-function growth expression in the **white-noise** case. The new results here are (3), its sharp all-noise bound (4), both nonperturbative endpoint analyses, and the resulting rigorous attained optimality in the original colored-noise system. The source's infinite-patch weak-noise coefficient concerns a different limiting dimension.

Hening, Nguyen, and Yin (Journal of Mathematical Biology, 2018; DOI 10.1007/s00285-017-1153-2) establish general structured-population growth principles and analyze a **white-noise**, sometimes correlated-patch setting. Benaïm, Lobry, Sari, and Strickler (arXiv:2111.12633) study finite optimal/beneficial migration under **switching** environments rather than independent OU fluctuations with the explicit response ceiling above. Neither of those results is asserted to be a novelty certificate: any broader theorem implying equations (3)–(4) would supersede the present originality assessment.

## Limitations

The proof assumes precisely two patches, symmetric migration, independent mean-zero OU growth fluctuations with equal intensities, and strictly positive \(M,\lambda,D\). It establishes existence, not uniqueness or an exact location, of the optimal migration rate. The logarithmic small-migration estimate is an upper bound and is not claimed as a sharp asymptotic equivalence. The proof does not address mortality, nonlinear density dependence, demographic noise, spatially correlated forcing, or an arbitrary number of patches. Historical priority beyond inspected primary sources remains subject to independent confirmation.

## References

1. J. F. D. Henderson and A. Tiffeau-Mayer, *Fluctuating environments are sufficient to drive substantial variability in species abundance across locations*, arXiv:2603.02403v1 (first public posting 2 March 2026). https://arxiv.org/html/2603.02403
2. A. Hening, D. H. Nguyen, and G. Yin, *Stochastic population growth in spatially heterogeneous environments: the density-dependent case*, Journal of Mathematical Biology 76 (2018). https://doi.org/10.1007/s00285-017-1153-2
3. M. Benaïm, C. Lobry, T. Sari, and E. Strickler, *Untangling the role of temporal and spatial variations in persistence of populations*, arXiv:2111.12633 (2021). https://arxiv.org/abs/2111.12633
