# A Gaussian-to-Laplace stationary crossover for a resetting Pólya urn

## Finding

A finite reinforced urn with complete independent resets has an exactly soluble stationary age-count law and autocovariance, but its fluctuation distribution changes shape according to the product of the initial population and reset probability. At critical scaling there is a continuous family of non-Gaussian normal mixtures; sufficiently frequent resets instead produce the Laplace stationary law of a Brownian motion with resetting. The process-level limit identifies the entire temporal mechanism, not only the one-time marginal.

For each even \(n\ge2\) and \(r\in(0,1)\), the joint stationary law of age \(A\) and red additions \(R\) is
\[
\Pr(A=k,R=j)=r(1-r)^k\binom{k}{j}
\frac{(n/2)^{\overline j}(n/2)^{\overline{k-j}}}{n^{\overline k}},
\qquad k\ge0,\ 0\le j\le k.
\]
In particular, for red fraction \(X\) in stationarity and every integer lag \(h\ge0\),
\[
\mathbb EX=\tfrac12,\quad
\operatorname{Var}(X)=\frac{1}{4(n+1)}\mathbb E\frac A{n+A},\quad
\operatorname{Cov}(X_0,X_h)=(1-r)^h\operatorname{Var}(X).
\]
If \(n\) increases through even integers and \(r=r_n\to0\), three limiting regimes hold:
\[
\begin{array}{rcl}
 nr_n\to0 &: &\sqrt n(X-\frac12)\Rightarrow N(0,\frac14),\\
 nr_n\to\lambda\in(0,\infty) &: &\sqrt n(X-\frac12)\Rightarrow Z_\lambda,\\
 nr_n\to\infty &: &n\sqrt{r_n}(X-\frac12)\Rightarrow L.
\end{array}
\]
Here \(Z_\lambda\) is a Gaussian variance mixture satisfying
\[
 T\sim\operatorname{Exp}(\lambda),\qquad
 (Z_\lambda\mid T=t)\sim N\!\left(0,\frac{t}{4(1+t)}\right),
\]
while \(L\) has density \(\sqrt2e^{-2\sqrt2|x|}\) and characteristic function \((1+s^2/8)^{-1}\). The endpoints of the critical family are
\[
 Z_\lambda\Rightarrow N(0,1/4)\ (\lambda\downarrow0),\qquad
 \sqrt\lambda Z_\lambda\Rightarrow L\ (\lambda\uparrow\infty).
\]
In the strong-reset regime the stationary processes
\[
 Y_n(t)=n\sqrt{r_n}\left(X_n(\lfloor t/r_n\rfloor)-\frac12\right),\quad t\ge0,
\]
converge in \(D([0,\infty),\mathbb R)\) with Skorokhod \(J_1\) topology to stationary Brownian motion with diffusivity \(1/8\), independently reset to zero at rate one. Its generator on smooth bounded test functions is
\[
 \mathcal Lf(x)=\tfrac18 f''(x)+f(0)-f(x).
\]
This stationary process has variance \(1/4\) and covariance \(e^{-|t|}/4\) at time separation \(t\).

## Assumptions and scope

At each integer time exactly one of the following occurs, independent of the past: with probability \(r\), replace the entire urn by its deterministic initial state of \(n/2\) red and \(n/2\) blue balls; otherwise draw one existing ball uniformly, replace it and add a same-coloured ball. On a reset no reinforcing draw occurs. After a reset, each successive non-reset is a classical balanced two-colour Pólya draw. The state is the two full ball counts; \(X\) is their red ratio. The age \(A\) counts non-reset transitions since the last reset. The initial \(n\) must be even. The stationary state exists uniquely for each \(r\in(0,1)\); the asymptotic statements all assume \(r_n\to0\). The exponential distribution uses its rate parameter.

## Proof

**1. Stationary regenerative identity.** Couple two copies using the same reset indicators and, after their first common reset, the same subsequent draws. They coincide from the first reset onward, so the total-variation distance to the unique stationary distribution at time \(h\) is at most \((1-r)^h\). In a bi-infinite sequence of independent reset indicators, the number \(A\) of most recent consecutive non-resets has \(\Pr(A=k)=r(1-r)^k\). Conditional on \(A=k\), the sequence of reinforced colours has the Pólya/Eggenberger exchangeable law. Multiplying its beta-binomial mass by the age probability gives the displayed stationary joint law. The red fraction conditional on \((A,R)=(k,j)\) is \((n/2+j)/(n+k)\).

