# A universal narrow-season incubation optimum for stochastic star epidemics

## Finding

**Theorem (single-window incubation optimum).** For every integer \(m\geq1\), rates \(\beta,\gamma>0\), and transmission window \(0<a<b<\infty\), consider the stochastic star epidemic defined below. For **every** nonconstant, nondecreasing utility \(U:\{0,\ldots,m\}\to\mathbb R\), the expected utility \(F_U(\sigma)=\mathbb E_\sigma[U(K)]\) of the number \(K\) of infected leaves has exactly one maximizer \(\sigma_U\in(0,\infty)\). It increases strictly before \(\sigma_U\) and decreases strictly afterward. In particular, the optimum strictly improves on both the vanishing incubation-progression limit and the immediately infectious limit.

Further, fix \(m,a,\beta,\gamma,U\) and set \(w=b-a\). As \(w\downarrow0\), all the optimal rates \(\sigma_U\) converge to the same positive value \(\sigma_0=\sigma_0(a,\gamma)\), characterized by the strictly monotone equation
\[
\gamma\int_0^a(a-u)e^{(\sigma_0-\gamma)u}\,du=a.
\]
This limit is independent of leaf count, transmission intensity, and the choice of monotone nonconstant outbreak-size utility. This includes the expected number of infections and the probability of at least any prescribed number of infections.

## Assumptions and scope

There is one central individual (root) and \(m\geq1\) initially susceptible peripheral individuals (leaves). At time zero the root is **exposed, not infectious**. It progresses from exposed to infectious after an independent exponential time \(L\sim\operatorname{Exp}(\sigma)\), \(\sigma>0\). After progression it recovers after a further independent \(R\sim\operatorname{Exp}(\gamma)\), \(\gamma>0\). The root transmits to each still susceptible leaf by independent Poisson processes of rate \(\beta>0\), but **only during** the absolute time window \([a,b]\) with \(0<a<b<\infty\). No other transmission is possible; leaves are terminal cases. Infection of a leaf is counted once, regardless of its later clinical transitions. Let \(K\) be the eventual number of leaves infected. The infectious recovery clock is independent of all contact clocks and the latent clock. No vaccination, reinfection, disease mortality during exposure, or secondary onward transmission is assumed.

The utility \(U\) is any nonconstant function on the attainable integers \(0,1,\ldots,m\) with \(U(k)\ge U(k-1)\). It need not be linear, convex, or strictly increasing at every integer. All conclusions are exact for fixed finite \(m\) and finite \(w=b-a>0\).

## Proof

