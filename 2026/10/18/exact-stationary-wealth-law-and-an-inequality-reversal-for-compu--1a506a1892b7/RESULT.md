# Exact stationary wealth law and an inequality reversal for compulsory unit transfers

## Finding

Consider the synchronous fixed-unit wealth-exchange mean-field model in which every agent with positive integer wealth pays one unit each round, and each payment is independently sent to a uniformly sampled recipient. In the infinite-population Poisson-income approximation, write \(p_j\) for a stationary probability of wealth \(j\ge0\), \(m>0\) for mean wealth, and \(\lambda=1-p_0\) for the fraction of active payers. **There is exactly one stationary probability distribution with each prescribed positive finite mean \(m\).** It has
\[
\lambda(m)=m+1-\sqrt{m^2+1},\qquad p_0(m)=\sqrt{m^2+1}-m,
\]
and probability generating function
\[
P_m(z)=\sum_{j\ge0}p_jz^j
=\frac{(1-\lambda)(1-z)}{1-z\exp[\lambda(1-z)]},\quad |z|\le1,
\]
with the apparent singularity at \(z=1\) removed continuously. Its variance is
\[
\operatorname{Var}(X)=m+\frac{\lambda^4}{4(1-\lambda)^2}+\frac{\lambda^3}{3(1-\lambda)}.
\]
In particular, at the source's normalized mean \(m=1\),
\[
\lambda=2-\sqrt2,\quad p_0=\sqrt2-1,\quad
\operatorname{Var}(X)=\frac43.
\]
The population Gini coefficient, defined by \(G(X)=\mathbb E|X-X'|/(2\mathbb EX)\) for independent identically distributed \(X,X'\), obeys the **strict comparison**
\[
G(X)<\frac23=G(Y),
\]
where \(Y\) has the equal-mean maximum-entropy geometric law \(\Pr(Y=j)=2^{-j-1}\). The calculated value is
\[
0.57992883311<G(X)<0.57992883312.
\]
Thus, with the same standard discrete Gini definition, the model's mean-one equilibrium is *less*, not more, unequal than its stated geometric benchmark. This is a comparison of two specific distributions, not a socioeconomic prediction and not a claim of inequality ordering for all initial states or finite populations.

## Assumptions and scope

Take the deterministic infinite-population map on probability mass functions \(p=(p_j)_{j\ge0}\) with strictly positive conserved mean \(m=\sum_j j p_j<\infty\). Set \(\lambda(p)=1-p_0\). A representative agent's one-step update conditional on the current law is
\[
X_{t+1}=(X_t-1)_++A_t,\qquad
 A_t\mid p(t)\sim\operatorname{Poisson}(\lambda(p(t))),
\]
independent of the agent's old wealth, where \((x)_+=\max(x,0)\). The distributional law reproduces the source's master equation (4) without imposing a finite wealth cutoff. Claims concern stationary solutions of **this Poisson mean-field map**; they do not assert exact finite-population product measures, convergence to equilibrium from every initial condition, or exact values for an agent-based simulation. The source initially fixes \(m=1\); the family \(m>0\) is the same mean-field master equation with another conserved wealth normalization.

## Proof

**1. Reduction to a fixed-arrival queue.** Suppose a stationary law exists and write its self-consistent arrival parameter as \(\lambda\). Since \(m>0\), the chain must have \(0<\lambda<1\). For fixed \(\lambda\) the recursion \(X_{t+1}=(X_t-1)_++A_t\), with independent Poisson arrivals, is the embedded discrete-time single-server unit-service queue. For states \(j\ge1\), the conditional drift is \(\lambda-1<0\), while state zero can reach every integer and has a positive self-loop. The irreducible aperiodic chain is positive recurrent and has a unique stationary law \(\pi_\lambda\), with exponential moments near one (the Poisson moment generating function gives a geometric drift for sufficiently small positive exponential test parameter). These conclusions can also be obtained using standard M/D/1 results, but the generating-function derivation below is direct.

**2. Stationary generating function.** Define \(P(z)=\mathbb E[z^X]\) and \(p_0=\Pr(X=0)\). The wealth immediately after compulsory expenditure has generating function \(p_0+(P(z)-p_0)/z\). Poisson income multiplies this by \(\exp[\lambda(z-1)]\). Hence
\[
P(z)=\exp[\lambda(z-1)]\left(p_0+\frac{P(z)-p_0}{z}\right),
\]
which rearranges to
\[
P(z)=\frac{p_0(1-z)}{1-z\exp[\lambda(1-z)]}.
\]
The expected expenditure at stationarity equals the expected income, so \(1-p_0=\lambda\). Equivalently the removable limit \(P(1)=1\) gives \(p_0=1-\lambda\). This supplies the stated formula.

**3. Exact mean closure and uniqueness.** Set \(h=z-1\). Expansion around \(h=0\) gives
\[
P(1+h)=\frac{(1-\lambda)e^{\lambda h}}
 {1-\lambda-\lambda^2 h/2-\lambda^3 h^2/6+O(h^3)}.
\]
Taking the linear coefficient yields
\[
m=P'(1)=\lambda+\frac{\lambda^2}{2(1-\lambda)}.
\]
Its right-hand side is strictly increasing on \((0,1)\), from zero to infinity. Solving the quadratic gives the unique admissible root \(\lambda=m+1-\sqrt{m^2+1}\). Conversely, for this \(\lambda\) the positive recurrent queue law has mean \(m\) and empty probability \(1-\lambda\); it therefore satisfies the nonlinear self-consistency condition and is a stationary solution. Any other stationary solution of mean \(m\) would have the same \(\lambda\) and coincide with the fixed-arrival queue law. This proves existence and uniqueness for every \(m>0\).

