# Exact range projection of sample variance under a uniform law
## Finding
Let \(X_1,\ldots,X_n\) be independent and identically distributed with the continuous uniform law \(\operatorname{Unif}[a,b]\), where \(a<b\), and put \(\ell=b-a\). For \(n\ge2\), define the sample range and unbiased sample variance by
\[
R=X_{(n)}-X_{(1)},\qquad
S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2.
\]
Then the exact conditional regression of sample variance on the range is
\[
\mathbb E[S^2\mid R]
=c_nR^2,\qquad
c_n=\frac{(n+1)(n+2)}{12n(n-1)}.
\]
Consequently
\[
\widehat V_R=c_nR^2
\]
is an unbiased estimator of the population variance \(\ell^2/12\). Its variance is
\[
\operatorname{Var}(\widehat V_R)
=\ell^4\frac{2n^2+6n+1}{36n(n-1)(n+3)(n+4)},
\]
whereas
\[
\operatorname{Var}(S^2)
=\ell^4\frac{2n+3}{360n(n-1)}.
\]
Hence
\[
\frac{\operatorname{Var}(\widehat V_R)}{\operatorname{Var}(S^2)}
=\frac{10(2n^2+6n+1)}{(n+3)(n+4)(2n+3)}.
\]
This ratio is \(1\) for \(n=2\), is strictly less than \(1\) for every \(n\ge3\), and satisfies
\[
\frac{\operatorname{Var}(\widehat V_R)}{\operatorname{Var}(S^2)}\sim\frac{10}n.
\]
The range and sample variance also have exact covariance and correlation
\[
\operatorname{Cov}(R,S^2)=\frac{\ell^3}{3(n+1)(n+3)},
\]
\[
\operatorname{Corr}(R,S^2)^2
=\frac{20n(n+2)}{(n+3)^2(2n+3)},
\qquad
\operatorname{Corr}(R,S^2)\sim\sqrt{\frac{10}n}.
\]

## Assumptions and scope
The result is for an iid sample from one continuous uniform interval with both endpoints unknown. The range is the difference of the extreme order statistics, and \(S^2\) uses the usual \(n-1\) denominator. The theorem is exact for every integer \(n\ge2\). No optimality among all unbiased estimators is asserted. The phrase “projection” refers only to the conditional-expectation identity \(\mathbb E[S^2\mid R]\), which is the \(L^2\)-projection of \(S^2\) onto functions of \(R\).

The primary subject is order-statistic estimation, classified as MSC \(62G30\).

## Proof
Condition first on the sample minimum \(m=X_{(1)}\) and maximum \(M=X_{(n)}\), and write \(r=M-m\). Conditional on these two extremes, the \(n-2\) interior observations, after translating by \(m\) and dividing by \(r\), have the same symmetric-functional law as \(n-2\) independent \(\operatorname{Unif}[0,1]\) variables together with the fixed endpoints \(0\) and \(1\).

Let \(Z_1,\ldots,Z_n\) denote that normalized collection. With \(p=n-2\),
\[
\mathbb E\!\left[\sum_{i=1}^n Z_i^2\right]=1+\frac p3,
\qquad
\mathbb E\!\left[\left(\sum_{i=1}^n Z_i\right)^2\right]
=\frac p{12}+\frac{n^2}4.
\]
Using
\[
S_Z^2=\frac1{n-1}\left(\sum_{i=1}^nZ_i^2-\frac1n\left(\sum_{i=1}^nZ_i\right)^2\right),
\]
one obtains
\[
\mathbb E[S_Z^2]
=\frac{(n+1)(n+2)}{12n(n-1)}=c_n.
\]
Since sample variance scales quadratically,
\[
\mathbb E[S^2\mid X_{(1)}=m,X_{(n)}=M]=c_nr^2.
\]
The right-hand side depends on the extremes only through \(R=r\). The tower property therefore gives
\[
\mathbb E[S^2\mid R]=c_nR^2.
\]

For a continuous uniform sample,
\[
Y=\frac R\ell\sim\operatorname{Beta}(n-1,2).
\]
Thus
\[
\mathbb E[Y]=\frac{n-1}{n+1},\qquad
\mathbb E[Y^2]=\frac{n(n-1)}{(n+1)(n+2)},
\]
\[
\mathbb E[Y^3]=\frac{n(n-1)}{(n+2)(n+3)},\qquad
\mathbb E[Y^4]=\frac{n(n-1)}{(n+3)(n+4)}.
\]
The second moment immediately yields
\[
\mathbb E[\widehat V_R]=c_n\ell^2\mathbb E[Y^2]=\frac{\ell^2}{12}.
\]
The fourth and second moments give
\[
\operatorname{Var}(\widehat V_R)
=c_n^2\ell^4\left(\mathbb E[Y^4]-\mathbb E[Y^2]^2\right)
=\ell^4\frac{2n^2+6n+1}{36n(n-1)(n+3)(n+4)}.
\]

