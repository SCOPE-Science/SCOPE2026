# Exact harmonic covariance of range and sample variance in exponential sampling

## Finding

Let
\[
X_1,\ldots,X_n,
\qquad
n\ge2,
\]
be independent and identically distributed exponential random variables with rate
\[
\lambda>0.
\]
Define
\[
M=X_{(1)},
\qquad
R=X_{(n)}-X_{(1)},
\]
and the unbiased sample variance
\[
S^2
=
\frac1{n-1}
\sum_{i=1}^n(X_i-\bar X)^2.
\]

Then
\[
\boxed{
M\ \text{is independent of the pair}\ (R,S^2).
}
\tag{1}
\]

Write
\[
H_m=\sum_{k=1}^m\frac1k,
\qquad
H_m^{(2)}=\sum_{k=1}^m\frac1{k^2}.
\]
The same-sample range and variance have exact covariance
\[
\boxed{
\operatorname{Cov}(R,S^2)
=
\frac{H_{n-1}^2+H_{n-1}^{(2)}}{(n-1)\lambda^3}
>0.
}
\tag{2}
\]

Their exact correlation is
\[
\boxed{
\operatorname{Corr}(R,S^2)
=
\bigl(H_{n-1}^2+H_{n-1}^{(2)}\bigr)
\sqrt{
\frac{n}
{2(n-1)(4n-3)H_{n-1}^{(2)}}
}.
}
\tag{3}
\]

Consequently,
\[
\boxed{
\operatorname{Corr}(R,S^2)
\sim
\frac{\sqrt3}{2\pi}
\frac{(\log n)^2}{\sqrt n}
\longrightarrow0.
}
\tag{4}
\]

Thus the range and unbiased sample variance are positively correlated for every exponential sample size, but the correlation decays to zero. The minimum separates completely: it is independent of both the range and the translation-invariant sample variance jointly.

## Assumptions and scope

The parent law is exponential with rate \(\lambda\), and \(S^2\) uses divisor \(n-1\).

Equation (1) is joint independence of the minimum from the pair \((R,S^2)\). It does not say that \(R\) and \(S^2\) are independent; equation (2) shows that they are not.

The asymptotic statement concerns correlation. Although the expected range grows like \(\lambda^{-1}\log n\), the variance of the range remains bounded, while \(S^2\) concentrates at the usual \(n^{-1/2}\) scale.

## Proof

Let
\[
D_1=X_{(1)},
\qquad
D_k=X_{(k)}-X_{(k-1)},
\quad
2\le k\le n.
\]
For an exponential sample, the spacings are independent and
\[
D_k\sim\operatorname{Exp}((n-k+1)\lambda).
\tag{5}
\]
In particular, \(D_1\) is independent of
\[
(D_2,\ldots,D_n).
\]
The range is a function only of \(D_2,\ldots,D_n\), and sample variance is invariant under adding the same constant to every observation, so it too is a function only of these later spacings. This proves (1).

Now put
\[
Z_i=D_{i+1},
\qquad
1\le i\le n-1.
\]
Then the \(Z_i\) are independent exponentials with
\[
\mu_i=\mathbb EZ_i=\frac1{(n-i)\lambda},
\]
\[
v_i=\operatorname{Var}(Z_i)=\frac1{(n-i)^2\lambda^2},
\]
and third central moment
\[
\tau_i
=
\mathbb E[(Z_i-\mu_i)^3]
=
\frac2{(n-i)^3\lambda^3}.
\tag{6}
\]
Also
\[
R=\sum_{i=1}^{n-1}Z_i.
\tag{7}
\]

After subtracting the minimum, the ordered sample is
\[
0,\quad
Z_1,\quad
Z_1+Z_2,\quad
\ldots,\quad
Z_1+\cdots+Z_{n-1}.
\]
Therefore
\[
S^2=Z^\top A Z,
\tag{8}
\]
where
\[
A_{ij}
=
\frac{\min(i,j)\bigl(n-\max(i,j)\bigr)}
{n(n-1)}.
\tag{9}
\]

For independent coordinates \(Z_i\), a direct centered expansion gives
\[
\operatorname{Cov}
\left(
\sum_i Z_i,\,
Z^\top A Z
\right)
=
2\sum_i v_i(A\mu)_i
+
\sum_i A_{ii}\tau_i.
\tag{10}
\]
Indeed, after writing \(Z=\mu+\varepsilon\), only the linear term
\[
2\mu^\top A\varepsilon
\]
and the diagonal cubic terms in
\[
\varepsilon^\top A\varepsilon
\]
can have nonzero covariance with \(\sum_i\varepsilon_i\).

