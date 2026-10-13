# Sharp cover-time laws and a log-gamma-to-Gaussian transition for steered bipartite walks

## Finding
Let \(K_{m,m}\), \(m\geq 2\), be a complete bipartite graph, and start a walk at any vertex. At each step, independently, with probability \(1-\varepsilon\) the walk chooses a uniform random neighbor and with probability \(\varepsilon\) a history-dependent controller may choose any neighbor. Let \(\tau\) be its vertex-cover time. For every \(\varepsilon\in[0,1]\), the strategy that always chooses an as-yet-unvisited neighbor when one is available **stochastically minimizes** \(\tau\) among all adaptive, possibly randomized, strategies.

Define \(p_{m,k}=\varepsilon+(1-\varepsilon)k/m\) for \(1\leq k\leq m\). Let \(G_{m,k}\) be independent geometric random variables supported on \(\{1,2,\ldots\}\) with success probabilities \(p_{m,k}\), put \(S_m=\sum_{k=1}^{m}G_{m,k}\), and write \(F_m(j)=\Pr(S_m\leq j)\) for integral \(j\). Under the optimal strategy the **complete, finite-size cover-time law** is, for all integers \(j\geq1\),
\[
\Pr(\tau\leq 2j-1)=F_m(j)^2,\qquad
\Pr(\tau\leq 2j)=F_m(j)F_m(j+1).
\]
Moreover, for \(|z|\) in the product's convergence disk,
\[
\mathbb E[z^{S_m}]=\prod_{k=1}^{m}\frac{p_{m,k}z}{1-(1-p_{m,k})z}.
\]

There is a sharp **vanishing-intervention crossover**. If \(\varepsilon_m\to0\), \(m\varepsilon_m\to c\in[0,\infty)\), and \(H_1,H_2\) are independent \(\operatorname{Gamma}(c+1,1)\) variables (shape and rate), then
\[
\frac{\tau_{m,\varepsilon_m}}{2m}-\log m
\ \Longrightarrow\ \max\{-\log H_1,-\log H_2\}.
\]
The limiting cumulative distribution function at \(x\in\mathbb R\) is
\[
\left[\frac{\Gamma(c+1,e^{-x})}{\Gamma(c+1)}\right]^2,
\]
with \(\Gamma(a,y)=\int_y^\infty t^{a-1}e^{-t}\,dt\). At \(c=0\) it is \(\exp(-2e^{-x})\), a standard Gumbel shifted by \(\log2\).

If instead \(\varepsilon_m\to0\) and \(m\varepsilon_m\to\infty\), define the **exact** one-side centering and variance
\[
\mu_m=\sum_{k=1}^{m}\frac1{p_{m,k}},\qquad
\sigma_m^2=\sum_{k=1}^{m}\frac{1-p_{m,k}}{p_{m,k}^2}.
\]
Then \(\sigma_m^2\sim m/\varepsilon_m\), and for independent standard normal \(Z_1,Z_2\),
\[
\frac{\tau_{m,\varepsilon_m}-2\mu_m}{2\sigma_m}
\ \Longrightarrow\ \max\{Z_1,Z_2\},
\qquad \Pr(\max\{Z_1,Z_2\}\leq x)=\Phi(x)^2.
\]
The **one-side** limit is Gaussian; the **whole cover time** has the maximum-of-two-Gaussians law, not a Gaussian law.

## Assumptions and scope
The graph is a simple balanced biclique. All uncontrolled neighbor choices, steering opportunities and controller randomizations are generated with independent randomness as appropriate. The controller may inspect the entire walk history but has no power on uncontrolled steps. A geometric variable counts its successful trial. The probability statements above concern the optimal policy; every other admissible policy has cover time stochastically no smaller. The exact finite law includes both \(\varepsilon=0\) and \(\varepsilon=1\); both limiting assertions concern \(\varepsilon_m\to0\).

