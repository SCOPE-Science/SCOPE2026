# Stable signed-area fluctuations and a critical variance anomaly for Pareto-reset Brownian motion

## Finding

For stationary Brownian motion reset to the origin at independent Pareto renewal times, the **signed time-averaged position** has three sharply distinct fluctuation regimes. In the finite-position-variance range \(\alpha>2\), let \(X_t\) be the stationary process, \(I_T=\int_0^T X_t\,dt\), and \(M_T=I_T/T\). For \(2<\alpha<3\),
\[
T^{-3/(2\alpha)}I_T\ \Rightarrow\ S_{2\alpha/3},\qquad
\mathbb E e^{ik S_{2\alpha/3}}=\exp\!\left[-\frac{\alpha-1}{\alpha}\Gamma\!\left(1-\frac\alpha3\right)\left(\frac D3\right)^{\alpha/3}|k|^{2\alpha/3}\right].
\]
At the critical exponent \(\alpha=3\),
\[
\frac{I_T}{\sqrt{T\log T}}\Rightarrow N\!\left(0,\frac{4D}{9}\right),
\qquad
\frac{\operatorname{Var}(I_T)}{T\log T}\longrightarrow\frac{4D}{3}.
\]
The factor-three discrepancy between the limiting Gaussian variance and the limit of normalized second moments is exact. For \(\alpha>3\),
\[
\frac{I_T}{\sqrt T}\Rightarrow N\!\left(0,\frac{2D}{3}\frac{\alpha-1}{\alpha-3}\right),
\]
with convergence of the corresponding normalized variances. This last standard finite-reward-variance central limit regime is included for comparison, **not claimed as independently novel**.

The exact stationary autocovariance, for every \(h\ge0\), is
\[
\operatorname{Cov}(X_0,X_h)=
\begin{cases}
D\left(\frac{\alpha-1}{\alpha-2}-2h+\frac{\alpha-1}{\alpha}h^2\right),&0\le h\le1,\\
\frac{2D}{\alpha(\alpha-2)}h^{2-\alpha},&h\ge1.
\end{cases}
\]
In particular, for \(2<\alpha<3\),
\[
\operatorname{Var}(M_T)\sim
\frac{4D}{\alpha(\alpha-2)(3-\alpha)(4-\alpha)}T^{2-\alpha}.
\]
Thus the typical stable-law scale of \(M_T\), namely \(T^{3/(2\alpha)-1}\), is different from its root-mean-square scale, which reflects rare prolonged excursions.

## Assumptions and scope

Fix \(D>0\), \(\alpha>2\), and the time-unit cutoff \(1\). Successive inter-reset intervals \(L_j\) are independent with \(\Pr(L_j>\ell)=1\) for \(0\le\ell<1\), and \(\Pr(L_j>\ell)=\ell^{-\alpha}\) for \(\ell\ge1\). Each reset starts an independent standard Brownian excursion \(X_s=\sqrt{2D}\,B_s\), which is independent of all reset intervals. The renewal process is placed in its equilibrium (two-sided stationary) version; a stationary time is sampled using the length-biased cycle law. All convergences in distribution hold as \(T\to\infty\) under this stationary preparation, and \(S_{2\alpha/3}\) is the centered symmetric stable law specified by the displayed characteristic function. Brownian positions and the integrated observable are signed. We do not claim an unsigned-area or nonstationary-start analogue.

## Proof

**1. Complete-cycle rewards.** A single cycle of duration \(L\) contributes \(Y=\int_0^L\sqrt{2D}B_s\,ds\). Conditional on \(L=\ell\), the centered Gaussian reward has variance \(2D\ell^3/3\). Thus, writing \(c=D/3\),
\[
\phi_Y(k)=\mathbb E(e^{ikY})=\mathbb E(e^{-ck^2L^3}),\qquad
\mu=\mathbb EL=\frac\alpha{\alpha-1}.
\]
The random variable \(L^3\) has tail \(\Pr(L^3>x)=x^{-\alpha/3}\) for \(x\ge1\). When \(2<\alpha<3\), the elementary Laplace-tail calculation, by substituting \(u=ck^2x\) in \(\mathbb E(1-e^{-ck^2L^3})\), gives
\[
1-\phi_Y(k)\sim \Gamma\!\left(1-\frac\alpha3\right)c^{\alpha/3}|k|^{2\alpha/3}.
\]
The independent complete-cycle rewards are consequently in the normal domain of attraction of a centered symmetric stable law of index \(2\alpha/3\). At \(\alpha=3\), the same integral instead gives
\[
1-\phi_Y(k)\sim ck^2\log\frac1{ck^2},
\]
so the sum of \(n\) rewards, divided by \(\sqrt{2cn\log n}\), converges to a unit normal. For \(\alpha>3\), \(\mathbb EY^2=(2D/3)\mathbb EL^3=(2D/3)\alpha/(\alpha-3)\), and the ordinary centered finite-variance central limit theorem applies.

