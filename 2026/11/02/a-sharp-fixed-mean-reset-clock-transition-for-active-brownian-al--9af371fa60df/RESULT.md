# A sharp fixed-mean reset-clock transition for active Brownian alignment

## Finding

Consider a two-dimensional active Brownian particle that is completely reset to a fixed position and heading at independent, identically distributed renewal intervals. Its time-averaged displacement along the reset heading has an exact, globally optimal protocol at every prescribed mean reset interval. The optimizer changes sharply from an unattained burst-clock supremum to a unique deterministic clock.

Let \(v,k,\gamma>0\), \(D\ge0\), and let \(T>0\) almost surely be independent of the particle noises, with \(\mathbb ET=m\in(0,\infty)\). Set
\[
F(t)=\begin{cases}
\displaystyle v\frac{e^{-\gamma t}-e^{-kt}}{k-\gamma},&k\ne\gamma,\\[5pt]
\displaystyle vt e^{-kt},&k=\gamma,
\end{cases}\qquad
G(t)=\int_0^t F(s)\,ds.
\]
The function \(F\) has a unique positive maximum at
\[
t_0=\begin{cases}\displaystyle\frac{\log(k/\gamma)}{k-\gamma},&k\ne\gamma,\\[4pt]1/k,&k=\gamma.\end{cases}
\]
There is a unique \(\tau>t_0\) satisfying \(\tau F(\tau)=G(\tau)\). Write \(\mathcal M(T)\) for the almost-sure long-run time average of the position component parallel to the reset heading. Its exact supremum over all admissible renewal laws of mean \(m\) is
\[
\boxed{\sup_{T>0\,\text{a.s.},\ \mathbb ET=m}\mathcal M(T)
=\begin{cases}
F(\tau),&0<m\le\tau,\\[2pt]
G(m)/m,&m\ge\tau.
\end{cases}}
\]
For \(m\ge\tau\), the only maximizing renewal law is \(T=m\) almost surely. For \(0<m<\tau\), no strictly positive inter-reset law attains the supremum; it is approached by the two-point laws
\[
\mathbb P(T=\tau)=\frac{m-\varepsilon}{\tau-\varepsilon},\qquad
\mathbb P(T=\varepsilon)=\frac{\tau-m}{\tau-\varepsilon},\qquad 0<\varepsilon<m,
\]
as \(\varepsilon\downarrow0\). If zero-length resets are formally admitted, the unique attaining law in the low-mean regime is supported on \(\{0,\tau\}\) with masses \(1-m/\tau\) and \(m/\tau\), respectively.

By comparison, every Poisson clock of rate \(r>0\) yields \(\mathcal M_{\mathrm P}(r)=vr/[(r+k)(r+\gamma)]\), and its unique optimum is \(v/(\sqrt{k}+\sqrt\gamma)^2\). The unrestricted renewal optimum \(F(\tau)\) is strictly larger for every \(k,\gamma>0\). At matched relaxation and heading decorrelation, \(k=\gamma\), the positive dimensionless number \(\xi=k\tau\) is the unique positive root of \(e^\xi=1+\xi+\xi^2\); numerically \(\xi=1.7932821329008\ldots\) and \(F(\tau)=0.2984256075256\ldots\,v/k\), compared with the best Poisson value \(v/(4k)\), an improvement of approximately \(19.3702\%\).

## Assumptions and scope

Within each reset cycle, write \(\mathbf X_t=(X_t,Y_t)\), \(\mathbf u_t=(\cos\theta_t,\sin\theta_t)\), and take
\[
d\mathbf X_t=(-k\mathbf X_t+v\mathbf u_t)\,dt+\sqrt{2D}\,d\mathbf B_t,\qquad
d\theta_t=\sqrt{2\gamma}\,dW_t.
\]
The Brownian noises are independent of each other and of the renewal clock. Each reset restores \((\mathbf X,\theta)=(\mathbf0,0)\) instantaneously, without overhead. Distinct cycles use independent noises, and the intervals are i.i.d. and positive with finite mean. All averages are in physical time, and \(\mathcal M(T)=\lim_{H\to\infty}H^{-1}\int_0^H X_t\,dt\), almost surely. An equilibrium renewal construction has the same mean at a typical observation time. For deterministic periods, the distribution at a fixed clock phase is periodic; the theorem concerns its *phase-averaged* long-run mean, not convergence of its phase-resolved mean to a constant.

The result remains valid at \(D=0\), since centered translational noise does not affect first moments. The theorem does not cover state-dependent or adaptive clocks, incomplete resets, reset overhead, constraints imposing a positive lower bound on individual intervals, or maximizing unsigned displacement or first-passage success.

## Proof