## Proof
**1. Pathwise optimality.** The walk alternates sides deterministically, regardless of strategy. Suppose \(k\) vertices on the side about to be entered have not yet been visited. On its next visit to that side, the probability of discovering a new vertex under any strategy lies in
\[
\left[(1-\varepsilon)\frac{k}{m},\,\varepsilon+(1-\varepsilon)\frac{k}{m}\right].
\]
The upper endpoint is attained by choosing an unvisited neighbor whenever available. Consider on a common probability space the unvisited counts for a greedy walk and an arbitrary controlled walk, separately for each side, updated at the same (alternating) instants. Initially both counts agree. When both counts agree at \(k\), use a common uniform random variable to couple the next-step success Bernoulli indicators; the arbitrary policy's success threshold is no larger than the greedy threshold, so the greedy count remains no greater. When greedy has \(i<j\) unvisited vertices and the other process has \(j\), each count falls by at most one, so their order cannot reverse. This inductively yields coordinatewise ordering of unvisited counts at all times. Hence the greedy cover time is no greater almost surely in this coupling, proving the claimed stochastic optimality even against fully history-dependent randomization.

**2. Exact independent coupon clocks.** Start on side \(A\). On the \(j\)-th visit to side \(B\), at time \(2j-1\), the greedy missing-count chain decreases with probability \(p_{m,k}\) from state \(k\). On side \(A\), whose start vertex is already marked, the same chain starts at state \(m-1\) and evolves at even times \(2j\). Independent step randomness on the odd and even subsequences makes the two completion clocks independent. By memorylessness of independent Bernoulli trials at each missing-count level, the \(B\)-clock has law \(S_m\). Since \(p_{m,m}=1\), the \(A\)-clock has law \(S_m-1\), independently. Thus
\[
\tau\ \stackrel{d}=\ \max\{2S_m^{(B)}-1,\,2(S_m^{(A)}-1)\},
\]
where the two superscripted sums are independent and each has law \(S_m\). The odd- and even-horizon formulas follow by integer inequalities. The PGF follows by multiplying the geometric PGFs.

**3. Critical log-gamma law.** Suppose \(m\varepsilon_m\to c<\infty\); then eventually \(\varepsilon_m<1\). Write
\[
a_m=\frac{m\varepsilon_m}{1-\varepsilon_m},\qquad
\delta_m(s)=\frac{m(e^{s/m}-1)}{1-\varepsilon_m}.
\]
Using the geometric Laplace transform yields, for every real \(s\) in a sufficiently small fixed interval containing zero,
\[
\begin{aligned}
\mathbb E\exp\{-sS_m/m\}
&=\prod_{k=1}^{m}\frac{k+a_m}{k+a_m+\delta_m(s)}\\
&=\frac{\Gamma(m+1+a_m)\Gamma(1+a_m+\delta_m(s))}{\Gamma(1+a_m)\Gamma(m+1+a_m+\delta_m(s))}.
\end{aligned}
\]
Here \(a_m\to c\), \(\delta_m(s)\to s\), and \((s-\delta_m(s))\log m\to0\), since \(\varepsilon_m=O(m^{-1})\). The uniform gamma-ratio estimate on compact parameter sets therefore gives
\[
\mathbb E\exp\{-s(S_m/m-\log m)\}\longrightarrow
\frac{\Gamma(c+1+s)}{\Gamma(c+1)}
=\mathbb E[H^s],\qquad H\sim\operatorname{Gamma}(c+1,1).
\]
The convergence of moment-generating functions around zero implies \(S_m/m-\log m\Rightarrow-\log H\). Independence of the two side clocks and the continuous mapping theorem give the asserted limit for \(\tau\). The upper-incomplete-gamma distribution formula follows from \(\{-\log H\leq x\}=\{H\geq e^{-x}\}\). At \(c=0\), \(H\) is exponential and the maximum of two such log-exponentials has distribution \(\exp(-2e^{-x})\).