**2. Physical clock and boundary excursions.** The number \(N_T\) of complete cycles by time \(T\) obeys \(N_T/T\to1/\mu\) almost surely. The corresponding iid reward partial-sum processes obey the stable or Gaussian functional limit theorem. Their random evaluation at \(N_T\), after deterministic rescaling, is legitimate by the random-time-change theorem because the renewal clock converges to deterministic time and the limiting process has no jump at a fixed deterministic time almost surely. No independence between a cycle's duration and its reward is assumed. The partial initial and terminal Brownian excursions have tight integrated rewards under the stationary law: their ages and residual times have fixed proper equilibrium distributions; hence each partial-area distribution is proper and does not grow with \(T\). The same applies to a terminal partial cycle by stationarity. Dividing them by any of the diverging normalizations above makes their contributions vanish in probability. Substituting \(N_T\sim T/\mu\) into the cycle-limit constants proves all distributional claims.

**3. Covariance and variance.** The only contribution to \(\mathbb E(X_0X_h)\) comes from the event of **no reset** in \((0,h]\); conditioned on age \(A\) at time zero, the Brownian covariance then equals \(2DA\). Writing \(R\) for the forward residual cycle time, stationary renewal calculus yields
\[
\mathbb E[X_0X_h]=2D\mathbb E[A\mathbf1_{\{R>h\}}]
=\frac{D}{\mu}\mathbb E[(L-h)_+^2].
\]
Integrating the Pareto tail explicitly gives the displayed two-piece covariance. Since \(I_T\) is centered,
\[
\operatorname{Var}(I_T)=2\int_0^T(T-h)\operatorname{Cov}(X_0,X_h)\,dh.
\]
For \(2<\alpha<3\), integrate the power-law tail over \([1,T]\) to obtain \(\operatorname{Var}(I_T)\sim4D T^{4-\alpha}/[\alpha(\alpha-2)(3-\alpha)(4-\alpha)]\). At \(\alpha=3\), the tail is exactly \(2D/(3h)\), giving \(\operatorname{Var}(I_T)\sim(4D/3)T\log T\). For \(\alpha>3\), the autocovariance is integrable, giving \(\operatorname{Var}(I_T)/T\to (2D/3)(\alpha-1)/(\alpha-3)\). The critical weak Gaussian variance is \(4D/9\), so its normalized second moments instead tend to three times that value; convergence in law does not imply convergence of unbounded second moments.

## Verification

A standalone checker evaluates stationary covariance against direct renewal integrals, integrated variances against numerical quadrature, exact cycle characteristic functions against their small-frequency leading terms, and the three asymptotic variance coefficients. It passed **106 deterministic analytical-numerical assertions** at the recorded precision. The exact Laplace-tail and renewal arguments above, not those finite checks, prove the infinite-time statements. To reproduce, run `python checker.py` with `mpmath` installed. Its output is stored in `checker_output.txt`.

## Relationship to prior work

Barkai, Flaquer-Galmés and Méndez [1] analyze the renewal-age description, stationary densities and ergodicity transitions of reset Brownian motion, including power-law clocks; they do not state the present signed-area stable index, limiting characteristic-function constant, or critical variance discrepancy. Zamparo [2] rigorously treats general renewal rewards and proves finite-second-moment central limit results; the **regenerative methodology and finite-variance branch are prior work**. The current contribution uses the cycle-area distribution in the infinite-second-moment regime and evaluates its symmetric stable law and the logarithmic borderline, with an exact stationary covariance showing the failure of second-moment convergence at criticality. Méndez and Flaquer-Galmés [3] provide general stochastic-functional transform and moment techniques; their conclusion identifies the time-averaged position and trajectory area as possible further applications, rather than calculating the present signed-area law. A recent study [4] considers **absolute** Brownian area under scaled Brownian dynamics and does not give this signed-area theorem.

## Limitations

The conclusions assume independent Brownian excursions, exact resets to zero, a unit-cutoff Pareto law, finite mean interarrival time, and stationary initialization with \(\alpha>2\). Behavior at \(\alpha\le2\), nonzero drift, dependent excursions, soft or partial resets, and unsigned area are not determined here. The stable-limit step uses classical renewal-reward functional limit theory rather than constructing a new general stable-limit theorem. Although the evaluated constants and critical factor-three mismatch were not located in the inspected works, broader mathematical probability literature could contain equivalent formulas; an independent scholarly priority assessment remains outstanding.

## References

[1] E. Barkai, R. Flaquer-Galmés, and V. Méndez, *Ergodic properties of Brownian motion under stochastic resetting*, arXiv:2306.13621v1 (first posted 2023-06-23), https://arxiv.org/abs/2306.13621.

[2] M. Zamparo, *Statistical fluctuations under resetting: rigorous results*, arXiv:2207.07521 (2022), https://arxiv.org/abs/2207.07521.

[3] V. Méndez and R. Flaquer-Galmés, *Statistical properties of stochastic functionals under general resetting*, arXiv:2507.05955 (2025), https://arxiv.org/abs/2507.05955.

[4] V. Méndez and related collaborators, *Absolute area under a scaled Brownian motion with resetting*, arXiv:2610.19985v1 (2026), https://arxiv.org/abs/2610.19985.
