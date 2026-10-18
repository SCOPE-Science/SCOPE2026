# A Weibull-power limit for coupon-collector siblings at logarithmically growing indices

## Finding

In the uniform siblings coupon-collector model with \(N\) equally likely types, let \(U_j^{(N)}\) denote the number of types missing from album \(j\ge 2\) when album 1 first becomes complete. Fix any \(r\ge1\) and sequences of integers \(j_{N,i}\ge 2\), with \(i=1,\ldots,r\), such that
\[
\frac{j_{N,i}-1}{\log N}\longrightarrow \alpha_i\in(0,1).
\]
Define the exact normalizers
\[
a_{N,i}=\frac{(\log N)^{j_{N,i}-1}}{(j_{N,i}-1)!}.
\]
There is a coupling of the laws for every \(N\) under which, jointly for all \(1\le i\le r\),
\[
\left(\frac{U_{j_{N,i}}^{(N)}}{a_{N,i}}\right)_{i=1}^{r}
\xrightarrow{\mathbb P}
\left(\frac{W^{1-\alpha_i}}{1-\alpha_i}\right)_{i=1}^{r},
\qquad W\sim\operatorname{Exp}(1).
\]
For every such single sequence, there is also exact asymptotic mean agreement:
\[
\frac{\mathbb E U_{j_N}^{(N)}}{(\log N)^{j_N-1}/(j_N-1)!}
\longrightarrow \Gamma(1-\alpha).
\]
Consequently, the limiting cumulative distribution function at any \(x\ge0\) is
\[
1-\exp\left[-\bigl((1-\alpha)x\bigr)^{1/(1-\alpha)}\right].
\]
Thus the usual exponential law at fixed sibling index is replaced by a nonexponential power-of-exponential distribution at indices proportional to \(\log N\). The finite-dimensional limits share the *same* exponential random variable and have a nonlinear dependence profile.

## Assumptions and scope

All logarithms are natural. There are \(N\ge2\) coupon types, each sampled independently with probability \(1/N\) at every draw. Album 1 takes the first occurrence of each type; the next occurrence goes to album 2; and in general its \(j\)-th occurrence goes to album \(j\). Sampling stops when album 1 contains every type. The variable \(U_j^{(N)}\) counts types not yet received by album \(j\) at that stopping time. The dimension \(r\) of the joint statement is fixed, while the indices may grow at unrelated rates \(\alpha_i\log N\), with all \(0<\alpha_i<1\). No assertion is made for \(\alpha=1\), faster index growth, unequal coupon weights, or joint limits with an increasing number of coordinates.

## Proof

**Step 1: a simultaneous exponential-spacing representation.** Poissonize the uniform draws using \(N\) independent rate-one Poisson processes, one for each type. The superposition has type-uniform marks, so the sequence of coupon types, and hence the missing-album counts at first completion, have the original discrete-time law. The first arrival times of the \(N\) type processes are independent standard exponentials. When ordered from largest to smallest, the successive gaps from the largest first-arrival time have independent exponential distributions with rates \(1,2,\ldots,N-1\). Write these gaps as independent \(\xi_\ell\sim\operatorname{Exp}(\ell)\), and let \(S_\ell=\xi_1+\cdots+\xi_\ell\). A type ranked \(\ell\) below the last first arrival has \(S_\ell\) time units between its first arrival and completion. Conditional on the first arrival times, the further arrivals of distinct types are independent unit-rate Poisson processes. Therefore, if \(P_\ell\) are independent unit-rate Poisson processes, independent of the gaps, there is a single construction satisfying, for all \(N\ge2\) and all \(j\ge2\),
\[
\widetilde U_j^{(N)}=1+\sum_{\ell=1}^{N-1}
\mathbf1\{P_\ell(S_\ell)\le j-2\},
\qquad \widetilde U_j^{(N)}\overset d=U_j^{(N)}.
\]
The initial 1 accounts for the type whose first arrival completes album 1. This identity also follows from the exponential-order-statistic coupling in Long (2026). In particular, conditional on the gaps, the summands for a fixed \(j\) are independent Bernoulli variables. Their conditional success probabilities are
\[
F_k(S_\ell),\qquad F_k(s)=e^{-s}\sum_{a=0}^{k}\frac{s^a}{a!},\qquad k=j-2.
\]

