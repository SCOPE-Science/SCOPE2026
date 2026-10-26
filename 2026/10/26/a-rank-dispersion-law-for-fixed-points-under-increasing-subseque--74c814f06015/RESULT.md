# A rank-dispersion law for fixed points under increasing-subsequence size bias

## Finding
Let \(\pi\) be uniform on the permutations of \(\{1,\ldots,n\}\), where \(n\ge2\). For \(2\le k\le n\), let \(Z_{n,k}\) be the number of (not necessarily consecutive) increasing subsequences of length \(k\), \(F=\sum_{i=1}^n\mathbf1\{\pi(i)=i\}\), and
\[
q_{i,r}=\frac{\binom{i-1}{r-1}\binom{n-i}{k-r}}{\binom{n-1}{k-1}},\qquad 1\le i\le n,\quad 1\le r\le k.
\]
A binomial coefficient is zero if its lower index is outside its allowed range. For each \(i\), the numbers \(q_{i,1},\ldots,q_{i,k}\) constitute a probability distribution: the rank of position \(i\) inside a uniformly chosen \(k\)-subset of positions conditioned to contain \(i\).

The exact local covariance is a nonnegative rank-dispersion energy:
\[
\boxed{\operatorname{Cov}\bigl(\mathbf1\{\pi(i)=i\},Z_{n,k}\bigr)=
 \frac{\binom{n-1}{k-1}}{n(k-1)!}
 \sum_{r=1}^k\left(q_{i,r}-\frac1k\right)^2.}
\]
It vanishes exactly when \(k=2\), \(n\) is odd, and \(i=(n+1)/2\); otherwise it is strictly positive. In particular,
\[
\boxed{\operatorname{Cov}(F,Z_{n,k})=
\frac{\binom{n-1}{k-1}}{n(k-1)!}\sum_{i=1}^n\sum_{r=1}^k
\left(q_{i,r}-\frac1k\right)^2>0.}
\]

Let \(\mu_{n,k}\) be the increasing-subsequence-size-biased law, with density \(Z_{n,k}/\mathbb EZ_{n,k}\) relative to the uniform law. Then
\[
\boxed{\mathbb E_{\mu_{n,k}}F=1+
\frac{k^2}{n^2}\sum_{i=1}^n\sum_{r=1}^k\left(q_{i,r}-\frac1k\right)^2>1.}
\]
The endpoint \(k=n\) gives \(\mathbb E_{\mu_{n,n}}F=n\), as the size-biased law is concentrated on the identity permutation.

For every *fixed* integer \(k\ge2\), the covariance has the sharp asymptotic
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(F,Z_{n,k})}{n^{k-1}}
=\frac{1}{((k-1)!)^2}
\left(\frac{4^{k-1}((k-1)!)^2}{(2k-1)!}-\frac1k\right)>0.}
\]
In particular \(\operatorname{Cov}(F,Z_{n,2})=(n+1)/6\) and \(\operatorname{Cov}(F,Z_{n,3})=(n+1)(3n-4)/60\).

## Assumptions and scope
All permutations are equally likely; positions and values both range over \(\{1,\ldots,n\}\). A subsequence consists of increasing *positions* whose *values* increase strictly, without a consecutive-position restriction. The theorem holds for every pair of integers \(n\ge2\), \(2\le k\le n\). The asymptotic assertion holds only with \(k\) fixed as \(n\) tends to infinity. The source date attached to this result is the earliest verified public version of the antecedent increasing-subsequence model, not a claim of first publication for the new identity.

## Proof
Write \(I_i=\mathbf1\{\pi(i)=i\}\) and \(B=\binom{n-1}{k-1}\). Under \(I_i=1\), every \(k\)-subset of positions avoiding \(i\) is increasing with probability \(1/k!\), exactly as without conditioning, because its distinct images have exchangeable relative ranks.

For a \(k\)-subset containing \(i\), suppose \(i\) is its \(r\)-th smallest position. There are \(K_{i,r}=\binom{i-1}{r-1}\binom{n-i}{k-r}\) such subsets. Under \(\pi(i)=i\), the remaining \(k-1\) images are sampled without replacement from the other \(n-1\) values. To increase across \(i\), the \(r-1\) left images must all be below \(i\) and the \(k-r\) right images all above \(i\), with each side increasing. For each choice of the two image-value sets there is exactly one increasing ordering. Consequently the probability for this particular subset is \(K_{i,r}/(n-1)_{\underline{k-1}}\), where \((t)_{\underline j}=t(t-1)\cdots(t-j+1)\).

Summing over subsets containing \(i\) gives
\[
\mathbb E[Z_{n,k}^{\mathrm{through}\ i}\mid I_i=1]
=\sum_{r=1}^k\frac{K_{i,r}^2}{(n-1)_{\underline{k-1}}}
=\frac{B}{(k-1)!}\sum_{r=1}^k q_{i,r}^2.
\]
Unconditionally the same contribution is \(B/k!\). Vandermonde's identity \(\sum_rK_{i,r}=B\) yields \(\sum_rq_{i,r}=1\), hence
\[
\mathbb E[Z_{n,k}\mid I_i=1]-\mathbb EZ_{n,k}
=\frac{B}{(k-1)!}\left(\sum_rq_{i,r}^2-\frac1k\right)
=\frac{B}{(k-1)!}\sum_r\left(q_{i,r}-\frac1k\right)^2.
\]
As \(\Pr(I_i=1)=1/n\), multiplication by \(1/n\) proves the local formula; summing over \(i\) proves the global formula.

