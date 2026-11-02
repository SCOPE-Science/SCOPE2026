# An exact temporal-averaging transition for confined diffusion with uniform-history resetting

## Finding
Consider equilibrium-initialized Ornstein–Uhlenbeck diffusion in a harmonic well, interrupted by Poisson resets to a position chosen uniformly from its **own complete earlier trajectory**. Every one-time position law remains exactly Gibbs–Gaussian, yet the variance of its empirical time average has a sharp three-regime transition at equality of the resetting and confinement rates.

Put \(\sigma^2=D/\kappa\), \(a=\kappa+r\), \(\beta=2r/(\kappa+r)\in(0,2)\), \(A_T=\int_0^T X_s\,ds\), and \(J(T)=\operatorname{Var}(A_T)\). For every \(T>0\), if \(r\ne\kappa\),
\[
J(T)=\frac{2\sigma^2T}{a(\beta-1)}\left[{}_1F_1(1-\beta;2;-aT)-1\right].
\]
At the critical point \(r=\kappa\) (hence \(a=2\kappa\), \(\beta=1\)), with the exponential integral \(E_1(z)=\int_z^\infty e^{-u}\,du/u\),
\[
J(T)=\frac{2\sigma^2}{a}\left\{T\left[\gamma_{\rm E}+\log(aT)+E_1(aT)-1\right]+\frac{1-e^{-aT}}a\right\}.
\]
The exact asymptotics for the **time-average** \(\overline X_T=A_T/T\) are
\[
\operatorname{Var}(\overline X_T)\sim
\begin{cases}
\displaystyle\frac{2\sigma^2}{\kappa-r}\,T^{-1},&0<r<\kappa,\\[4pt]
\displaystyle\frac{\sigma^2}{\kappa}\,\frac{\log(2\kappa T)}T,&r=\kappa,\\[4pt]
\displaystyle\frac{2\sigma^2(\kappa+r)^{\beta-1}}{(r-\kappa)\Gamma(1+\beta)}\,T^{\beta-2},&r>\kappa.
\end{cases}
\]
All three regimes have vanishing variance, but the usual inverse-time rate is lost at and beyond \(r=\kappa\). The rate \(T^{-2\kappa/(\kappa+r)}\) above threshold can approach arbitrarily slow decay as the resetting rate increases. No statement about central-limit convergence or almost-sure convergence is asserted.

## Assumptions and scope
Fix \(\kappa,D,r>0\). At time zero, \(X_0\) has the independent equilibrium Gaussian law \(N(0,D/\kappa)\). Between resets the process solves \(dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t\); reset times are an independent homogeneous Poisson process of rate \(r\). At each reset time \(t>0\), a fresh uniform \(U\in[0,t]\) is sampled, independently of future Brownian motion, and the position is instantly set to its earlier value \(X_U\). The remembered trajectory is never erased. Reset times have probability zero of hitting any prescribed time. All expectations are over the equilibrium initialization, diffusion, Poisson times, and historical choices. Position is one-dimensional and the time average starts at the creation time of the historical record.

## Proof
**(1) Exact Gaussian marginal law.** The usual OU semigroup preserves \(N(0,\sigma^2)\); a uniform-history reset samples a previous time whose unconditional marginal law is also \(N(0,\sigma^2)\). A chronological conditioning/first-reset argument, or uniqueness for the linear forward equation, implies \(X_t\sim N(0,\sigma^2)\) for all \(t\ge0\). In particular \(\mathbb E X_t=0\) and \(\mathbb E X_t^2=\sigma^2\), uniformly in \(t\). This does **not** assert that the joint process is stationary.

**(2) Two-time information closes the area moment.** Set \(H(t)=\mathbb E[A_tX_t]\). Since \(dA_t=X_t\,dt\) and the resets leave \(A_t\) continuous, the jump-Itô product rule and historical-uniform reset rule give, for \(t>0\),
\[
\begin{aligned}
J'(t)&=2H(t),\\
H'(t)&=\sigma^2-(\kappa+r)H(t)
+\frac r t\,\mathbb E\left[A_t\int_0^t X_u\,du\right]
=\sigma^2-(\kappa+r)H(t)+\frac r t J(t).
\end{aligned}
\]
Indeed, conditional on the entire trajectory immediately before a jump at time \(t\), its new position averages to \(A_t/t\). Hence, for \(t>0\),
\[
J''(t)+aJ'(t)-\frac{2r}{t}J(t)=2\sigma^2,
\quad J(0)=J'(0)=0.
\]
The bounded second moment implies \(0\le J(t)\le\sigma^2t^2\). The local regular solution obeys \(J(t)=\sigma^2t^2-(\kappa\sigma^2/3)t^3+O(t^4)\); regularity fixes the solution uniquely.

