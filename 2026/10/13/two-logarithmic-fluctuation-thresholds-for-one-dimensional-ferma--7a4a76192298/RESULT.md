# Two logarithmic fluctuation thresholds for one-dimensional Fermat distances

## Finding

Let \(N\ge 2\), let \(N-1\) points be sampled independently and uniformly from \([0,1]\), and let \(\Delta_1,\ldots,\Delta_N\) be the successive spacings, including those adjacent to \(0\) and \(1\). For \(\alpha\ge1\), set
\[
D_{N,\alpha}=\sum_{j=1}^{N}\Delta_j^\alpha,
\qquad R_{N,\alpha}=D_{N,\alpha}/\mathbb E D_{N,\alpha},
\qquad C_{N,\alpha}^2=\operatorname{Var}(D_{N,\alpha})/(\mathbb E D_{N,\alpha})^2.
\]
Write \(L=\log N\). The two thresholds are distinct:

1. For every fixed \(c\in(0,1)\), at \(\alpha=cL\), \(R_{N,\alpha}\to1\) in probability; for every fixed \(c>1\), \(R_{N,\alpha}\to0\) in probability. The full boundary window has the explicit profile
\[
\alpha=L+s\sqrt L\quad\Longrightarrow\quad
R_{N,\alpha}\xrightarrow{\mathbb P}\Phi(-s)
\qquad (s\in\mathbb R\text{ fixed}),
\]
where \(\Phi\) is the standard normal distribution function.

2. For every fixed \(c>0\) with \(\alpha=cL\),
\[
C_{N,\alpha}^2\sim\frac{4^\alpha}{N\sqrt{\pi\alpha}}.
\]
More sharply, for each fixed real \(x\),
\[
\alpha=\frac{L+\tfrac12\log L}{\log4}+x
\quad\Longrightarrow\quad
C_{N,\alpha}^2\longrightarrow4^x\sqrt{\frac{\log4}{\pi}},
\qquad R_{N,\alpha}\xrightarrow{\mathbb P}1.
\]
In particular, for every \(1/\log4<c<1\), the relative fluctuations converge to zero in probability while their squared coefficient of variation diverges to infinity. Thus the variance threshold and the typical-sample concentration threshold do not coincide.

## Assumptions and scope

All observations are independent and uniform on the unit interval, the endpoints are inserted to form the \(N\) gaps, and the exponent may vary with \(N\) exactly as specified. The statements concern the full one-dimensional monotone-path Fermat distance, not a higher-dimensional shortest path or nonuniform sampling. Logs are natural; all asymptotics are as integers \(N\to\infty\), and \(\alpha\ge1\) holds eventually in every regime displayed.

## Proof

**Exact moments.** The vector of gaps is Dirichlet with \(N\) unit shape parameters. For every \(\alpha>0\), Dirichlet integration gives
\[
\mathbb E D_{N,\alpha}
=\frac{N\Gamma(N)\Gamma(1+\alpha)}{\Gamma(N+\alpha)},
\quad
\mathbb E D_{N,\alpha}^2
=\frac{\Gamma(N)}{\Gamma(N+2\alpha)}
\bigl[N\Gamma(1+2\alpha)+N(N-1)\Gamma(1+\alpha)^2\bigr].
\]
Put \(B_\alpha=\Gamma(1+2\alpha)/\Gamma(1+\alpha)^2\). An exact simplification is
\[
1+C_{N,\alpha}^2
=\frac{\Gamma(N+\alpha)^2}{\Gamma(N)\Gamma(N+2\alpha)}
\left(1+\frac{B_\alpha-1}{N}\right).
\tag{1}
\]
For \(\alpha=O(\log N)\), uniform Taylor expansion of \(\log\Gamma\) about \(N\) yields
\[
\log\frac{\Gamma(N+\alpha)^2}{\Gamma(N)\Gamma(N+2\alpha)}
=-\frac{\alpha^2}{N}+O\!\left(\frac{\alpha^2+\alpha^3}{N^2}\right).
\]
Stirling's formula gives \(B_\alpha\sim4^\alpha/\sqrt{\pi\alpha}\) whenever \(\alpha\to\infty\). If \(\alpha=cL\) with fixed \(c>0\), then \(B_\alpha\gg\alpha^2\) and (1) implies \(C_{N,\alpha}^2\sim B_\alpha/N\). The shifted critical-window formula follows upon substituting \(\alpha=(L+\tfrac12\log L)/\log4+x\).

**Exponential representation and normalization.** Let \(E_1,\ldots,E_N\) be independent unit-rate exponential random variables, \(T=\sum_j E_j\), \(W=\sum_j E_j^\alpha\), and \(\mu=N\Gamma(1+\alpha)=\mathbb EW\). Then \((\Delta_1,\ldots,\Delta_N)\) has the law of \((E_1/T,\ldots,E_N/T)\), hence \(D_{N,\alpha}=T^{-\alpha}W\) in distribution. Since \(T/N=1+O_{\mathbb P}(N^{-1/2})\), for \(\alpha=O(\log N)\) we have \((N/T)^\alpha\to1\) in probability. Also \(\mathbb ED_{N,\alpha}/(N^{-\alpha}\mu)\to1\), by the same gamma-ratio expansion. It therefore suffices to find the probability limit of \(W/\mu\).