The rank-dispersion sum is zero only when all \(q_{i,r}=1/k\). For \(k=2\), these probabilities are \((n-i)/(n-1)\) and \((i-1)/(n-1)\), so equality holds exactly at the stated middle position. For \(k\ge3\), either the rank distribution omits some rank or (when all ranks have positive probability) strict log-concavity of the two binomial-factor sequences forces \(q_{i,2}^2>q_{i,1}q_{i,3}\); in either case it cannot be uniform. This proves all strictness statements, including the global one since an endpoint position always has a point-mass rank distribution.

The classical mean is \(\mathbb EZ_{n,k}=\binom nk/k!\), and \(\mathbb EF=1\). Using the density \(Z_{n,k}/\mathbb EZ_{n,k}\) and \(\binom{n-1}{k-1}/\binom nk=k/n\) yields the exact size-bias formula.

For fixed \(k\), uniformly in \(1\le i\le n\),
\[
q_{i,r}=\binom{k-1}{r-1}(i/n)^{r-1}(1-i/n)^{k-r}+O_k(n^{-1}).
\]
The Riemann sum of squared rank probabilities tends to
\[
\begin{aligned}
\sum_{r=1}^k\binom{k-1}{r-1}^2\int_0^1 x^{2r-2}(1-x)^{2k-2r}\,dx
&=\frac{((k-1)!)^2}{(2k-1)!}\sum_{j=0}^{k-1}\binom{2j}{j}\binom{2k-2-2j}{k-1-j}\\
&=\frac{4^{k-1}((k-1)!)^2}{(2k-1)!},
\end{aligned}
\]
where the last equality is the coefficient identity from \((1-4z)^{-1/2}(1-4z)^{-1/2}=(1-4z)^{-1}\). Subtracting \(1/k\), since each rank distribution sums to one, and applying \(\binom{n-1}{k-1}\sim n^{k-1}/(k-1)!\), gives the limit. Positivity follows because the limiting beta-binomial rank vector is not uniform on a set of positive measure (it concentrates on rank one near \(x=0\)).

## Verification
The standalone Python 3 file `verify.py` reproduces the exact formulas with rational arithmetic. It exhaustively enumerates all \(46{,}232\) permutations of sizes \(2\) through \(8\) and compares every local and total mixed moment with the rank-dispersion expression. It also checks the rank distributions, strictness boundary, special polynomial formulas, and beta-integral constants on larger symbolic grids. On execution the program reports \(2{,}814\) passed exact comparisons. Exhaustive checks through size eight do not replace the unrestricted combinatorial proof or the fixed-length asymptotic argument.

## Relationship to prior work
Pinsky introduced and analyzed the increasing-subsequence count and its size-biased law, proving laws of large numbers and second-moment results. The contribution here is the explicit response of fixed-point counts under that law, with a nonnegative rank-dispersion decomposition at every labeled position; these cross-moments and their strict signs are not consequences of Pinsky's reported variance bounds. Lifschitz and Pittel earlier studied the number of increasing subsequences. Diaconis, Evans and Graham studied fixed points and *consecutive* unseparated pairs; their equidistribution concerns a different statistic and does not give this mixed law. Hossein and Starr developed a generating function for the Pinsky second-moment array, rather than the fixed-point mixed moment.

## Limitations
The result concerns the mean of fixed points under subsequence size bias; it does not establish stochastic domination of the entire fixed-point distribution. Its asymptotic constant is proved for fixed subsequence length, not for length increasing with permutation size. A historically relevant 1981 paper by Lifschitz and Pittel was identifiable but its complete text could not be inspected; priority beyond the sources read therefore remains uncertain. Finite computational checks are not a substitute for the proof.

## References
1. Ross G. Pinsky, *Law of large numbers for increasing subsequences of random permutations and an approximation result for the uniform measure*, arXiv:math/0407353 (initial public posting 2004-07-21); published in *Random Structures & Algorithms* 29 (2006), 277–295. https://arxiv.org/abs/math/0407353
2. Vladimir Lifschitz and Boris Pittel, *The Number of Increasing Subsequences of the Random Permutation*, *Journal of Combinatorial Theory, Series A* 31 (1981), 1–20.
3. Persi Diaconis, Steven N. Evans and Ron Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Technical Report 822 (2013). https://statistics.berkeley.edu/tech-reports/822
4. Samen Hossein and Shannon Starr, *Generating Function for Pinsky's Combinatorial Second Moment Formula for the Generalized Ulam Problem*, arXiv:2301.00125 (2023). https://arxiv.org/abs/2301.00125
