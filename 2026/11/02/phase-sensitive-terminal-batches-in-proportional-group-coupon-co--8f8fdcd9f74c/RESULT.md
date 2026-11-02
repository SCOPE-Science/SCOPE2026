# Phase-sensitive terminal batches in proportional group coupon collection

## Finding

Suppose each round of coupon collection draws a uniformly random fixed-size subset comprising asymptotically a proportion \(c\in(0,1)\) of all types. The number of different types first discovered **in the last, collection-completing round** has no ordinary limiting distribution: its probabilities retain a nonconstant phase in \(\log_{1/(1-c)} n\). Along every convergent phase subsequence its exact distribution is described below. Averaging over coupon counts with logarithmic weights yields the logarithmic-series law with parameter \(c\), including an exact averaged probability of a unique final type.

Put \(q=1-c\) and \(a=-\log q\). For each integer \(n\), independently draw uniformly chosen subsets of size \(d_n=\lfloor cn\rfloor\) from \(\{1,\ldots,n\}\), independently between rounds. Let \(\tau_i\) be the first round in which coupon \(i\) occurs. Define
\[
 T_n=\max_{1\le i\le n}\tau_i,\qquad B_n=\#\{i:\tau_i=T_n\},\qquad t_n=\left\lfloor\frac{\log n}{a}\right\rfloor,
 \quad\alpha_n=\frac{\log n}{a}-t_n.
\]

For each integer \(r\ge1\), define the positive, absolutely convergent periodic profile
\[
 H_{c,r}(\alpha)=\frac{c^r}{r!}\sum_{k\in\mathbb Z}q^{r(k-\alpha)}\exp(-q^{k-\alpha}),\qquad \alpha\in\mathbb R.
\]
Then
\[
 \Pr(B_n=r)=H_{c,r}(\alpha_n)+o(1).
\]
Each \(H_{c,r}\) is continuous, strictly positive, one-periodic and **nonconstant**. With the Fourier convention \(\widehat H(m)=\int_0^1 H(\alpha)e^{-2\pi im\alpha}\,d\alpha\),
\[
 \boxed{\widehat H_{c,r}(m)=\frac{c^r}{a\,r!}\,\Gamma\!\left(r-\frac{2\pi i m}{a}\right),\quad m\in\mathbb Z.}
\]
In particular no \(\Pr(B_n=r)\) converges as \(n\to\infty\). The logarithmic Cesàro average exists and is exactly
\[
 \boxed{\lim_{N\to\infty}\frac{1}{\log N}\sum_{n=2}^N\frac{\Pr(B_n=r)}{n}=\frac{c^r}{a r},\qquad r\ge1.}
\]
These masses sum to one and form the logarithmic-series probability law. The averaged probability that exactly one coupon is discovered in the completing round is \(c/[-\log(1-c)]\).

More precisely, along any sequence with \(\alpha_n\to\alpha\in[0,1]\), for each finite set of integer offsets \(K\), the counts
\[
 N_{n,k}=\#\{i:\tau_i=t_n+k\},\qquad k\in K,
\]
converge jointly to mutually independent Poisson variables of respective means \(c q^{k-1-\alpha}\). Consequently, for fixed integers \(k\) and \(r\ge1\),
\[
 \boxed{\Pr(T_n-t_n=k,\ B_n=r)\longrightarrow
   \exp(-q^{k-1-\alpha})\frac{(c q^{k-1-\alpha})^r}{r!}.}
\]
This joint limit describes the terminal discovery round and its multiplicity, not just the waiting-time distribution.

## Assumptions and scope

Throughout, \(0<c<1\) is fixed, \(n\) tends through positive integers, \(d_n=\lfloor cn\rfloor\), and we consider only sufficiently large \(n\) with \(1\le d_n<n\). Within a round the \(d_n\) coupons are distinct; the subsets chosen in different rounds are independent. All first-discovery times are positive integers. The limiting statements for a fixed multiplicity \(r\) are not claimed uniformly when \(r\) grows with \(n\). No endpoint claim is made for \(c=0\) or \(c=1\).

## Proof

