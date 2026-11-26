# A sharp factorial-dependence transition and an equicovariance rigidity point in Ewens cycle counts

## Finding

Let \(C_j\) be the number of \(j\)-cycles in an Ewens-\(\theta\) permutation of \(n\) labels, with \(\theta>0\). For every \(n\ge4\), all the covariances \(\operatorname{Cov}(C_r,C_s)\) for **distinct** lengths with \(r+s\le n\) have a common value if and only if \(\theta=1\) or \(\theta=2\). The common value is zero at \(\theta=1\), and is \(-4/(n+1)^2\) at \(\theta=2\). Thus \(2\) is the unique positive parameter with nonzero equicovariance across all these pairs.

Two consequences of the classical Ewens moment formula put the rigidity statement in context. For distinct positive lengths \(r_i\), positive integers \(k_i\), and \(d\ge2\) with \(\sum_{i=1}^d r_i k_i\le n\),
\[
\mathbb E\prod_{i=1}^d(C_{r_i})_{\underline{k_i}}
\begin{cases}
>\prod_i\mathbb E(C_{r_i})_{\underline{k_i}},&0<\theta<1,\\
=\prod_i\mathbb E(C_{r_i})_{\underline{k_i}},&\theta=1,\\
<\prod_i\mathbb E(C_{r_i})_{\underline{k_i}},&\theta>1.
\end{cases}
\]
Here \((z)_{\underline k}\) denotes a falling factorial. In particular, for distinct \(r,s\) with \(r+s\le n\), their covariance has sign \(\operatorname{sgn}(1-\theta)\). For distinct \(1\le r,s\le n\) with \(r+s>n\), it is strictly negative for every \(\theta>0\). If either length exceeds \(n\), its count is identically zero, and the covariance is zero. For fixed distinct positive \(r,s\) and fixed \(\theta\),
\[
\lim_{n\to\infty} n^2\operatorname{Cov}(C_r,C_s)=\theta^2(1-\theta).
\]

## Assumptions and scope

An Ewens-\(\theta\) permutation \(\pi\) assigns probability \(\theta^{K(\pi)}/\theta_{(n)}\), where \(K\) counts cycles and \(\theta_{(n)}=\prod_{a=0}^{n-1}(\theta+a)\). Cycle lengths are positive integers, with \(C_j=0\) for \(j>n\). Equicovariance concerns off-diagonal pairs with \(r+s\le n\) only. There is no claim of ordinary association, negative association or independence.

## Proof

**Marked-cycle law.** Set \(F_n(0)=1\), and for \(1\le t\le n\) set
\[
F_n(t)=\prod_{a=0}^{t-1}\frac{n-a}{n+\theta-1-a}.
\]
The Ewens cycle-count law, proportional to \(\prod_j(\theta/j)^{c_j}/c_j!\) subject to \(\sum_j j c_j=n\), gives for marked size \(m=\sum_i r_i k_i\le n\)
\[
\mathbb E\prod_i(C_{r_i})_{\underline{k_i}}=F_n(m)\prod_i(\theta/r_i)^{k_i}.
\]
Indeed, replacing \(c_{r_i}\) by \(c_{r_i}-k_i\) in the sum cancels the marking factors against the factorial denominators. The remaining normalizer gives the ratio \(n!\theta_{(n-m)}/((n-m)!\theta_{(n)})\). In particular for distinct lengths with \(r+s\le n\),
\[
\operatorname{Cov}(C_r,C_s)=\frac{\theta^2}{rs}\left[F_n(r+s)-F_n(r)F_n(s)\right].
\tag{1}
\]

**Equicovariance and rigidity.** For \(\theta=1\), every \(F_n(t)=1\). For \(\theta=2\), \(F_n(t)=1-t/(n+1)\) by telescoping. In (1), the difference in brackets becomes \(-rs/(n+1)^2\), which cancels the length factors. To establish necessity, write \(D=n+\theta-1\), \(q_a=(n-a)/(D-a)\). For \(2\le s\le n-1\), \(F_n(s+1)=F_n(s)q_s\) and
\[
q_s-q_0=\frac{-s(\theta-1)}{D(D-s)},\qquad
\operatorname{Cov}(C_1,C_s)=-\frac{\theta^2(\theta-1)(n)_{\underline s}}{D(D)_{\underline{s+1}}}.
\]
At \(n\ge4\) both \((1,2)\) and \((1,3)\) are admissible. Subtracting their covariances gives
\[
\operatorname{Cov}(C_1,C_2)-\operatorname{Cov}(C_1,C_3)
=-\frac{\theta^2(\theta-1)(\theta-2)n(n-1)}{D^2(D-1)(D-2)(D-3)}.
\]
Every denominator factor is positive. Hence equality for these two pairs forces \(\theta\in\{1,2\}\); the preceding calculations show these parameters suffice for all admissible pairs.