For the ordinary unbiased sample variance, the standard exact identity
\[
\operatorname{Var}(S^2)
=\frac1n\left(\mu_4-\frac{n-3}{n-1}\sigma^4\right)
\]
applies. For \(\operatorname{Unif}[a,b]\),
\[
\sigma^2=\frac{\ell^2}{12},\qquad
\mu_4=\frac{\ell^4}{80},
\]
so
\[
\operatorname{Var}(S^2)=\ell^4\frac{2n+3}{360n(n-1)}.
\]
Dividing gives the stated variance ratio. Its deficit from one factors as
\[
1-\frac{10(2n^2+6n+1)}{(n+3)(n+4)(2n+3)}
=\frac{(n-2)(2n^2+n-13)}{(n+3)(n+4)(2n+3)},
\]
which is positive for every \(n\ge3\). Comparing leading powers of \(n\) gives the asymptotic ratio \(10/n\).

Finally, conditional expectation gives
\[
\operatorname{Cov}(R,S^2)
=\operatorname{Cov}(R,c_nR^2)
=c_n\left(\mathbb E[R^3]-\mathbb E[R]\mathbb E[R^2]\right)
=\frac{\ell^3}{3(n+1)(n+3)}.
\]
The beta variance
\[
\operatorname{Var}(R)
=\ell^2\frac{2(n-1)}{(n+1)^2(n+2)}
\]
and the displayed variance of \(S^2\) then yield the exact squared correlation. Its asymptotic form follows by comparing leading powers.

## Verification
The accompanying `checker.py` uses exact rational arithmetic and independently replays the normalized conditional moment calculation and the beta-moment consequences for every integer \(2\le n\le250\). It checks the projection coefficient, unbiasedness, the covariance, both marginal variances, the exact correlation, the range-projection variance, the variance ratio, and the strict-improvement factorization. `CHECKER_OUTPUT.txt` records 3,486 exact assertions.

## Relationship to prior work
Sajeevkumar (2011) develops best linear unbiased and invariant scale estimators from quasi-ranges in symmetric location-scale families. The full eight-page article was inspected. Its Theorem 3.1 characterizes when the optimal linear scale estimator is a constant multiple of the sample range. It does not square the range, estimate the population variance, condition the ordinary sample variance on the range, or state the covariance/correlation formulas above.

Rao (1981) gives classical exact spacing calculations for rectangular distributions and records that the normalized sample range has a beta law. That provides standard background for the range moments used here, but the paper estimates an unknown endpoint and does not compare the range to sample variance.

Hozo, Djulbegovic, and Hozo (2005) address the practically motivated problem of reconstructing a reported sample variance from the median, range, and sample size. Their open-access article uses inequalities, approximations, and simulation-guided rules such as range divided by four or six. It does not specialize to random samples from a continuous uniform population and does not give the exact conditional projection above.

Galili and Meilijson (2016) study Rao–Blackwell improvement in a one-parameter scale-uniform family. Their full open-access article concerns estimation of the population mean from extreme order statistics; it does not treat sample variance or the squared-range projection here.

Tate (1959) is a broad classical source on unbiased estimation for location-scale models. Open-access and preprint searches did not yield machine-readable full text, and an authorized scan had readable bibliographic material but no extractable mathematical body text. It therefore remains a residual historical-literature risk rather than evidence of coverage.

## Limitations
The theorem is distribution-specific: the parameter-free quadratic conditional projection uses the exact interior self-similarity of a uniform sample. The variance comparison is only between \(c_nR^2\) and the ordinary unbiased sample variance; no global UMVU claim is made. The exact beta law and range-based scale estimation are classical, so the originality claim is limited to the stated conditional projection and its finite-sample covariance/efficiency consequences after comparison with the inspected literature. A broad 1959 location-scale paper could not be fully text-inspected because the available scan was not machine-readable.

## References
1. N. K. Sajeevkumar, “Use of Quasi-Ranges in the Estimation of Scale Parameter of a Symmetric Distribution,” *Communications in Statistics—Theory and Methods* 40 (2011), 1780–1786. DOI: 10.1080/03610921003666438.
2. J. S. Rao, “Estimation Problems for Rectangular Distributions (Or the Taxi Problem Revisited),” *Metrika* 28 (1981), 257–262. DOI: 10.1007/BF01902899.
3. S. P. Hozo, B. Djulbegovic, and I. Hozo, “Estimating the mean and variance from the median, range, and the size of a sample,” *BMC Medical Research Methodology* 5 (2005), article 13. DOI: 10.1186/1471-2288-5-13.
4. T. Galili and I. Meilijson, “An Example of an Improvable Rao–Blackwell Improvement, Inefficient Maximum Likelihood Estimator, and Unbiased Generalized Bayes Estimator,” *The American Statistician* 70 (2016), 108–113. DOI: 10.1080/00031305.2015.1100683.
5. R. F. Tate, “Unbiased Estimation: Functions of Location and Scale Parameters,” *The Annals of Mathematical Statistics* 30 (1959), 341–366. DOI: 10.1214/aoms/1177706256.
