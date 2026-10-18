# Two local velocity covariances determine both boundary resetting rates

## Finding

Consider the stationary ordered harmonic chain driven by two independently resetting Brownian boundary walls, as specified below. Its *thermodynamic-limit bulk* velocity variance and nearest-neighbor velocity covariance determine the two wall-resetting rates uniquely, **up to interchange of left and right**, when the two wall diffusion constants are equal and known.

Set \(\Omega=2\sqrt{k/m}\), \(K=Dk/\gamma\), and \(S=C_0/K\), \(T=C_1/K\). A pair of bulk observations arises from **some pair of finite, strictly positive resetting rates** if and only if

\[
S>0,\qquad \sqrt{1+S^2}-1\le T<\frac{\sqrt{1+4S^2}-1}{2}.
\]

For every such \((S,T)\), the unordered rate pair is unique. The lower boundary holds exactly for equal resetting rates; the upper boundary is never attained with both rates finite, but is sharp. A single bulk variance is insufficient to identify the pair. These conclusions concern the exact thermodynamic-limit second moments, not finite-chain or finite-sample inference.

## Assumptions and scope

Fix \(m,k,\gamma,D>0\). Let an ordered chain of \(N\ge3\) oscillators obey, for \(j=1,\ldots,N\),

\[
m\ddot x_j=k(x_{j-1}-2x_j+x_{j+1})-\gamma\dot x_j(\mathbf1_{j=1}+\mathbf1_{j=N}).
\]

The walls \(x_0\) and \(x_{N+1}\) are independent one-dimensional Brownian motions with diffusion constant \(D\) (quadratic variation rate \(2D\)), each instantaneously reset to zero by an independent Poisson clock of rates \(r_1,r_2>0\). They are taken in their stationary resetting regimes. There is no separate thermal noise. Take the chain in its stationary state, then let \(N\to\infty\) with indices a fixed distance from the center:

\[
C_n=\lim_{N\to\infty}\operatorname{Cov}\bigl(\dot x_{\lfloor N/2\rfloor},\dot x_{\lfloor N/2\rfloor+n}\bigr),\quad n=0,1,2,\ldots.
\]

The limit is taken at fixed \(n\). Parameters \(m,k,\gamma,D\) are known, and both wall diffusion constants have the same value \(D\). Rate labels cannot be distinguished by a reflection-symmetric bulk second-moment measurement.

## Proof

**1. Fourier reduction of the forward covariance.** A stationary resetting Brownian wall with resetting rate \(r\) has covariance \((2D/r)e^{-r|t|}\); this follows by conditioning on whether a reset occurs in a lag and evaluating the stationary exponential age. Its force \(kx_0\) on the boundary chain oscillator consequently has covariance amplitude \(a^2=2Dk^2/r\). Applying the linear chain's exact bulk response (see Reference 1, Section 4 and Appendix B) to the two independent walls yields

\[
C_n=\sum_{i=1}^2\frac{a_i^2r_i}{2\gamma m}\,\frac1\pi\int_0^\pi
\frac{\cos(nq)}{r_i^2+\Omega^2\sin^2(q/2)}\,dq,
\qquad a_i^2=\frac{2Dk^2}{r_i}.
\]

This is a stationary *second-moment* relation; Gaussianity of the reset walls is not assumed. Put \(A=r^2+\Omega^2/2\), \(B=\Omega^2/2\). For every integer \(n\ge0\), the standard Poisson-kernel cosine transform gives

\[
\frac1\pi\int_0^\pi\frac{\cos(nq)}{A-B\cos q}\,dq
=\frac{1}{\sqrt{A^2-B^2}}\left(\frac{A-\sqrt{A^2-B^2}}{B}\right)^n.
\]

Set

\[
\rho(r)=\frac{\sqrt{r^2+\Omega^2}-r}{\sqrt{r^2+\Omega^2}+r}\in(0,1).
\]

Then \(\sqrt{A^2-B^2}=r\sqrt{r^2+\Omega^2}\) and \(\rho/(1-\rho^2)=\Omega^2/[4r\sqrt{r^2+\Omega^2}]\). Substituting gives the entire exact spatial covariance sequence

\[
\boxed{C_n=K\sum_{i=1}^2\frac{\rho(r_i)^{n+1}}{1-\rho(r_i)^2}},\qquad n=0,1,\ldots.
\]

**2. Reparametrization and strict convexity.** Let \(y_i=\rho(r_i)/(1-\rho(r_i)^2)>0\). The map \(r\mapsto y\) is a continuous strictly decreasing bijection from \((0,\infty)\) onto \((0,\infty)\). With

\[
h(y)=\frac{\sqrt{1+4y^2}-1}{2},\quad h''(y)=\frac{2}{(1+4y^2)^{3/2}}>0,
\]

we have \(S=y_1+y_2\) and \(T=h(y_1)+h(y_2)\). For fixed \(S>0\), relabel the two walls so that

\[
y_1=(S+\delta)/2,\qquad y_2=(S-\delta)/2,\qquad 0\le\delta<S.
\]

