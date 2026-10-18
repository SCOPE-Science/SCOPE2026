# Universal far-tail failure of Poisson-minimum ultra-log-concavity under random sample sizes

## Finding

Let \(X_1,X_2,\ldots\) be independent Poisson random variables with common mean \(\lambda>0\), and let \(N\) be an independent positive-integer-valued random variable. Put \(w_j=\Pr(N=j)\), and let \(Y=\min_{1\le i\le N}X_i\), with \(r_k=\Pr(Y=k)\) and \(p_k=e^{-\lambda}\lambda^k/k!\).

**Theorem.** For every \(\lambda>0\) and every sample-size law with \(w_1>0\) and \(w_2>0\), without any moment assumption on \(N\),
\[
\frac{k+1}{k}\frac{r_{k-1}r_{k+1}}{r_k^2}-1
\sim \frac{w_2}{w_1}\,p_{k-1}>0
\qquad(k\to\infty).
\]
In particular, for every sufficiently large integer \(k\ge1\),
\[
k r_k^2<(k+1)r_{k-1}r_{k+1}.
\]
Thus the law of \(Y\) is **not ultra-log-concave**, even though every deterministic finite-sample Poisson minimum is ultra-log-concave.

For the smallest random-sample-size family, \(\Pr(N=1)=w\), \(\Pr(N=2)=1-w\), with \(0\le w\le1\), the exact classification is
\[
\boxed{\quad Y\text{ is ultra-log-concave}\ \Longleftrightarrow\ w\in\{0,1\}.\quad}
\]
In particular, both pure endpoint distributions satisfy ultra-log-concavity, but **every** nontrivial mixture violates it at all sufficiently large indices. The asymptotic leading term depends only on \(w_1\) and \(w_2\), regardless of the distribution of \(N\) above two.

## Assumptions and scope

For any positive sequence \((a_k)_{k\ge0}\), ultra-log-concavity (ULC) means
\[
k a_k^2\ge(k+1)a_{k-1}a_{k+1}\qquad\text{for every integer }k\ge1.
\]
The sample-size variable \(N\) takes values in \(\{1,2,\ldots\}\), is almost surely finite and is independent of all \(X_i\). Only \(w_1,w_2>0\) are required; higher sample sizes can have arbitrary probabilities, and \(\mathbb E[N]\) need not be finite. The deterministic endpoint assertion is limited to \(N\in\{1,2\}\).

## Proof

Set \(S_k=\Pr(X_1\ge k)\), so that \(S_k-S_{k+1}=p_k\). Conditional on \(N=n\),
\[
\Pr(Y=k\mid N=n)=S_k^n-S_{k+1}^n
=p_k\sum_{j=0}^{n-1}S_k^{n-1-j}S_{k+1}^j.
\]
Thus \(r_k=p_kH_k\), where \(H_k>0\) satisfies
\[
H_k=w_1+w_2(S_k+S_{k+1})+R_k,\qquad
R_k=\sum_{n=3}^{\infty}w_n\sum_{j=0}^{n-1}S_k^{n-1-j}S_{k+1}^j.
\]
For \(S_k\le1/2\), the inner sum is at most \(n S_k^{n-1}\le3S_k^2\) for every \(n\ge3\); hence \(0\le R_k\le3S_k^2\), uniformly over all sample-size distributions (including those with infinite expectation).

For the Poisson law,
\[
1\le\frac{S_k}{p_k}
=1+\sum_{j=1}^{\infty}\frac{\lambda^j}{(k+1)(k+2)\cdots(k+j)}
\le\frac1{1-\lambda/(k+1)}
\]
when \(k+1>\lambda\). Consequently \(S_k\sim p_k\), \(S_{k+1}=o(p_k)\), and \(R_k=O(p_k^2)\). We obtain
\[
H_k=w_1+w_2p_k(1+o(1)).
\]
Since \(p_k/p_{k-1}=\lambda/k\to0\) and \(p_{k+1}/p_{k-1}\to0\),
\[
H_{k-1}H_{k+1}-H_k^2
=w_1w_2p_{k-1}(1+o(1)).
\]
The Poisson identity \(p_{k-1}p_{k+1}/p_k^2=k/(k+1)\) now gives
\[
\frac{k+1}{k}\frac{r_{k-1}r_{k+1}}{r_k^2}-1
=\frac{H_{k-1}H_{k+1}-H_k^2}{H_k^2}
\sim\frac{w_2}{w_1}p_{k-1}.
\]
This proves the universal asymptotic and eventual strict failure of ULC.

For the pure endpoints of the \(\{1,2\}\) family, \(N=1\) gives the Poisson law, which satisfies ULC with equality. For \(N=2\), \(r_k=p_k(S_k+S_{k+1})\). The coefficient sequence \(S_k+S_{k+1}=p_k+2\sum_{j\ge1}p_{k+j}\) is the convolution of the Poisson mass sequence with the sequence \(q_0=1\), \(q_j=2\) for \(j\le-1\), and \(q_j=0\) for \(j\ge1\). Both sequences are log-concave. Truncating \(q\) to a finite contiguous support preserves its log-concavity, and the standard closure of log-concavity under discrete convolution, followed by pointwise passage to the limit, shows that \((S_k+S_{k+1})\) is log-concave. Multiplication by the Poisson mass then gives ULC. This is also a special case of the fixed-sample theorem of Badiella, del Castillo and Puig (2023). If \(0<w<1\), the already proved asymptotic excludes ULC. The classification follows.

## Verification

The self-contained `verify.py` uses exact rational arithmetic to check the conditional minimum mass identity on a finite probability model and high-precision decimal arithmetic to check Poisson masses, survival tails, and the normalized ULC reversal for representative choices of \(\lambda\), sample-size probabilities and large \(k\). Run `python3 verify.py` from the directory containing the file. It requires only the Python standard library. The numerical computations are reproducibility checks, **not proofs** of the infinite-tail assertion; the latter follows from the uniform remainder bound and Poisson tail ratios above.

## Relationship to prior work

Badiella, del Castillo and Puig (2023), Theorem 2, show that fixed-sample discrete order statistics preserve log-concavity and ultra-log-concavity. The finding here concerns an *independent random sample size*, not a fixed order statistic: both pure sample sizes one and two preserve ULC, while any positive mixing of them destroys ULC in the far tail. The displayed asymptotic is uniform in the choice of higher sample-size probabilities in the sense that its leading coefficient involves only \(w_1,w_2\). Watt (2021/2024) studies concavity in deterministic sample size of **expected** order statistics, not curvature of the mass function under random sample size. Related ULC concentration inequalities for already ULC distributions do not imply preservation under mixtures.

## Limitations

The theorem assumes iid Poisson observations and the positivity of the two sample-size probabilities \(w_1,w_2\). It does not classify arbitrary random sample-size laws lacking one of these masses; it does not give a uniform finite threshold index over all \(\lambda,w_1,w_2\), nor does failure of ULC itself prove failure of ordinary log-concavity or of underdispersion. No independent priority audit has been performed; equivalent earlier formulations under different terminology remain possible.

## References

1. L. Badiella, J. del Castillo and P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters 201 (2023), 109900, DOI: 10.1016/j.spl.2023.109900. Available online 26 June 2023.
2. M. Watt, *Concavity and Convexity of Order Statistics in Sample Size*, arXiv:2111.04702 (first public version 8 November 2021; revised 2024).
3. H. Aravinda, A. Marsiglietti and J. Melbourne, *Concentration Inequalities for Ultra Log-Concave Distributions*, arXiv:2104.05054 (2021).
