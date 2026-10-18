# Sharp infinite-divisibility threshold for zero-inflated negative-binomial laws of integer shape

## Finding

Let \(m\ge1\) be an integer and let \(0<q,w<1\). Suppose \(X\) has the zero-inflated negative-binomial law
\[
\Pr(X=k)=w\mathbf 1_{\{k=0\}}+(1-w)\binom{k+m-1}{m-1}(1-q)^m q^k,\quad k=0,1,\ldots.
\]
Set
\[
c=(1-q)\left(\frac{1-w}{w}\right)^{1/m}.
\]
Then the following is an exact if-and-only-if classification:
\[
\boxed{X\text{ is infinitely divisible under convolution}\ \Longleftrightarrow\ c\ge 2\cos(\pi/m).}
\]
In particular, all such laws are infinitely divisible for shapes \(m=1,2\). For every integer \(m\ge3\), the sharp admissible structural-zero weight is
\[
\boxed{0<w\le w_*(m,q):=\left[1+\left(\frac{2\cos(\pi/m)}{1-q}\right)^m\right]^{-1}.}
\]
Within this range the law admits an explicit compound-Poisson representation with jump intensities
\[
\nu_k=\frac{1}{k}\left[mq^k-\sum_{j=0}^{m-1}\left(\frac{q}{1-ce^{i(2j+1)\pi/m}}\right)^k\right],\quad k\ge1.
\]
These intensities are real, nonnegative, and summable. Above the threshold (for \(m\ge3\)) at least one logarithmic coefficient is negative, so no compound-Poisson representation exists.

## Assumptions and scope

The negative-binomial parameterization uses the probability-generating function \(((1-q)/(1-qz))^m\), corresponding to a count supported on all nonnegative integers. The zero weight \(w\) is the probability of adding an independent structural zero, not the total probability at zero. The classification covers all positive integer shapes and all interior \(q,w\) simultaneously. Infinite divisibility means that for every positive integer the law can be expressed as that many identically distributed independent summands. For laws supported on the nonnegative integers, this is equivalent to being compound Poisson with positive integer jumps. The degenerate endpoints \(w=0,1\) are excluded from the parameter domain.

## Proof

**1. Factorization and unique logarithmic coefficients.** The generating function is
\[
G(z)=w+(1-w)\left(\frac{1-q}{1-qz}\right)^m
=\frac{w[(1-qz)^m+c^m]}{(1-qz)^m}.
\]
For \(\theta_j=(2j+1)\pi/m\), \(0\le j<m\), factor the numerator as
\[
(1-qz)^m+c^m=\prod_{j=0}^{m-1}(1-qz-ce^{i\theta_j}).
\]
With \(\lambda_j=q/(1-ce^{i\theta_j})\), this gives \(G(z)=G(0)\prod_j(1-\lambda_jz)/(1-qz)^m\), and therefore, as a formal Taylor expansion at zero,
\[
\log G(z)-\log G(0)=\sum_{k\ge1}\frac{mq^k-\sum_j\lambda_j^k}{k}z^k.
\]
The coefficients are real because the complex roots occur in conjugate pairs. They are uniquely determined by the law.

**2. Sufficiency including equality.** Among the angles \(\theta_j\), the largest cosine is \(\cos(\pi/m)\). Thus
\[
\min_j|1-ce^{i\theta_j}|^2=1+c^2-2c\cos(\pi/m).
\]
For positive \(c\), this minimum is at least one exactly when \(c\ge2\cos(\pi/m)\). This includes every positive \(c\) when \(m=1\) or \(m=2\). Under that condition, each \(|\lambda_j|\le q<1\), hence
\[
\sum_j\lambda_j^k\le\left|\sum_j\lambda_j^k\right|\le\sum_j|\lambda_j|^k\le mq^k
\]
and \(\nu_k\ge0\) for all positive integers \(k\). Moreover \(0\le\nu_k\le 2mq^k/k\), so the intensity series converges at one. Since \(G(1)=1\), we have \(\log G(0)=-\sum_{k\ge1}\nu_k\); consequently
\[
G(z)=\exp\left(\sum_{k\ge1}\nu_k(z^k-1)\right),
\]
which is the probability-generating function of a compound-Poisson law with independent Poisson counts of jumps of size \(k\), having rates \(\nu_k\). Equality at the threshold is included because the bounds are non-strict.

**3. Necessity.** Failure of the displayed inequality can happen only for \(m\ge3\). If \(0<c<2\cos(\pi/m)\), the numerator has a zero at
\[
z_0=(1-ce^{i\pi/m})/q,\qquad R=|z_0|<1/q.
\]
The minimum over all numerator-zero moduli is \(R\), by the cosine computation above. None of the numerator zeros cancels the pole at \(1/q\) because \(c>0\). Therefore the Taylor series \(F(z)=\log G(z)-\log G(0)=\sum_{k\ge1}\nu_k z^k\) has finite radius of convergence exactly \(R\) (a nonzero numerator zero makes the logarithm singular).