**4. The Gaussian-components regime.** Suppose \(\varepsilon_m\to0\) and \(m\varepsilon_m\to\infty\). The centered independent geometric increments have total variance \(\sigma_m^2\). For every \(0<\varepsilon\leq1/2\), monotone integral comparisons, with \(p_{m,k}=\varepsilon+(1-\varepsilon)k/m\), give
\[
\sum_{k=1}^{m}p_{m,k}^{-2}=\frac m\varepsilon+O(\varepsilon^{-2}),
\qquad
\sum_{k=1}^{m}p_{m,k}^{-1}=O\!\left(m\log\frac1\varepsilon+\varepsilon^{-1}\right).
\]
The first identity follows from the exact integral \(\int_0^m[\varepsilon+(1-\varepsilon)x/m]^{-2}dx=m/\varepsilon\). Hence \(\sigma_m^2\sim m/\varepsilon_m\). A geometric variable with success probability \(p\) has third absolute centered moment at most \(C p^{-3}\) for a universal \(C\), and further monotone integration gives
\[
\sum_{k=1}^{m}p_{m,k}^{-3}=O\!\left(\frac{m}{\varepsilon_m^2}+\frac1{\varepsilon_m^3}\right).
\]
Consequently, the normalized Lyapunov ratio is
\[
\frac{\sum_{k=1}^{m}\mathbb E|G_{m,k}-\mathbb EG_{m,k}|^3}{\sigma_m^3}
=O\!\left((m\varepsilon_m)^{-1/2}+(m\varepsilon_m)^{-3/2}\right)\longrightarrow0.
\]
Lyapunov's central limit theorem gives \((S_m-\mu_m)/\sigma_m\Rightarrow N(0,1)\). The two completion clocks are independent, \(\sigma_m\to\infty\), and their integer start offsets are negligible; the continuous mapping theorem finishes the proof for their maximum.

## Verification
The standalone, dependency-free `verify.py` checks independent exact finite-horizon dynamic programming against the two-parity CDF, exact rational geometric-convolution coefficients against the coupon-clock law, and representative finite-size gamma-transform approximations. It reports 906 successful checks using Python standard-library arithmetic. These checks diagnose normalization and indexing; the claims for all \(m\) and all parameter sequences are proved analytically above.

## Relationship to prior work
Bukh and Dubroff, *Faster random walks via infrequent steering* (arXiv:2605.18712v1; May 18, 2026), study optimal adaptive steering and obtain graph-uniform cover-time bounds via efficient graph decompositions. Haslegrave, Sauerwald and Sylvester, *Time Dependent Biased Random Walks* (arXiv:2006.02475), establish general cover/hitting-time bounds and computational hardness for optimal policies. Olesker-Taylor, Sauerwald and Sylvester, *Time-Biased Random Walks and Robustness of Expanders* (arXiv:2412.13109), give expander cover-time bounds, including vanishing-bias obstructions. These results do not supply the stated biclique-specific optimal distribution or the crossover laws.

Nakata and Kubo, *A coupon collector's problem with bonuses* (DMTCS 2006, doi:10.46298/dmtcs.3515), previously established a Gumbel-to-normal classification for a **different** bonus mechanism: drawing a distinguished bonus coupon triggers an additional coupon, possibly recursively. Their waiting-time law and critical scale differ from the model here, whose controlled steps force one currently unseen neighbor, with success probability affine in the remaining-count \(k\). The present claim does not assert novelty of standard geometric waiting-time decompositions, the ordinary Gumbel coupon limit, or the Lyapunov theorem themselves.

## Limitations
The exact optimality and distributional law are proved only for complete bipartite graphs with equal part sizes and the specified stepwise steering access. The crossover concerns interventions tending to zero; the exact finite-size formula, but not a separate limiting theorem here, covers fixed positive intervention probabilities. No analogous result is claimed for unbalanced bipartite or general regular graphs. The classification describes distributional limits, not quantitative convergence rates or tail uniformity. A separate independent mathematical audit has not been carried out.

## References
1. B. Bukh and Q. Dubroff, *Faster random walks via infrequent steering*, arXiv:2605.18712v1 (2026), https://arxiv.org/html/2605.18712v1.
2. J. Haslegrave, T. Sauerwald and J. Sylvester, *Time Dependent Biased Random Walks*, arXiv:2006.02475 (2020), https://arxiv.org/html/2006.02475v2.
3. S. Olesker-Taylor, T. Sauerwald and J. Sylvester, *Time-Biased Random Walks and Robustness of Expanders*, arXiv:2412.13109 (2024), https://arxiv.org/html/2412.13109v1.
4. T. Nakata and I. Kubo, *A coupon collector's problem with bonuses*, DMTCS Proceedings AG (2006), 215–224, doi:10.46298/dmtcs.3515, https://dmtcs.episciences.org/articles/3515.
5. N. Tung and R. Ueltzen, *On efficient graph covers and steered random walks*, arXiv:2607.25016v1 (2026), https://arxiv.org/abs/2607.25016.
