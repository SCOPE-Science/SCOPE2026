# Exact beta edge and quadratic-log cooling tail in a synchronously partially reset harmonic Brownian gas

## Finding

For every confinement rate \(\alpha>0\), diffusion coefficient \(D>0\), common Poisson reset rate \(r>0\), and retention factor \(0<q<1\), consider arbitrarily many independent Ornstein–Uhlenbeck particles exposed to the *same* clock, with each event multiplying every position by \(q\). Let \(V\) be the stationary variance of one particle conditional on that clock. Put \(a=2\alpha\), \(b=2D\), \(c=q^2\), \(\beta=r/a\), and \(Y=aV/b\). Then \(0<Y<1\) almost surely; the stationary empirical particle cloud converges to the **random** Gaussian measure \(\mathcal N(0,V)\); and the law of its macroscopic width has two exact, unequal endpoint signatures:

\[
\Pr(Y>1-\varepsilon)=K_{c,\beta}\varepsilon^\beta
\quad (0<\varepsilon<1-c),\qquad
K_{c,\beta}=\mathbb E[(1-cY)^{-\beta}],
\]

\[
\lim_{\varepsilon\downarrow0}\frac{\log\Pr(Y<\varepsilon)}{[\log(1/\varepsilon)]^2}
=-\frac{1}{2\log(1/c)}.
\]

In particular, the **entire** top interval \(c<y<1\), not just its limiting edge, has the explicit beta-form density \(f_Y(y)=\beta K_{c,\beta}(1-y)^{\beta-1}\). The upper exponent records the clock-to-trap ratio \(r/(2\alpha)\); the sharply different lower coefficient records the reset strength \(q\). Moreover, the first two stationary macroscopic width moments determine \(r\) and \(q\) exactly when \(\alpha,D\) are known. These statements are for the exact finite-strength jump model, with no small-reset or diffusion approximation.

## Assumptions and scope

For each \(N\ge1\), let \(B_1,\ldots,B_N\) be independent two-sided standard Brownian motions, independent of a shared two-sided rate-\(r\) homogeneous Poisson point process. Between clock events the position satisfies \(dX_i(t)=-\alpha X_i(t)\,dt+\sqrt{2D}\,dB_i(t)\), and at every clock event \(X_i(t)=qX_i(t-)\) simultaneously for all particles. The parameters \(\alpha,D,r\) are strictly positive, and \(0<q<1\). All conclusions are stationary; there are no interactions, intrinsic correlations between Brownian driving noises, or particle-dependent reset clocks.

Let \(N_{(s,t]}\) denote the common-clock count in \((s,t]\). A stationary coupling is the stochastic convolution

\[
X_i(t)=\sqrt{2D}\int_{-\infty}^{t}e^{-\alpha(t-s)}q^{N_{(s,t]}}\,dB_i(s).
\]

The Itô integrals are taken conditionally on the Poisson clock, when their integrands are predictable with respect to the independent Brownian motions. Convergence holds in conditional and unconditional \(L^2\), because the integrand is bounded by \(e^{-\alpha(t-s)}\). Define \(V\) by conditional variance, and \(M_N=N^{-1}\sum_{i=1}^N X_i(0)^2\). An infinite sequence of particles on the same clock provides the almost-sure coupling for the limit \(N\to\infty\).

## Proof

**(1) Conditional stationary Gaussian law and variance dynamics.** Conditional on the common Poisson history, the stochastic integrals are independent centered Gaussians with common variance

\[
V=b\int_0^\infty e^{-au}c^{N_{(-u,0]}}\,du,
\qquad 0<V<b/a.
\]

The strict bounds follow from a positive integrand and at least one clock event in the infinite past almost surely. This backward stationary construction yields a unique invariant law: differences between two solutions driven by the same noises and clock contract at least as \(e^{-\alpha t}\). Conditional strong laws give, almost surely, the weak empirical-measure limit \(N^{-1}\sum_i\delta_{X_i(0)}\Rightarrow\mathcal N(0,V)\), and \(M_N\to V\). Conditional Gaussian fourth moments give the stronger identity

\[
\mathbb E[(M_N-V)^2]=\frac{2\mathbb E[V^2]}N,
\]

