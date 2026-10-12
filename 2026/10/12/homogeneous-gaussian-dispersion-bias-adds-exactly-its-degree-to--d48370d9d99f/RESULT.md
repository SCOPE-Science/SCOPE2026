# Homogeneous Gaussian dispersion bias adds exactly its degree to residual chi-square dimension

## Finding

Let
\[
X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}N(\mu,\sigma^2),
\qquad n\ge2,
\]
and write
\[
\bar X=\frac1n\sum_{i=1}^nX_i,
\qquad
Y=(X_1-\bar X,\ldots,X_n-\bar X),
\qquad
d=n-1.
\]
Let
\[
S^2=\frac1d\sum_{i=1}^n(X_i-\bar X)^2.
\]

Suppose
\[
T=h(Y)\ge0
\]
is not almost surely zero, has finite mean, and is positively homogeneous of degree
\[
q\ge0,
\]
so that
\[
h(cy)=c^qh(y)
\qquad(c>0).
\]

Define the \(T\)-size-biased law by
\[
\mathbb P_T(A)
=
\frac{\mathbb E[T\mathbf 1_A]}{\mathbb ET}.
\]

Then
\[
\boxed{
\frac{dS^2}{\sigma^2}
\ \overset{\mathbb P_T}{\sim}\
\chi^2_{d+q}.
}
\tag{1}
\]

Thus weighting by a degree-\(q\) homogeneous residual dispersion statistic adds exactly \(q\) residual chi-square degrees of freedom.

Equivalently, for every
\[
t\ge0,
\]
\[
\boxed{
\frac{\mathbb E\!\left[
T\exp\!\left\{-t\,dS^2/\sigma^2\right\}
\right]}{\mathbb ET}
=
(1+2t)^{-(d+q)/2}.
}
\tag{2}
\]

More generally, whenever the moment exists,
\[
\boxed{
\frac{\mathbb E[T(S^2)^r]}{\mathbb ET}
=
\left(\frac{\sigma^2}{d}\right)^r
2^r
\frac{\Gamma((d+q)/2+r)}
{\Gamma((d+q)/2)}.
}
\tag{3}
\]

Taking
\[
r=1
\]
gives
\[
\boxed{
\operatorname{Cov}(T,S^2)
=
\frac{q\sigma^2}{d}\mathbb ET.
}
\tag{4}
\]

For every nonzero statistic of positive degree, the covariance with sample variance is therefore strictly positive.

Two degree-one consequences are the sample range
\[
R_n=X_{(n)}-X_{(1)}
\]
and Gini's mean difference
\[
G_n=
\frac{1}{n(n-1)}
\sum_{i=1}^n\sum_{j=1}^n|X_i-X_j|.
\]
For either statistic, size-biasing changes the residual chi-square law from
\[
\chi^2_{n-1}
\]
to
\[
\chi^2_n.
\]
In particular,
\[
\boxed{
\operatorname{Cov}(R_n,S^2)
=
\frac{\sigma^2}{n-1}\mathbb ER_n,
}
\tag{5}
\]
and
\[
\boxed{
\operatorname{Cov}(G_n,S^2)
=
\frac{\sigma^2}{n-1}\mathbb EG_n.
}
\tag{6}
\]

The law (1), rather than a single covariance, is the main result: all mixed powers with \(S^2\) follow without computing the joint density of \(T\) and \(S^2\).

## Assumptions and scope

The parent law is exactly normal. The statistic \(T\) depends only on the centered residual vector, is nonnegative, and is positively homogeneous.

No differentiability of \(h\) is required. This includes nonsmooth statistics such as the sample range and Gini's mean difference.

The size-biased law is well defined because
\[
0<\mathbb ET<\infty.
\]
The moment identity (3) is asserted only when the displayed moment exists.

The theorem determines the radial coordinate after biasing. The angular law generally changes and depends on \(h\).

## Proof

The residual vector \(Y\) lies in the subspace
\[
H=
\left\{
y\in\mathbb R^n:
\sum_{i=1}^ny_i=0
\right\},
\]
which has dimension
\[
d=n-1.
\]
Under normal sampling, \(Y\) is an isotropic Gaussian vector on \(H\) with covariance
\[
\sigma^2I_H.
\]

Choose orthonormal coordinates on \(H\). Then
\[
Y=\sigma RU,
\]
where
\[
R\sim\chi_d,
\]
\(U\) is uniform on the unit sphere of \(H\), and \(R\) is independent of \(U\).

The sample variance is purely radial:
\[
\frac{dS^2}{\sigma^2}=R^2.
\tag{7}
\]

By homogeneity,
\[
T=h(\sigma RU)
=
\sigma^qR^qh(U).
\tag{8}
\]

