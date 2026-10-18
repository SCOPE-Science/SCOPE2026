# An explicit logarithmic-versus-exponential mixing dichotomy for synchronous social response

## Finding
For the synchronous binary-opinion model specified below, **every** finite population with finite sensitivity has a unique stationary distribution, yet its approach to that distribution can change from logarithmic to exponentially slow with the population size. The explicit bounds are uniform over the bias of the common environmental signal.

For \(0<\beta\gamma<2\), write \(c=\beta\gamma/2\). The total-variation mixing time at threshold \(1/4\) obeys
\[
t_{\mathrm{mix}}(1/4)\le\left\lceil\frac{\log(4N)}{-\log c}\right\rceil.
\]
For \(\gamma=0\), mixing occurs in one step.

For \(2/3<\gamma\le1\), choose \(0<\delta<(3\gamma-2)/(2\gamma)\) and finite \(\beta>0\) large enough that
\[
q=\frac{1}{1+\exp(\beta[\gamma(1-2\delta)-2(1-\gamma)])}<\delta.
\]
Then, with the binary relative entropy \(D(\delta\|q)>0\),
\[
t_{\mathrm{mix}}(1/4)\ge\left\lfloor\tfrac14\exp(ND(\delta\|q))\right\rfloor.
\]
These are two proved parameter regimes, **not** a complete phase diagram and not claimed to give optimal exponential constants.

## Assumptions and scope
There are \(N\ge1\) binary agents, all updated synchronously and independently conditional on the current positive count and a **single shared** signal. At each integer time, the environmental signal \(X_t\in\{-1,1\}\) is drawn independently, with \(\mathbb P(X_t=1)=p\in[0,1]\). There is no signal memory. The common opinion-payoff difference at count \(k\) is
\[
\Delta(k,x)=\gamma(2k/N-1)+2(1-\gamma)x.
\]
Each agent's next opinion is positive with probability
\[
s(k,x)=\sigma(\beta\Delta(k,x)),\qquad \sigma(u)=(1+e^{-u})^{-1},
\]
independently of the other agents conditional on \((k,x)\). Hence \(K_{t+1}\mid(K_t=k,X_t=x)\sim\operatorname{Bin}(N,s(k,x))\). We consider finite \(0<\beta<\infty\), \(0\le\gamma\le1\), and the transition operator on counts \(\{0,\ldots,N\}\). Its worst-start total variation mixing time is the minimum nonnegative integer \(t\) such that \(\max_k\|P^t(k,\cdot)-\pi\|_{\mathrm{TV}}\le1/4\), where \(\pi\) is the stationary distribution.

## Proof
**Irreducibility and uniqueness.** Both conditional success probabilities \(s(k,1)\) and \(s(k,-1)\) lie strictly between zero and one whenever \(\beta\) is finite. Each conditional binomial distribution assigns positive probability to every next count \(\ell\in\{0,\ldots,N\}\). Their mixture does too (including \(p=0\) and \(p=1\)). Therefore the entire transition matrix is strictly positive. The finite chain is irreducible and aperiodic and has a unique invariant probability.