**Step 2: the common random amplitude.** Since \(\mathbb E\xi_\ell=1/\ell\) and \(\sum_{\ell\ge1}\operatorname{Var}(\xi_\ell)=\sum_{\ell\ge1}\ell^{-2}<\infty\), the centered series of gaps converges almost surely. Using the harmonic-number asymptotic gives a finite random variable \(G\) with
\[
S_\ell-\log\ell\longrightarrow G\quad\text{almost surely},\qquad W=e^{-G}>0.
\]
The gap-sum \(S_\ell\) has the same law as the maximum of \(\ell\) independent unit-rate exponentials. Hence for fixed \(w>0\),
\[
\Pr\{\ell e^{-S_\ell}>w\}
=\left(1-\frac w\ell\right)^\ell\longrightarrow e^{-w},
\]
with the left expression interpreted for \(\ell>w\). As \(\ell e^{-S_\ell}\to W\) almost surely, it follows that \(W\sim\operatorname{Exp}(1)\). On the same almost-sure event, for every fixed \(\delta>0\), uniformly in \(\ell\ge N^\delta\),
\[
S_\ell=\log\ell-\log W+o(1),\qquad e^{-S_\ell}=\frac W\ell(1+o(1)).
\]

**Step 3: a uniform lower-Poisson-tail asymptotic.** Let \(m_N=j_N-1\), \(k_N=m_N-1\), and \(L=\log N\), with \(m_N/L\to\alpha\in(0,1)\). For any fixed \(0<\rho<1\), uniformly along sequences with \(k\to\infty\), \(s>0\) and \(0\le k/s\le\rho\),
\[
F_k(s)=e^{-s}\frac{s^k}{k!}
\left(\frac{1+o(1)}{1-k/s}\right).
\]
Indeed, dividing the defining sum by its final term gives \(\sum_{v=0}^{k}(k)_v/s^v\). For every fixed \(v\), \((k)_v/k^v\to1\), while the summands are bounded by \(\rho^v\). A geometric-series cutoff, uniform in \(k/s\le\rho\), proves the displayed approximation. This is not an approximation near the Poisson mean; keeping \(k/s\) strictly below 1 is essential.

**Step 4: the conditional mean and its endpoint integral.** Write \(b_N=L^{m_N}/m_N!\). Stirling's formula gives
\[
\frac{\log b_N}{L}\longrightarrow
\beta=\alpha(1-\log\alpha),\qquad \alpha<\beta<1.
\]
Choose any fixed \(\delta\) satisfying \(\alpha<\delta<\beta\). The contribution of \(\ell\le N^\delta\) to the conditional mean is at most \(N^\delta=o(b_N)\). For \(\ell>N^\delta\), the preceding two steps yield, almost surely and uniformly,
\[
F_{k_N}(S_\ell)=
\frac{W}{\ell}\frac{(\log\ell-\log W)^{k_N}}{k_N!}
\frac{1+o(1)}{1-k_N/(\log\ell-\log W)}.
\]
The denominator is uniformly bounded away from zero. The resulting sum is a logarithmic Riemann sum: replacing \(\sum f(\log\ell)/\ell\) by \(\int f(t)\,dt\) incurs a negligible relative error, because the lower endpoint is \(N^\delta\) and the logarithmic derivative of the displayed factor is \(O(1/\ell)\) there, uniformly in \(N\). Setting \(c=\log W\), the conditional mean \(\mu_N=\mathbb E[\widetilde U_{j_N}^{(N)}\mid(\xi_\ell)_{\ell\ge1}]\) thus satisfies
\[
\mu_N=\frac W{k_N!}\int_{\delta L}^{L}
\frac{(t-c)^{k_N}}{1-k_N/(t-c)}\,dt\,(1+o(1))+o(b_N)
\quad\text{almost surely}.
\]
The factor \(1/(1-k_N/(t-c))\) tends to \(1/(1-\alpha)\) uniformly on any fixed relative neighborhood of the upper endpoint. Since the integral of \((t-c)^{k_N}\) is dominated by such a neighborhood, and since \(\bigl((\delta L-c)/(L-c)\bigr)^{m_N}\to0\), elementary endpoint concentration gives
\[
\int_{\delta L}^{L}\frac{(t-c)^{k_N}}{1-k_N/(t-c)}\,dt
\sim\frac{(L-c)^{m_N}}{m_N(1-\alpha)}.
\]
It follows that
\[
\frac{\mu_N}{b_N}\longrightarrow
\frac W{1-\alpha}\lim_{N\to\infty}
\left(1-\frac{\log W}{L}\right)^{m_N}
=\frac{W^{1-\alpha}}{1-\alpha}
\quad\text{almost surely}.
\]
Here all approximations are pathwise for finite positive \(W\); none presupposes boundedness of \(W\) away from zero or infinity uniformly over outcomes.

