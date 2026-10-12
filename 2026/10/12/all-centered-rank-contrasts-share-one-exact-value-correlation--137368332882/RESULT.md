# All centered rank contrasts share one exact value-correlation
## Finding
Let
\[
X_1,\ldots,X_N,
\qquad N\ge2,
\]
be independent and identically distributed from a nondegenerate atomless distribution with finite variance
\[
\sigma^2=\operatorname{Var}(X_1)>0.
\]
Let \(R_i\) denote the rank of \(X_i\) among the \(N\) observations and write
\[
G=\mathbb E|X_1-X_2|
\]
for the population Gini mean difference.

For every nonzero deterministic contrast
\[
c=(c_1,\ldots,c_N),
\qquad
\sum_{i=1}^N c_i=0,
\]
define the value contrast and matching rank contrast
\[
V_c=\sum_{i=1}^N c_iX_i,
\qquad
T_c=\sum_{i=1}^N c_iR_i.
\]
Then
\[
\boxed{
\operatorname{Cov}(T_c,V_c)
=
\frac{NG}{4}\sum_{i=1}^Nc_i^2
}
\]
and
\[
\operatorname{Var}(T_c)
=
\frac{N(N+1)}{12}\sum_{i=1}^Nc_i^2,
\qquad
\operatorname{Var}(V_c)
=
\sigma^2\sum_{i=1}^Nc_i^2.
\]
Therefore every centered contrast direction has the same exact correlation:
\[
\boxed{
\operatorname{Corr}(T_c,V_c)
=
\frac{\sqrt3}{2}\frac{G}{\sigma}
\sqrt{\frac{N}{N+1}}
}.
\]
The value is independent of the contrast's direction, sparsity, and grouping pattern.

The continuous Gini-variance inequality
\[
G\le\frac{2\sigma}{\sqrt3}
\]
gives the sharp envelope
\[
\boxed{
0<\operatorname{Corr}(T_c,V_c)
\le
\sqrt{\frac{N}{N+1}}
}.
\]
The upper bound is attained exactly when the parent law is uniform on an interval, up to location and positive scale.

As a two-sample corollary, let \(X_1,\ldots,X_m\) and \(Y_1,\ldots,Y_n\) be independent samples from the same atomless parent, with \(N=m+n\), and define
\[
U=\sum_{i=1}^m\sum_{j=1}^n\mathbf1\{X_i<Y_j\},
\qquad
\Delta=\bar Y-\bar X.
\]
Then
\[
\boxed{
\operatorname{Cov}(U,\Delta)=\frac{NG}{4}
}
\]
and
\[
\boxed{
\operatorname{Corr}(U,\Delta)
=
\frac{\sqrt3}{2}\frac{G}{\sigma}
\sqrt{\frac{N}{N+1}}
}.
\]
Thus the exact null correlation between Mann-Whitney and the raw mean difference is allocation-invariant at fixed total sample size. For a uniform parent it equals \(\sqrt{N/(N+1)}\).

## Assumptions and scope
The parent distribution is atomless, nondegenerate, and has finite second moment. Atomlessness ensures almost surely unique ranks and makes \(F(X_1)\) uniform on \((0,1)\).

The contrast coefficients are deterministic and sum to zero. Non-centered coefficient vectors contain a sample-location component and are outside the isotropic contrast statement.

The theorem is a null-distribution identity for iid observations. It does not assert that the rank and value contrasts are jointly Gaussian or independent, and it does not compare power under alternatives.

## Proof
Let \(F\) be the common distribution function and \(\mu=\mathbb EX_1\). The rank has the representation
\[
R_i
=
1+\sum_{j\ne i}\mathbf1\{X_j<X_i\}.
\]
For a continuous distribution,
\[
G
=
4\operatorname{Cov}(X_1,F(X_1))
=
4\left(\mathbb E[X_1F(X_1)]-\frac\mu2\right).
\]
Consequently the diagonal rank-value covariance is
\[
\operatorname{Cov}(X_i,R_i)
=
(N-1)\operatorname{Cov}(X_1,F(X_1))
=
\frac{(N-1)G}{4}.
\]
By exchangeability, for \(i\ne j\) the covariance
\[
b=\operatorname{Cov}(X_i,R_j)
\]
is constant. Since the rank sum is deterministic,
\[
\sum_{j=1}^NR_j=\frac{N(N+1)}2,
\]
we have
\[
0
=
\operatorname{Cov}\!\left(X_i,\sum_jR_j\right)
=
\frac{(N-1)G}{4}+(N-1)b.
\]
Thus
\[
b=-\frac G4.
\]

Now expand the contrast covariance. Because \(\sum_i c_i=0\),
\[
\sum_{i\ne j}c_ic_j
=
-\sum_i c_i^2.
\]
Therefore
\[
\begin{aligned}
\operatorname{Cov}(T_c,V_c)
&=
\sum_i c_i^2\frac{(N-1)G}{4}
+
\sum_{i\ne j}c_ic_j\left(-\frac G4\right)\\
&=
\frac{NG}{4}\sum_i c_i^2.
\end{aligned}
\]