**2. Exact second moments and temporal decay.** For fixed \(k\), the beta-binomial mass yields \(\mathbb E[X\mid A=k]=1/2\) and
\[
 \operatorname{Var}(X\mid A=k)=\frac{k}{4(n+1)(n+k)}.
\]
The law of total variance yields the asserted stationary variance. On any non-reset step the red fraction is a martingale because the added colour is red with probability equal to the present red fraction. Hence, given the entire state at time zero, if no reset occurs in the next \(h\) steps the conditional expected fraction is the current fraction; otherwise its conditional expectation is exactly \(1/2\), by colour symmetry after the latest reset. Since the reset indicators are independent, 
\[
 \mathbb E[X_h\mid\mathcal F_0]=\frac12+(1-r)^h(X_0-\frac12).
\]
Multiply by \(X_0-1/2\) and take expectations. This proves the covariance for every \(h\), without invoking asymptotics.

**3. The scaling variable.** Let \(A_n\) denote stationary age. As \(r_n\to0\), \(r_nA_n\Rightarrow E\), where \(E\) is exponential of rate one; indeed \(\Pr(r_nA_n>x)=(1-r_n)^{\lfloor x/r_n\rfloor+1}\to e^{-x}\). If \(nr_n\to\lambda\in(0,\infty)\), then \(A_n/n\Rightarrow T=E/\lambda\sim\operatorname{Exp}(\lambda)\). The same relation gives \(A_n/n\to\infty\) in probability when \(nr_n\to0\), and \(A_n/n\to0\) in probability when \(nr_n\to\infty\).

**4. The Gaussian and intermediate regimes.** The classical urn admits the de Finetti construction \(\Theta_n\sim\operatorname{Beta}(n/2,n/2)\), and, conditional on \((A_n=k,\Theta_n)\), \(R\sim\operatorname{Bin}(k,\Theta_n)\), with the age independent of \(\Theta_n\). The beta central limit theorem gives \(\sqrt n(\Theta_n-1/2)\Rightarrow N(0,1/4)\). When \(A_n/n\to\infty\), the conditional binomial variance shows \(\sqrt n(X-\Theta_n)\to0\) in probability: the contribution from \(R-A_n\Theta_n\) has conditional variance bounded by \(nA_n/[4(n+A_n)^2]\to0\), and the initial-composition correction is \(n\sqrt n(1/2-\Theta_n)/(n+A_n)\to0\). Thus the weak-reset Gaussian result holds.

For deterministic age sequences \(k_n/n\to t\in(0,\infty)\), write
\[
 \sqrt n(X-\frac12)=\frac{k_n}{n+k_n}\sqrt n(\Theta_n-\frac12)
 +\frac{\sqrt n}{n+k_n}(R-k_n\Theta_n).
\]
The first term tends to a normal variable of variance \(t^2/[4(1+t)^2]\); the conditional binomial central limit theorem gives an asymptotically independent normal variable of variance \(t/[4(1+t)^2]\). Independence follows from the joint conditional characteristic functions and \(\Theta_n\to1/2\) in probability. Their total variance is \(t/[4(1+t)]\). Integrating over the independent random ages, first on compact positive age-ratio intervals and then using tightness and negligible tails, gives the claimed \(Z_\lambda\) mixture. The characteristic function is therefore
\[
 \mathbb E e^{isZ_\lambda}
 =\int_0^\infty \lambda e^{-\lambda t}
 \exp\!\left(-\frac{s^2t}{8(1+t)}\right)\,dt.
\]
Since \(T=E/\lambda\), dominated convergence gives both stated endpoint laws: as \(\lambda\downarrow0\), the conditional variance tends to \(1/4\); as \(\lambda\uparrow\infty\), the conditional variance of \(\sqrt\lambda Z_\lambda\) tends to \(E/4\), and \(\mathbb E e^{-s^2E/8}=(1+s^2/8)^{-1}\), the stated Laplace characteristic function.

**5. Functional strong-reset limit.** Assume \(r_n\to0\) and \(nr_n\to\infty\). In one fresh episode started at the balanced configuration, let \(U_n(j)\) be the red fraction after \(j\) ordinary urn draws, and set \(M_n(j)=n\sqrt{r_n}(U_n(j)-1/2)\). It is a martingale with jumps of absolute size at most \(n\sqrt{r_n}/(n+j+1)\le\sqrt{r_n}\). Its predictable quadratic variation through \(\lfloor t/r_n\rfloor\) is
\[
 \sum_{j< t/r_n}
 \frac{n^2r_n}{(n+j+1)^2}U_n(j)(1-U_n(j)).
\]
Uniformly on bounded time intervals, \(j/n\le t/(nr_n)\to0\); moreover, by the exact conditional variance in step 2 and Doob's inequality, \(\sup_{j\le T/r_n}|U_n(j)-1/2|\to0\) in probability. Consequently this quadratic variation converges uniformly in probability to \(t/4\). The martingale functional central limit theorem (vanishing maximum jumps and the quadratic-variation limit) gives \(M_n(\lfloor t/r_n\rfloor)\Rightarrow\tfrac12 B(t)\) on compact intervals, for standard Brownian \(B\).