**1. Excess utility from a fresh infectious root.** Put \(\Delta_k=U(k)-U(k-1)\geq0\). At least one \(\Delta_k\) is positive. For a root just becoming infectious at the beginning of a window of length \(z\), let
\[
Q_k(z)=\Pr\bigl(\operatorname{Bin}(m,1-e^{-\beta\min(R,z)})\geq k\bigr),\qquad
Q_U(z)=\sum_{k=1}^{m}\Delta_k Q_k(z).
\]
Here the binomial law is understood conditional on the single shared recovery duration \(R\), and is then averaged over \(R\). Since \(U(K)=U(0)+\sum_{k=1}^m\Delta_k\mathbf1_{\{K\geq k\}}\), \(Q_U(z)\) is the expected excess utility. Differentiate with respect to the end of the transmission window, conditioning on whether the root remains infectious at time \(z\). For \(z>0\),
\[
Q_k'(z)=m\binom{m-1}{k-1}\beta e^{-[\gamma+\beta(m-k+1)]z}\bigl(1-e^{-\beta z}\bigr)^{k-1}.
\]
Thus \(Q_U(0)=0\) and \(Q_U'(z)>0\) for every \(z>0\), even when utility has zero increments at some counts. The formula includes the correlation between infections of different leaves through the shared recovery time; the marginal independence approximation is not used.

**2. Conditioning on latent time.** Write \(w=b-a\) and \(q=Q_U(w)>0\). If latency ends at \(0\leq l<a\), the root must survive to time \(a\), with probability \(e^{-\gamma(a-l)}\); the remaining infectious lifetime is again exponential. If \(a\leq l<b\), the available window has length \(b-l\). Hence the exact conditional excess is the continuous function
\[
g(l)=\begin{cases}
e^{-\gamma(a-l)}q,&0\leq l<a,\\
Q_U(b-l),&a\leq l<b,\\
0,&l\geq b.
\end{cases}
\]
The two expressions agree at \(l=a\). The expected utility is
\[
F_U(\sigma)=U(0)+\int_0^b\sigma e^{-\sigma l}g(l)\,dl.
\]
This conditioning formula can also be used directly to compute outbreak-size tails \(\Pr(K\geq k)\) by taking \(U(j)=\mathbf1_{\{j\geq k\}}\).

**3. A one-crossing derivative.** Because \(g(b)=0\) and \(g\) is piecewise continuously differentiable, integration by parts yields \(F_U(\sigma)=U(0)+g(0)+\int_0^b e^{-\sigma l}g'(l)\,dl\). Differentiation under the finite integral gives
\[
F_U'(\sigma)=B(\sigma)-A(\sigma),
\]
where
\[
\begin{aligned}
A(\sigma)&=\gamma q\int_0^a l e^{-\gamma(a-l)-\sigma l}\,dl,\\
B(\sigma)&=\int_a^b l e^{-\sigma l}Q_U'(b-l)\,dl.
\end{aligned}
\]
Both are strictly positive. The logarithmic derivative of \(A/B\) is \(\mathbb E_B[l]-\mathbb E_A[l]>0\), with the two expectations taken under their respective normalized positive integrands. This strict inequality follows because the first measure has support in \([a,b]\), whereas the second has support in \([0,a]\), with nonzero interior mass. Thus \(A/B\) is strictly increasing. Moreover,
\[
F_U'(0+)=\int_0^b g(l)\,dl>0,
\]
so \(A(0)<B(0)\). As \(\sigma\to\infty\), \(A(\sigma)\sim \gamma q e^{-\gamma a}/\sigma^2\), while \(B(\sigma)\leq C e^{-\sigma a}\) for some finite \(C>0\). Consequently \(A/B\to\infty\). The intermediate value theorem and strict monotonicity give exactly one \(\sigma_U\) with \(A=B\), with \(F_U'>0\) below and \(F_U'<0\) above. The limiting utilities are \(U(0)\) at \(\sigma\downarrow0\) and \(U(0)+e^{-\gamma a}q\) at \(\sigma\to\infty\); the strict finite maximum exceeds both.

**4. Universal short-window limit.** Let \(r=\min\{k: \Delta_k>0\}\). As \(w\downarrow0\),
\[
q=\Delta_r\binom mr\beta^r w^r+O(w^{r+1})>0.
\]
This follows from the exact binomial tail and the smooth recovery survival factor. Divide \(A=B\) by \(q\). The measure \(Q_U'(z)\,dz/q\) is a probability measure supported on \([0,w]\). Hence, uniformly for \(\sigma\) in any compact subset of \([0,\infty)\),
\[
\begin{aligned}
A(\sigma)/q &=\gamma\int_0^a l e^{-\gamma(a-l)-\sigma l}\,dl,\\
B(\sigma)/q &\longrightarrow a e^{-\sigma a}.
\end{aligned}
\]
After multiplying the limiting crossing equation by \(e^{\sigma a}\) and substituting \(u=a-l\), the equation becomes \(\gamma\int_0^a(a-u)e^{(\sigma-\gamma)u}\,du=a\). Its left side is strictly increasing in \(\sigma\geq0\). At \(\sigma=0\) it equals \(a-(1-e^{-\gamma a})/\gamma<a\); it tends to infinity as \(\sigma\to\infty\). Thus its unique zero is \(\sigma_0>0\). The strict one-crossing property and uniform compact convergence imply \(\sigma_U\to\sigma_0\). This argument applies to every permitted \(U\), irrespective of the value of \(r\). \(\square\)

## Verification

The included stand-alone `verify.py` (standard Python library only) independently integrates the finite continuous-time Markov chain forward equations with states consisting of root state \(E,I,R\) and cumulative number of infected leaves \(0,\ldots,m\). It compares the resulting exact-model numerical probabilities against the conditional one-dimensional formula at sixteen parameter/threshold combinations. It also checks the signs of the stationarity equation, verifies the optimized payoff exceeds the immediately infectious limit, and tests the short-window convergence. Successful output ends with `CHECK_OK`. These finite checks support, but do not replace, the preceding all-parameter proof.

For \(m=4\), \(a=1\), \(b=1.4\), \(\beta=2\), and \(\gamma=1\), the optimizers for utilities \(U(K)=\mathbf1_{\{K\geq k\}}\) for \(k=1,2,3,4\) are approximately \(1.994736\), \(2.171050\), \(2.319641\), and \(2.427796\), respectively. Yet as \(b\downarrow a=1\), their common limit is \(\sigma_0\approx2.7932821329\).

## Relationship to prior work

Hall and Siebert [1] proved exact node-probability equations for Markovian SIR and SEIR dynamics on rooted trees from one initial infected or exposed source, including multistage exposure. Their theory underpins the relevance of exactly solvable tree epidemics, but their primary results treat fixed edge rates and node-level state probabilities, rather than the present transmission pulse, payoff-dependent global optimality, and utility-independent short-window limit. An exact forward equation alone does not assert or imply unimodality as a direct corollary: the one-crossing argument above is needed.

Cocomello and Ramanan [2] study limiting SIR/SEIR processes on locally tree-like graphs, including time-dependent epidemic rates and varying outbreak-size distributions. Their random-graph large-population setting and equations do not state the finite-star all-utility optimum and short-window limit. Seasonal deterministic SEIR threshold studies such as Ma and Ma [3] address invasion criteria, not the stochastic finite-pulse objective optimized here. These comparisons support a differentiated contribution but cannot establish absolute novelty.

## Limitations

Uniqueness is asserted only for an exposed index case with exponentially distributed incubation and recovery, an initially susceptible finite star, constant per-edge transmission intensity during one strictly positive, bounded window, and a nondecreasing nonconstant utility of the final number of leaf infections. If the pulse starts at time zero, the argument for a finite interior optimum fails; this theorem makes no assertion in that case. Multiwave forcing, general graph spread, changing infectiousness, nonexponential waiting times, disease mortality during exposure, and nonmonotone utilities are not covered. The common narrow-window optimum characterizes an asymptotic \(w\downarrow0\) limit and is not an equality of optimal rates for all positive widths. Literature comparisons are not a proof of publication priority. Independent validation has not been performed.

## References

[1] C. L. Hall and B. A. Siebert, “Exact solutions and bounds for network SIR and SEIR models using a rooted-tree approximation,” arXiv:2108.07128v1 (first posted 2021-08-16); *Journal of Mathematical Biology* 86, 22 (2023). https://arxiv.org/abs/2108.07128 ; https://doi.org/10.1007/s00285-022-01854-9 .

[2] J. Cocomello and K. Ramanan, “Exact description of limiting SIR and SEIR dynamics on locally tree-like graphs,” arXiv:2309.08829v1 (2023). https://arxiv.org/abs/2309.08829 .

[3] J. Ma and Z. Ma, “Epidemic threshold conditions for seasonally forced SEIR models,” *Mathematical Biosciences and Engineering* 3 (2006). https://doi.org/10.3934/mbe.2006.3.161 .
