# Sharp Gaussian–Poisson boundary for growing-rank finite-population order statistics

## Finding

For each integer index \(r\), draw a simple random sample of \(n_r\) distinct numbers from \(\{1,\ldots,N_r\}\), and write \(X_{r,(k_r)}\) for its \(k_r\)-th smallest observation. Assume \(1\le k_r\le n_r<N_r\), and all three sequences \(k_r\), \(n_r-k_r+1\), and \(m_r=N_r-n_r\) diverge to infinity. Define
\[
A_r=n_r+1,\quad p_r=\frac{k_r}{A_r},\quad q_r=1-p_r,\quad Y_r=X_{r,(k_r)}-k_r,
\]
\[
\mu_r=m_rp_r,\qquad \sigma_r^2=m_rp_rq_r\frac{A_r+m_r}{A_r+1}.
\]
Then the following criterion is **necessary and sufficient** for a standard Gaussian limit:
\[
\frac{Y_r-\mu_r}{\sigma_r}\ \Longrightarrow\ N(0,1)
\quad\Longleftrightarrow\quad
\min\{m_rp_r,m_rq_r\}\longrightarrow\infty.
\]
The criterion makes no assumption that the sample fraction or rank fraction has a limit in the interior of the unit interval. It includes near-census and near-endpoint rank paths as well as oscillating sampling fractions.

The failure boundary has an exact alternative. On any subsequence where \(m_rp_r\to\lambda\in[0,\infty)\), one has \(Y_r\Longrightarrow\operatorname{Pois}(\lambda)\), in fact in total variation. By reflection, on any subsequence where \(m_rq_r\to\lambda\), \(m_r-Y_r\Longrightarrow\operatorname{Pois}(\lambda)\). When \(\lambda>0\), the standardized count converges to a standardized Poisson law rather than a Gaussian; when \(\lambda=0\), it converges weakly to a point mass at zero. More quantitatively, for every admissible parameter triple, letting \(\alpha=k\), \(\beta=n-k+1\), \(A=\alpha+\beta\), \(p=\alpha/A\), and \(m=N-n\),
\[
d_{\mathrm{TV}}\bigl(\mathcal L(Y),\operatorname{Pois}(mp)\bigr)
\le \frac{mp}{\sqrt{\alpha}}+mp^2.
\]
The reflected bound holds for \(m-Y\), with \(p,\alpha\) replaced by \(q,\beta\).

## Assumptions and scope

The sample is uniform among all \(\binom{N}{n}\) unordered size-\(n\) subsets. The rank and population size are deterministic within each row; all three quantities \(k_r\), \(n_r-k_r+1\), and \(N_r-n_r\) tend to infinity. The limiting assertion concerns one marginal order statistic, centered by its **exact mean** and divided by its **exact standard deviation**. The Poisson assertion is for subsequences with finite missing-count expectations; its explicit finite-row bound does not require the asymptotic assumptions. No multivariate conclusion, Berry–Esseen constant, or uniform-in-all-parameters finite-sample Gaussian error is claimed.

## Proof

**1. Exact distribution and variance.** Counting subsets having their rank-\(k\) member equal to \(k+j\) yields
\[
\Pr(Y=j)=\frac{\binom{k+j-1}{k-1}\binom{N-k-j}{n-k}}{\binom{N}{n}},\quad 0\le j\le m.
\]
It is the beta-binomial distribution \(\operatorname{BetaBin}(m,\alpha,\beta)\), hence admits the established mixture representation
\[
\Theta\sim\operatorname{Beta}(\alpha,\beta),\qquad Y\mid\Theta\sim\operatorname{Bin}(m,\Theta).
\]
From \(\mathbb E\Theta=p\), \(\operatorname{Var}(\Theta)=pq/(A+1)\), and \(\mathbb E[\Theta(1-\Theta)]=pqA/(A+1)\), total variance gives the displayed formulas, with its independent-noise and mixing parts
\[
 b^2=mpq\frac{A}{A+1},\qquad d^2=m^2\frac{pq}{A+1},\qquad \sigma^2=b^2+d^2.
\]

