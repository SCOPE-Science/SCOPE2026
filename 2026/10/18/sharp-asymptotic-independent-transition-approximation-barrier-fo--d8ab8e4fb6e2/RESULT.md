# Sharp asymptotic independent-transition approximation barrier for categorical runs

## Finding
Let \(X_1,\dots,X_n\) be iid categorical observations with probabilities \(p_1,\dots,p_d>0\), \(d\ge2\), \(\sum_i p_i=1\). Let \(T_n=\sum_{j=1}^{n-1}\mathbf 1\{X_j\ne X_{j+1}\}\), the number of changes (one less than the number of runs). The optimal approximation class contains sums of **at most \(n-1\) independent Bernoulli variables**, one possible independent proxy for each of the \(n-1\) transitions, with no constraints on their success probabilities. Its finite-sample Kolmogorov error is
\[
e_n=\inf_{a_1,\dots,a_{n-1}\in[0,1]}\sup_{k\in\mathbb Z}\left|\Pr(T_n\le k)-\Pr\!\left(\sum_{j=1}^{n-1}B_j\le k\right)\right|,
\qquad B_j\text{ independent Bernoulli}(a_j).
\]
Write
\[
s_2=\sum_i p_i^2,\quad s_3=\sum_i p_i^3,\quad q=1-s_2,\quad\delta=s_3-s_2^2,\quad \tau^2=q(1-q),\quad\sigma^2=\tau^2+2\delta.
\]
Then \(\delta\ge0\), with equality exactly when the positive category probabilities are all equal. If \(\delta>0\), define \(u>0\) by
\[
u^2=\frac{\tau^2\sigma^2\log(\sigma^2/\tau^2)}{\sigma^2-\tau^2}.
\]
The sharp limit is
\[
\boxed{\lim_{n\to\infty}e_n=\kappa(p):=\Phi(u/\tau)-\Phi(u/\sigma)>0.}
\]
In particular, the independent surrogate \(\operatorname{Bin}(n-1,q)\) is **asymptotically optimal among all choices of \(n-1\) independent Bernoulli probabilities**. For a uniform distribution on its support, the adjacent-change indicators themselves are iid Bernoulli\((q)\), so \(e_n=0\) identically. For nonuniform \(p\), the finite-sample law of \(T_n\) is not Poisson-binomial for any \(n\ge3\), although the main contribution here is the *quantified, nonvanishing optimal asymptotic distance*, not this finite obstruction.

## Assumptions and scope
The number of categories \(d\ge2\) and the positive probability vector \(p\) are fixed as \(n\to\infty\). \(\Phi\) is the standard normal distribution function. The approximation is measured by Kolmogorov (CDF supremum) distance and allows arbitrary individual independent Bernoulli parameters but **not** more than one nontrivial Bernoulli term per adjacent pair. The distinction matters: allowing an unbounded excess of Bernoulli trials could alter the asymptotic variance constraint. Endpoints with a single positive category are excluded as degenerate.

## Proof
**1. Exact first and second moments.** Let \(I_j=\mathbf 1\{X_j\ne X_{j+1}\}\). Its mean is \(q\). Nonadjacent \(I_j\) are independent. For adjacent indices,
\[
\Pr(I_j=I_{j+1}=1)=\sum_i p_i(1-p_i)^2=1-2s_2+s_3,
\qquad \operatorname{Cov}(I_j,I_{j+1})=\delta.
\]
Consequently
\[
\mathbb ET_n=(n-1)q,\qquad
\operatorname{Var}(T_n)=(n-1)\tau^2+2(n-2)\delta.
\]
The Cauchy--Schwarz inequality applied to \((p_i^{3/2})_i\) and \((p_i^{1/2})_i\) gives \(s_2^2\le s_3\sum_i p_i=s_3\). Equality requires every positive \(p_i\) equal.

**2. Gaussian limit.** The bounded, stationary, one-dependent centered sequence \((I_j-q)\) has asymptotic variance \(\sigma^2>0\). The one-dependent central limit theorem gives
\[
\frac{T_n-(n-1)q}{\sqrt{n-1}}\ \Rightarrow\ N(0,\sigma^2).
\]
For completeness, partition the indicator indices into blocks of length \(\ell_n=\lfloor n^{1/5}\rfloor\), leaving one omitted index between blocks. Distinct retained blocks are independent; the centered omitted sum has variance \(O(n/\ell_n)\), negligible after division by \(\sqrt n\). Retained centered block sums have absolute size at most \(\ell_n\), and their Lyapunov-third-moment numerator is \(O(n\ell_n^2)=o(n^{3/2})\). The usual independent-block Lyapunov theorem and Slutsky's theorem yield the stated limit. (The omitted terms are centered before estimating their variance.)

**3. Upper bound.** The chosen surrogate \(Y_n\sim\operatorname{Bin}(n-1,q)\) satisfies
\[
\frac{Y_n-(n-1)q}{\sqrt{n-1}}\Rightarrow N(0,\tau^2).
\]
Both limits have continuous CDFs, so convergence of the two CDFs is uniform. Hence
\[
\lim_{n\to\infty}d_K(T_n,Y_n)
=\sup_{x\in\mathbb R}\left|\Phi(x/\tau)-\Phi(x/\sigma)\right|.
\]
Since \(\tau<\sigma\), differentiating the positive difference for \(x>0\) locates its unique maximum at the displayed \(u\); this supremum equals \(\kappa(p)\). Thus \(\limsup e_n\le\kappa(p)\).