For bounded measurable \(a\) and \(b\),
\[
\mathbb E_T[a(R)b(U)]
=
\frac{
\mathbb E[R^qa(R)]
\mathbb E[h(U)b(U)]
}{
\mathbb E[R^q]\mathbb E[h(U)]
}.
\tag{9}
\]
Thus radius and direction remain independent after \(T\)-biasing. The direction is tilted by \(h\), while the radial density is the original \(\chi_d\) density multiplied by \(r^q\).

The \(\chi_d\) density is proportional to
\[
r^{d-1}e^{-r^2/2},
\qquad r>0.
\]
After multiplication by \(r^q\), it is proportional to
\[
r^{d+q-1}e^{-r^2/2},
\]
which is exactly the \(\chi_{d+q}\) density, also for noninteger
\[
d+q>0.
\]
This proves (1).

The Laplace transform of a chi-square random variable with \(\nu\) degrees of freedom is
\[
(1+2t)^{-\nu/2},
\qquad t\ge0,
\]
which gives (2) using (7). The chi-square moment formula gives (3).

At \(r=1\),
\[
\frac{\mathbb E[TS^2]}{\mathbb ET}
=
\frac{\sigma^2}{d}(d+q).
\]
Since
\[
\mathbb ES^2=\sigma^2,
\]
subtraction proves (4).

Finally, the range and Gini mean difference are nonnegative translation-invariant residual statistics homogeneous of degree one. Substitution of
\[
q=1,\qquad d=n-1
\]
proves (5)--(6).

## Verification

The accompanying checker independently verifies the radial moment transformation over many dimensions and integer as well as noninteger homogeneity degrees.

For integer even degree shifts, it uses exact rational products for chi-square moments. For fractional shifts, it evaluates the gamma-ratio moments and checks the degree-shift covariance identity.

These computations are supplementary. The all-\(h\) theorem is established by the exact polar factorization in the proof.

## Relationship to prior work

Hwang and Hu's characterization work treats sample range, Gini's mean difference, sample standard deviation, and related order-statistic functionals as centered-sample statistics. Its later formulation with Hu and Lin explicitly organizes these examples through positive homogeneity. The central question there is independence from the sample mean and characterization of the normal law.

The full Hu--Lin manuscript states that for a normal parent the sample mean is independent of the residual vector and develops positively homogeneous residual statistics including sample range and Gini's mean difference. Targeted full-text searches for size-biased laws, covariance formulas, chi-square degree shifts, and polar formulations found no such statement.

Hwang and Hu's earlier full paper on studentized order statistics derives exact distributions of scale-free order-statistic functionals under normal sampling and identifies their residual-sphere geometry. Its inspected statements concern studentized directions rather than homogeneous size-biasing of the residual radius.

General size-biased-sampling literature studies selection proportional to a positive measurement, but the inspected reference does not specialize the mechanism to homogeneous Gaussian residual statistics.

The present result is a radial mixed-law statement: homogeneity alone determines exactly what weighting by \(T\) does to sample variance, independently of the angular form of \(T\).

## Limitations

The normal law is essential to the exact independent chi radius and uniform residual direction. Nonnormal or general elliptical samples require a separate radial law and need not produce a chi-square degree shift.

The theorem does not determine the angular distribution after biasing beyond the tilt proportional to \(h(U)\).

For the range, equation (5) still contains the classical expectation
\[
\mathbb ER_n;
\]
the theorem is not a closed formula for that expectation.

The proof is elementary after Gaussian polar decomposition and homogeneity are combined. The value is the complete all-statistic size-biased variance law and its mixed-moment consequences, not a claim that Gaussian spherical decomposition or size-biased sampling is new.

## References

1. T.-Y. Hwang and C.-Y. Hu, “On some characterizations of population distributions,” *Taiwanese Journal of Mathematics* 4 (2000), 427–437, DOI 10.11650/TWJM/1500407259.
2. C.-Y. Hu and G. D. Lin, “Characterizations of the Normal Distribution via the Independence of the Sample Mean and the Feasible Definite Statistics with Ordered Arguments,” arXiv:2112.06152, first submitted 2021-12-12; later *Annals of the Institute of Statistical Mathematics* 74 (2022), 473–488.
3. T.-Y. Hwang and C.-Y. Hu, “On the joint distribution of studentized order statistics,” *Annals of the Institute of Statistical Mathematics* 46 (1994), 165–177, DOI 10.1007/BF00773601.
4. D. L. Zimmerman, “Size-Biased Sampling,” *Wiley StatsRef: Statistics Reference Online*, first published 2014-09-29, DOI 10.1002/9781118445112.stat07583.
