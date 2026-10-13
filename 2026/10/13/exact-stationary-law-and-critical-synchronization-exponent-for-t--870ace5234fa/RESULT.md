# Exact stationary law and critical synchronization exponent for the careless coupon collector

## Finding

Fix any integer \(n\ge2\) and loss probability \(0<p<1\), writing \(q=1-p\). Each discrete step draws one uniformly random type from \([n]\), adds the type to the currently held collection, and then independently deletes every currently held type with probability \(p\). Let \(S_t\subseteq[n]\) be the collection **after** deletion, and let \(\pi_{n,p}\) be its stationary law.

For every fixed \(r\)-element subset \(A\subseteq[n]\), with \(0\le r\le n\), the exact joint presence probability is
\[
 s_{n,r}:=\Pr_{\pi_{n,p}}(A\subseteq S)
 =\frac{r!\,q^{r(r+1)/2}}{n^r\prod_{j=1}^{r}\left[1-(1-j/n)q^j\right]},\qquad s_{n,0}=1.
\]
This specifies the **entire** exchangeable stationary law through its generating polynomial
\[
\mathbb E_{\pi_{n,p}}(1+z)^{|S|}=\sum_{r=0}^n {n\choose r}s_{n,r}z^r.
\]
In particular, the all-present probability and the stationary frequency of newly entering the full state are exactly
\[
 \Pr_{\pi_{n,p}}(|S|=n)=s_{n,n},\qquad
 \mu_{n,p}=(1-q^n)s_{n,n}.
\]
Distinct coupon-presence indicators have strictly negative covariance:
\[
 \operatorname{Cov}_{\pi_{n,p}}({\bf1}_{i\in S},{\bf1}_{j\in S})
 =-\frac{u_{n,p}^2p^2}{1-q^2+2q^2/n}<0,
 \quad u_{n,p}=\frac q{q+np},\quad i\ne j.
\]

In the critical-loss regime \(p_n=c/n\) for any fixed \(c>0\) and integers \(n>c\), the exact exponential synchronization rate is
\[
 \lim_{n\to\infty}-\frac1n\log s_{n,n}
 =I(c):=1+\frac c2+\int_0^1\log\!\left[1-(1-x)e^{-cx}\right]dx.
\]
The entry frequency \(\mu_{n,p_n}\) has the same exponential rate. Furthermore, for **every** \(c>0\),
\[
 I(c)>\log(1+c),\qquad
 \lim_{n\to\infty}\frac1n\log\frac{s_{n,n}}{u_{n,p_n}^{\,n}}
 =-\bigl[I(c)-\log(1+c)\bigr]<0.
\]
Thus multiplying the correct stationary one-coupon marginals gives an exponentially overoptimistic estimate of full collection in precisely this critical regime.

## Assumptions and scope

The draw is uniform and independent between steps; after every draw, losses are independent across **all currently held types**, conditionally independent of the draw and the past. States are observed after this loss operation. The finite-state Markov chain is irreducible and aperiodic because every set can be completely emptied with positive probability and prescribed types can be retained after subsequent draws; therefore its unique stationary law is exchangeable under permutations of coupon labels. Probabilities, covariance and entry flux throughout refer to this law. The critical result holds for every fixed real \(c>0\) and only integers satisfying \(n>c\).

## Proof

**Stationary factorial recursion.** Put \(K_t=|S_t|\) and let \((k)_r=k(k-1)\cdots(k-r+1)\), with \((k)_0=1\). Given \(K_t=k\), the pre-deletion size is \(k+B\), where \(B\) is Bernoulli with success probability \((n-k)/n\). Conditional on this size, post-deletion survival is binomial with survival probability \(q\). Consequently
\[
 \mathbb E[(K_{t+1})_r\mid K_t=k]
 =q^r\left[(1-r/n)(k)_r+\frac{r(n-r+1)}n(k)_{r-1}\right].
\]
For \(r=1\) this identity uses \((k)_0=1\); for higher \(r\), it follows by adding a single new object to an existing collection and using \((k+1)_r-(k)_r=r(k)_{r-1}\), as well as \(k(k)_{r-1}=(k)_r+(r-1)(k)_{r-1}\).

At stationarity, write \(m_r=\mathbb E_\pi(K)_r\), with \(m_0=1\). The previous identity gives
\[
 m_r\left[1-(1-r/n)q^r\right]
 =\frac{r(n-r+1)}n q^r m_{r-1}.
\]
Every bracket on the left is positive. Iterating yields
\[
 m_r=\frac{r!(n)_r}{n^r}\frac{q^{r(r+1)/2}}{\prod_{j=1}^r[1-(1-j/n)q^j]}.
\]
Exchangeability gives \(\mathbb E_\pi(K)_r=(n)_r\Pr_\pi(A\subseteq S)\), proving the displayed formula. The generating polynomial follows from \(\mathbb E {K\choose r}={n\choose r}s_{n,r}\), and uniquely specifies the distribution of \(K\) by coefficient extraction after replacing \(z\) with \(t-1\). Since the conditional law given \(K=k\) is uniform over \(k\)-subsets, it also determines the complete law on subsets.