**2. Gaussian limit of the beta mixing variable.** Use independent unit-rate gamma sums \(G_\alpha,G_\beta\) with integer shapes \(\alpha,\beta\), and write \(\Theta=G_\alpha/(G_\alpha+G_\beta)\). Since \(\alpha,\beta\to\infty\), both independent standardized gamma sums satisfy their ordinary central limit theorems. A first-order expansion of the ratio, uniform along sequences with \(p\) tending even to zero or one, gives
\[
 Z_M=\frac{\Theta-p}{\sqrt{pq/(A+1)}}
 =\sqrt q\frac{G_\alpha-\alpha}{\sqrt\alpha}
 -\sqrt p\frac{G_\beta-\beta}{\sqrt\beta}+o_{\mathbb P}(1).
\]
To verify the remainder without an interior-\(p\) assumption, express the exact ratio difference as
\[
 \Theta-p=\frac{q(G_\alpha-\alpha)-p(G_\beta-\beta)}{G_\alpha+G_\beta},
\]
whose denominator divided by \(A\) converges in probability to one. The coefficient square sum is \(p+q=1\). On any subsequence choose a further subsequence with \(p\to p_*\in[0,1]\); the linear combination tends to a standard normal. Subsequence compactness gives \(Z_M\Longrightarrow N(0,1)\) without requiring convergence of \(p\).

**3. The conditional-binomial component and asymptotic independence.** Assume \(\min\{mp,mq\}\to\infty\). Then \(mpq\to\infty\), and the beta variance identity implies
\[
\frac{\Theta}{p}\to1,\qquad\frac{1-\Theta}{q}\to1
\quad\text{in probability},
\]
because the respective relative variances are bounded by \(1/\alpha\) and \(1/\beta\). Thus \(m\Theta(1-\Theta)/(mpq)\to1\) in probability, and the conditional binomial success and failure means both diverge in probability. The conditional characteristic function of
\[
 Z_B=\frac{Y-m\Theta}{b}
\]
converges in probability to \(\exp(-t^2/2)\) for each fixed real \(t\). This follows directly by expanding \(m\log\{(1-\Theta)e^{-it\Theta/b}+\Theta e^{it(1-\Theta)/b}\}\); the cubic remainder is \(O_{\mathbb P}((mpq)^{-1/2})\), while its quadratic part tends to \(-t^2/2\). The conditional characteristic functions are bounded by one, so for every bounded continuous function \(f\),
\[
\mathbb E[f(Z_M)e^{itZ_B}]
- e^{-t^2/2}\mathbb E[f(Z_M)]\to0.
\]
Together with Step 2 this proves joint convergence of \((Z_B,Z_M)\) to independent standard normal variables.

Finally, the exact identity
\[
\frac{Y-\mu}{\sigma}=\frac{b}{\sigma}Z_B+\frac{d}{\sigma}Z_M
\]
has nonnegative squared weights adding to one. On every subsequence a further subsequence makes both weights converge; the resulting linear combination of independent standard normals is always standard normal. Therefore the original sequence has a standard Gaussian limit, even when \(m/A\) oscillates.

