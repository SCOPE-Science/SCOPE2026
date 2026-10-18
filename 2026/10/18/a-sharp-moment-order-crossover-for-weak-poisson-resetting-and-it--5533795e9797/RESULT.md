# A sharp moment-order crossover for weak Poisson resetting and its diffusion approximation

## Finding

Frequent, weak multiplicative resets and their Gaussian diffusion approximation have **identical stationary variances whenever finite** but cease to agree relatively on high even moments at the sharp order \(m\asymp s^{-2/3}\). For a fixed growth-to-reset ratio \(0<\beta<1\), positive \(D,\lambda\), and \(\gamma=\beta\lambda\), let \(M_{2m}^{P}(s)\) and \(M_{2m}^{G}(s)\) be the respective stationary even moments defined below. When both are finite, put \(R_m(s)=M_{2m}^{P}(s)/M_{2m}^{G}(s)\). For **any integer sequence** \(m=m(s)\to\infty\) with \(ms\to0\),

\[
\log R_m(s)=-\frac{2\lambda}{9(\lambda-\gamma)}m^3s^2[1+o(1)].
\]

Consequently, if \(ms^{2/3}\to c\in(0,\infty)\),
\[
R_m(s)\longrightarrow\exp\!\left[-\frac{2\lambda c^3}{9(\lambda-\gamma)}\right].
\]
For \(ms^{2/3}\to0\), the ratio tends to one (including bounded \(m\)); if \(ms^{2/3}\to\infty\) while \(ms\to0\), it tends to zero. Thus a second-order diffusion approximation may match each fixed moment to relative order \(s^2\), and match the variance exactly, but fail relatively already on degrees much smaller than \(s^{-1}\).

There is a second, later mismatch in **moment existence**. The Gaussian approximation has critical absolute-moment order
\[
\kappa_G(s)=1+\frac{2(1-\beta)}s.
\]
The exact-reset process has a unique positive critical order \(\kappa_P(s)\) satisfying
\[
\beta s\kappa_P(s)=1-(1-s)^{\kappa_P(s)}.
\]
Here \(\mathbb E|X|^p<\infty\) holds exactly when \(p<\kappa_P(s)\), and similarly for the Gaussian model using \(\kappa_G(s)\), with divergence also at equality. If \(z_\beta>0\) is the unique positive root of \(\beta z=1-e^{-z}\), then
\[
s\kappa_P(s)\to z_\beta>2(1-\beta)=\lim_{s\downarrow0}s\kappa_G(s).
\]
In particular, every \(\alpha\) strictly between those limiting constants generates high orders \(p_s=\alpha/s\) for which the exact-reset model has finite moments while the diffusion approximation has infinite moments for all sufficiently small \(s\).

## Assumptions and scope

For every \(0<s<1\), let \(N_t\) be a Poisson counting process of rate \(\lambda/s\) and \(B_t\) an independent standard Brownian motion. The exact resetting process solves
\[
dX_t=\gamma X_t\,dt+\sqrt{2D}\,dB_t,
\qquad X_t=(1-s)X_{t-}\quad\text{at each Poisson event}.
\]
Its second-order Kramers--Moyal diffusion approximation solves, using independent standard Brownian motions \(W_t,\widetilde B_t\),
\[
dY_t=(\gamma-\lambda)Y_t\,dt+\sqrt{\lambda s}\,Y_t\,dW_t+\sqrt{2D}\,d\widetilde B_t.
\]
Parameters \(D,\lambda>0\), \(0<\beta=\gamma/\lambda<1\) are held fixed as \(s\downarrow0\). The exact process is not the diffusion approximation. Both have unique stationary laws because their respective multiplicative homogeneous solutions decay almost surely. The order \(m\) is an integer at least one, and \(p>0\) denotes an arbitrary real absolute-moment order. All ratio assertions require finite moments in both laws; \(ms\to0\) guarantees this eventually.

## Proof

