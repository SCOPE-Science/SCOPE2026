# Exact Gaussian coupling of sample mean absolute deviation and sample variance
## Finding
Let
\[
X_1,\ldots,X_n\stackrel{\mathrm{iid}}{\sim}N(\mu,\sigma^2),
\qquad n\ge2,
\]
and define the sample mean absolute deviation about the sample mean and the unbiased sample variance by
\[
M_n=\frac1n\sum_{i=1}^n|X_i-\bar X|,
\qquad
S_n^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2.
\]
Then
\[
\mathbb E M_n
=
\sigma\sqrt{\frac{2(n-1)}{\pi n}},
\]
and the exact finite-sample covariance is
\[
\boxed{
\operatorname{Cov}(M_n,S_n^2)
=
\frac{\sigma^2}{n-1}\mathbb E M_n
=
\sigma^3\sqrt{\frac{2}{\pi n(n-1)}}.
}
\]

There is a more general Gaussian residual law behind this identity. Let
\[
R=(X_1-\bar X,\ldots,X_n-\bar X)
\]
and let \(T(R)\) be integrable and positively homogeneous of degree \(p\ge0\):
\[
T(cr)=c^pT(r),\qquad c>0.
\]
Then
\[
\boxed{
\operatorname{Cov}(T(R),S_n^2)
=
\frac{p\sigma^2}{n-1}\mathbb E T(R).
}
\]
Thus every homogeneous residual statistic has an exact covariance with sample variance determined only by its degree and mean.

For \(M_n\), put \(d=n-1\) and
\[
q_d=
\frac{2}{\pi}
\left(
\sqrt{1-\frac1{d^2}}
+
\frac1d\arcsin\frac1d
\right).
\]
The exact variance is
\[
\boxed{
\operatorname{Var}(M_n)
=
\frac{\sigma^2d}{n}
\left[
\frac{1+dq_d}{d+1}
-\frac2\pi
\right].
}
\]
Together with
\[
\operatorname{Var}(S_n^2)=\frac{2\sigma^4}{n-1},
\]
this gives
\[
\boxed{
\operatorname{Corr}(M_n,S_n^2)^2
=
\frac{n}
{(n-1)\left(
\pi+2\sqrt{n(n-2)}
+2\arcsin\frac1{n-1}
-2n
\right)}.
}
\]
In particular,
\[
\operatorname{Corr}(M_2,S_2^2)=\frac1{\sqrt{\pi-2}},
\]
and
\[
\operatorname{Corr}(M_n,S_n^2)
\longrightarrow
\frac1{\sqrt{\pi-2}}
\approx0.935932.
\]
So mean absolute deviation and variance remain very strongly coupled under Gaussian sampling even though they use linear versus quadratic loss.

## Assumptions and scope
The observations are iid Gaussian. The mean absolute deviation is taken about the sample mean, not the population mean and not the sample median.

The homogeneous covariance law applies to any integrable residual functional \(T\) satisfying the displayed positive-homogeneity condition. The closed variance and correlation formulas are specific to \(T=M_n\).

The result concerns exact second moments. It does not assert that \(M_n\) and \(S_n^2\) are jointly Gaussian or that one is a deterministic function of the other.

## Proof
Let
\[
P=I_n-\frac1n\mathbf1\mathbf1^\top.
\]
Then the residual vector is
\[
R=P(X-\mu\mathbf1),
\]
which is centered Gaussian with covariance \(\sigma^2P\). Restricted to the \(d=n-1\) dimensional residual subspace, this is isotropic. Hence we may write
\[
R=\sigma\,Q\,U,
\]
where \(Q\) has the chi distribution with \(d\) degrees of freedom, \(U\) is uniform on the unit sphere in the residual subspace, and \(Q\) and \(U\) are independent.

Since
\[
S_n^2=\frac{\|R\|^2}{d}
=\frac{\sigma^2Q^2}{d}
\]
and \(T\) is homogeneous of degree \(p\),
\[
T(R)=\sigma^pQ^pT(U).
\]
The chi-moment recurrence gives
\[
\frac{\mathbb E Q^{p+2}}{\mathbb E Q^p}=d+p.
\]
Therefore
\[
\mathbb E[T(R)S_n^2]
=
\frac{d+p}{d}\sigma^2\mathbb ET(R).
\]
Since
\[
\mathbb ES_n^2=\sigma^2,
\]
subtraction proves
\[
\operatorname{Cov}(T(R),S_n^2)
=
\frac{p\sigma^2}{d}\mathbb ET(R).
\]

