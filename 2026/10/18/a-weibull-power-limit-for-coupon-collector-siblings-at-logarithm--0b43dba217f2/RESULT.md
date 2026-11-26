# A Weibull-power limit for coupon-collector siblings at logarithmically growing indices

## Finding

Draw independently and uniformly from \(N\) coupon types. For each type, its \(j\)-th occurrence goes to album \(j\). Let \(U_j^{(N)}\) count types missing from album \(j\) at the first completion of album 1. All logarithms are natural. Fix \(r<\infty\) and integer indices \(j_{N,i}\ge2\) with \(m_{N,i}=j_{N,i}-1\) satisfying \(m_{N,i}/\log N\to\alpha_i\in(0,1)\). Put \(b_{N,i}=(\log N)^{m_{N,i}}/m_{N,i}!\). There is a simultaneous coupling on which

\[
\left(\frac{U_{j_{N,i}}^{(N)}}{b_{N,i}}\right)_{i=1}^r
\xrightarrow{\mathbb P}
\left(\frac{W^{1-\alpha_i}}{1-\alpha_i}\right)_{i=1}^r,
\qquad W\sim\operatorname{Exp}(1).
\]

For every single such sequence, writing \(m_N=j_N-1\), \(b_N=(\log N)^{m_N}/m_N!\) and \(\alpha=\lim m_N/\log N\),
\[
\frac{\mathbb E U_{j_N}^{(N)}}{b_N}\longrightarrow\Gamma(1-\alpha).
\]
The marginal limit has distribution function \(1-\exp[-((1-\alpha)x)^{1/(1-\alpha)}]\) for \(x\ge0\) and zero for \(x<0\). The finite-dimensional limits share one exponential variable but are generally nonlinear functions of it.

## Proof

**Simultaneous representation.** Embed the draws as the ordered marks of the superposition of \(N\) independent unit-rate Poisson processes, one per type. Their first arrival times are independent standard exponentials. Counting down from the largest first arrival, successive gaps are independent exponentials with rates \(1,2,\ldots,N-1\), by the exponential order-statistic spacing law. Extend these to an infinite independent sequence \(\xi_\ell\sim\operatorname{Exp}(\ell)\) and set \(S_\ell=\sum_{a=1}^\ell\xi_a\). Given the first arrival times and their ranks, subsequent arrivals for the ranked types are independent unit-rate Poisson processes from their first arrivals. Thus for independent unit-rate Poisson processes \(P_\ell\), independent of the gaps, the vectors across albums at any \(N\) have their original joint laws under the representation
\[
\widetilde U_j^{(N)}=1+\sum_{\ell=1}^{N-1}\mathbf 1\{P_\ell(S_\ell)\le j-2\}.
\]
The final type has only arrived once and contributes 1. This representation uses the same gaps and Poisson processes for every \(N\) and every \(j\).

**Random amplitude.** The centered sums of independent gaps converge almost surely because their variances sum to \(\sum_{\ell\ge1}\ell^{-2}<\infty\). Since \(\sum_{a=1}^\ell1/a-\log\ell\) converges, \(S_\ell-\log\ell\to G\) almost surely. The distribution of \(S_\ell\) is that of the maximum of \(\ell\) independent standard exponentials, again by the spacing law. For fixed \(w>0\), \(\Pr(\ell e^{-S_\ell}>w)=(1-w/\ell)^\ell\) for \(\ell>w\), which tends to \(e^{-w}\). It follows that \(W=e^{-G}\) is standard exponential. In particular \(S_\ell=\log\ell-c+o(1)\) with \(c=\log W\), almost surely, uniformly in \(\ell\ge N^\delta\) for every fixed \(\delta>0\).

**Poisson lower tail.** For \(k\to\infty\), uniformly over \(s>0\) with \(k/s\le\rho<1\),
\[
F_k(s)=\Pr(\operatorname{Pois}(s)\le k)=e^{-s}\frac{s^k}{k!}\frac{1+o(1)}{1-k/s}.
\]
After dividing the finite sum by its last term the summands are \((k)_v/s^v\), where \((k)_v\) denotes the falling factorial. For fixed \(v\), these differ from \((k/s)^v\) by a factor tending to 1, uniformly in \(s\); both tails after any fixed cutoff are bounded by the tail of \(\sum_v\rho^v\). The resulting absolute uniform error is also relative since the geometric sum is at least 1.

**Conditional mean.** Set \(L=\log N\), \(k=m_N-1\), and \(b_N=L^{m_N}/m_N!\). Stirling's formula gives \(\log b_N/L\to\beta=\alpha(1-\log\alpha)\), with \(\alpha<\beta<1\). Fix \(\delta\) with \(\alpha<\delta<\beta\). The final type and all \(\ell\le N^\delta\) contribute \(o(b_N)\) to the conditional mean \(\mu_N\) given the gaps. For \(\ell>N^\delta\), \(k/S_\ell\le\rho<1\) eventually almost surely for a deterministic \(\rho>\alpha/\delta\). On the same event we can replace \(S_\ell\) by \(\log\ell-c\) in the exponent, power, and denominator in the tail estimate, with uniform relative error \(o(1)\); for the power the logarithm of the ratio is \(O(k/(\delta L))\,o(1)=o(1)\). Consequently
\[
\mu_N=(1+o(1))\frac{W}{k!}\int_{\delta L}^{L}
\frac{(t-c)^k}{1-k/(t-c)}\,dt+o(b_N)\qquad\text{almost surely}.
\]
For the sum-to-integral step, as a function of \(u\in[N^\delta,N]\) the summand without constant factors is \(u^{-1}(\log u-c)^k/[1-k/(\log u-c)]\). Its logarithmic derivative is \(O(1/u)\) uniformly on this range for each realized finite \(c\), so the relative change on each unit cell is \(O(N^{-\delta})\). Changing the lower summation boundary by a bounded number of cells is harmless because each corresponding Poisson probability is at most 1 and \(b_N\to\infty\).

