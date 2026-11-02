# An arcsine–Gaussian majority-reconstruction crossover for high-noise voter stars

## Finding

Let a star have \(n\ge1\) leaves. Each vertex independently copies a uniformly selected neighbor at rate one and, at rate \(\theta>0\), rerandomizes its binary opinion to a fair independent bit. Let \(\mu_{n,\theta}\) be the unique stationary law of its hub opinion \(H\) and all leaf opinions, and write \(K\) for the number of leaves in state one. Define \(\kappa=1+\theta\), \(a=\theta/(2\kappa)\), and \(\ell=\theta/(2\kappa)\).

**Finite-size surrogate theorem.** Define a comparison law \(\nu_{n,\theta}\) by sampling \(Y\sim\operatorname{Beta}(a,a)\), then \(H\mid Y=y\sim\operatorname{Bernoulli}(y)\), and independently, conditional on \(Y=y\), taking the \(n\) leaves to be independent \(\operatorname{Bernoulli}(\ell+y/\kappa)\) variables. The hub and leaves are independent *conditional on* \(Y\). Then, for every integer \(n\ge1\) and every \(\theta>0\),
\[
\boxed{d_{\mathrm{TV}}(\mu_{n,\theta},\nu_{n,\theta})\le\inf_{T>0}\left[T+(n+1)e^{-\theta T/2}\right]\le\frac{4\log(n+1)}\theta+\frac1{n+1}.}
\]
In particular, the entire stationary configuration—not only its leaf count—has an asymptotically exact explicit Beta-mixture representation whenever \(\theta_n/\log n\to\infty\).

**Sharp square-root crossover.** Suppose \(n\to\infty\), \(\theta_n/\log n\to\infty\), and write \(X_n=K/n\). Let \(Y\sim\operatorname{Beta}(1/2,1/2)\), \(H\mid Y=y\sim\operatorname{Bernoulli}(y)\), and \(G\sim N(0,1)\) independent of \((H,Y)\). The following joint limits hold:
\[
\begin{array}{ll}
\theta_n/\sqrt n\to0:&(H_n,\,\kappa_n(X_n-1/2))\Longrightarrow(H,Y-1/2),\\[3pt]
\theta_n/\sqrt n\to\lambda\in(0,\infty):&(H_n,\,\sqrt n(X_n-1/2))\Longrightarrow(H,(Y-1/2)/\lambda+G/2),\\[3pt]
\theta_n/\sqrt n\to\infty:&(H_n,\,\sqrt n(X_n-1/2))\Longrightarrow(H,G/2).
\end{array}
\]
In the final regime \(H\) and \(G\) are independent and \(H\) is fair. Let \(\widehat H_n\) predict the current hub by the strict majority of its leaves, with an independent fair tie-breaker. In the three regimes its limiting success probabilities are respectively
\[
\boxed{\frac12+\frac1\pi,\qquad
S(\lambda)=\int_0^1\!\frac{y\Phi((2y-1)/\lambda)+(1-y)\Phi((1-2y)/\lambda)}{\pi\sqrt{y(1-y)}}\,dy,\qquad\frac12.}
\]
The crossover curve \(S(\lambda)\) is strictly decreasing on \((0,\infty)\), with endpoint values \(1/2+1/\pi\) and \(1/2\). Here \(\Phi\) is the standard normal distribution function. These are accuracies of the stated majority rule; Bayes optimality is not claimed.

## Assumptions and scope

The rate-one neighbor-copy and rate-\(\theta\) fair-reset clocks are independent at every vertex, and the graph is the unweighted star. Both the original and surrogate processes are at stationarity. The crossover requires diverging noise satisfying \(\theta_n/\log n\to\infty\); no conclusion here applies to fixed noise or to noise smaller than this proved comparison regime. All limits are for the number of leaves tending to infinity.

## Proof