Independence of the values gives immediately
\[
\operatorname{Var}(V_c)
=
\sigma^2\sum_i c_i^2.
\]
The rank vector is a uniform random permutation of \(1,\ldots,N\). Hence
\[
\operatorname{Var}(R_i)=\frac{N^2-1}{12},
\qquad
\operatorname{Cov}(R_i,R_j)=-\frac{N+1}{12}
\quad(i\ne j).
\]
Using the zero-sum identity once more,
\[
\operatorname{Var}(T_c)
=
\frac{N(N+1)}{12}\sum_i c_i^2.
\]
Dividing the covariance by the two standard deviations proves the common correlation formula.

For the sharp upper bound, \(F(X_1)\) is uniform on \((0,1)\), so
\[
\operatorname{Var}(F(X_1))=\frac1{12}.
\]
Cauchy-Schwarz applied to
\[
G=4\operatorname{Cov}(X_1,F(X_1))
\]
gives
\[
G\le\frac{2\sigma}{\sqrt3}.
\]
Equality in Cauchy-Schwarz requires
\[
X_1-\mu=a\left(F(X_1)-\frac12\right)
\]
almost surely for some positive \(a\). Since \(F(X_1)\) is uniform, this is exactly the uniform distribution on an interval up to affine location and positive scale.

For the two-sample statement, use the pooled sample and the contrast coefficients
\[
c_i=-\frac1m
\]
for the \(X\)-observations and
\[
c_i=\frac1n
\]
for the \(Y\)-observations. Then \(V_c=\Delta\) and
\[
\sum_i c_i^2=\frac{N}{mn}.
\]
If \(W_Y\) is the pooled rank sum of the \(Y\)-sample, then
\[
U=W_Y-\frac{n(n+1)}2
\]
and
\[
T_c=rac{N}{mn}\left(U-\frac{mn}{2}\right).
\]
Substitution into the general contrast identity yields
\[
\operatorname{Cov}(U,\Delta)=\frac{NG}{4}
\]
and the allocation-free correlation formula.

## Verification
The accompanying `checker.py` performs three independent exact-rational checks.

First, for uniform samples and every \(2\le N\le8\), it enumerates every rank permutation for several qualitatively different zero-sum contrasts. Conditional order-statistic means reconstruct the rank-value covariance and are compared with the closed formula.

Second, for every \(2\le N\le12\) and every two-sample split \(m+n=N\), it enumerates all pooled-rank allocations and verifies the Mann-Whitney covariance and correlation formulas under a uniform parent.

Third, for the family with distribution function \(F(x)=x^k\) on \([0,1]\), \(1\le k\le500\), it checks the exact Gini-variance inequality and its unique uniform equality case using rational moments.

These finite checks supplement the all-distribution analytic proof; they do not replace it.

## Relationship to prior work
Stuart studied the correlation between an individual observation and its own rank in samples from a continuous distribution. Maturi and Elsayigh reproduce the resulting single-coordinate formula explicitly and apply it to a fourth-power exponential model. That formula supplies the diagonal entry of the rank-value cross-covariance matrix; it does not state the zero-sum contrast operator, its isotropy on the full contrast space, or the two-sample allocation invariance proved here.

Weber and Sawilowsky compare the independent-samples \(t\)-test, its permutation version, and the Wilcoxon rank-sum test by Type I error and power. Their complete article treats the practical comparison of rank and mean-based procedures but does not give their exact joint null covariance.

Kössler and Kumar develop an adaptive two-sample location test built from U-statistics and explicitly include Wilcoxon-Mann-Whitney procedures. The accessible abstract does not state a joint law with the sample mean difference.

The ingredients that ranks form a random permutation and that the Gini mean difference equals four times \(\operatorname{Cov}(X,F(X))\) are classical. The structural finding here is their combination into a scalar covariance operator on the entire centered contrast subspace.

## Limitations
The atomless assumption is essential to the stated rank covariance matrix. Ties require midranks or randomized ranks and introduce atom corrections.

The theorem concerns deterministic linear contrasts. Nonlinear rank statistics and studentized value contrasts require additional terms.

Stuart's 1954 paper is the closest historical source located for rank-value correlation. Its publisher abstract and the exact formula reproduced in later full text were inspected, but a complete article text was not available through the retrieval paths used here. Classical linear-rank literature could therefore contain an equivalent contrast-space formulation under different notation.

## References
1. T. A. Maturi and A. Elsayigh, “The Correlation between Variate-Values and Ranks in Samples from Complete Fourth Power Exponential Distribution,” *Journal of Mathematics Research* 1 (2009), DOI: 10.5539/jmr.v1n1p14.
2. A. Stuart, “The Correlation between Variate-Values and Ranks in Samples from a Continuous Distribution,” *British Journal of Statistical Psychology* 7 (1954), DOI: 10.1111/j.2044-8317.1954.tb00138.x.
3. M. D. Weber and S. S. Sawilowsky, “Comparative Power of the Independent t, Permutation t, and Wilcoxon Tests,” *Journal of Modern Applied Statistical Methods* 8 (2009), DOI: 10.22237/jmasm/1241136120.
4. W. Kössler and N. Kumar, “An Adaptive Test for the Two-Sample Location Problem Based on U-Statistics,” *Communications in Statistics—Theory and Methods*, DOI: 10.1080/03610910801983152.
5. H. B. Mann and D. R. Whitney, “On a Test of Whether One of Two Random Variables Is Stochastically Larger than the Other,” *Annals of Mathematical Statistics* 18 (1947), DOI: 10.1214/aoms/1177730491.