For fixed \(i\), equation (9) gives
\[
(A\mu)_i
=
\frac1{(n-1)\lambda}
\left[
(n-i)
\left(
H_{n-1}-H_{n-i-1}
\right)
-\frac{i}{n}
\right].
\tag{11}
\]
Substituting (6) and (11) into (10), the terms involving
\[
\frac{i}{(n-i)^2}
\]
cancel exactly, leaving
\[
\operatorname{Cov}(R,S^2)
=
\frac{2}{(n-1)\lambda^3}
\sum_{i=1}^{n-1}
\frac{
H_{n-1}-H_{n-i-1}
}{
n-i
}.
\tag{12}
\]
With
\[
r=n-i,
\]
the sum becomes
\[
\sum_{r=1}^{n-1}
\frac{H_{n-1}-H_{r-1}}r
=
\sum_{1\le r\le k\le n-1}\frac1{rk}.
\]
The triangular double sum is
\[
\frac12
\left(
H_{n-1}^2+H_{n-1}^{(2)}
\right).
\tag{13}
\]
Equations (12)--(13) prove (2).

For the range,
\[
R
\stackrel d=
\sum_{r=1}^{n-1}E_r,
\qquad
E_r\sim\operatorname{Exp}(r\lambda)
\]
independently, so
\[
\operatorname{Var}(R)
=
\frac{H_{n-1}^{(2)}}{\lambda^2}.
\tag{14}
\]

For an unbiased sample variance from a parent law with variance \(\sigma^2\) and fourth central moment \(\mu_4\),
\[
\operatorname{Var}(S^2)
=
\frac1n
\left[
\mu_4-
\frac{n-3}{n-1}\sigma^4
\right].
\tag{15}
\]
For the exponential law,
\[
\sigma^2=\lambda^{-2},
\qquad
\mu_4=9\lambda^{-4},
\]
hence
\[
\operatorname{Var}(S^2)
=
\frac{2(4n-3)}{n(n-1)\lambda^4}.
\tag{16}
\]
Combining (2), (14), and (16) proves (3).

Finally,
\[
H_{n-1}\sim\log n,
\qquad
H_{n-1}^{(2)}\longrightarrow\frac{\pi^2}{6}.
\]
Substitution into (3) gives (4).

## Verification

The accompanying checker uses exact rational arithmetic.

For each \(2\le n\le120\), it reconstructs the quadratic-form matrix in (9), the exponential spacing means, variances, and third central moments, evaluates the unsimplified covariance identity (10), and verifies exact equality with (2).

For each \(2\le n\le500\), it separately verifies the harmonic double-sum identity, the range variance, the sample-variance variance formula specialized to the exponential law, and the squared correlation formula.

These finite calculations are supplementary. The all-\(n\) theorem is the spacing argument and exact quadratic-form calculation above.

## Relationship to prior work

Vellaisamy and Zeleke give a direct treatment of exponential order statistics and explicitly recover the independent exponential spacing representation. Their paper supplies the key spacing input used here, but it does not study sample range jointly with sample variance.

Royen derives the exact distribution of sample variance for gamma parents; the exponential case is the shape-one specialization. That work focuses on the marginal law of the quadratic statistic and does not treat its covariance with the sample range.

Lam's earlier article gives exact sample-variance distributions for small exponential samples and is a plausible older source for related moments. The accessible abstract describes only the marginal sample-variance distribution, not a joint range-variance law; the full text was not available in the inspected sources, so it remains a residual originality risk.

The present result combines the independent-spacing geometry with the translation-invariant quadratic form of sample variance. The new structural content claimed here is the exact harmonic covariance, its strict sign for every \(n\), the closed correlation, and its vanishing asymptotic rate.

## Limitations

The exponential spacing independence is essential. The formula does not extend unchanged to a general gamma parent or to arbitrary lifetime laws.

The result concerns sample variance rather than sample standard deviation. The square root destroys the quadratic-form covariance calculation used in the proof.

A plausible inaccessible older source on exponential sample variance remains an originality risk. No claim is made that the harmonic formula could not have appeared under different notation.

## References

1. T. Royen, “On the Laplace transform of some quadratic forms and the exact distribution of the sample variance from a gamma or uniform parent distribution,” arXiv:0710.5749, first submitted 2007-10-30.
2. P. Vellaisamy and A. Zeleke, “Exponential Order Statistics, the Basel problem and Combinatorial Identities,” arXiv:1604.02644, first submitted 2016-04-10.
3. H.-K. Lam, “Remarks on the distribution of the sample variance in exponential sampling,” *Communications in Statistics—Simulation and Computation* 9 (1980), 639–647, DOI 10.1080/03610918008812181.
