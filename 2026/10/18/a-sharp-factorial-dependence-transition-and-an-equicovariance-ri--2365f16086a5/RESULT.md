# A sharp factorial-dependence transition and an equicovariance rigidity point in Ewens cycle counts

## Finding
Let \(C_j\) denote the number of cycles of length \(j\) in an Ewens-\(\theta\) permutation of \(n\) labels, with \(\theta>0\). Fix pairwise distinct positive lengths \(r_1,\ldots,r_d\), positive multiplicities \(k_1,\ldots,k_d\), and \(m=\sum_{i=1}^d r_i k_i\le n\), where \(d\ge2\). Writing \((z)_{\underline{k}}\) for a falling factorial, the following *strict factorial-moment product transition* holds:
\[
\mathbb E\prod_{i=1}^d (C_{r_i})_{\underline{k_i}}
\begin{cases}
>\prod_{i=1}^d\mathbb E(C_{r_i})_{\underline{k_i}},&0<\theta<1,\\
=\prod_{i=1}^d\mathbb E(C_{r_i})_{\underline{k_i}},&\theta=1,\\
<\prod_{i=1}^d\mathbb E(C_{r_i})_{\underline{k_i}},&\theta>1.
\end{cases}
\]
In particular, for distinct \(r,s\) with \(r+s\le n\), the covariance \(\operatorname{Cov}(C_r,C_s)\) is positive, zero, or negative according as \(\theta<1\), \(\theta=1\), or \(\theta>1\). If \(r+s>n\), it is always negative.

For fixed distinct positive integers \(r,s\), the leading finite-size covariance correction is *independent of both lengths*:
\[
\lim_{n\to\infty} n^2\operatorname{Cov}(C_r,C_s)=\theta^2(1-\theta).
\]
Furthermore, for every \(n\ge4\), **all** admissible off-diagonal covariances \(\operatorname{Cov}(C_r,C_s)\), with distinct \(r,s\) and \(r+s\le n\), have a common value precisely when \(\theta=1\) or \(\theta=2\). At \(\theta=1\) they all vanish, whereas at the unique nonzero equicovariance parameter \(\theta=2\),
\[
\operatorname{Cov}(C_r,C_s)=-\frac{4}{(n+1)^2}
\quad(r\ne s,\ r+s\le n).
\]

## Assumptions and scope
An Ewens-\(\theta\) permutation \(\pi\in S_n\) assigns probability \(\theta^{K(\pi)}/\theta_{(n)}\), where \(K(\pi)\) is its number of cycles and \(\theta_{(n)}=\prod_{j=0}^{n-1}(\theta+j)\). All lengths and multiplicities in the first assertion are positive integers; the strict comparison requires at least two distinct selected lengths and total marked size not exceeding \(n\). There is no claim of ordinary association, negative association, or full independence of the cycle-count vector. The asymptotic statement keeps \(r,s,\theta\) fixed. Off-diagonal equicovariance concerns the admissible pairs only; pairs consuming more than \(n\) labels are excluded from that rigidity assertion.

## Proof
**Exact marked-cycle moments.** For \(0\le t\le n\), define
\[
F_n(t)=\prod_{a=0}^{t-1}\frac{n-a}{n+\theta-1-a},\qquad F_n(0)=1.
\]
The Ewens sampling formula gives, for pairwise distinct lengths and \(m=\sum_i r_i k_i\le n\),
\[
\mathbb E\prod_i(C_{r_i})_{\underline{k_i}}
=F_n(m)\prod_i\left(\frac{\theta}{r_i}\right)^{k_i}.
\tag{1}
\]
Indeed, in the Ewens cycle-count sum, replacing each \((C_{r_i})_{\underline{k_i}}\) by its combinatorial marking weight removes \(k_i\) cycles of size \(r_i\), contributes \((\theta/r_i)^{k_i}\), and leaves an Ewens normalizer on \(n-m\) labels. The ratio is \(n!\theta_{(n-m)}/((n-m)!\theta_{(n)})=F_n(m)\). If \(m>n\), that marked moment is zero.

**Sharp multiplicative transition.** Set \(q_a=(n-a)/(n+\theta-1-a)\) for \(0\le a<n\). The difference of consecutive terms has the sign of \(1-\theta\):
\[
q_{a+1}-q_a
=\frac{1-\theta}{(n+\theta-2-a)(n+\theta-1-a)}.
\]
Therefore \(q_a\) increases strictly in \(a\) when \(\theta<1\), is constant when \(\theta=1\), and decreases strictly when \(\theta>1\). For positive integers \(u,v\) with \(u+v\le n\), comparing the factors of \(F_n(u+v)/F_n(u)\) with the first \(v\) factors of \(F_n(v)\) gives
\[
F_n(u+v)\begin{cases}>F_n(u)F_n(v),&\theta<1,\\=F_n(u)F_n(v),&\theta=1,\\<F_n(u)F_n(v),&\theta>1.\end{cases}
\]
Iterating over the positive block sizes \(r_i k_i\), then applying (1), proves the first assertion. For \(r\ne s\) with \(r+s\le n\), (1) yields
\[
\operatorname{Cov}(C_r,C_s)=\frac{\theta^2}{rs}\left[F_n(r+s)-F_n(r)F_n(s)\right].\tag{2}
\]
For \(r+s>n\), the product \(C_rC_s\) is identically zero while both expectations are positive, proving the remaining sign.