hence \(M_N\to V\) in \(L^2\). Between resets, \(\dot V=b-aV\); at each reset, \(V\mapsto cV\). Its generator on differentiable test functions is \(\mathcal L\varphi(v)=(b-av)\varphi'(v)+r[\varphi(cv)-\varphi(v)]\).

**(2) Exact distributional fixed point and upper beta edge.** Let \(T\) be the elapsed time since the last clock event, which at a stationary Poisson observation has the exponential distribution of rate \(r\). The older variance is an independent stationary copy \(V'\). Thus

\[
V\stackrel d=\frac ba(1-e^{-aT})+ce^{-aT}V',\qquad
Y\stackrel d=1-U+cUY',
\]

where \(U=e^{-aT}\) has distribution \(\Pr(U\le u)=u^\beta\) for \(0<u<1\), and \(Y'\) is independent of \(U\) with the law of \(Y\). Therefore \(1-Y=U(1-cY')\). Since \(1-c\le1-cY'\le1\), for every \(0<\varepsilon<1-c\), conditioning on \(Y'\) yields the **exact** probability

\[
\begin{aligned}
\Pr(Y>1-\varepsilon)
&=\mathbb E\left[\Pr\left(U<\frac\varepsilon{1-cY'}\,\middle|\,Y'\right)\right]\\
&=\varepsilon^\beta\mathbb E[(1-cY')^{-\beta}].
\end{aligned}
\]

The coefficient is finite and obeys \(1\le K_{c,\beta}\le(1-c)^{-\beta}\). The fixed-point law is continuous (condition on \(Y'\), then change variables in the continuous \(U\)); differentiating the exact upper survival law on \((c,1)\) gives its density as claimed. This is an interval identity, not merely a leading asymptotic.

**(3) Sharp quadratic-log lower tail.** Write \(F(y)=\Pr(Y\le y)\). The fixed-point recursion gives, for \(0<y<1\),

\[
F(y)\le[1-(1-y)^\beta]F\left(\frac{y}{c(1-y)}\right).
\]

Indeed, \(Y\le y\) forces \(U\ge1-y\) and \(Y'\le y/[c(1-y)]\), and \(U,Y'\) are independent. Conversely, for each fixed \(\delta\in(0,1-c)\),

\[
F(y)\ge[1-(1-\delta y)^\beta]F\left(\frac{(1-\delta)y}{c}\right)
\]

because \(U\ge1-\delta y\) and \(Y'\le(1-\delta)y/c\) imply \(Y\le\delta y+cY'\le y\). Both coefficients in square brackets are bounded above and below by positive constant multiples of \(y\) for sufficiently small \(y\).

To justify iteration to a fixed intermediate threshold, observe that \(F(y_0)>0\) for every \(y_0>0\): a positive-probability event with sufficiently many common jumps in a short recent interval makes the older contribution at most \(c^k\), and the recent contribution at most the recent interval length in normalized units. The fixed-point law also ensures \(F(y)<1\) for \(y<1\). For any small fixed \(\eta>0\), on sufficiently small \(y\) one has \((1-y)^{-1}\le1+\eta\). The two inequalities above can thus be compared with recursions of the type \(F(y)\le C y F(\lambda_+y)\) with \(\lambda_+=(1+\eta)/c>1\), and \(F(y)\ge c_\delta y F(\lambda_-y)\) with \(\lambda_-=(1-\delta)/c>1\). Repeatedly scale from \(y=e^{-t}\) to a fixed positive threshold. There are \(t/\log\lambda_\pm+O(1)\) steps, and summing \(\log y_j=-t+j\log\lambda_\pm\) contributes

\[
-\frac{t^2}{2\log\lambda_\pm}+O(t).
\]

This bounds the liminf and limsup of \(\log F(e^{-t})/t^2\); sending \(\delta,\eta\downarrow0\) makes both \(\lambda_\pm\to1/c\). The asserted limit follows. In particular, a simple power-law approximation at the *lower* edge is false.

**(4) Exact moments, non-self-averaging, and inverse recovery.** Apply the stationary generator to \(v^n\). Writing \(m_n=\mathbb E[V^n]\), all moments are finite because \(V<b/a\), and

\[
m_0=1,\qquad
m_n=\frac{nb}{na+r(1-c^n)}m_{n-1}
=\prod_{k=1}^n\frac{kb}{ka+r(1-c^k)}.
\]

Thus \(m_1=b/[a+r(1-c)]\), \(m_2=2bm_1/[2a+r(1-c^2)]\), and direct subtraction yields

\[
\operatorname{Var}(V)=
\frac{b^2r(1-c)^2}{[a+r(1-c)]^2[2a+r(1-c^2)]}>0.
\]

Conditional Gaussian sampling also gives \(\operatorname{Var}(M_N)=\operatorname{Var}(V)+2m_2/N\). Thus increasing the number of particles does not remove the cloud-width fluctuations. Finally, if \(a,b\) are known and the two macroscopic stationary moments \(m_1,m_2\) are given, define \(A=b/m_1\) and \(B=2bm_1/m_2\). On the stated parameter range \(A-a=r(1-c)>0\), and elementary elimination yields

\[
c=\frac{B-2a}{A-a}-1,
\qquad r=\frac{A-a}{1-c},
\qquad q=\sqrt c.
\]

This is exact injective recovery on \(r>0,0<q<1\), not a claim of estimation robustness at finite sample size.

## Verification

The standalone file `verify.py` checks the exact variance simplification and inverse-moment identity symbolically, independently samples the stationary beta-driven perpetuity for four distinct parameter sets, compares sample moments with generator predictions, checks exact upper-tail probabilities at two interior thresholds per set, verifies finite-\(N\) variance identities, and tests the first six moment recursions. Running `python verify.py` with NumPy and SymPy passes 66 finite/symbolic assertion groups. The perpetuity truncation error is bounded by \(c^{130}\) in the normalized variable under the specified 130-iteration computation. These finite and symbolic checks supplement but cannot replace the infinite-population and endpoint proofs above.

## Relationship to prior work

Galla [1] derives conditional independence given common reset history for simultaneously partially reset particles and a diffusion approximation for frequent weak resets. Its supplemental Section S2 analyzes multi-walker correlations for a linear model, including stationary second moments in the approximation. The present **exact finite-contraction**, restoring Ornstein–Uhlenbeck model shares those mechanisms: conditional independence and generic second-moment balance are not claimed as new. The new assessed content is the exact beta-form density on a nontrivial full endpoint interval of the *common environmental variance*, the sharp opposite-end quadratic-log probability law, and simultaneous exact parameter recovery from macroscopic cloud-width moments.

Biroli et al. [2] obtain the stationary *single-particle* spatial law for partial rescaling of unconfined free diffusion, plus first-passage results. Olsen and Löwen [3] study partial resetting and refractory periods for a single particle, including moments. Their conclusions concern different objects and do not give the law of the clock-conditioned empirical variance for a confined simultaneously reset gas. A further close physical precedent, Biroli et al. [5], derives correlations for a gas under a *switching trap stiffness*; its common environment changes a linear relaxation rate, rather than instantaneously multiplying every particle position by a fixed factor. Boyer and Majumdar [6] analyze common resetting to *previously visited* positions; the memory-based reset kernel is not a contraction-to-fraction jump. Their conditional-iid observations, like [1], are prior art, not new claims here. Generic stochastic-recursion, renewal-perpetuity, and small-deviation theory can contain mathematical tools from which some arguments may follow; only the model-specific, joint endpoint classification is assessed here. No assertion of absolute priority or of exhaustive literature coverage is made.

## Limitations

The theorem requires strictly positive confinement and thermal diffusion, strictly interior retention \(0<q<1\), a common memoryless Poisson clock, independent Brownian innovations, Gaussian harmonic dynamics, and stationary sampling. No uniform statement is made as \(q\to0\), \(q\to1\), \(r\to0\), or \(\alpha\to0\). The low-tail result is a logarithmic equivalent, not an exact prefactor. Macroscopic recovery assumes known \(\alpha,D\), unlimited population, and exact first two moments, not a finite-data confidence bound. The term ``Gaussian cloud'' means a random conditional Gaussian measure; the unconditional one-particle mixture is generally not Gaussian. Independent expert validation and comprehensive originality certification have not been performed.

## References

1. Tobias Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1 (first public 2026-02-25), https://arxiv.org/html/2602.21635v1; especially main-text multiparticle section and supplemental S2.
2. Marco Biroli, Yannick Feld, Alexander K. Hartmann, Satya N. Majumdar and Grégory Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (2024-06-12), https://arxiv.org/html/2406.08387v1.
3. Kristian Stølevik Olsen and Hartmut Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039v1 (2024-06-14), https://arxiv.org/abs/2406.10039.
4. C. Di Bello and collaborators, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722 (2023), https://arxiv.org/abs/2305.13722; relevant single-particle partial-resetting precedent.
5. Marco Biroli, Manas Kulkarni, Satya N. Majumdar and Grégory Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570v1 (2023-12-05), https://arxiv.org/abs/2312.02570.
6. Denis Boyer and Satya N. Majumdar, *Emerging correlations between diffusing particles evolving via simultaneous resetting with memory*, arXiv:2510.21972 (2025-10-24), https://arxiv.org/abs/2510.21972.