**Moment signs and length-independent covariance scale.** For \(0\le a<n-1\), the difference \(q_{a+1}-q_a=(1-\theta)/((D-a-1)(D-a))\) has sign \(\operatorname{sgn}(1-\theta)\). For positive \(u,v\) with \(u+v\le n\), compare the last \(v\) factors of \(F_n(u+v)\) with the first \(v\) factors of \(F_n(v)\): each pair differs strictly in the same direction when \(\theta\ne1\). This gives the comparison with \(F_n(u)F_n(v)\), and iteration over the positive marked sizes gives the displayed factorial-moment result. When two possible lengths cannot coexist because their sum exceeds \(n\), their product count is zero while each expectation is positive; impossible individual lengths instead have zero count.

For fixed \(a\), put \(\beta=\theta-1\). Expanding \(-\log(1+\beta/(n-a))\) gives \(\log q_a=-\beta/n+(\beta^2/2-\beta a)/n^2+O(n^{-3})\). Consequently
\[
\log\frac{F_n(r+s)}{F_n(r)F_n(s)}
=\sum_{a=0}^{s-1}(\log q_{r+a}-\log q_a)
=-\frac{\beta rs}{n^2}+O_{r,s,\theta}(n^{-3}).
\]
Since \(F_n(r)F_n(s)\to1\), expanding the exponential and substituting in (1) proves the limit. At \(\theta=1\) the covariance is identically zero once the fixed pair is admissible.

## Verification

Run `python3 verify.py` with the Python standard library. The supplied finite check enumerates permutations for \(2\le n\le7\) at five rational parameters. It checks moments, covariance signs on the individual range \(1\le r,s\le n\), and the \(\theta=2\) formula, and tests the rigidity factorization at further orders and parameters. The recorded run reports 1,165 checks. The general rigidity, asymptotic and sign assertions follow from the analytic proof above; in particular, the zero covariance at a length exceeding \(n\) follows directly from its identically zero count.

## Relationship to prior work

The joint count law is the classical Ewens sampling formula; neither that law nor its marked-cycle moments are claimed here as new. Tavaré [2] is a review of the sampling formula and conditioning representation. Da Silva, Jamshidpey and Tavaré [1, p. 1, Eq. (1)] restate the joint law; their §2.1, Eq. (6), gives related falling-factorial moments for the law conditioned to have no one-cycles, with a different normalizer. Stark [3] treats factorial moments in a random-injection model. The sign and fixed-length scale calculations above are consequences of the classical ratio. The specific classification at issue is which positive parameters make **every** distinct-length admissible covariance equal for each \(n\ge4\) in the unconditioned law.

## Limitations

Equicovariance excludes pairs that cannot fit together, and does not characterize other moments or arbitrary functionals of the counts. At \(\theta=1\), the feasible marked moments factorize, but total size remains constrained. The limit is for fixed lengths only. The classification is for the unconditioned Ewens law; it is not a result about derangements or other conditioned measures. Historical priority outside the inspected sources is not certified.

## References

1. P. H. da Silva, A. Jamshidpey and S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840, https://arxiv.org/abs/2006.04840.
2. S. Tavaré, *The magical Ewens sampling formula*, Bulletin of the London Mathematical Society **53** (2021), 1563–1582, DOI:10.1112/blms.12537.
3. D. Stark, *The component counts of random injections*, Electronic Journal of Combinatorics **28** (2021), P1.5, DOI:10.37236/9496.
4. T. Bakshajeva and E. Manstavičius, *On Statistics of Permutations Chosen From the Ewens Distribution*, Combinatorics, Probability and Computing **23** (2014), 889–913, DOI:10.1017/S0963548314000376.
