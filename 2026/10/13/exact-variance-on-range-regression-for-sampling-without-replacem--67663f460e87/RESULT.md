# Exact variance-on-range regression for sampling without replacement
## Finding
Draw a simple random sample without replacement of size \(n\) from the consecutive integer population
\[
\{0,1,\ldots,M\},
\qquad
2\le n\le M+1.
\]
Let
\[
R=X_{(n)}-X_{(1)}
\]
be the sample range, and let
\[
S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
\]
be the unbiased sample variance.

For every feasible integer
\[
n-1\le r\le M,
\]
the conditional mean is
\[
\boxed{
\mathbb E[S^2\mid R=r]
=
\frac{r(n+1)\bigl((n+2)r-(n-2)\bigr)}
{12n(n-1)}.
}
\]
Equivalently,
\[
\boxed{
\frac{\mathbb E[S^2\mid R=r]}{r^2}
=
\frac{(n+1)(n+2)}{12n(n-1)}
-
\frac{(n+1)(n-2)}{12n(n-1)r}.
}
\]

The formula is independent of \(M\). Thus, once the observed lattice range is fixed, the ambient population contributes no further parameter to the expected sample variance. The second displayed term is the exact finite-lattice correction to the continuous-uniform quadratic range regression.

## Assumptions and scope
The population consists of consecutive equally spaced points. By location-scale equivariance, the same formula holds for any arithmetic progression after multiplying the right-hand side by the squared lattice spacing.

Sampling is uniform without replacement and the variance uses the unbiased divisor \(n-1\). The theorem does not claim the same regression for a nonuniform finite population, unequal inclusion probabilities, sampling with replacement, or a non-arithmetic support.

## Proof
Condition first on
\[
X_{(1)}=a,\qquad X_{(n)}=a+r.
\]
After translation by \(a\), the two extremes become \(0\) and \(r\). The remaining
\[
k=n-2
\]
sample points form a simple random sample without replacement from
\[
\{1,\ldots,r-1\}.
\]
This conditional law depends on \(n\) and \(r\), but not on \(a\) or \(M\).

Let the interior sample be \(Y_1,\ldots,Y_k\), and put
\[
T_1=\sum_{\ell=1}^kY_\ell,
\qquad
T_2=\sum_{\ell=1}^kY_\ell^2.
\]
For the finite population \(\{1,\ldots,r-1\}\),
\[
\mathbb E T_1=\frac{kr}{2}
\]
and
\[
\mathbb E T_2
=
k\frac{r(2r-1)}6.
\]
The population variance, with denominator \(r-1\), is
\[
\frac{r(r-2)}{12}.
\]
The usual finite-population variance formula for a sample sum gives
\[
\operatorname{Var}(T_1)
=
\frac{k\,r(r-n+1)}{12}.
\]
The expression remains valid at the degenerate boundary where all interior points are selected.

For the full translated sample, write
\[
T=r+T_1
\]
for the sum and
\[
Q=r^2+T_2
\]
for the sum of squares. Then
\[
\mathbb ET=\frac{nr}{2},
\]
and
\[
\mathbb ET^2
=
\frac{n^2r^2}{4}
+
\frac{(n-2)r(r-n+1)}{12}.
\]
Also
\[
\mathbb EQ
=
r^2
+
(n-2)\frac{r(2r-1)}6.
\]
Since
\[
S^2=\frac{Q-T^2/n}{n-1},
\]
substitution and simplification give
\[
\mathbb E[S^2\mid X_{(1)}=a,X_{(n)}=a+r]
=
\frac{r(n+1)\bigl((n+2)r-(n-2)\bigr)}
{12n(n-1)}.
\]
The right-hand side is independent of \(a\). Averaging over the possible minima conditional on \(R=r\) therefore proves the stated regression.

Dividing by \(r^2\) yields the normalized form. Its leading coefficient is exactly the continuous-uniform coefficient, while the additional negative term is of order \(1/r\).

## Verification
The accompanying `checker.py` exhaustively enumerates every subset of every consecutive integer population
\[
\{0,\ldots,M\},
\qquad
2\le M\le17,
\]
for every admissible sample size. Within each range stratum it computes the exact rational conditional mean of the unbiased sample variance and compares it with the closed formula.

The checker uses integer enumeration and `fractions.Fraction`; no floating-point approximation enters the verification. The finite census supplements, rather than replaces, the all-parameter proof.

## Relationship to prior work
Takahasi and Futatsuya study dependence between order statistics under simple random sampling without replacement from a finite population. Their work supplies the natural finite-population order-statistic setting.

Balakrishnan, Charalambides, and Papadatos derive sharp bounds for expectations of finite-population order statistics and the sample range, with additional covariance results in the two-observation case. The accessible abstract does not state a conditional sample-variance regression given the range.

For independent continuous uniform sampling, endpoint normalization makes the sample shape independent of the extrema and yields a purely quadratic conditional variance-on-range regression. The present without-replacement lattice model has a different conditional interior law. Its exact regression contains a nonzero linear correction and therefore is not obtained by simply substituting a discrete range into the continuous formula.

## Limitations
The exact regression depends essentially on the arithmetic-progression population. A general ordered finite population has range-dependent interior geometry and need not admit a formula involving only \(n\) and \(r\).

The most directly relevant 2003 finite-population range paper could be inspected at abstract and metadata level, but a complete article text was not available through the retrieval paths used here. An equivalent identity buried in older finite-population sampling literature therefore remains a residual originality risk.

## References
1. K. Takahasi and M. Futatsuya, “Dependence between order statistics in samples from finite population and its application to ranked set sampling,” *Annals of the Institute of Statistical Mathematics* 50 (1998). DOI: 10.1023/A:1003497213823.
2. N. Balakrishnan, C. Charalambides, and N. Papadatos, “Bounds on expectation of order statistics from a finite population,” *Journal of Statistical Planning and Inference* 113 (2003), 569–588. DOI: 10.1016/S0378-3758(01)00321-4.