For \(M_n\), \(p=1\). Each residual coordinate has variance
\[
\tau^2=\sigma^2\frac{d}{n},
\]
so
\[
\mathbb E M_n=\tau\sqrt{\frac2\pi}.
\]
This yields the covariance formula immediately.

It remains to compute \(\operatorname{Var}(M_n)\). For \(i\ne j\),
\[
\operatorname{Corr}(R_i,R_j)=-\frac1d.
\]
For standard bivariate Gaussian variables with correlation \(\rho\),
\[
\mathbb E(|Z_1||Z_2|)
=
\frac2\pi
\left(
\sqrt{1-\rho^2}
+\rho\arcsin\rho
\right).
\]
One derivation differentiates the expectation with respect to \(\rho\): Gaussian differentiation gives derivative
\[
\mathbb E[\operatorname{sgn}(Z_1)\operatorname{sgn}(Z_2)]
=
\frac2\pi\arcsin\rho,
\]
and integration from \(\rho=0\), where the expectation is \(2/\pi\), gives the displayed identity.

With \(\rho=-1/d\), this expectation equals \(q_d\). Hence
\[
\mathbb E M_n^2
=
\frac{\tau^2}{n}
\left(1+dq_d\right).
\]
Subtracting
\[
(\mathbb EM_n)^2=\frac{2\tau^2}{\pi}
\]
proves the variance formula. Combining the covariance and the two variances and simplifying gives the stated correlation.

Finally, using
\[
\sqrt{n(n-2)}=n-1+O(n^{-1}),
\qquad
\arcsin((n-1)^{-1})=(n-1)^{-1}+O(n^{-3}),
\]
in the exact expression yields
\[
\operatorname{Corr}(M_n,S_n^2)^2\to\frac1{\pi-2}.
\]

## Verification
The accompanying `checker.py` verifies the algebraic covariance law from chi moments for several homogeneity degrees, numerically checks the bivariate absolute-Gaussian moment formula by high-precision quadrature, and independently evaluates the closed variance and correlation formulas for \(2\le n\le5000\).

The finite numerical checks are supplementary. The universal covariance identity and finite-\(n\) formulas follow from the analytic derivation.

## Relationship to prior work
Mean absolute deviation about the mean is a classical competitor to standard deviation as a dispersion measure. Goroncy studies positive \(L\)-statistics in units generated by central absolute moments and explicitly singles out mean absolute deviation. Segers gives a full asymptotic treatment of the sample mean absolute deviation about the sample mean under very broad assumptions.

Segers' complete paper develops the asymptotic law of \(M_n\), but it does not state a finite Gaussian covariance with sample variance; searches of the complete text for sample variance and covariance found no such result. Later work by Bräutigam and Kratz treats sample variance and sample mean absolute deviation side by side in joint asymptotic problems with quantile estimators, but does not state their exact finite mutual covariance.

The finding here supplies an exact Gaussian finite-sample bridge between the two dispersion estimators and identifies the broader radial-homogeneity mechanism responsible for it.

## Limitations
Gaussian spherical symmetry is essential to the universal homogeneous covariance law. For non-Gaussian samples the radial and angular parts of the residual vector need not be independent.

The exact correlation formula uses the Gaussian absolute-product identity and the equicorrelation structure of residual coordinates. It therefore does not transfer unchanged to elliptical samples with a non-Gaussian radial law.

An equivalent finite identity may occur in older normal-theory or robust-scale literature under different notation; targeted searches did not locate one.

## References
1. A. Goroncy, “Lower Bounds on Positive L-Statistics,” *Communications in Statistics—Theory and Methods* 38 (2009), 1989–2002. DOI: 10.1080/03610920802393087.
2. J. Segers, “On the asymptotic distribution of the mean absolute deviation about the mean,” arXiv:1406.4151, first submitted 16 June 2014.
3. M. Bräutigam and M. Kratz, “On the Dependence between Functions of Quantile and Dispersion Estimators,” arXiv:1904.11871.