**4. Variance.** Write \(u=\lambda^2/[2(1-\lambda)]\) and \(v=\lambda^3/[6(1-\lambda)]\). The quadratic coefficient in the expansion is \(\lambda^2/2+\lambda u+u^2+v\). As \(m=\lambda+u\), the factorial-moment identity \(\operatorname{Var}(X)=P''(1)+m-m^2\) simplifies to
\[
\operatorname{Var}(X)=m+u^2+2v.
\]
For \(m=1\), \(\lambda=2-\sqrt2\) and \(u=\sqrt2-1\), giving \(\operatorname{Var}(X)=4/3\) by exact substitution. For comparison, the geometric law of mean one has variance two.

**5. Gini ordering.** For any two independent nonnegative integer-valued random variables \(X,X'\) with identical mean \(m>0\),
\[
\mathbb E\min(X,X')=\sum_{j\ge1}\Pr(X\ge j)^2,\qquad
G(X)=1-\frac1m\sum_{j\ge1}\Pr(X\ge j)^2.
\]
When \(m=1\), \(\Pr(X\ge1)=\lambda=2-\sqrt2\) and
\[
\lambda^2=6-4\sqrt2>\frac13;
\]
the inequality follows, for example, from \(\sqrt2<17/12\). The other nonnegative terms in the survival sum give
\[
G(X)\le1-\lambda^2<\frac23.
\]
For the geometric benchmark \(\Pr(Y\ge j)=2^{-j}\), whence \(G(Y)=1-\sum_{j\ge1}4^{-j}=2/3\), exactly. This uses the same integer-valued Gini normalization for both laws.

**6. Explicit numerical enclosure.** The stationary probabilities are generated without truncating the chain by \(p_0=1-\lambda\), \(p_1=p_0(e^{\lambda}-1)\), and, for \(k\ge1\),
\[
p_{k+1}=e^{\lambda}p_k-(p_0+p_1)\frac{\lambda^k}{k!}
-\sum_{j=2}^{k}p_j\frac{\lambda^{k-j+1}}{(k-j+1)!}.
\]
Write \(S_j=1-\sum_{i=0}^{j-1}p_i\). The finite sum \(1-\sum_{j=1}^{K}S_j^2\) is an upper bound on \(G(X)\). Since \(\lambda=2-\sqrt2<\log2\), the generating function is finite at two and gives
\[
B=\mathbb E[2^X]=\frac{1-\lambda}{2e^{-\lambda}-1}.
\]
Markov's inequality and a geometric sum give the complementary **analytic** truncation bound
\[
0\le\left(1-\sum_{j=1}^{K}S_j^2\right)-G(X)
\le\frac{B^2}{3\cdot4^K}.
\]
At \(K=35\) this bound, combined with high-precision coefficient arithmetic, gives the displayed decimal enclosure. The independent source-included checker implements the recurrence and tail bound.

## Verification

Run \(\texttt{python3 check.py}\) with the Python standard library. It checks the exact mean and variance relations to high decimal precision; constructs 36 stationary coefficients by recurrence; checks the stationary transition identities, the generating function at two interior points, and the Gini enclosure with the analytic tail uncertainty. The program passes these checks. Symbolic algebra and finite decimal calculations are not substitutes for the infinite-state positive-recurrence and generating-function arguments in this proof.

## Relationship to prior work

Liuh (arXiv:2511.08202v1, publicly available 2025-11-11), Sections 2–5, defines the synchronous fixed-payment process and derives the Poisson mean-field master equation. The paper reports a stationary numerical wealth law and compares its numerical Gini to a geometric maximum-entropy benchmark, but does not establish the above self-consistent exact rate, full generating function, variance, or exact like-for-like Gini ordering.

The **fixed-\(\lambda\) queue law is classical**, not claimed as new. Published M/D/1 work, including Nakagawa (2005), gives explicit queue stationary probabilities. The additional model-specific step is the conserved-mean **self-consistency equation**, followed by a strict Gini comparison to the *particular benchmark used in the economic model*. Sakagawa (arXiv:2501.02490v1, 2025-01-05) treats distinct immediate-exchange and uniform-saving coin-transfer systems, whose update rules are not the simultaneous unit-payment rule. Standard probability-generating functions and queue theory are used with attribution; the contribution is the complete analytic resolution and inequality comparison for the cited economic model, not a new queueing identity.

## Limitations

The proof concerns the infinite-population Poisson mean-field closure, not a rigorous interchange of finite-population and long-time limits. It proves uniqueness of fixed points for prescribed mean, not global convergence of every nonlinear orbit. The Gini reversal is rigorously proved at the source's mean-one normalization; the statement does not assert an all-mean Gini order. Interpretation depends on comparing the explicitly stated integer-geometric reference using the **standard** Gini definition. Previously known M/D/1 stationary-distribution formulas cover the fixed-rate queue component; the precise novelty lies in the coupling to the wealth model and the model-specific economic comparison. A more direct prior analysis of this same synchronous transfer process remains possible.

## References

1. J. Liuh, *How Fixed-Amount Transactions and Liquidity Constraints Amplify Wealth Inequality: A Kinetic Model Deviating from the Maximum Entropy Benchmark*, arXiv:2511.08202v1 (2025-11-11), https://arxiv.org/html/2511.08202v1 .
2. K. Nakagawa, *On the Series Expansion for the Stationary Probabilities of an M/D/1 Queue*, Journal of the Operations Research Society of Japan **48** (2005), 111–122, DOI:10.15807/jorsj.48.111.
3. H. Sakagawa, *Limiting Distributions of Generalized Money Exchange Models*, arXiv:2501.02490v1 (2025-01-05), https://arxiv.org/abs/2501.02490 .