**4. Poisson boundary and necessity.** For any \(\alpha,\beta,m\), couple binomial variables having parameters \(\Theta\) and \(p\) using the same \(m\) independent uniforms. Then
\[
 d_{\mathrm{TV}}(\mathcal L(Y),\operatorname{Bin}(m,p))
 \le m\mathbb E|\Theta-p|
 \le m\sqrt{\frac{pq}{A+1}}
 \le \frac{mp}{\sqrt\alpha}.
\]
Le Cam's elementary Bernoulli–Poisson coupling gives \(d_{\mathrm{TV}}(\operatorname{Bin}(m,p),\operatorname{Pois}(mp))\le mp^2\), proving the explicit error. If \(mp\to\lambda<\infty\) while \(m,\alpha,\beta\to\infty\), then \(p\to0\) and the bound tends to zero. Also \(m/A=(mp)/\alpha\to0\), so \(\sigma^2\to\lambda\). For \(\lambda>0\), the standardized limit is the non-Gaussian law \((\operatorname{Pois}(\lambda)-\lambda)/\sqrt\lambda\). When \(\lambda=0\), Markov's inequality shows \(\Pr(Y\ne0)\le mp\to0\), and \(\mu/\sigma\to0\), proving weak convergence to the point mass at zero. Reflecting success and failure gives the \(mq\) conclusion.

If \(\min\{mp,mq\}\) fails to diverge, some subsequence has one of its two entries bounded, hence a further subsequence converging to finite \(\lambda\). On it the standardized law has the non-Gaussian limit just established, which is incompatible with convergence to a standard normal along the full sequence. This proves necessity and the equivalence.

## Verification

The companion `verify.py` uses exact fractions to compare the beta-binomial mass function with independent subset enumeration, normalizes all masses, and checks exact means and variances against the stated formulas for small populations. It also computes finite-parameter Gaussian Kolmogorov errors and beta-binomial–Poisson distances for representative large examples. These tests guard against counting or normalization errors; the infinite-sequence necessity and sufficiency follow from the proof, not finite numerics. Reproduce by running `python verify.py` in a clean Python 3 standard-library environment.

## Relationship to prior work

O'Neill's finite-population-order-statistic analysis (arXiv:2207.00270, originally public in 2022; journal version 2025) supplies the exact distribution, the beta-binomial mixture and moments. Its Theorems 6 and 7 prove Gaussian limits in two specified regimes: convergent interior sample and rank fractions, and a particular near-census extreme-rank path. Those statements do not classify all diverging-rank paths, including oscillating fractions; they do not provide the present necessary-and-sufficient expected-missing-count threshold and accompanying finite-mean Poisson alternative. These foundational identities and those two sufficient limits are not claimed as new.

Chatterjee's *Asymptotic properties of sample quantiles from a finite population* concerns quantile sampling with fixed interior quantile level in a continuous superpopulation setting. Li and Ding's finite-population central limit theorems apply to sample averages and related rank tests, rather than the all-parameter discrete order-statistic threshold. Khan's 1994 negative-hypergeometric generating-function paper is cited by O'Neill for the particular near-census limit; its complete text has not been independently examined here. Historical equivalence under negative-hypergeometric or beta-binomial language remains a genuine residual priority risk.

## Limitations

The precise scope requires both the rank and the reverse rank to diverge; fixed-rank boundary regimes are excluded and can have gamma or negative-binomial rather than Gaussian limits. The result treats a single marginal statistic only; it does not establish a multivariate joint quantile process, a finite-sample Gaussian rate, or uniform accuracy over all triangular paths. The remaining historical-priority uncertainty particularly concerns older negative-hypergeometric limit results. All conclusions are analytical and subject to independent scholarly assessment.

## References

1. B. O'Neill, *The distribution of order statistics under sampling without replacement*, arXiv:2207.00270 (first posted 1 July 2022), especially the distribution formula, beta-mixture representation and Theorems 6–7; published in *Journal of Statistical Theory and Applications* 24 (2025), 663–698, doi:10.1007/s44199-025-00125-y.
2. A. Chatterjee, *Asymptotic properties of sample quantiles from a finite population*, *Annals of the Institute of Statistical Mathematics* (2011), doi:10.1007/s10463-008-0210-4.
3. X. Li and P. Ding, *General forms of finite population central limit theorems with applications to causal inference*, arXiv:1610.04821 (2016).
4. R. A. Khan, *A note on the generating function of a negative hypergeometric distribution*, *Sankhyā*, Series B 56 (1994), 309–313, cited in O'Neill; full text not reviewed here.