**Correlations and entry frequency.** For \(r=1\), \(u_{n,p}=q/(q+np)\). For \(r=2\), write \(d_2=1-(1-2/n)q^2\). The recursion gives \(s_{n,2}=2q^2u_{n,p}/(n d_2)\). Because \(d_2-2q(1-q+q/n)=p^2\), this simplifies to the claimed strictly negative covariance. The all-present state stays all-present in the next step exactly when all \(n\) retained types survive, with probability \(q^n\). Under stationarity, the outgoing and incoming full-state fluxes coincide. Therefore the incoming flux from proper subsets is \((1-q^n)\pi(K=n)\), as stated.

**Critical exponential rate.** Set \(p_n=c/n\), \(q_n=1-c/n\), and \(d_{n,j}=1-(1-j/n)q_n^j\). The exact product gives
\[
 -\frac1n\log s_{n,n}
 =-\frac{\log(n!)-n\log n}{n}-\frac{n+1}{2}\log q_n
 +\frac1n\sum_{j=1}^n\log d_{n,j}.
\]
Stirling's formula sends the first term to \(1\), and the second to \(c/2\). When \(j/n\to x>0\), \(d_{n,j}\to1-(1-x)e^{-cx}\). The elementary estimates
\[
 \frac jn\le d_{n,j}\le (1+c)\frac jn
\]
follow from \(0<q_n^j\le1\) and Bernoulli's inequality \(q_n^j\ge1-cj/n\). These bounds give a uniform integrable logarithmic majorant near zero and justify the improper Riemann-sum limit
\[
 \frac1n\sum_{j=1}^n\log d_{n,j}
 \longrightarrow\int_0^1\log\left[1-(1-x)e^{-cx}\right]dx.
\]
This proves the rate \(I(c)\). Since \(1-q_n^n\to1-e^{-c}>0\), the same rate holds for the entry frequency.

**Strict exponential failure of independent marginals.** Define \(H(c)=I(c)-\log(1+c)\). Continuity at zero and \(\int_0^1\log x\,dx=-1\) show \(H(0)=0\). Differentiating under the improper integral (for each fixed positive \(c\)) yields
\[
 H'(c)=\frac12-\frac1{1+c}+
 \int_0^1\frac{x(1-x)e^{-cx}}{1-(1-x)e^{-cx}}\,dx.
\]
For \(c\ge1\), the first two terms are nonnegative, while the integral is strictly positive. For \(0<c<1\), \(e^{-cx}\ge1-cx\) and \(1-(1-x)e^{-cx}\le x[1+c(1-x)]\). Thus for \(0<x<1\), the integrand is strictly larger than \((1-x)(1-c)/(1+c)\), and its integral exceeds \((1-c)/[2(1+c)]\), exactly enough to give \(H'(c)>0\). Hence \(H(c)>0\) for all \(c>0\). Finally \(u_{n,p_n}=q_n/(q_n+c)\to1/(1+c)\), giving the strict logarithmic ratio limit.

## Verification

The accompanying standalone Python file `checker.py` uses only exact rational arithmetic to construct the independent finite-state transition kernel, solve its stationary linear system, and compare the resulting probabilities with every inclusion moment, the full-state flux and both-site covariance. Executing `python checker.py` passes 280 exact assertions for sizes \(2\le n\le8\) and four distinct survival probabilities. A separate numerical quadrature check of the limiting integral corroborated convergence for \(c=1\), but neither finite calculation is used to prove the all-size theorem. The analytic argument above proves the universal formulas and strict critical-rate gap.

## Relationship to prior work

Cruciani and Dudeja (2026, arXiv:2602.20705) introduce the per-coupon-loss careless collector and study marginal recurrence, hitting times, the critical loss scale and a mean-field approximation which explicitly introduces independence assumptions. The present theorem gives the **exact stationary joint law**, including all inclusion probabilities; it does not substitute the mean-field approximation for a proof. Long (2026, arXiv:2605.14511) derives a stationary-entry-flux framework and a fixed-positive-loss asymptotic. That result uses \(p\) fixed as \(n\) varies and does not imply the present \(p=c/n\) rate. The stationary incoming/outgoing flux identity is standard and credited to the existing flux framework; the new content is the exact full-state stationary probability and its critical dependence exponent. Attrill and Garoni (2026, arXiv:2605.14206) analyze a related but different clumsy-collector transition that modifies only a drawn coupon, not independent losses of all held types. The same-parameter results are therefore not statements about the Markov chain here.

## Limitations

The model requires uniform coupon arrivals, independent Bernoulli losses across retained types, and observation after loss. The theorem concerns the stationary distribution and stationary entry frequency, not the distribution or expectation of first hitting times from the empty state, nor a Poisson entry-process limit. The rate is for fixed \(c>0\), not a uniform assertion in moving \(c\). The exact stationary law could potentially be rewritten using earlier general immigration/thinning machinery that was not identified; mathematical priority outside the inspected sources remains open to external audit.

## References

1. E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, arXiv:2602.20705 (first public version 24 February 2026), https://arxiv.org/abs/2602.20705.
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511 (first public version 14 May 2026), https://arxiv.org/abs/2605.14511.
3. L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206 (first public version 14 May 2026), https://arxiv.org/abs/2605.14206.
