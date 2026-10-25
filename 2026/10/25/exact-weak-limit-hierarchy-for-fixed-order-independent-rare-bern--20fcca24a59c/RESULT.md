# Exact weak-limit hierarchy for fixed-order independent rare Bernoulli sums

## Finding

Fix an integer \(k\ge 4\) and a real \(\lambda>0\). For each sufficiently large integer \(n\), let \(X_{n,1},\ldots,X_{n,n}\) be an exchangeable row of \(k\)-wise independent Bernoulli variables with common success probability \(\lambda/n\), and put \(S_n=\sum_{i=1}^n X_{n,i}\). The set of all possible weak limits of \(S_n\) is exactly the set of laws of nonnegative-integer-valued random variables \(Y\) satisfying

\[
\mathbb E (Y)_j=\lambda^j\quad (1\le j<k),\qquad \mathbb E (Y)_k\le \lambda^k,
\]

where \((y)_j=y(y-1)\cdots(y-j+1)\) is the falling factorial. Every such law is attainable as a full-sequence weak limit of exchangeable \(k\)-wise independent rows. Thus the first \(k-1\) factorial moments are rigid under weak convergence, while a deficit in the \(k\)-th moment can be carried by vanishing probability at counts tending to infinity.

## Assumptions and scope

The order \(k\) and intensity \(\lambda\) are fixed as \(n\to\infty\); \(n\) is taken large enough that \(n\ge k\) and \(\lambda/n\le1\). Here \(k\)-wise independent means every subset of at most \(k\) coordinates is jointly independent. The result concerns the possible laws of the count, not the uniqueness of a row's joint law. Exchangeability is required for the constructive converse; the necessary moment restrictions hold without exchangeability.

## Proof

For any \(k\)-wise independent row with success probability \(p_n=\lambda/n\), counting ordered distinct successful coordinates gives, for \(0\le j\le k\),

\[
\mathbb E(S_n)_j=(n)_j p_n^j=\lambda^j\frac{(n)_j}{n^j}.
\tag{1}
\]

In particular, \(\mathbb ES_n=\lambda\), so the laws are tight. Any weak limit \(Y\) is supported on \(\mathbb Z_{\ge0}\), since this is a closed subset of \(\mathbb R\). For \(j<k\), the family \((S_n)_j\) is uniformly integrable: for integers \(R>j\),

\[
\mathbb E\big[(S_n)_j\mathbf1_{\{S_n>R\}}\big]
\le \frac{\mathbb E(S_n)_{j+1}}{R-j}
\le \frac{\lambda^{j+1}}{R-j}.
\]

Consequently, (1) and weak convergence imply \(\mathbb E(Y)_j=\lambda^j\) for \(j<k\). For each integer \(M>0\), define \(g_M\) on nonnegative integers by \(g_M(m)=\min\{(m)_k,M\}\), interpolate linearly between consecutive integers, and set \(g_M(s)=0\) for \(s<0\). Then \(g_M\) is bounded, continuous, and nonnegative. Weak convergence gives \(\mathbb E g_M(Y)=\lim_n\mathbb E g_M(S_n)\le\lim_n\mathbb E(S_n)_k=\lambda^k\). Letting \(M\) increase and using monotone convergence yields \(\mathbb E(Y)_k\le\lambda^k\).

For the converse, let \(\mu\) be a law satisfying the displayed moment conditions, write \(m_k=\mathbb E(Y)_k\), and set \(\delta=\lambda^k-m_k\ge0\). For each \(n\), form \(\mu^{[n]}\) by moving all mass of \(\mu\) above \(n\) to zero. Let \(\pi_\lambda\) be the Poisson law of mean \(\lambda\), and truncate it in the same way. Write \(t_n=\mathbb E[(Y)_k\mathbf1_{\{Y>n\}}]\to0\) and choose \(\varepsilon_n=\sqrt{t_n+1/n}\) for all sufficiently large \(n\). The mixture

\[
\beta_n=(1-\varepsilon_n)\mu^{[n]}+\varepsilon_n\pi_\lambda^{[n]}
\]

converges weakly to \(\mu\), has mass at each fixed integer \(0,\ldots,k\) at least \(\varepsilon_n e^{-\lambda}\lambda^i/i!\), and its factorial moments of orders below \(k\) differ from the targets in (1) by \(O(1/n)\). Indeed, for \(j<k\),