**Stationarity and moment cutoffs.** Write \(q=1-s\), \(r=\lambda/s\). The almost-sure Lyapunov exponent of the exact homogeneous multiplier is \(\gamma+r\log q<0\), because \(\gamma<\lambda<-r\log q\). Reversing stationary increments gives a centered conditional Gaussian representation with conditional variance
\[
V_P=2D\int_0^\infty e^{2\gamma u}q^{2N_u}\,du.
\]
The diffusion model has the same representation with
\[
V_G=2D\int_0^\infty\exp\!\bigl([2(\gamma-\lambda)-\lambda s]u+2\sqrt{\lambda s}\,W_u\bigr)\,du.
\]
Both integrals are almost surely finite by strong laws, and \(\mathbb E|X|^p\) is a positive Gaussian constant times \(\mathbb E V_P^{p/2}\) (likewise for \(Y\)).

For \(V_P\), split its defining integral into unit-interval integrals \(I_n\). Poisson independent increments give
\[
\mathbb E I_n^{p/2}=C_p\exp(n\phi_P(p)),\qquad
\phi_P(p)=p\gamma+\frac\lambda s(q^p-1),\quad 0<C_p<\infty.
\]
If \(\phi_P(p)<0\), subadditivity for \(p/2\le1\), or Minkowski's inequality for \(p/2>1\), yields finite \(\mathbb E V_P^{p/2}\). If \(\phi_P(p)>0\), the lower bound \(V_P\ge2D I_n\) forces divergence. At equality, the interval integrals tend almost surely to zero while their \(p/2\)-moments stay constant; dominated convergence would be contradicted if \(\mathbb E V_P^{p/2}\) were finite. Since \(\phi_P\) is strictly convex, has negative derivative at zero and tends to infinity, it has exactly one positive root \(\kappa_P\). Brownian independent increments repeat the same argument with
\[
\phi_G(p)=p(\gamma-\lambda)+\frac{\lambda s}{2}p(p-1),
\]
whose positive root is \(\kappa_G\). This proves the exact finite/infinite criteria, including both equality boundaries.

**Even-moment recursion.** Generator identities for the monomials \(x^{2j}\), justified whenever the moments are finite, yield
\[
\begin{aligned}
M_{2j}^{P}&=\frac{2j(2j-1)D}{A_j^{P}}M_{2j-2}^{P},
&A_j^{P}&=\frac\lambda s[1-(1-s)^{2j}]-2j\gamma,\\
M_{2j}^{G}&=\frac{2j(2j-1)D}{A_j^{G}}M_{2j-2}^{G},
&A_j^{G}&=2j(\lambda-\gamma)-\lambda s\,j(2j-1).
\end{aligned}
\]
Both zeroth moments are one. The second-order Taylor polynomial of \(1-(1-s)^{2j}\) shows \(A_1^P=A_1^G\); for every \(j\ge2\) the third derivative of that function is strictly positive on \((0,1)\), hence \(A_j^P>A_j^G\). Thus \(M_2^P=M_2^G\) whenever finite, and \(M_{2m}^P<M_{2m}^G\) for \(m\ge2\) when both are finite. Furthermore,
\[
R_m(s)=\prod_{j=1}^{m}\frac{A_j^G}{A_j^P}.
\]

**Uniform growing-order comparison.** Put \(\mu=\lambda-\gamma>0\). Uniformly for \(1\le j\le m\) when \(ms\to0\), Taylor's theorem with its signed remainder gives
\[
A_j^P-A_j^G
=\lambda\binom{2j}{3}s^2[1+O(js)]
\quad(j\ge2),\qquad
A_j^G=2j\mu[1+O(js)].
\]
The logarithmic error in replacing \(-\log(1+(A_j^P-A_j^G)/A_j^G)\) by its negative linear term is bounded in total by \(O(m^5s^4)\). Therefore
\[
\begin{aligned}
\log R_m(s)
&=-\frac{\lambda s^2}{\mu}
\sum_{j=1}^m\frac{\binom{2j}{3}}{2j}
+O(m^4s^3+m^5s^4)\\
&=-\frac{2\lambda}{9\mu}m^3s^2
+O(m^2s^2+m^4s^3+m^5s^4).
\end{aligned}
\]
For \(m\to\infty\) and \(ms\to0\), every displayed remainder is \(o(m^3s^2)\). For fixed \(m\), the exact product separately gives \(R_m=1+O(s^2)\). The three asserted regimes follow.