**1. One-cycle response.** Starting from the prescribed reset state, \(\mathbb E\cos\theta_t=e^{-\gamma t}\) and \(\mathbb EX_t\) solves \((\mathbb EX_t)'=-k\mathbb EX_t+ve^{-\gamma t}\), with initial value zero. Therefore \(\mathbb EX_t=F(t)\), including its continuous \(k=\gamma\) limit. The expected integrated alignment in a cycle of duration \(t\) is \(G(t)\). In particular, \(0<F(t)\le v/k\), \(G(t)\le vt/k\), and \(G(t)\uparrow v/(k\gamma)\) as \(t\to\infty\).

**2. Renewal reward.** The cycle reward is \(R=\int_0^T X_s\,ds\). Independence of \(T\) and the within-cycle path implies \(\mathbb ER=\mathbb E G(T)\). Both \(\mathbb ET\) and \(\mathbb E|R|\) are finite: the solution is a bounded-mean propulsion convolution plus a Gaussian Ornstein–Uhlenbeck convolution whose expected absolute value is bounded uniformly in time. The regenerative renewal-reward theorem consequently gives
\[
\mathcal M(T)=\frac{\mathbb E G(T)}{m}.
\]
For arbitrary nonlattice renewal distributions the same formula follows from the equilibrium age density \(\mathbb P(A\in da)=\mathbb P(T>a)\,da/m\); the reward argument also covers deterministic and other lattice clocks.

**3. Unique tangency.** The derivative \(F'(t)\) is positive for \(0<t<t_0\) and negative for \(t>t_0\), with \(F(0)=0\) and \(F(t)\to0\). Set \(H(t)=tF(t)-G(t)\). Then \(H(0)=0\), \(H'(t)=tF'(t)\), so \(H\) increases strictly until \(t_0\), then decreases strictly, and \(H(t)\to-v/(k\gamma)<0\). Thus it has exactly one positive zero \(\tau>t_0\). Moreover \((G(t)/t)'=H(t)/t^2\), proving that \(G(t)/t\) rises strictly until \(\tau\), declines strictly afterward, and has unique maximum \(F(\tau)\).

**4. Sharp concave majorant.** Let \(s=F(\tau)=G(\tau)/\tau\) and define
\[
C(t)=\begin{cases}st,&0\le t\le\tau,\\G(t),&t\ge\tau.\end{cases}
\]
Because \(G(t)/t\le s\), one has \(G(t)\le C(t)\) for every nonnegative \(t\). The derivatives join at \(\tau\), and \(G''(t)=F'(t)<0\) for \(t>\tau\), hence \(C\) is concave. Jensen's inequality yields
\[
\mathcal M(T)=\frac{\mathbb EG(T)}m\le\frac{\mathbb EC(T)}m\le\frac{C(m)}m.
\]
For \(m\ge\tau\), setting \(T=m\) achieves equality. Strict concavity beyond \(\tau\) and the equality conditions in the two inequalities force this law to be the unique optimizer. For \(m<\tau\), equality would require support in the affine interval of \(C\), and simultaneously support where \(C=G\), namely \(\{0,\tau\}\); strict positivity rules it out. The displayed two-point positive laws have mean exactly \(m\) and their reward tends to \(mG(\tau)/\tau\) as \(\varepsilon\downarrow0\), proving sharpness and nonattainment.

**5. Poisson comparison.** For \(T\sim\operatorname{Exp}(r)\), integration by parts gives \(\mathcal M(T)=r\int_0^\infty e^{-rt}F(t)\,dt=vr/[(r+k)(r+\gamma)]\). Differentiation in \(r\) gives its unique maximum at \(r=\sqrt{k\gamma}\). A nondegenerate exponential law cannot satisfy the concave-majorant equality conditions, so its optimal value is strictly smaller than \(F(\tau)\). For \(k=\gamma\), the tangency equation reduces to \(e^\xi=1+\xi+\xi^2\); the uniqueness already established excludes the extraneous zero root.

## Verification

The standalone file `check.py` differentiates and integrates the response symbolically, independently quadratures the expected reward, solves the tangency equation for eight distinct parameter pairs, compares the bound against randomized finite-support clocks, checks the positive two-point limiting construction, and recovers the exact Poisson expression. On the packaged script's stated environment, all 2,390 finite and symbolic diagnostic assertions passed. These checks corroborate formulas and edge cases but are not a proof of the all-distribution Jensen bound; that bound is established in the preceding analytic proof. The numerical root and improvement percentage are approximate, not interval-certified constants.

## Relationship to prior work

Shee (arXiv:2409.06920v1, September 11, 2024) derives the complete-reset active Brownian model, the mean displacement under Poisson resetting, and the optimum Poisson rate. Those facts are prior work, not new claims here. Eule and Metzger (2016) establish the general renewal-resetting framework and dependence on reset-time distributions, including constrained-search comparisons. Guéneau, Majumdar and Schehr (arXiv:2306.09453, 2023) analyze periodic and Poisson protocols for a *resetting driving noise without full position resetting*, a different regenerative structure. The contribution here is the exact fixed-mean global optimization and equality/nonattainment phase classification for the *fully reset active Brownian trap*, with the sharp all-renewal comparison to the best Poisson clock. The proof uses classical renewal reward and concave-envelope ideas; no novelty is asserted for those general techniques themselves.

## Limitations

The model assumes a common reset heading, independent stationary-in-law Brownian increments per complete reset cycle, i.i.d. intervals and instantaneous resets. Short-interval burst protocols are idealizations: any nonzero reset overhead or minimum separation can change the low-mean optimum. Only the signed mean projection is optimized; not variance, energetic cost, entropy production, or a target-finding functional. Literature priority is not independently certified; generic optimal-control or convex-envelope statements may imply the phase-classification method even without naming this physical model.

## References

1. A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920v1, September 11, 2024. https://arxiv.org/html/2409.06920v1
2. S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New Journal of Physics **18**, 033006 (2016). https://doi.org/10.1088/1367-2630/18/3/033006
3. M. Guéneau, S. N. Majumdar and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453 (2023). https://arxiv.org/abs/2306.09453
4. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic resetting and applications*, Journal of Physics A **53**, 193001 (2020). https://doi.org/10.1088/1751-8121/ab7cfe
