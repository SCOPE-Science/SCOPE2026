# Lattice-phase Gaussian law at the flip boundary of stochastic-rounding descent

## Finding

Let \(\theta\in(0,1)\), \(0<q<1\), and \(U_1,U_2,\ldots\) be independent uniform random variables on \([0,1]\). Define the unbiased nearest-integer rounding operator \(\mathcal R(y,U)=\lfloor y+U\rfloor\) and the integer-valued iteration
\[
X_{n+1}=\mathcal R((1+q)\theta-qX_n,U_{n+1}),\qquad X_0\in\mathbb Z.
\]
It is the exact-gradient step for \(f(x)=\kappa(x-\theta)^2/2\) with \(\eta\kappa=1+q\), followed by one stochastic rounding of the complete step to the unit grid. Let \(\pi_q\) be its stationary law, \(V_q=\mathbb E_{\pi_q}(X-\theta)^2\), and let \(\psi(t)=\{t\}(1-\{t\})\), with \(\{t\}=t-\lfloor t\rfloor\).

**Theorem.** The chain has a unique stationary probability law with finite second moment and converges to it in \(1\)-Wasserstein distance at least at factor \(q\) per iteration. It has stationary mean \(\theta\). Uniformly for \(0<q<1\),
\[
\left|(1-q^2)V_q-\psi(2\theta)\right|
\le\frac12\sqrt{\frac{1-q}{1+q}}.
\]
In particular, if \(\theta\ne1/2\), then
\[
V_q\sim\frac{\psi(2\theta)}{1-q^2}
\sim\frac{\psi(2\theta)}{2(1-q)}
\quad(q\uparrow1),
\]
and the entire stationary marginal obeys the Gaussian limit
\[
\boxed{\sqrt{1-q^2}\,(X-\theta)\ \Longrightarrow\
\mathcal N(0,\psi(2\theta))\quad (X\sim\pi_q).}
\]
At the unique interior resonant phase \(\theta=1/2\), however, \(\pi_q=(\delta_0+\delta_1)/2\) for **every** \(q\in(0,1)\), and \(V_q=1/4\). Thus, as the exact-arithmetic descent stepsize approaches its stability boundary, the stationary variance diverges at every off-half-grid minimizer yet remains exactly bounded at the half-grid minimizer.

For every fixed \(q\in(0,1)\), stationary temporal covariances are
\[
\operatorname{Cov}(X_0,X_m)=(-q)^m V_q,\qquad m\ge0,
\]
and the stationary long-run sample-mean variance has the exact value
\[
\lim_{N\to\infty}N\operatorname{Var}\left(\frac1N\sum_{n=1}^N X_n\right)
=V_q\frac{1-q}{1+q}.
\]
The latter tends to \(\psi(2\theta)/4\) away from the half-grid phase, despite divergence of single-iterate variance. At the half-grid phase it tends to zero.

## Assumptions and scope

The lattice is the *unbounded* unit integer lattice; exact real arithmetic evaluates the deterministic gradient step, and only its final value is rounded. Each round uses a fresh independent \(U_n\). There is no gradient noise or additive innovation, no rounding of intermediate arithmetic, and no floating-point underflow or overflow. The fixed-point minimizer satisfies \(0<\theta<1\). The normal limit is taken under the stationary distribution \(\pi_q\), first fixing \(q<1\) and then letting \(q\uparrow1\); it is not a finite-time limit with simultaneous initialization and stepsize scaling. By scale change, for a grid of width \(\Delta>0\), replace \(\theta\) by \(\theta/\Delta\) and \(X-\theta\) by \((X-\theta)/\Delta\), when the minimizer is in one grid cell. The parameter \(\kappa>0\) merely sets \(\eta=(1+q)/\kappa\).

## Proof