**4. Uniform lower bound over independent surrogates.** For any sequence of independent-Bernoulli surrogates \(Z_n\), pad with Bernoulli\((0)\) terms to \(m=n-1\). Write \(\mu_n=\mathbb EZ_n\), \(v_n=\operatorname{Var} Z_n\). Cauchy--Schwarz gives
\[
v_n=\sum_{j=1}^m a_j(1-a_j)\le\mu_n\left(1-\frac{\mu_n}{m}\right).
\]
Take an arbitrary subsequence along which the distances approach their liminf, choosing near-minimizers (within \(1/n\)) if needed. Since \(\operatorname{Var}(T_n)=O(m)\) and \(v_n\le m/4\), a difference \(|\mu_n-mq|/\sqrt m\to\infty\) forces the Kolmogorov distance to tend to one, certainly not below \(\kappa(p)<1/2\). Therefore any potentially improving subsequence can be further restricted so that \((\mu_n-mq)/\sqrt m\to a\in\mathbb R\). Compactness permits \(v_n/m\to v\in[0,\tau^2]\), since \(\mu_n/m\to q\). For \(v>0\), the bounded independent triangular-array CLT gives
\[
\frac{Z_n-mq}{\sqrt m}\Rightarrow N(a,v).
\]
For \(v=0\), Chebyshev's inequality makes the normalized surrogate converge to the point mass at \(a\), whose Kolmogorov distance from the continuous \(N(0,\sigma^2)\) is at least \(1/2\).

For \(v>0\), the Kolmogorov distance between \(N(0,\sigma^2)\) and \(N(a,v)\) is at least \(\kappa(p)\). Indeed, if \(a\ge0\), evaluate the two CDFs at \(-u\):
\[
\Phi(-u/\sigma)-\Phi((-u-a)/\sqrt v)
\ge \Phi(-u/\sigma)-\Phi(-u/\tau)=\kappa(p).
\]
If \(a\le0\), evaluation at \(+u\) gives the analogous inequality, using \(\sqrt v\le\tau\). Weak convergence at these continuity points transfers the same lower bound to the original distributions. Thus \(\liminf e_n\ge\kappa(p)\), proving sharpness.

**5. Uniform and finite-sample boundary.** If the categorical probabilities are all equal, conditional on the past symbols the probability of the next change is always \(q\); sequential conditioning makes the \(I_j\) independent. Hence \(T_n\sim\operatorname{Bin}(n-1,q)\). If \(\delta>0\) and \(n\ge3\), the variance in Step 1 strictly exceeds \((n-1)q(1-q)\). Any Poisson-binomial representation of \(T_n\) has at most \(n-1\) nonzero Bernoulli parameters because its support is contained in \(\{0,\ldots,n-1\}\) and \(\Pr(T_n=0)>0\). The displayed variance bound contradicts this representation. This last finite obstruction is supporting context, not asserted to be the new asymptotic conclusion.

## Verification
Run `python3 check.py` using only the Python standard library. The checker independently enumerates short categorical samples using exact fractions and matches the variance formula, verifies the equal-probability binomial case, and compares dynamic-programming CDF distances with the predicted constant for two rational nonuniform probability vectors at three sample sizes. The checks are finite and supplement, but do not replace, the proof of the asymptotic and minimax quantifiers. For \(p=(3/4,1/4)\), the limiting distance is about \(0.04061249\); for \(p=(1/2,1/3,1/6)\), it is about \(0.01476805\).

## Relationship to prior work
Kumar and Upadhye (2017 preprint, 2020 publication) develop discrete-Gibbs/Stein approximations for specified success--failure patterns, with Poisson, pseudo-binomial and negative-binomial comparison classes. Wentzel-Larsen and Anhøj (2019) study the exact joint distribution of the number of crossings and the longest run, explaining that symmetric binary crossings have a binomial law. Johnson and Fu (2014) treat general run/pattern approximations by normal, Poisson and compound Poisson methods. Godbole and Gornowicz (1992) derive exact and asymptotic Bernoulli-run distributions. These works motivate approximation and provide related distributional tools, but the inspected accessible statements do not give the sharp minimum Kolmogorov error across **all** independent Bernoulli proxies constrained to the number of adjacent transitions, nor the displayed positive constant. The ordinary finite nonrepresentability of biased binary runs is not the distinctive claim; the asymptotically sharp *uniform approximation barrier* is.

## Limitations
The error is Kolmogorov distance, not total variation; the class is limited to at most \(n-1\) independent Bernoulli terms, and \(p\) is fixed. The minimizing sequence is established, not an exact finite-\(n\) optimizer. No claim of absolute novelty or independent validation is made. The 1992 historical runs article was available only in abstract/summary form; a differently indexed minimax result could still exist. The finite checker does not certify the infinite limit.

## References
1. A. N. Kumar and N. S. Upadhye, *On Discrete Gibbs Measure Approximation to Runs*, arXiv:1701.03294, first posted 2017-01-12; https://arxiv.org/html/1701.03294v2 .
2. T. Wentzel-Larsen and J. Anhøj, *Joint distribution for number of crossings and longest run in independent Bernoulli observations*, PLoS ONE 14 (2019), e0223233; https://doi.org/10.1371/journal.pone.0223233 .
3. B. C. Johnson and J. C. Fu, *Approximating the distributions of runs and patterns*, Journal of Statistical Distributions and Applications 1 (2014), article 5; https://doi.org/10.1186/2195-5832-1-5 .
4. A. P. Godbole and M. C. Gornowicz, *Exact and approximate runs distributions*, Communications in Statistics -- Theory and Methods 21 (1992), 2151--2167; https://doi.org/10.1080/03610929208830904 .