**1. A decoupled-hub comparison process.** Construct a second process on the same star by suppressing the hub's rate-one neighbor-copy events, while retaining all hub fair-rerandomizations and every leaf's copy and rerandomization events. Its unique stationary law is \(\nu_{n,\theta}\), as identified in Step 3. Drive the original and comparison process with the *same* fair-reset clocks and bits at the hub, and identical leaf clocks, neighbor choices and reset bits. The original hub additionally has a rate-one copy clock.

Fix \(T>0\). Start the two processes at time \(-T\) from their respective stationary distributions, under any coupling. On the event that (i) the original hub has no copy events during \([-T,0]\), (ii) the shared hub has at least one fair reset during \([-T,-T/2]\), and (iii) every leaf has at least one update during \([-T/2,0]\), the full binary configurations agree at time zero. Indeed the hub states coalesce at the first common reset and remain identical, and every subsequent leaf update makes that pair of leaf opinions identical. The failure probability is bounded by \(T+e^{-\theta T/2}+n e^{-(1+\theta)T/2}\), hence by \(T+(n+1)e^{-\theta T/2}\). The coupling inequality gives the first displayed total-variation estimate for the entire configuration. Choosing \(T=4\log(n+1)/\theta\) gives the explicit second bound, valid even when it exceeds one.

**2. Conditional independence of surrogate leaves.** In the decoupled process the hub evolves independently, rerandomizing to fair bits at rate \(\theta\), equivalently changing state at rate \(\theta/2\). Conditioned on its complete past path, independent leaf clocks make stationary leaf opinions independent and identically distributed Bernoulli variables with a random success probability \(P_t\). This probability satisfies the linear random differential equation
\[
\dot P_t=\theta/2+H_t-\kappa P_t,
\qquad P_t=\int_{-\infty}^{t}e^{-\kappa(t-s)}(\theta/2+H_s)\,ds.
\]
Let \(Y_t=\kappa(P_t-\ell)\). When the hub is zero, \(\dot Y_t=-\kappa Y_t\); when it is one, \(\dot Y_t=\kappa(1-Y_t)\). In either hub state, flipping to the other occurs at the constant rate \(\theta/2\).

