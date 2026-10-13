# Exponential sample maximum and sample variance have exact harmonic covariance

## Finding

Let
\[
X_1,\ldots,X_n
\]
be iid exponential random variables with rate
\[
\lambda>0,
\qquad n\ge2.
\]
Let
\[
M_n=\max_{1\le i\le n}X_i
\]
and let
\[
S_n^2
=
\frac1{n-1}
\sum_{i=1}^n
(X_i-\bar X)^2
\]
be the unbiased sample variance. Write
\[
H_n=\sum_{r=1}^n\frac1r,
\qquad
H_n^{(2)}=\sum_{r=1}^n\frac1{r^2}.
\]

Then
\[
\boxed{
\operatorname{Cov}(M_n,S_n^2)
=
\frac{
H_n^2+H_n^{(2)}-\frac{2H_n}{n}
}{
(n-1)\lambda^3
}.
}
\tag{1}
\]
The numerator is positive, so
\[
\operatorname{Cov}(M_n,S_n^2)>0
\qquad(n\ge2).
\]

The marginal variances are
\[
\operatorname{Var}(M_n)
=
\frac{H_n^{(2)}}{\lambda^2}
\tag{2}
\]
and
\[
\operatorname{Var}(S_n^2)
=
\frac{2(4n-3)}{n(n-1)\lambda^4}.
\tag{3}
\]
Consequently
\[
\boxed{
\operatorname{Corr}(M_n,S_n^2)
=
\frac{
\sqrt n\,
\left[
H_n^2+H_n^{(2)}-\frac{2H_n}{n}
\right]
}{
\sqrt{
2(4n-3)(n-1)H_n^{(2)}
}
}.
}
\tag{4}
\]

As \(n\to\infty\),
\[
\boxed{
\operatorname{Cov}(M_n,S_n^2)
\sim
\frac{(\log n)^2}{n\lambda^3}
}
\tag{5}
\]
while
\[
\boxed{
\operatorname{Corr}(M_n,S_n^2)
\sim
\frac{\sqrt3}{2\pi}
\frac{(\log n)^2}{\sqrt n}
\longrightarrow0.
}
\tag{6}
\]

Thus the maximum and quadratic dispersion are positively dependent at every finite sample size, yet their standardized fluctuations asymptotically decouple.

## Assumptions and scope

The sample is iid from the exponential law with density
\[
x\mapsto\lambda e^{-\lambda x},
\qquad x\ge0.
\]
The sample variance uses the unbiased denominator \(n-1\).

The result is exact for every integer \(n\ge2\) and every rate \(\lambda>0\). Scale equivariance accounts for the factor \(\lambda^{-3}\) in the covariance.

No claim is made here for gamma samples of nonunit shape, censored samples, heterogeneous exponential rates, or robust scale estimators.

## Proof

Let
\[
X_{(1)}\le\cdots\le X_{(n)}
\]
be the order statistics, with \(X_{(0)}=0\). The independent-spacing representation for exponential order statistics gives
\[
Z_r
=
r\lambda
\left(
X_{(n-r+1)}-X_{(n-r)}
\right),
\qquad r=1,\ldots,n,
\]
as iid \(\operatorname{Exp}(1)\) variables. Therefore
\[
M_n
=
\frac1\lambda
\sum_{r=1}^n\frac{Z_r}{r}.
\tag{7}
\]

Write the ordered sample vector as
\[
x=\lambda^{-1}Az,
\]
where
\[
A_{ir}
=
\frac1r
\mathbf1\{i\ge n-r+1\}.
\]
Let
\[
P=I-\frac1n\mathbf1\mathbf1^{\mathsf T}.
\]
Then
\[
S_n^2
=
\frac1{\lambda^2}
z^{\mathsf T}Bz,
\qquad
B=\frac{A^{\mathsf T}PA}{n-1}.
\tag{8}
\]
A direct calculation gives
\[
B_{rs}
=
\frac1{n-1}
\left(
\frac{\min(r,s)}{rs}-\frac1n
\right).
\tag{9}
\]

Put
\[
a_r=\frac1r.
\]
For independent \(\operatorname{Exp}(1)\) variables, the centered variance is \(1\) and the centered third moment is \(2\). Expanding a linear form against a quadratic form therefore gives, for symmetric \(B\),
\[
\operatorname{Cov}
\left(
a^{\mathsf T}Z,
Z^{\mathsf T}BZ
\right)
=
2a^{\mathsf T}B\mathbf1
+
2\sum_{r=1}^na_rB_{rr}.
\tag{10}
\]