**Step 5: concentration and joint convergence.** Conditional independence gives
\[
\operatorname{Var}(\widetilde U_{j_N}^{(N)}\mid(\xi_\ell))
\le\mu_N.
\]
Because \(b_N\to\infty\) and \(\mu_N/b_N\) converges almost surely to a finite variable, conditional Chebyshev followed by bounded convergence shows
\[
(\widetilde U_{j_N}^{(N)}-\mu_N)/b_N\xrightarrow{\mathbb P}0.
\]
For any fixed finite collection of indices \(j_{N,i}\), applying this argument coordinatewise on the *same* gap-and-Poisson-process coupling and taking a union bound proves the joint assertion with a single \(W\).

**Step 6: expectation asymptotics, independently checked.** Let \(M_N=\max(E_1,\ldots,E_N)\) for independent \(E_i\sim\operatorname{Exp}(1)\). The exact expected-deficit identity, obtainable from the exponential occupancy integral or by inclusion–exclusion, is
\[
\mathbb E U_{m+1}^{(N)}
=\sum_{a=1}^{N}(-1)^{a+1}\binom Na a^{-m}
=\frac{\mathbb E M_N^m}{m!},\qquad m\ge1.
\]
To check the second equality, expand \(\Pr(M_N>t)=1-(1-e^{-t})^N\) and integrate \(m t^{m-1}\Pr(M_N>t)\). Now \(G_N=M_N-\log N\) converges in distribution to a standard Gumbel variable \(G\), characterized by \(e^{-G}\sim\operatorname{Exp}(1)\). Thus
\[
\frac{\mathbb E U_{m_N+1}^{(N)}}{b_N}
=\mathbb E\left(1+\frac{G_N}{L}\right)^{m_N}
\longrightarrow \mathbb E e^{\alpha G}=\Gamma(1-\alpha).
\]
The exchange of limit and expectation is justified uniformly: on \(G_N<0\), the integrand is bounded by 1; on \(G_N\ge0\), it is bounded by \(e^{\gamma G_N}\) for any fixed \(\alpha<\gamma<1\) and all large \(N\). The elementary bound \(\Pr(G_N>x)\le e^{-x}\) for \(x\ge0\) provides bounded exponential moments at every order below 1 and uniform integrability. This completes the proof.

## Verification

The accompanying standalone `verify.py` checks, using exact rational arithmetic, the equality between the finite alternating-binomial formula and coefficients of the exponential-order-statistic moment generating function for multiple finite \(N\) and \(m\). It separately checks the conditional Poisson lower-tail series, its geometric approximation away from the mean, and the relationship between the claimed limit distribution and its mean. These are diagnostic finite computations; the conclusions for all \(N\) and all admissible index sequences follow from the proof above, not from enumeration.

## Relationship to prior work

Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector* (arXiv:2606.29635v1, first public June 28, 2026), establishes the exact exponential-spacing coupling and joint exponential limits when all sibling indices stay fixed. Its discussion explicitly distinguishes growing sibling indices as outside that theorem's scope. The result here retains Long's coupling but studies \(j_N\) proportional to \(\log N\), requiring uniform moving-index Poisson-tail estimates and producing a different limit law and an exact leading expectation constant. Doumas and Papanicolaou (arXiv:1412.4346) treat expected deficits for fixed sibling indices and general coupon distributions; their later *The Coupon Collector's Brother* (arXiv:2005.05270) proves the exponential limit for the first sibling. Doumas and Spektor (arXiv:2606.21591) address finite-\(N\) expectation extremality over coupon distributions. These published statements do not provide the moving-index distributional theorem. Earlier or unindexed results in the generalized occupancy literature could conceivably imply it; independent priority verification remains necessary.

## Limitations

The result uses equal coupon probabilities, the precise hand-down-of-duplicates model, fixed finite-dimensional joint limits, and strictly subcritical index rates \(0<\alpha_i<1\). The proof does not cover the critical scale \(j_N/\log N\to1\), which has no separating exponent \(\delta\), nor supercritical regimes, rates approaching an endpoint, nonuniform weights, or quantitative convergence errors. The random-limit statement is convergence in probability only under the constructed joint coupling; for the original separate models it entails weak convergence, not an intrinsic across-\(N\) almost-sure assertion. The novelty comparison is necessarily limited to inspected and indexed sources.

## References

1. C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635v1 (first public June 28, 2026). https://arxiv.org/abs/2606.29635
2. A. V. Doumas and V. G. Papanicolaou, *The Siblings of the Coupon Collector*, arXiv:1412.4346 (2014). https://arxiv.org/abs/1412.4346
3. V. G. Papanicolaou and A. V. Doumas, *The Coupon Collector's Brother*, arXiv:2005.05270 (2020). https://arxiv.org/abs/2005.05270
4. A. V. Doumas and S. Spektor, *Equal probabilities maximize the expected deficit in the siblings of the coupon collector*, arXiv:2606.21591 (2026). https://arxiv.org/abs/2606.21591