Now place independent full resets at Bernoulli rate \(r_n\) at each integer step. The rescaled reset point process converges to a unit-rate Poisson point process. Separate reinforced episodes are independent of each other and of the reset indicators. For the stationary initial episode, \(r_nA_n\Rightarrow E\sim\operatorname{Exp}(1)\) independently of its reinforced colours, so the rescaled initial value converges to \(\tfrac12B(E)\); future resets start new independent Brownian paths at zero. Joint convergence of the finite collection of episode lengths and paths on each bounded horizon, followed by path concatenation, gives the \(J_1\) limit. This concatenation is continuous at configurations with distinct interior Poisson reset times and continuous Brownian episode paths, events of probability one. At reset times the process jumps to zero, as required. The initial law is stationary by the exponential age identity and memorylessness. The limiting Brownian variance rate is \(1/4\), so the diffusion coefficient in the generator is \(1/8\); reset rate one contributes \(f(0)-f(x)\). Averaging \(N(0,E/4)\) over independent exponential \(E\) gives the Laplace characteristic function \((1+s^2/8)^{-1}\). The exact covariance from step 2, together with stationary-variance convergence obtained from \(\mathbb E[A/(n+A)]\sim1/(nr_n)\), yields the limiting covariance \(e^{-|t|}/4\). This completes all claims.

## Verification

The standalone `checker.py` uses only the Python standard library and exact rational arithmetic. It independently derives beta-binomial masses from the one-step red/blue transition recursion; verifies normalization, conditional mean and variance, stationary age-count flow equations and tail mass; and verifies the conditional contraction formula using independently propagated finite Markov states. Run with `python3 checker.py`. The script passes 9,580 exact assertions. These computations test finite algebra only; the asymptotic claims rely on the preceding proof, not on numerical extrapolation.

## Relationship to prior work

Dean, *Functional limit theorems for Pólya urns with growing initial compositions* (arXiv:2206.05138, first posted 10 June 2022), proves functional Gaussian regimes for urns without complete random resets, including an identity replacement structure. Those no-reset results are closely related ingredients, but do not state a stationary regenerative law, an exact reset-dependent autocovariance, or a joint stationary reset crossover. The reset-to-origin Brownian stationary Laplace law was established by Evans and Majumdar in *Diffusion with Stochastic Resetting* (arXiv:1102.2704, 2011). It is not claimed as new; the contribution here is the exact discrete Pólya-urn identity and its three-regime connection, with a process-level limit. Mori, Hisakado and Nakayama (arXiv:2105.10653, 2021) investigate altered memory kernels rather than wholesale resets of an urn's ball counts. The comparison concerns the complete mathematical statements, not titles or coincident Gaussian/Laplace keywords.

## Limitations

The initial urn is exactly balanced; resetting replaces the entire state; each reinforcement adds precisely one ball of the drawn colour; reset indicators are independent and geometric. All limiting results require \(r_n\to0\); the strong-reset Laplace statement is not asserted for fixed nonzero reset probabilities. The process-level result is for fixed compact time horizons and the \(J_1\) topology, not for an unbounded observation horizon or varying initial colour imbalance. The cited Brownian-reset law is prior art, and an exhaustive priority determination for all reinforced regenerative models is not claimed. No independent mathematical audit has been performed.

## References

1. Christopher B. C. Dean, *Functional limit theorems for Pólya urns with growing initial compositions*, arXiv:2206.05138, first public version 2022-06-10, https://arxiv.org/abs/2206.05138.
2. Martin R. Evans and Satya N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704, first public version 2011-02-14, https://arxiv.org/abs/1102.2704.
3. Shintaro Mori, Masato Hisakado and Kazuaki Nakayama, *Pólya urn with memory kernel and asymptotic behaviours of autocorrelation function*, arXiv:2105.10653, first public version 2021-05-22, https://arxiv.org/abs/2105.10653.
4. Eggenberger and Pólya, classical reinforced-urn distribution; standard beta-binomial identity (used and separately proved by the reinforcement recursion in `checker.py`).