\[
\mathbb E[(Y)_j\mathbf1_{\{Y>n\}}]
\le \frac{t_n}{(n-k+1)^{k-j}}=o(1/n),
\]

while the truncated Poisson tails are exponentially small.

If \(\delta>0\), then for all sufficiently large \(n\), the deficit
\(d_n=\lambda^k(n)_k/n^k-\mathbb E_{\beta_n}(Z)_k\) is positive and bounded. Add mass \(q_n=d_n/(n)_k\) at \(n\); this makes the \(k\)-th factorial moment exact. The added mass changes each lower factorial moment by \(q_n(n)_j=O(1/n)\). Correct the moments of orders \(0,\ldots,k-1\) by signed adjustments to the masses at \(0,\ldots,k-1\). The matrix with entries \((i)_j\), \(0\le j,i<k\), is triangular with diagonal \(j!\), so this correction exists uniquely and has size \(O(1/n)\). It does not change the \(k\)-th factorial moment because \((i)_k=0\) for \(i<k\).

If \(\delta=0\), no escaping atom is needed. Correct all moments of orders \(0,\ldots,k\) by signed adjustments at \(0,\ldots,k\). The corresponding triangular matrix has diagonal \(j!\), so the correction is unique and of size \(O(t_n+1/n)=o(\varepsilon_n)\). In both cases, the corrections are smaller than the positive masses supplied by the Poisson mixture, so the adjusted measures are nonnegative for all sufficiently large \(n\). They are supported on \(\{0,\ldots,n\}\), satisfy (1) exactly, and converge weakly to \(\mu\); in the case \(\delta>0\), additionally \(q_n=O(n^{-k})\to0\).

Finally, given an adjusted count \(S_n\), choose uniformly a subset of \(S_n\) coordinates to set equal to one and set the rest to zero. This row is exchangeable and satisfies

\[
\mathbb P(X_{n,1}=\cdots=X_{n,j}=1)
=\frac{\mathbb E(S_n)_j}{(n)_j}
=(\lambda/n)^j,\qquad j\le k.
\]

Inclusion-exclusion then gives the product probability for every pattern of at most \(k\) zeros and ones, so the row is \(k\)-wise independent with the required marginal. Its sum has the prescribed law, proving attainability.

## Verification

The proof uses exact factorial-moment identities and a finite triangular moment-correction argument. The only asymptotic estimates are: \((n)_j/n^j=1+O(1/n)\) for fixed \(j\), vanishing factorial-moment tails, and the resulting correction sizes stated above. No finite simulation is used as proof. The construction is asserted only for sufficiently large \(n\); finitely many initial row sizes may be omitted or defined arbitrarily.

## Relationship to prior work

Finite exchangeable \(k\)-wise independent Bernoulli rows are classically encoded by the first \(k\) moments of their count; see Peled, Yadin, and Yehudayoff. Recent moment-hierarchy work for exchangeable Bernoulli sequences studies posterior moment identification rather than sparse triangular arrays. The closest indexed classifications found for rare Bernoulli sums settle the pairwise case and the unit-intensity three-wise case. The present statement addresses fixed orders \(k\ge4\), arbitrary fixed intensity \(\lambda\), and the converse that every admissible limiting law is realizable. Those lower-order cases are not claimed as new here.

## Limitations

The result does not give a quantitative rate of weak convergence, classify the higher factorial moments of \(Y\), or treat \(k=k(n)\to\infty\). The literature comparison is not an exhaustive proof of novelty; an unindexed result on arbitrary-order sparse k-wise independent limits remains a residual possibility. Independent mathematical review has not been performed.

## References

1. R. Peled, A. Yadin, and A. Yehudayoff, “The Maximal Probability that \(k\)-wise Independent Bits are All \(1\),” *Random Structures & Algorithms* 38 (2011), 502–525; arXiv:0801.0059. https://doi.org/10.1002/rsa.20329. Its finite-dimensional moment characterization is relevant background, but the paper's extremal objective is the probability that all bits are one.
2. N. G. Polson and D. Zantedeschi, “Predictive Coherence and the Moment Hierarchy: Martingale Posteriors for Exchangeable Bernoulli Sequences,” arXiv:2603.00661 (first submitted 2026-02-28). https://arxiv.org/abs/2603.00661.
3. R. Fontana and P. Semeraro, “Computational and Analytical Bounds for Multivariate Bernoulli Distributions,” *Journal of Statistical Theory and Practice* 16, article 6 (2022). https://doi.org/10.1007/s42519-021-00231-x.