Use the endpoint window \([L-\sqrt L,L]\). There \(k/(t-c)\to\alpha\) uniformly. On the whole integration range, \(1/[1-k/(t-c)]\) is uniformly bounded. Since \(k+1=m_N\), the integral of \((t-c)^k\) below \(L-\sqrt L\), divided by \((L-c)^{m_N}/m_N\), is bounded by \(((L-\sqrt L-c)/(L-c))^{m_N}\), which tends to zero because \(m_N/L\to\alpha>0\). The integral of \((t-c)^k\) over the endpoint window is therefore asymptotic to \((L-c)^{m_N}/m_N\). This proves
\[
\frac{\mu_N}{b_N}=(1+o(1))\frac{W}{1-\alpha}\left(1-\frac cL\right)^{m_N}+o(1)
\longrightarrow\frac{W^{1-\alpha}}{1-\alpha}\quad\text{almost surely}.
\]
These estimates are pathwise for a finite \(c=\log W\); no deterministic bound on its absolute value is needed.

**Concentration.** The conditional variance of \(\widetilde U_{j_N}^{(N)}\) is at most \(\mu_N\) by conditional independence. Thus the conditional probability of a deviation from \(\mu_N\) by more than \(\varepsilon b_N\) is at most \(\min(1,\mu_N/(\varepsilon^2b_N^2))\), which tends to zero almost surely. Taking expectations and a finite union bound yields the asserted joint convergence in probability on the same coupling.

**Expected deficit.** Write \(M_N\) for the maximum of \(N\) independent standard exponentials. A unit-rate Poisson process has at most \(m-1\) arrivals by time \(s\) exactly when its \(m\)-th arrival time exceeds \(s\). The density of the latter arrival time is \(e^{-t}t^{m-1}/(m-1)!\). Applying this to the representation, \(S_\ell\) has distribution function \((1-e^{-t})^\ell\); including \(\ell=0\) for the final type and summing the resulting geometric series gives
\[
\mathbb E U_{m+1}^{(N)}=\int_0^\infty\frac{t^{m-1}}{(m-1)!}\left[1-(1-e^{-t})^N\right]dt
=\frac{\mathbb E M_N^m}{m!}
=\sum_{a=1}^N(-1)^{a+1}\binom Na a^{-m}.
\]
The ratio to \(b_N\) is \(\mathbb E(1+G_N/L)^{m_N}\), with \(G_N=M_N-L\) converging in law to the standard Gumbel \(G\). The integrands as functions of \(G_N\) converge uniformly on compact sets to \(e^{\alpha G_N}\). On \(G_N<0\) they are at most 1; on \(G_N\ge0\) they are at most \(e^{\gamma G_N}\) for fixed \(\alpha<\gamma<1\) and all sufficiently large \(N\). By the union bound \(\Pr(G_N>x)\le e^{-x}\) for \(x\ge0\). Taking a power \(p>1\) with \(p\gamma<1\) gives a uniform \(L^p\) bound and hence uniform integrability. The means converge to \(\mathbb E e^{\alpha G}=\mathbb E W^{-\alpha}=\Gamma(1-\alpha)\). This also equals the limit variable's mean \(\Gamma(2-\alpha)/(1-\alpha)\); its distribution function follows directly from the exponential distribution of \(W\).

## Verification

The accompanying `verify.py` checks finite cases of the alternating-binomial mean identity against exponential-order-statistic moments using rational arithmetic. It also illustrates the Poisson lower-tail approximation away from the mean and checks the relation between the marginal limit and its mean. The moving-index limit and the specific dependence across indices are proved analytically above; they are not conclusions of the finite checks.

## Relationship to prior work and limitations

Long [1] uses the exponential-spacing coupling and proves common exponential limits at fixed sibling indices. The distinction here is the growing subcritical index \(m_N\sim\alpha\log N\), which requires an estimate uniform in a moving Poisson cutoff and yields a power of the common exponential variable. Doumas and Papanicolaou [2] give the exact expected-deficit sum for uniform probabilities and fixed-index expectation asymptotics; Papanicolaou and Doumas [3] treat the exponential limit for the first sibling. Doumas and Spektor [4] compare finite-population means over coupon distributions. This theorem concerns only uniform probabilities, strictly subcritical fixed limit ratios, the given album stopping rule, and a fixed finite set of indices. The claimed convergence in probability is for the displayed coupling and does not assert an intrinsic almost-sure limit under unrelated models at different \(N\). No conclusions are drawn at or beyond the critical ratio 1.

## References

1. C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, [arXiv:2606.29635v1](https://arxiv.org/abs/2606.29635v1).
2. A. V. Doumas and V. G. Papanicolaou, *The Siblings of the Coupon Collector*, [arXiv:1412.4346](https://arxiv.org/abs/1412.4346).
3. V. G. Papanicolaou and A. V. Doumas, *The Coupon Collector's Brother*, [arXiv:2005.05270](https://arxiv.org/abs/2005.05270).
4. A. V. Doumas and S. Spektor, *Equal probabilities maximize the expected deficit in the siblings of the coupon collector*, [arXiv:2606.21591](https://arxiv.org/abs/2606.21591).