**Rounding identities.** For \(y\in\mathbb R\), writing \(r=\{y\}\), the two possible rounded values are \(\lfloor y\rfloor\) and \(\lfloor y\rfloor+1\), with probabilities \(1-r\) and \(r\). Hence \(\mathbb E[\mathcal R(y,U)]=y\), \(\operatorname{Var}[\mathcal R(y,U)]=\psi(y)\), and \(|\mathcal R(y,U)-y|\le1\). If \(a\le b\), the coupled pair \(\mathcal R(a,U)\le\mathcal R(b,U)\) almost surely. Therefore
\[
\mathbb E\left|\mathcal R(a,U)-\mathcal R(b,U)\right|=b-a.
\]
With the common random number coupling, the one-step distance between transitions from integer states \(x,x'\) is exactly \(q|x-x'|\) in mean. The induced Markov operator is a strict \(q\)-contraction in \(W_1\) on probability laws on \(\mathbb Z\) with finite first moment. This space is complete; the operator preserves it. Banach's fixed-point theorem gives a unique \(\pi_q\) and geometric convergence.

**Moments and phase bound.** Write \(Z=X-\theta\). The conditional mean and second moment satisfy
\[
\mathbb E[Z_{n+1}\mid X_n]=-qZ_n,\qquad
\mathbb E[Z_{n+1}^{2}\mid X_n]=q^2Z_n^2+\psi((1+q)\theta-qX_n).
\]
Since \(\psi\le1/4\), iteration from an integer initial state gives a uniform bound on second moments and hence, by convergence to \(\pi_q\) and Fatou, \(V_q\le1/[4(1-q^2)]\). Stationarity gives \(\mathbb E_{\pi_q}X=\theta\) and the exact balance
\[
(1-q^2)V_q=\mathbb E_{\pi_q}\psi((1+q)\theta-qX).
\]
Since \(X\) is an integer and \(\psi\) has period one,
\[
\psi((1+q)\theta-qX)
=\psi\big(2\theta+(1-q)(X-\theta)\big).
\]
The continuous periodic function \(\psi\) is globally \(1\)-Lipschitz. Thus Cauchy–Schwarz yields
\[
\left|(1-q^2)V_q-\psi(2\theta)\right|
\le(1-q)\sqrt{V_q}
\le\frac12\sqrt{\frac{1-q}{1+q}},
\]
proving the stated uniform estimate and off-resonance asymptotics. For \(\theta\in(0,1)\), \(\psi(2\theta)=0\) precisely at \(\theta=1/2\). There, the set \(\{0,1\}\) is closed, and its transition matrix has rows \(((1-q)/2,(1+q)/2)\) and \(((1+q)/2,(1-q)/2)\); its unique stationary law is fair Bernoulli. Global uniqueness identifies this with \(\pi_q\).

**Gaussian stationary law.** Let \(\varepsilon_{n+1}=X_{n+1}-((1+q)\theta-qX_n)\). Conditional on the past, \(\varepsilon_{n+1}\) has mean zero, absolute value at most one and variance \(\psi((1+q)\theta-qX_n)\). Construct the two-sided stationary chain and put \(\rho_q=\sqrt{1-q^2}\) and \(N_q=\lceil(1-q)^{-2}\rceil\). Iterating \(Z_n=-qZ_{n-1}+\varepsilon_n\),
\[
\rho_q Z_0=\rho_q(-q)^{N_q}Z_{-N_q}
+\sum_{j=0}^{N_q-1}\rho_q(-q)^j\varepsilon_{-j}.
\]
The first term has second moment at most \(q^{2N_q}/4\), hence tends to zero. Written in forward chronological order, the sum is a triangular array of martingale differences, each bounded by \(\rho_q\to0\). Its predictable quadratic variation is
\[
Q_q=(1-q^2)\sum_{j=0}^{N_q-1}q^{2j}
\psi\big(2\theta+(1-q)(X_{-j-1}-\theta)\big).
\]
Using the Lipschitz bound and stationarity,
\[
\mathbb E\left|Q_q-\psi(2\theta)(1-q^{2N_q})\right|
\le(1-q)\mathbb E|X-\theta|
\le\frac12\sqrt{\frac{1-q}{1+q}}\longrightarrow0.
\]
Also \(q^{2N_q}\to0\). Thus \(Q_q\to\psi(2\theta)\) in probability, while the bounded increments make the Lindeberg condition automatic. The martingale triangular-array central limit theorem, followed by Slutsky's lemma, proves the Gaussian limit. When the limiting variance is zero it is interpreted as the point mass at zero; the stronger half-grid Bernoulli description was already proved.