**(3) Exact inversion.** Let \(\widehat J(s)=\int_0^\infty e^{-st}J(t)\,dt\) for \(s>0\). The identity \(\mathcal L[J/t](s)=\int_s^\infty\widehat J(q)\,dq\) and the moment equation yield
\[
s(s+a)\widehat J(s)-2r\int_s^\infty\widehat J(q)\,dq=\frac{2\sigma^2}{s}.
\]
Differentiating, setting \(\beta=2r/a\), and using \(\widehat J(s)=O(s^{-3})\) as \(s\to\infty\), gives
\[
\widehat J(s)=\frac{2\sigma^2}{a(\beta-1)}
\left[s^{-1-\beta}(s+a)^{\beta-1}-s^{-2}\right]
\quad(\beta\ne1).
\]
The integral in the integrating-factor solution is elementary after \(y=q/(q+a)\). Termwise inversion of the generalized binomial expansion gives the displayed \({}_1F_1\) formula. At \(\beta=1\), the continuous limit is \(\widehat J(s)=2\sigma^2\log(1+a/s)/(as^2)\). Inverting with \(\mathcal L^{-1}\{\log(1+a/s)\}=(1-e^{-at})/t\) yields the stated exponential-integral expression.

**(4) Sharp asymptotics.** For \(0<\beta<1\), the Kummer factor \({}_1F_1(1-\beta;2;-aT)\to0\), giving \(J(T)\sim2\sigma^2T/[a(1-\beta)]\). For \(1<\beta<2\), the standard negative-argument Kummer asymptotic is
\[
{}_1F_1(1-\beta;2;-aT)
\sim\frac{(aT)^{\beta-1}}{\Gamma(1+\beta)},
\]
so \(J(T)\sim2\sigma^2a^{\beta-2}T^\beta/[(\beta-1)\Gamma(1+\beta)]\). At \(\beta=1\), \(E_1(aT)\to0\), giving \(J(T)\sim(2\sigma^2/a)T\log(aT)\). Division by \(T^2\) completes all three claims; \(\beta=1\) is exactly \(r=\kappa\).

## Verification
The independently implementable program `verification/check_memory_time_average.py` checked 64 parameter/time comparisons of the exact special-function expression against numerical integration of the closed two-moment ODE, 12 numerical inverse-Laplace comparisons, five remote-time asymptotic checks, and three independently generated path-ensemble comparisons: **84 checks passed**. The path ensembles used 18,000 randomly generated trajectories in each of three regimes with time mesh 0.006; relative errors in the area second moment were about 0.98%, 0.77%, and 1.36%. Neither finite simulation nor special-function evaluation is used as an infinite-time proof: the latter follows from the analytic transform and known Kummer asymptotics.

## Relationship to prior work
Boyer and Majumdar, arXiv:2405.10283 (first posted 2024-05-16), establish the Gibbs one-time marginal and spectral power-law relaxation for resetting to a uniformly selected past position in a confining potential. The source's Ornstein–Uhlenbeck specialization includes spectral decay exponents, but its one-time Fokker–Planck calculation does not determine \(\mathbb E[(\int_0^T X_s ds)^2]\) for a non-Markovian path. Boyer, Evans, and Majumdar, arXiv:2411.00641 (first posted 2024-11-01), analyze general time-dependent relocation kernels and single-time density asymptotics rather than this path-integrated statistic. Budini, arXiv:1605.08930, studies time averages and ergodicity in a different finite-state urn-memory process rather than the harmonic diffusion and its \(r=\kappa\) rate threshold. These are conceptual and mathematical comparators, not evidence of definitive publication priority.

## Limitations
The result is for harmonic drift, constant Poisson reset rate, uniform sampling of the complete past, a thermally initialized process, and ideal ensemble variance. It is not a general result for arbitrary potentials, nonuniform memory, finite-record initialization from a deterministic point, temporal central-limit laws, noisy finite-sample estimation, or pathwise ergodic convergence. Stronger unlocated general time-additive-functional theorems could subsume the comparison; priority remains independently unverified.

## References
1. D. Boyer and S. N. Majumdar, *Power-law relaxation of a confined diffusing particle subject to resetting with memory*, arXiv:2405.10283, initial public version 2024-05-16; J. Stat. Mech. (2024) 073206.
2. D. Boyer, M. R. Evans and S. N. Majumdar, *Diffusion with preferential relocation in a confining potential*, arXiv:2411.00641, initial public version 2024-11-01; J. Stat. Mech. (2025) 013209.
3. A. A. Budini, *Weak ergodicity breaking induced by global memory effects*, arXiv:1605.08930, initial public version 2016-05-28; Phys. Rev. E 94, 022108 (2016).
4. NIST Digital Library of Mathematical Functions, confluent hypergeometric functions, their Laplace transforms and asymptotics (standard special-function identities).