**3. Exact stationary mixing measure.** This two-state piecewise-deterministic process on \(\{0,1\}\times[0,1]\) has invariant densities
\[
p_0(y)=\frac{(1-y)y^{a-1}(1-y)^{a-1}}{B(a,a)},\qquad
p_1(y)=\frac{y\,y^{a-1}(1-y)^{a-1}}{B(a,a)}.
\]
They have zero total transport flux because \((-\kappa y)p_0+\kappa(1-y)p_1=0\). With \(J(y)=\kappa yp_0(y)=\kappa y^a(1-y)^a/B(a,a)\), the remaining stationary balance equation is \(J'(y)=(\theta/2)(p_0(y)-p_1(y))\), since \(\kappa a=\theta/2\). Boundary fluxes vanish. Uniqueness follows from strictly positive hub-reset rates and contraction of the deterministic flows: a positive-probability prescribed sequence of two hub resets, with a variable second-reset time, gives a common interior density minorization after sufficiently long holding times. The mixing law is therefore exactly \(Y\sim\operatorname{Beta}(a,a)\) and \(\Pr(H=1\mid Y=y)=y\). Conditional leaf independence from Step 2 completes the claimed surrogate law.

**4. Critical limits.** As \(\theta_n\to\infty\), the Beta shape \(a_n=\theta_n/[2(1+\theta_n)]\to1/2\), so \((H,Y_{\theta_n})\) converges to the stated arcsine/Bernoulli pair. Conditional on \(Y_{\theta_n}=y\), the surrogate leaf count is \(\operatorname{Bin}(n,p_n(y))\), where \(p_n(y)=1/2+(y-1/2)/\kappa_n\). Since \(\sup_y|p_n(y)-1/2|\to0\), the uniform binomial characteristic-function expansion gives
\[
\left(H,Y_{\theta_n},\frac{K-np_n(Y_{\theta_n})}{\sqrt n}\right)
\Longrightarrow (H,Y,G/2),
\]
with \(G\) independent. The exact decomposition
\[
\sqrt n(X_n-1/2)=\frac{\sqrt n}{\kappa_n}(Y_{\theta_n}-1/2)+\frac{K-np_n(Y_{\theta_n})}{\sqrt n}
\]
then proves the critical and supercritical limits. Multiplying by \(\kappa_n/\sqrt n\) gives the subcritical limit. The total-variation comparison from Step 1 transfers all these joint weak limits from the surrogate to the true stationary star.

**5. Majority inference.** The event \(X_n>1/2\) is a continuity event in each limiting law, since the limiting arcsine and arcsine-plus-Gaussian variables have continuous densities. Conditional on \(Y=y\), the critical-limit centered observation has success probability \(\Phi((2y-1)/\lambda)\) when the hub is one and \(\Phi((1-2y)/\lambda)\) when it is zero, giving \(S(\lambda)\). Writing \(A=2Y-1\), symmetry yields \(S(\lambda)=1/2+\mathbb E[A(\Phi(A/\lambda)-1/2)]\), so
\[
S'(\lambda)=-\lambda^{-2}\mathbb E\left[A^2\varphi(A/\lambda)\right]<0,
\]
where \(\varphi\) is the standard Gaussian density. At \(\lambda\downarrow0\), the success equals \(1/2+\mathbb E|Y-1/2|=1/2+1/\pi\), by an elementary arcsine integral, and at \(\lambda\uparrow\infty\) it tends to chance. The strict-majority tie convention does not change these limits.

## Verification

The standalone standard-library `CHECK.py` reconstructs exact finite stationary Markov generators by rational arithmetic and checks finite means, variance, covariance and balance equations. It also builds the independent-hub Beta/binomial surrogate by exact Beta moments for \(n=1,\ldots,8\) and five rational noise rates, verifies its normalization/positivity and the rigorous coupling bound, and numerically checks the critical Gaussian-convolution variance and hub covariance. The observed output is `PASS 680 exact finite-state assertions` followed by `PASS 100 additional exact-mixture and critical-moment checks`. Finite tests and numerical asymptotics are not substitutes for Steps 1–5.

## Relationship to prior work

Cox, Peres and Steif (first posted 2014-08-21, Section 4) analyze the noisy-voter star's reduced hub/leaf-count chain and its mixing time; this model and reduction are prior work. Caligiuri and Galla (first posted 2023-05-30, Section III.3) establish the standard two-state PDMP stationary-density framework, including formulas for constant switching; this analytic framework is prior work. Carro, Toral and San Miguel (first posted 2016-02-22, Sections 2–3) derive general noisy-voter pair-moment equations on networks, so finite second moments are not the priority claim. The present result instead gives a **quantitative whole-configuration stationary coupling** with an explicitly mixed independent-hub process under diverging noise, a simultaneous square-root-noise arcsine–Gaussian crossover, and an explicit majority-reconstruction curve. These require a comparison of two different interacting processes and are not stated or directly implied by the fixed-noise star-mixing or two-state PDMP stationary formulas alone.

## Limitations

The theorem is restricted to the specified star and to \(\theta_n\gg\log n\). The derived total-variation bound may be nonsharp; no necessity of the logarithmic condition is claimed. There is no result here for sparse nonstar graphs, nonsymmetric noise, nonstationary initializations or optimality of majority prediction. General Markov-chain coupling literature may contain related approximation principles; historical novelty remains subject to independent review.

## References

1. J. T. Cox, Y. Peres, J. E. Steif, *Cutoff for the noisy voter model*, arXiv:1408.5122 (first public 2014-08-21), Section 4. https://arxiv.org/abs/1408.5122
2. A. Caligiuri, T. Galla, *Noisy voter models in switching environments*, arXiv:2305.19096 (first public 2023-05-30), Section III.3. https://arxiv.org/abs/2305.19096
3. A. Carro, R. Toral, M. San Miguel, *The noisy voter model on complex networks*, arXiv:1602.06935 (first public 2016-02-22), Sections 2–3. https://arxiv.org/abs/1602.06935
4. R. Pymar, N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478 (first public 2021-12-02). https://arxiv.org/abs/2112.01478