**Sharp higher-order existence gap.** Let \(h_s=-\log(1-s)/s\to1\) and \(z_s=-\kappa_P(s)\log(1-s)>0\). Its defining relation becomes
\[
\frac\beta{h_s}z_s=1-e^{-z_s}.
\]
Strict concavity of \(1-e^{-z}\) gives a unique positive solution and convergence \(z_s\to z_\beta\), hence \(s\kappa_P(s)\to z_\beta\). At \(\beta=(1-e^{-z})/z\), the inequality \(z>2(1-\beta)\) is equivalent to \(z^2-2z+2(1-e^{-z})>0\), true because this function vanishes at zero and has strictly positive derivative \(2(z-1+e^{-z})\) for \(z>0\). This proves the nonempty divergence-disagreement window without asserting a pointwise stationary tail prefactor.

## Verification

`check_moments.py` uses exact rational arithmetic to compare the finite-order jump and diffusion generator denominators and verify moment ordering, then numerically computes moment cutoff roots and growing-order logarithmic ratios using cancellation-stable `log1p` and `expm1`. It reports **110659 deterministic finite checks passed**. In particular, at \(\lambda=1\), \(\gamma=1/2\), \(s=1/4\), the exact stationary fourth-moment ratio is \(32/47\), while the variances are equal whenever finite. These computations do not prove the real-order moment criteria or the asymptotic crossover; the proof above does.

## Relationship to prior work

Galla (2026) derives the frequent-weak-reset diffusion approximation and its stationary density, including the linear-growth model; the displayed Gaussian approximation itself, and its fixed-order stationary density, are not new here. General theories of multiplicative stochastic processes and power-law exponents predate this result. Biroli et al. (2024) solve a partial-rescaling model without positive linear growth. The present claim is specifically the **joint Poisson-versus-Gaussian comparison in a growing moment order**, including the exact \(s^{-2/3}\) relative-error crossover and a different \(s^{-1}\) existence frontier. It does not claim the elementary generator recurrence, the existence of heavy tails, or generic power-law exponent theory as novel.

## Limitations

The comparison is for one scalar particle with deterministic multiplicative factor per Poisson event, independent additive Brownian noise, fixed \(0<\gamma/\lambda<1\), and the specified second-order diffusion approximation. The \(s^{-2/3}\) law compares ideal stationary even moments, not finite-sample estimation errors or general finite-time distributions. It is not uniform as \(\gamma/\lambda\uparrow1\), nor a theorem for state-dependent or randomly sized resets. The critical moment-order comparison is not itself an assertion of an exact power-law tail prefactor. The formulas cannot be used beyond finite-moment domains. Broader general asymptotic results might imply aspects of this comparison; independent validation of novelty has not been performed.

## References

1. Tobias Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1 (first submitted 25 February 2026), especially main equations (3)--(8) and Supplemental Material sections S1.1 and S2.2. https://arxiv.org/html/2602.21635
2. Marco Biroli, Yannick Feld, Alexander K. Hartmann, Satya N. Majumdar and Grégory Schehr, *Resetting by rescaling: Exact results for a diffusing particle in one dimension*, Physical Review E 110, 044142 (2024), arXiv:2406.08387. https://doi.org/10.1103/PhysRevE.110.044142
3. Brendan K. Beare and Alexis Akira Toda, *Determination of Pareto Exponents in Economic Models Driven by Markov Multiplicative Processes*, Econometrica 90 (2022), 1811--1833. https://doi.org/10.3982/ECTA17984