**1. Joint late first-discovery intensities.** Set \(c_n=d_n/n\) and \(q_n=1-c_n\); both differ from \(c,q\), respectively, by \(O(n^{-1})\). For any fixed collection of \(R\) distinct coupon labels, the probability that a single uniform group contains one particular specified \(s\)-subset of these labels and omits the remaining \(u=R-s\) specified labels is exactly
\[
 \frac{(d_n)_{\underline{s}}(n-d_n)_{\underline{u}}}{(n)_{\underline{R}}}
 =c_n^s q_n^u\bigl(1+O_R(n^{-1})\bigr).
\]
This formula holds uniformly over the finitely many choices of the specified selected set, for fixed \(R\). Its right side is the probability of the corresponding pattern for \(R\) independent Bernoulli-\(c_n\) selections. To require specified distinct labels to make their first appearance at prescribed rounds \(t_n+k_1,\ldots,t_n+k_R\), every round before the latest of these prescribes, for each relevant label, whether it is still absent or first appears there. The remaining labels can be ignored after their first appearance. Across the \(O(\log n)\) relevant rounds, the exact probability of these prescriptions therefore differs from the independent geometric first-arrival probability by the relative factor
\[
 1+O_R\!\left(\frac{\log n}{n}\right).
\]
For fixed integer offsets \(k_1,\ldots,k_R\), the reference probability is \(\prod_{j=1}^R c_n q_n^{t_n+k_j-1}\). Moreover,
\[
 n c_n q_n^{t_n+k-1}\longrightarrow c q^{k-1-\alpha}
\]
along any subsequence with \(\alpha_n\to\alpha\), since \((\log n)(\log q_n-\log q)\to0\). For a finite set of distinct offsets and any prescribed nonnegative factorial-moment orders, exchangeability and the preceding relative estimate give
\[
 \mathbb E\prod_{k\in K}(N_{n,k})_{\underline{r_k}}
 \longrightarrow\prod_{k\in K}(c q^{k-1-\alpha})^{r_k}.
\]
These are the mixed factorial moments of independent Poisson variables. The latter joint distribution is moment-determinate (its multivariate moment-generating function is finite everywhere), so the claimed finite-dimensional joint convergence follows.