**Universal small-cycle correction.** Set \(\beta=\theta-1\). At each fixed integer \(a\), as \(n\to\infty\),
\[
\log q_a=-\frac{\beta}{n}+\frac{\beta^2/2-\beta a}{n^2}+O_{a,\theta}(n^{-3}).
\]
Summing over \(a=0,\ldots,t-1\) for fixed \(t\) and taking the mixed difference gives
\[
\log\frac{F_n(r+s)}{F_n(r)F_n(s)}=-\frac{\beta rs}{n^2}+O_{r,s,\theta}(n^{-3}).
\]
Since \(F_n(r)F_n(s)\to1\), substitution into (2) gives the stated limit.

**Exact equicovariance and rigidity.** For \(\theta=1\), \(F_n(t)=1\). For \(\theta=2\), the product telescopes to \(F_n(t)=(n-t+1)/(n+1)\); thus (2) equals \(-4/(n+1)^2\) for every admissible pair. Conversely, if all admissible distinct-length covariances are equal for an integer \(n\ge4\), comparing the pairs \((1,2)\) and \((1,3)\) yields, by direct substitution into (2),
\[
\operatorname{Cov}(C_1,C_2)-\operatorname{Cov}(C_1,C_3)
=-\frac{n(n-1)\theta^2(\theta-1)(\theta-2)}{(\theta+n-4)(\theta+n-3)(\theta+n-2)(\theta+n-1)^2}.
\]
Its denominator is strictly positive for \(\theta>0\) and \(n\ge4\). Therefore equality forces \(\theta\in\{1,2\}\), proving rigidity. This is an all-parameter algebraic argument, independent of finite enumeration.

## Verification
The standalone Python program `verify.py` uses rational arithmetic and enumerates all permutations for \(2\le n\le7\) at five rational Ewens parameters. It verifies normalizers, marked-cycle means, all distinct-length mixed second moments and signs, the \(\theta=2\) equicovariance identity, feasible mixed third moments, and selected repeated falling-factorial moments. It also checks the displayed rigidity factorization at 80 additional rational parameter choices and orders. On the packaged source it reports **1,165 exact assertions passed**. These finite checks are corroboration, not a substitute for the proof of universal quantifiers or the asymptotic expansion.

## Relationship to prior work
The Ewens sampling formula and its independent-Poisson conditioning relation are classical. Tavaré (2021), Sections 2.1 and 4.3, states the joint cycle-count distribution and conditioning relation, while da Silva, Jamshidpey and Tavaré (2020) develops marked-cycle moments for Ewens **derangements**, a different conditioned law. Stark (2021) treats a random-injection model and its component factorial moments. These sources supply probabilistic context and/or ingredients, not a stated cross-length factorial-moment sign transition with the exact nonzero equicovariance rigidity point and universal second-order coefficient of the unconditioned Ewens law. The sign and rigidity claims are derived here directly from (1), not asserted to be independent of the established Ewens probability formula. In particular, this result does not claim a new joint cycle-count distribution or a new Poisson limit.

## Limitations
The all-order comparison concerns products of falling-factorial moments across **different** cycle lengths and does not imply monotonicity of arbitrary increasing functions or joint positive/negative association. At \(\theta=1\), vanishing mixed covariances within \(r+s\le n\) does not mean unconditional independence: global size conservation still creates constraints. Historical originality cannot be certified by a mathematical proof; older treatments of Ewens moment ratios and negative-dependence inequalities may contain an equivalent reformulation, and independent literature verification remains necessary. All asymptotics are fixed-length; a separate analysis is required for lengths growing with \(n\).

## References
1. P. H. da Silva, A. Jamshidpey and S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840, first public version 2020-06-08; Sections 1 and 2.1. https://arxiv.org/abs/2006.04840
2. S. Tavaré, *The magical Ewens sampling formula*, Bulletin of the London Mathematical Society 53 (2021), 1563–1582, DOI:10.1112/blms.12537; Sections 2.1, 4.2–4.4. https://doi.org/10.1112/blms.12537
3. D. Stark, *The component counts of random injections*, Electronic Journal of Combinatorics 28 (2021), P1.5, DOI:10.37236/9496; Sections 2–3. https://doi.org/10.37236/9496
4. T. Bakshajeva and E. Manstavičius, *On Statistics of Permutations Chosen From the Ewens Distribution*, Combinatorics, Probability and Computing 23 (2014), 889–913, DOI:10.1017/S0963548314000376 (asymptotic additive-statistic context). https://doi.org/10.1017/S0963548314000376