**Temporal covariance and averaging.** Conditional expectation gives \(\mathbb E[Z_{n+m}\mid X_n]=(-q)^mZ_n\). Hence \(\operatorname{Cov}(X_n,X_{n+m})=(-q)^mV_q\). Summing the geometric covariance series gives the stated fixed-\(q\) long-run variance of the stationary sample mean. Its near-flip limit follows from the preceding variance result; no claim is made about a simultaneous \(N,q\) double limit.

## Verification

The included `verify.py` uses only the Python standard library. It builds an invariant finite lattice from \(|X-\theta|\le1/(1-q)\), constructs exact-rational transitions, solves the finite stationary linear system, and checks normalization, means, second moments, balance identities, the half-grid exception, and lag-one covariances. Additional floating-point finite-state iterations check the approach to the phase constant. Run `python verify.py` from this directory. These finite checks are auxiliary: the global convergence and Gaussian statement are proven analytically above, not inferred from finite tests.

As an illustrative exact-kernel numerical value, \(\theta=3/10\) and \(q=9/10\) yield \(V_q\approx1.20000365777\) and \((1-q^2)V_q\approx0.228000695\); the proved limiting phase constant is \(\psi(3/5)=6/25\). At \(\theta=1/2\), \(V_q=1/4\) exactly at both these and all other allowed step sizes.

## Relationship to prior work

Unbiased stochastic rounding and gradient-descent error analysis are well established (Xia et al.; El Arar et al.). Liu and Yuan's random-rounded time-series model already studies first-order mean-preserving rounding and negative serial dependence; Weiß and Zhu's 2024 mean-preserving integer ARMA analysis establishes stationary behavior, conditional variance and Yule–Walker autocorrelation laws for related integer models. The basic rounding variance and AR(1) covariance calculation are consequently **not** claimed novel. The result here isolates the *joint* critical-step limit, the explicit fractional lattice-phase Gaussian variance, the unique half-grid bounded-variance resonance and their consequence for average-risk scaling under a deterministic affine gradient step with a noninteger intercept. Deterministic rounded integer AR models (Kachour and Yao) have another update kernel. The literature comparisons are not a proof of global priority; possible obscure near-unit-root stochastic-rounding results remain a risk.

## Limitations

This is a one-dimensional idealized final-step rounding model. It does not describe conventional floating-point roundoff at every intermediate operation, saturating fixed-point arithmetic, stochastic gradients, correlated random seeds, adaptive steps, multivariate quadratics or general nonconvex objectives. The normal limit concerns the invariant distribution and does not quantify how many iterations are needed for a changing \(q\). Prior literature already includes mean-preserving rounding, stationary integer autoregressions and generic martingale central limit theory; independent novelty and proof auditing have not been performed.

## References

1. L. Xia, S. Massei, M. E. Hochstenbach and B. Koren, *On the influence of stochastic roundoff errors and their bias on the convergence of the gradient descent method with low-precision floating-point computation* (first public 2022-02-24), https://arxiv.org/abs/2202.12276.
2. B. El Arar et al., *Stochastic rounding variance and probabilistic bounds: A new approach* (first public 2022-07-21), https://arxiv.org/abs/2207.10321.
3. T. Liu and X. Yuan, *Random rounded integer-valued autoregressive conditional heteroskedastic process*, Statistical Papers 54 (2013), 645–683, https://www.researchgate.net/publication/236616464_Random_rounded_integer-valued_autoregressive_conditional_heteroskedastic_process.
4. C. H. Weiß and F. Zhu, *Mean-preserving rounding integer-valued ARMA models* (first public 2024-02-24), https://arxiv.org/abs/2402.15772.
5. M. Kachour and J. F. Yao, *First-order rounded integer-valued autoregressive (RINAR(1)) process*, Journal of Time Series Analysis 30 (2009), 417–448, https://www.researchgate.net/publication/46537819_First-order_rounded_integer-valued_autoregressive_RINAR1_process.