From (9),
\[
(B\mathbf1)_r
=
\frac{H_n-H_r}{n-1}
\tag{11}
\]
and
\[
B_{rr}
=
\frac1{n-1}
\left(
\frac1r-\frac1n
\right).
\tag{12}
\]
Hence (10) becomes
\[
\frac{2}{n-1}
\left[
H_n^2
-
\sum_{r=1}^n\frac{H_r}{r}
+
H_n^{(2)}
-
\frac{H_n}{n}
\right].
\]
Using
\[
\sum_{r=1}^n\frac{H_r}{r}
=
\frac{H_n^2+H_n^{(2)}}2,
\tag{13}
\]
we obtain
\[
\operatorname{Cov}
\left(
a^{\mathsf T}Z,
Z^{\mathsf T}BZ
\right)
=
\frac{
H_n^2+H_n^{(2)}-\frac{2H_n}{n}
}{
n-1
}.
\]
Restoring the factors \(\lambda^{-1}\) and \(\lambda^{-2}\) proves (1).

Equation (2) follows immediately from (7), because the \(Z_r\) are independent with unit variance.

For (3), the exponential distribution has
\[
\sigma^2=\lambda^{-2}
\]
and fourth central moment
\[
\mu_4=9\lambda^{-4}.
\]
The standard unbiased-sample-variance identity
\[
\operatorname{Var}(S_n^2)
=
\frac1n
\left[
\mu_4
-
\frac{n-3}{n-1}\sigma^4
\right]
\]
then simplifies to (3). Combining (1)--(3) gives (4).

Finally,
\[
H_n=\log n+O(1),
\qquad
H_n^{(2)}\longrightarrow\frac{\pi^2}{6}.
\]
Substitution into (1) and (4) gives (5) and (6).

## Verification

The accompanying exact checker reconstructs the quadratic-form matrix \(B\) with rational arithmetic for every \(2\le n\le8\).

For each such \(n\), it independently evaluates
\[
\mathbb E M_n,
\qquad
\mathbb E S_n^2,
\qquad
\mathbb E[M_nS_n^2],
\]
and
\[
\mathbb E[(S_n^2)^2]
\]
directly from factorial moments of independent \(\operatorname{Exp}(1)\) spacings. These raw-moment calculations verify the covariance formula and the sample-variance formula without using the matrix covariance shortcut.

The checker also verifies every row-sum identity in (11) exactly and evaluates the asymptotic correlation normalization at large \(n\).

Finite checks are supplementary. The arbitrary-\(n\) proof is the independent-spacing quadratic-form calculation above.

## Relationship to prior work

Vellaisamy and Zeleke give the exponential-order-statistic representation by independent spacings, including the normalized spacing law used in (7), and record the harmonic-number mean and variance structure of the maximum. Their manuscript is therefore a direct proof ingredient. Its stated results concern exponential order statistics, spacings, and identities derived from them; the inspected text does not state a mixed covariance with the sample variance.

Classical exponential order-statistic literature contains extensive formulas for moments and covariances among order statistics themselves. Those results do not by themselves determine the covariance with \(S_n^2\), which is a quadratic statistic of the full unordered sample.

Related work on heterogeneous exponential samples studies stochastic ordering of the sample range. That addresses a different extreme statistic and does not imply the mixed maximum/sample-variance law (1).

The new point here is the exact cross-scale identity and its asymptotic consequence: a finite positive dependence between the extreme and quadratic dispersion coexists with an explicit decay of their correlation to zero.

## Limitations

The result relies on the independent-spacing representation specific to exponential samples.

The correlation decay in (6) is an asymptotic statement about standardized second-order dependence; it does not imply asymptotic independence without additional analysis.

The literature on exponential order statistics is extensive. Although targeted searches and inspection of the strongest spacing source found no equivalent maximum/sample-variance covariance formula, an older sampling-theory source may contain the same cross-moment under different notation.

The numerical asymptotic checks in the accompanying verifier do not replace the analytic limit.

## References

1. P. Vellaisamy and A. Zeleke, “Exponential Order Statistics, the Basel problem and Combinatorial Identities,” arXiv:1604.02644, first public version 2016-04-10.
2. Q. Zhao and X. Li, “Stochastic order of sample range from heterogeneous exponential random variables,” *Journal of Applied Probability* 45 (2008), 906–916.