**Rapid-mixing regime.** The derivative of \(\sigma\) satisfies \(0<\sigma'(u)\le1/4\). For a fixed signal \(x\),
\[
|s(k,x)-s(l,x)|\le\frac{\beta\gamma}{2N}|k-l|.
\]
Couple two copies by using the same signal and the same \(N\) independent uniform random variables to sample the next agents' opinions. Then the expected number of discordant updated agents is exactly \(N|s(k,x)-s(l,x)|\). The difference between the next positive counts is no greater than the number of discordant agents. Averaging gives
\[
\mathbb E[|K' - L'|\mid K=k,L=l]\le c|k-l|,\qquad c=\beta\gamma/2.
\]
Iterating from two deterministic initial counts gives \(\mathbb E|K_t-L_t|\le N c^t\). Since the count difference is integer-valued, \(\mathbb P(K_t\ne L_t)\le N c^t\). Coupling one initial count to a stationary draw yields \(\|P^t(k,\cdot)-\pi\|_{\mathrm{TV}}\le Nc^t\), uniformly in \(k\) and \(p\), proving the upper bound. At \(\gamma=0\), the next-count law depends only on the current signal, not on the incoming count, so all starts share exactly the same distribution after one step; that law is stationary.

**Slow-mixing regime.** Fix \(2/3<\gamma\le1\) and the stated \(\delta,\beta\). Define \(A=\{k:k/N\ge1-\delta\}\), \(B=\{k:k/N\le\delta\}\); they are disjoint because \(\delta<1/2\). For every count \(k\in A\) and signal \(x\in\{-1,1\}\),
\[
\Delta(k,x)\ge\gamma(1-2\delta)-2(1-\gamma)>0.
\]
Consequently, the conditional number of negative opinions after one step is stochastically dominated by \(\operatorname{Bin}(N,q)\). The Chernoff–Cramér inequality gives
\[
\mathbb P(K_{t+1}\notin A\mid K_t\in A)\le \exp[-ND(\delta\|q)]=:\epsilon_N,
\]
where \(D(a\|b)=a\log(a/b)+(1-a)\log((1-a)/(1-b))\). The same argument with opinions reversed shows \(\mathbb P(K_{t+1}\notin B\mid K_t\in B)\le\epsilon_N\). Each assertion is uniform in the shared signal, and hence in its bias \(p\). Starting from the unanimous-positive and unanimous-negative configurations, the union bound yields respectively \(\mathbb P_N(K_t\in A)\ge1-t\epsilon_N\) and \(\mathbb P_0(K_t\in B)\ge1-t\epsilon_N\). Since \(A\cap B=\varnothing\),
\[
\|P^t(N,\cdot)-P^t(0,\cdot)\|_{\mathrm{TV}}\ge1-2t\epsilon_N.
\]
If \(t<\exp[ND(\delta\|q)]/4\), this total variation distance exceeds \(1/2\). By the triangle inequality, at least one initial distribution is then more than \(1/4\) from stationarity. Thus the stated integer lower bound holds.

## Verification
A standalone checker, `verify.py`, evaluates the actual finite transition matrices and the claimed inequalities for representative rational parameters. It reconstructs the stochastic kernel, checks positivity and row sums, implements the common-uniform coupling coefficient, and tests the transition-tail Chernoff comparison, plus the explicit admissibility certificate \(\gamma=4/5\), \(\delta=1/10\), \(\beta=20\). These computations supplement, rather than replace, the quantified analytic proof above.

## Relationship to prior work
De Domenico, Caccioli, and Livan (2025) introduced the same synchronous peer-influence model with a common random signal and described an apparent finite-horizon ergodicity-breaking transition. Their work analyzes high-sensitivity thresholds and finite-time simulations. The present result bounds worst-case **mixing time as a function of population size at fixed finite sensitivity**, showing rigorously that unique stationarity and exponentially persistent, initially opposite consensus states are compatible. Standard path-coupling and binomial large-deviation inequalities are the underlying proof techniques; they are not claimed as novel. Classical mean-field Ising mixing research generally treats a different single-site transition mechanism, without an independently drawn common signal at each synchronous step.

## Limitations
Neither bound is a matching, optimal asymptotic mixing constant. The sufficient rapid-mixing criterion and the sufficient slow-mixing criterion leave an unclassified parameter region, and no necessity is claimed. The result is restricted to independent conditional synchronous agent decisions with an i.i.d. shared binary signal and finite sensitivity. It does not analyze general networks, correlated per-agent decisions, or memory-averaged signals. It does not imply persistent nonergodicity for any finite population under these hypotheses.

## References
1. F. De Domenico, F. Caccioli, G. Livan, *Peer influence breaks ergodicity in an opinion dynamics model with external information*, arXiv:2507.06661v1 (first posted 2025-07-09), Sections 2–4 and Appendix A, https://arxiv.org/html/2507.06661v1.
2. J. Ding, E. Lubetzky, Y. Peres, *The mixing time evolution of Glauber dynamics for the mean-field Ising model*, Communications in Mathematical Physics 2010, arXiv:0806.1906. Different (asynchronous single-site) chain, useful comparison for exponential mixing-time regimes.
3. The standard common-randomness coupling inequality and the binomial Chernoff–Cramér bound; reproduced directly in the proof above.