The function \(F_S(\delta)=h((S+\delta)/2)+h((S-\delta)/2)\) satisfies \(F_S'(\delta)=[h'((S+\delta)/2)-h'((S-\delta)/2)]/2>0\) for \(0<\delta<S\). Hence it is strictly increasing on the entire nonnegative interval, with

\[
F_S(0)=2h(S/2)=\sqrt{1+S^2}-1
\]

and \(\lim_{\delta\uparrow S}F_S(\delta)=h(S)=(\sqrt{1+4S^2}-1)/2\), a value not attained because it requires \(y_2=0\), equivalently \(r_2=\infty\). Continuity gives every intermediate \(T\). Strict monotonicity gives exactly one unordered positive pair \(\{y_1,y_2\}\), including the equal-rate endpoint.

**3. Constructive inversion.** Given admissible \((S,T)\), solve the strictly monotone scalar equation \(F_S(\delta)=T\) for the unique \(\delta\in[0,S)\). Compute the two \(y_i\) above, then

\[
\rho_i=\frac{2y_i}{1+\sqrt{1+4y_i^2}},\qquad
r_i=\frac{\Omega(1-\rho_i)}{2\sqrt{\rho_i}}.
\]

These give the two positive finite rates, up to their exchange. Conversely, holding \(S\) fixed but allowing \(\delta\) to vary through \([0,S)\) produces a continuum of distinct unordered pairs with the same \(C_0\); thus one covariance alone does not identify both rates.

**4. Local conditioning near equal rates.** As \(\delta\to0\) at fixed \(S\), Taylor expansion of the same exact function gives

\[
T-[\sqrt{1+S^2}-1]=\frac{\delta^2}{2(1+S^2)^{3/2}}+O(\delta^4).
\]

The exact inverse is therefore non-Lipschitz at the equal-rate boundary: the recovered imbalance generally scales as the square root of the deviation in the second observable. This is a sensitivity warning, not a claim about empirical error bars.

## Verification

The included standalone `check.py` uses `numpy` and `scipy` and passes 218 numerical assertions when run as `python check.py`: independent cosine quadratures for the Fourier kernel; exact forward/inverse consistency for disparate parameter values and equal rates; admissible-range and boundary tests; and independent finite-chain Lyapunov-equation covariance computations. For the Lyapunov tests, a Gaussian Ornstein–Uhlenbeck boundary surrogate is used **only** because it has the same two-time wall covariance; the surrogate does not assert equality of higher moments or full state laws. These finite tests cross-check normalization, signs, and formulas. They do not substitute for the all-positive-parameter proof above.

## Relationship to prior work

Sarkar and Roy's boundary-resetting harmonic-chain study [1] defines this model and derives the bulk equal-time velocity correlations as Fourier-integral and hypergeometric forward formulas (Section 4.2 and Appendix B). The physics and the forward covariance identity are prior results and are not claimed as new. The result here addresses the separate **inverse** question: *whether only the onsite and nearest-neighbor bulk covariances identify the two reset rates, and which measured pairs are physically possible*. The exact two-statistic uniqueness and sharp admissibility wedge are not stated or derived in the inspected source.

Sarkar, Santra, and Basu [2] study different active-force reservoirs, including Ornstein–Uhlenbeck and run-and-tumble forcing, and [3] treats a different active Rubin-bath model. Those works reinforce why a two-point covariance alone does not identify a unique microscopic noise mechanism. General convex moment methods and exponential/Prony inversion long predate this note. The claimed contribution is *not* a new general moment-inversion algorithm, nor a claim of unique detection of Poisson resetting versus a matched Gaussian active reservoir.

## Limitations

Only the specified zero-thermal-noise harmonic chain with equal *known* wall diffusivities and known bulk mechanical parameters is covered. The results are asymptotic in chain length at fixed central separation and in stationary time; they are not finite-system identities. Symmetric bulk correlations identify only an **unordered** rate pair. Unknown, unequal wall diffusion strengths introduce additional free amplitudes and need more observations. Small data errors near equal rates cause intrinsically poor imbalance conditioning. No statistical sample-size guarantee, finite-chain convergence rate, identifiability of the microscopic reset mechanism, or extension to anharmonic chains is established. A prior equivalent specialization of a broader linear inverse-system theorem remains possible and requires independent priority assessment.

## References

1. R. Sarkar and P. Roy, *Stationary state of harmonic chains driven by boundary resetting*, arXiv:2307.06127, first posted 2023-07-12, https://arxiv.org/html/2307.06127v3 . Section 4.2 and Appendix B were inspected.
2. R. Sarkar, I. Santra and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035, first posted 2022-10-17, https://arxiv.org/abs/2210.09035 .
3. R. Sarkar, I. Santra and U. Basu, *Harmonic chain driven by active Rubin bath: transport properties and steady-state correlations*, arXiv:2404.00615, first posted 2024-03-31, https://arxiv.org/abs/2404.00615 .