**Fixed logarithmic ratios below one.** If \(\alpha=cL\) with \(0<c\le1/\log4\), the just-proved second-moment estimate gives \(C_{N,\alpha}^2\to0\), proving concentration in probability. For \(1/\log4<c<1\), choose a fixed \(b>1\) sufficiently close to \(1\) so that \(b<2c\) and
\[
g_c(b)=2c\log(b/c)+2c-b-1<0;
\]
such a choice exists because \(g_c(1)=2[c(1-\log c)-1]<0\) for \(c<1\). Truncate \(W\) to \(W_- =\sum_j E_j^\alpha\mathbf1_{\{E_j\le bL\}}\). Exponential tilting shows
\[
\frac{\mathbb E(W-W_-)}\mu
=\Pr\{G_{\alpha+1}>bL\}\longrightarrow0,
\qquad G_{\alpha+1}\sim\operatorname{Gamma}(\alpha+1,1),
\]
by a gamma Chernoff bound, since \(b>c\). Because \(u^{2\alpha}e^{-u}\) is increasing for \(0<u\le bL<2\alpha\),
\[
\frac{\operatorname{Var}(W_-)}{\mu^2}
\le\frac{(bL)^{2\alpha+1}e^{-bL}}{N\Gamma(1+\alpha)^2}
=\exp\{L[g_c(b)+o(1)]\}\longrightarrow0.
\]
Markov's and Chebyshev's inequalities now imply \(W/\mu\to1\) in probability.

**Above one.** If \(\alpha=cL\) with \(c>1\), choose fixed \(1<b<c\). The event \(\max_jE_j\le bL\) has probability tending to one because \(\Pr(\max E_j>bL)\le N^{1-b}\). On this event \(W=\sum E_j^\alpha\mathbf1_{\{E_j\le bL\}}\), whose expectation divided by \(\mu\) equals \(\Pr(G_{\alpha+1}\le bL)\to0\) by a gamma lower-tail Chernoff bound. Markov's inequality proves \(W/\mu\to0\) in probability.

**The \(\sqrt{\log N}\) boundary profile.** Fix \(s\in\mathbb R\), set \(\alpha=L+s\sqrt L\), choose fixed \(K>0\), and put \(a=L-K\log L\), \(b=L+K\log L\). Decompose \(W=W_-+W_0+W_+\) by \(E_j\le a\), \(a<E_j\le b\), and \(E_j>b\). The gamma central limit theorem gives
\[
\mathbb EW_-/\mu=\Pr(G_{\alpha+1}\le a)\longrightarrow\Phi(-s),
\qquad \mathbb EW_0/\mu=\Pr(a<G_{\alpha+1}\le b)\longrightarrow0.
\]
For large \(N\), \(a<2\alpha\). The increasing-integrand bound above and Stirling's formula give
\[
\frac{\operatorname{Var}(W_-)}{\mu^2}
\le\frac{a^{2\alpha+1}e^{-a}}{N\Gamma(1+\alpha)^2}
=O(L^{-K})\longrightarrow0.
\]
Moreover \(\Pr(W_+>0)\le N e^{-b}=L^{-K}\to0\). Chebyshev for \(W_-\) and Markov for \(W_0\) therefore establish \(W/\mu\to\Phi(-s)\) in probability. Normalizing by \(T\) completes the proof.

## Verification

The accompanying dependency-free `verify.py` independently evaluates the integer-exponent Dirichlet moment identities, the two-gap beta integral, the quadratic-spacing closed form, and the critical coefficient-of-variation numerics. It does not establish the infinite-parameter limits; those follow from the explicit gamma and exponential truncation arguments above.

## Relationship to prior work

Chazal, Ferraris, Groisman, Jonckheere, Pascal and Sapienza (2023) identify the one-dimensional Fermat distance with a sum of uniform-spacings powers, compute fixed-exponent asymptotic mean and variance (Proposition 4.1), and motivate balancing geometry against noise by the coefficient of variation. The exact Dirichlet moments used here are implicit in their appendix. The statements above address a different joint limit in which the power grows logarithmically with the number of samples, exhibit a sharp second-moment crossover with its logarithmic correction, and additionally determine the distinct typical-sample crossover and its normal-distribution profile. Aly (2020) treats weak convergence of weighted uniform-spacing power sums with a **fixed** power, not the growing-power phenomenon.

## Limitations

No quantitative convergence rate, universality for nonuniform sampling, higher-dimensional analog, or distributional limit beyond convergence in probability is established. General earlier theorems for rapidly increasing powers of normalized spacings may cover some formulations; the novelty assessment is bibliographic rather than independent expert priority certification. The second-moment limit cannot be used as a concentration criterion in the logarithmic exponent regime.

## References

- Frédéric Chazal, Laure Ferraris, Pablo Groisman, Matthieu Jonckheere, Frédéric Pascal and Facundo Sapienza, *Choosing the parameter of the Fermat distance: navigating geometry and noise*, arXiv:2311.18663 (first posted 2023-11-30), Section 4.1 and Appendix A. https://arxiv.org/abs/2311.18663
- Emad-Eldin A. A. Aly, *On The Distribution of Partial Sums of Randomly Weighted Powers of Uniform Spacings*, *The Open Mathematics, Statistics and Probability Journal* **10** (2020), 1–7. https://doi.org/10.2174/1876527002010010001