Suppose for contradiction that every \(\nu_k\ge0\). Pringsheim's theorem for power series with nonnegative coefficients and finite radius then forces a singularity of \(F\) at the positive real point \(z=R\). But \(0<R<1/q\), and the explicit function \(G\) is strictly positive and analytic on the positive interval from zero to \(1/q\); in particular, it is nonzero and has an analytic logarithm near \(R\), a contradiction. Hence at least one \(\nu_k<0\). A nonnegative-integer-valued infinitely divisible law must be compound Poisson, whose logarithmic coefficients at positive powers are its nonnegative jump rates. The unique negative coefficient therefore rules out infinite divisibility.

For completeness, Pringsheim's fact follows by contradiction: if a nonnegative-coefficient series were analytic at its positive convergence radius, then its Taylor expansion there, with derivative values equal to termwise nonnegative limits from below, would converge at some larger positive point. Interchanging these nonnegative sums would force the original power series to converge beyond its radius.

**4. Conversion to an inflation threshold.** For \(m\ge3\), both \(1-q\) and \(2\cos(\pi/m)\) are positive, and solving \(c\ge2\cos(\pi/m)\) for \(w\) yields precisely the bound in the finding. For \(m=3\) and \(q=1/2\), the exact threshold is \(w_*=1/9\); for \(m=4\) and \(q=1/2\), it is \(w_*=1/65\). These are genuine phase transitions rather than numerical estimates.

## Verification

A standalone standard-library Python checker `verify.py` computes the coefficients of \(\log G\) using exact rational arithmetic, independently of complex-root numerical approximations. It applies
\[
\nu_k=\frac{kp_k-\sum_{j=1}^{k-1}j\nu_jp_{k-j}}{kp_0},\quad p_k=\Pr(X=k),
\]
for positive \(k\). Execution completed successfully on 126 rational parameter configurations, through degree 85 (and through degree 120 for six boundary configurations). It checked nonnegative coefficients on the predicted infinitely divisible side, negative coefficients on selected forbidden-side cases, and both exact equalities at \(w=1/9\) for shape three and \(w=1/65\) for shape four. These finite checks support, but do not replace, the all-parameter analytical proof above. Running `python verify.py` reproduces them without external packages.

## Relationship to prior work

Zero-inflated and zero-modified negative-binomial counts and their mixture interpretation are established statistical models; see the distribution-theory survey by Xekalaki (2014) and Bar-Lev and Ridder (2020). Standard discrete infinite divisibility is characterized through nonnegative compound-Poisson jump intensities; the signed Lévy-measure perspective and general integer-valued criteria are discussed by Berger and Lindner (arXiv:2011.08530v1, 2020). These general results provide the framework but do not, in the material inspected, give a closed zero-inflation boundary for each integer negative-binomial shape. Puri and Goldie (1979) develop a much broader theory of infinite divisibility for Poisson mixtures; its inaccessible full text remains an originality risk, rather than evidence of noncoverage. The present statement is the explicit sharp phase classification for this named family, not a new characterization of general discrete infinite divisibility.

## Limitations

The theorem is restricted to positive integer negative-binomial shapes; it does not cover arbitrary positive real shape or zero deflation. A positive inflation weight may destroy infinite divisibility for shapes at least three, but this does not imply nonexistence of other stochastic representations or count-regression uses. The inverse logarithmic coefficients are derived in a neighborhood of zero; their possible nonconvergence at one outside the classified domain is not used to make an invalid compound-Poisson claim. The general mixed-Poisson literature, particularly the inaccessible 1979 Puri–Goldie article, has not been exhaustively ruled out as containing an equivalent special case. Novelty therefore remains subject to independent literature assessment.

## References

- Berger, D. and Lindner, A. (2020). *A Cramér–Wold device for infinite divisibility of integer-valued distributions*. arXiv:2011.08530v1, 17 November 2020. https://arxiv.org/html/2011.08530v1 . Primary MSC 60E07.
- Bar-Lev, S. K. and Ridder, A. (2020). *Exponential Dispersion Models for Overdispersed Zero-Inflated Count Data*. arXiv:2003.13854. https://arxiv.org/abs/2003.13854 .
- Xekalaki, E. (2014). *On the distribution theory of over-dispersion*. Journal of Statistical Distributions and Applications 1, article 19. https://doi.org/10.1186/s40488-014-0019-z .
- Puri, P. S. and Goldie, C. M. (1979). *Poisson mixtures and quasi-infinite divisibility of distributions*. Journal of Applied Probability 16, 138–153. https://doi.org/10.2307/3213382 . Full text not accessible in this review.