**2. Last-discovery tightness and the terminal-batch probability.** Let \(U_{n,t}=\#\{i:\tau_i>t\}\) be the number of unseen coupon types after \(t\) rounds. For every fixed positive integer \(R\), its exact falling factorial moment is
\[
 \mathbb E(U_{n,t})_{\underline R}
 =(n)_{\underline R}\left[\frac{(n-d_n)_{\underline R}}{(n)_{\underline R}}\right]^t.
\]
For \(t=t_n+k\) with fixed \(k\), this tends to \((q^{k-\alpha})^R\), so \(U_{n,t_n+k}\Rightarrow\operatorname{Poisson}(q^{k-\alpha})\). In particular,
\[
 \Pr(T_n\le t_n+k)\longrightarrow\exp(-q^{k-\alpha}).
\]
To show the completion offset cannot escape to either infinity, the union bound gives
\[
 \limsup_{n\to\infty}\Pr(T_n>t_n+K)\le q^{K-1}
\]
for positive \(K\), and for negative offsets the displayed Poisson limit implies
\[
 \limsup_{n\to\infty}\Pr(T_n\le t_n-K)=\exp(-q^{-K-\alpha})\le\exp(-q^{-K}).
\]
Both right sides tend to zero as \(K\to\infty\). At any fixed offset \(k\), \(T_n=t_n+k\) and \(B_n=r\) mean precisely that \(N_{n,k}=r\) and all \(N_{n,j}\) with \(j>k\) vanish. First impose this condition only through a fixed large \(k+K\), apply the joint Poisson limit from Step 1, and remove the truncation using the upper tightness bound. Since
\[
 \sum_{j\ge k}c q^{j-1-\alpha}=q^{k-1-\alpha},
\]
the resulting joint mass is
\[
 \exp(-q^{k-1-\alpha})\frac{(c q^{k-1-\alpha})^r}{r!}.
\]
Summing over \(k\) is justified by the two-sided tightness bounds, proving \(\Pr(B_n=r)\to H_{c,r}(\alpha)\) along the chosen subsequence. Notice that summing the joint mass over \(r\ge1\) gives
\(e^{-q^{k-\alpha}}-e^{-q^{k-1-\alpha}}\), whose sum over all integers \(k\) equals one. Reindexing \(k\) by one yields the stated profile formula. Because every sequence of phases has a convergent subsequence in \([0,1]\) and the profiles are continuous with matching endpoints, the uniform-in-phase asymptotic \(\Pr(B_n=r)=H_{c,r}(\alpha_n)+o(1)\) follows by contradiction and compactness.

**3. Fourier coefficients and genuine nonconvergence.** The series for \(H_{c,r}\) converges uniformly on compact phase intervals. Its positive-index terms form a geometric tail, while negative-index terms decay superexponentially. Periodicity follows by shifting the integer summation index. Unfolding the Fourier integral, using the substitution \(x=k-\alpha\) and then \(z=q^x=e^{-ax}\), gives
\[
 \begin{split}
 \widehat H_{c,r}(m)
 &=\frac{c^r}{r!}\int_{-\infty}^{\infty}
          e^{-arx}e^{-e^{-ax}}e^{2\pi imx}\,dx\\
 &=\frac{c^r}{a\,r!}\int_0^{\infty}
          z^{r-1-2\pi im/a}e^{-z}\,dz
  =\frac{c^r}{a\,r!}\Gamma\!\left(r-\frac{2\pi im}{a}\right).
 \end{split}
\]
The Gamma function has no zeros, so every nonzero Fourier coefficient is nonzero, proving each profile is nonconstant. To realize any prescribed limiting phase \(\alpha\in[0,1)\), choose integer coupon counts nearest to \(\exp(a(j+\alpha))\) as \(j\to\infty\), with minor one-sided rounding at \(\alpha=0\). Hence the nonconstant profiles yield distinct subsequential probability limits and ordinary convergence fails.

**4. Logarithmic mixing.** For any continuous periodic \(f\), elementary integral comparison and the change of variables \(u=\log x\) show
\[
 \frac1{\log N}\sum_{n=2}^N\frac{f(\{\log n/a\})}{n}
 \longrightarrow\int_0^1 f(u)\,du.
\]
Indeed the normalized weighted sum differs by \(o(1)\) from \((\log N)^{-1}\int_{\log2}^{\log N} f(\{u/a\})\,du\), an average over increasingly many complete periods of length \(a\). A pointwise error \(o(1)\) in the profile approximation is negligible under these logarithmic weights. Evaluating the zero Fourier coefficient and using \(\Gamma(r)=(r-1)!\) now gives
\[
 \int_0^1H_{c,r}(u)\,du=\frac{c^r}{a\,r}.
\]
Finally \(\sum_{r\ge1}c^r/r=-\log(1-c)=a\), so these averaged masses constitute a probability distribution. This completes the proof.

## Verification

The standalone standard-library Python checker `verify.py` compares, for all \(3\le n\le7\) and all possible nonempty proper group sizes, direct exact-rational subset-process enumeration to the independent inclusion–exclusion formula
\[
 \Pr(T_n=t,B_n=r)
 =\binom nr\frac{\binom{n-r}{d_n-r}}{\binom n{d_n}}
 \sum_{j=0}^{n-r}(-1)^j\binom{n-r}{j}
 \left(\frac{\binom{n-r-j}{d_n}}{\binom n{d_n}}\right)^{t-1},
\]
with inadmissible binomial coefficients interpreted as zero. It also checks Poisson-phase normalization, numerically integrates several phase profiles against the logarithmic-series probabilities, and checks a Fourier coefficient using the identity \(|\Gamma(1+iy)|^2=\pi y/\sinh(\pi y)\). Replaying the checker produces `verify_output.txt` reporting **365 passed assertions**. These finite checks do not certify the limit theorem independently; Steps 1–4 supply the proofs of the infinite statements.

For illustration at \(c=0.9\), the asymptotic probability of a unique final type equals approximately \(0.4228450039\) at phase \(0\) and \(0.3586455548\) at phase \(1/2\). Its logarithmic average is \(0.9/\log10\), approximately \(0.3908650337\).

## Relationship to prior work

Berend and Sher (2026, arXiv:2605.06953v1) derive sharp expected completion times and phase behavior for group sizes proportional to the total coupon count; their Proposition 3.2 analyzes the number of *unseen* coupons at a specified round. The present theorem concerns the distinct marked sequence of **first-discovery counts by round**, the number of simultaneous first appearances in the completing round, its full phase-dependent distribution, and the logarithmic-series mixing law. A single-round deficit limit alone does not give independent discovery counts at several rounds or their final multiplicity.

Schilling and Henze (2021) establish Poisson limits for counts under fixed-size group drawings and related completion-time results. Betken and Thäle (2023) treat error bounds for marginal occupancy-count limits. Stadje (1990) contains classical finite-group collector formulas. These foundational studies motivate the problem; the present proof gives the separate multitime marked limit and terminal-batch laws in the proportional regime. The 1990 article was not available for full-text examination, so possible implicit prior formulations remain a priority risk.

## Limitations

The result is proved only for independent, uniformly chosen subsets with fixed limiting fraction \(c\in(0,1)\). It does not cover biased packages, correlated rounds, fractions tending to either endpoint, or multiplicities growing with \(n\). It provides pointwise fixed-multiplicity and finite-dimensional limits rather than a claim of full process convergence in a particular infinite-dimensional topology. The originality assessment is provisional because not every historical group-collection source was accessible in full; independent mathematical validation and final priority assessment have not been performed.

## References

1. D. Berend and T. Sher, *Asymptotic Results for Uniform Group Drawing in the Coupon Collector's Problem*, arXiv:2605.06953v1, 7 May 2026, https://arxiv.org/html/2605.06953v1 .
2. J. Schilling and N. Henze, *Two Poisson limit theorems for the coupon collector's problem with group drawings*, Journal of Applied Probability 58 (2021), 966–977, DOI: 10.1017/jpr.2021.15.
3. M. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, Journal of Applied Probability 60 (2023), 1352–1366, https://doi.org/10.1017/jpr.2023.6 .
4. W. Stadje, *The collector's problem with group drawings*, Advances in Applied Probability 22 (1990), 866–882, DOI: 10.2307/1427566 (abstract available; full text not inspected).
