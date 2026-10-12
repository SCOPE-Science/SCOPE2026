# Exponential Gini mean difference and sample variance have an exact finite-sample correlation

## Finding

Let
\[
X_1,\ldots,X_n\stackrel{\mathrm{iid}}{\sim}\operatorname{Exp}(\lambda),
\qquad
\lambda>0,
\qquad
n\ge2.
\]
Define the sample Gini mean difference
\[
G_n=
\binom n2^{-1}
\sum_{1\le i<j\le n}|X_i-X_j|
\]
and the unbiased sample variance
\[
S_n^2=
\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2.
\]
The pairwise-difference identity
\[
S_n^2=
\binom n2^{-1}
\sum_{i<j}\frac{(X_i-X_j)^2}{2}
\]
shows that both statistics are degree-two \(U\)-statistics built from the same sample.

Their exact covariance is
\[
\boxed{
\operatorname{Cov}(G_n,S_n^2)
=
\frac{3n-2}{n(n-1)\lambda^3}.
}
\tag{1}
\]

Their exact marginal variances are
\[
\boxed{
\operatorname{Var}(G_n)
=
\frac{2(2n-1)}{3n(n-1)\lambda^2},
}
\tag{2}
\]
and
\[
\boxed{
\operatorname{Var}(S_n^2)
=
\frac{2(4n-3)}{n(n-1)\lambda^4}.
}
\tag{3}
\]

Consequently,
\[
\boxed{
\operatorname{Corr}(G_n,S_n^2)
=
\frac{\sqrt3(3n-2)}
{2\sqrt{(2n-1)(4n-3)}}.
}
\tag{4}
\]

The correlation is strictly increasing with sample size. More precisely,
\[
\rho_{n+1}^2-\rho_n^2
=
\frac{3(6n^2-4n-1)}
{4(2n-1)(2n+1)(4n-3)(4n+1)}
>0,
\tag{5}
\]
where \(\rho_n=\operatorname{Corr}(G_n,S_n^2)\). It has the nontrivial limit
\[
\boxed{
\rho_n\longrightarrow\frac{3\sqrt6}{8}
=
0.9185586535\ldots.
}
\tag{6}
\]

Thus the order-based Gini scale statistic and the quadratic moment-based scale statistic remain strongly aligned under exponential sampling, but they do not become asymptotically equivalent.

## Assumptions and scope

The exponential distribution is parameterized by its rate \(\lambda\), so
\[
\mathbb EX_i=\lambda^{-1},
\qquad
\operatorname{Var}(X_i)=\lambda^{-2}.
\]
For this model the population Gini mean difference is also \(\lambda^{-1}\). Hence \(G_n\) estimates the same scale as the population standard deviation, while \(S_n^2\) estimates the squared scale.

Equation (1) therefore carries units \(\lambda^{-3}\), whereas the correlation in (4) is scale-free.

The theorem concerns the unnormalized sample Gini mean difference, not the Gini coefficient obtained by dividing by the sample mean.

## Proof

By scale equivariance it is enough to prove the formulas for \(\lambda=1\). Put
\[
h(x,y)=|x-y|,
\qquad
q(x,y)=\frac{(x-y)^2}{2}.
\]
Then \(G_n\) and \(S_n^2\) are the normalized degree-two \(U\)-statistics associated with \(h\) and \(q\).

For two normalized degree-two \(U\)-statistics, pair-overlap counting gives
\[
\operatorname{Cov}(U_h,U_q)
=
\frac{2c_2+4(n-2)c_1}{n(n-1)},
\tag{7}
\]
where
\[
c_2=
\operatorname{Cov}
\bigl(h(X_1,X_2),q(X_1,X_2)\bigr)
\]
is the common-pair covariance and
\[
c_1=
\operatorname{Cov}
\bigl(h(X_1,X_2),q(X_1,X_3)\bigr)
\]
is the one-index-overlap covariance.

For independent standard exponentials,
\[
|X_1-X_2|\sim\operatorname{Exp}(1).
\]
Therefore
\[
\mathbb Eh=1,
\qquad
\mathbb Eq=1,
\qquad
\mathbb E[hq]
=
\frac12\mathbb E|X_1-X_2|^3
=
3,
\]
so
\[
c_2=2.
\tag{8}
\]

For the overlapping-pair term, condition on \(X_1=x\). Direct integration gives
\[
a(x)
=
\mathbb E[|x-X_2|\mid X_1=x]
=
x-1+2e^{-x},
\tag{9}
\]
and
\[
b(x)
=
\mathbb E\left[\frac{(x-X_3)^2}{2}\,\middle|\,X_1=x\right]
=
\frac{x^2}{2}-x+1.
\tag{10}
\]
With \(X_1\sim\operatorname{Exp}(1)\),
\[
\mathbb Ea(X_1)=\mathbb Eb(X_1)=1
\]
and
\[
\mathbb E[a(X_1)b(X_1)]
=
\frac74.
\]
Hence
\[
c_1=\frac34.
\tag{11}
\]
Substitution of (8) and (11) into (7) gives
\[
\operatorname{Cov}(G_n,S_n^2)
=
\frac{3n-2}{n(n-1)}
\]
when \(\lambda=1\), proving (1) after rescaling.

The same overlap formula applied to a single kernel gives
\[
\operatorname{Var}(U_h)
=
\frac{2v_2+4(n-2)v_1}{n(n-1)},
\tag{12}
\]
where \(v_2\) is the kernel variance and \(v_1\) is the variance of its first conditional projection.

For \(h\),
\[
v_2=\operatorname{Var}|X_1-X_2|=1
\]
and, from (9),
\[
v_1=\operatorname{Var}(a(X_1))=\frac13.
\]
This proves (2).

For \(q\),
\[
v_2=
\operatorname{Var}\left(\frac{(X_1-X_2)^2}{2}\right)
=
5
\]
and, from (10),
\[
v_1=\operatorname{Var}(b(X_1))=2.
\]
This proves (3).

Equation (4) follows by dividing (1) by the square root of (2) times (3). Squaring (4) and subtracting consecutive terms gives (5), whose numerator is positive for every \(n\ge2\). Taking the leading terms in (4) gives (6).

## Verification

The accompanying deterministic checker reconstructs the conditional moments in (9)--(11) from exact exponential integrals using rational arithmetic. It then verifies the covariance and both variance formulas for a large integer range using only the degree-two overlap count.

As an independent calculation, the checker also writes the ordered exponential sample in independent spacings. With independent
\[
Y_k\sim\operatorname{Exp}(k),
\qquad
1\le k\le n,
\]
the Gini statistic is the linear form
\[
G_n=
\sum_{k=1}^{n}
\frac{2k(n-k)}{n(n-1)}Y_k,
\]
while the sample variance is the quadratic form
\[
S_n^2=Y^\mathsf{T}BY,
\qquad
B_{kr}
=
\frac{\min(k,r)-kr/n}{n-1}.
\]
The checker evaluates the covariance of this linear-quadratic pair from exact independent-exponential moments and obtains (1) again.

These finite checks are supplementary. The all-\(n\) proof is the exact \(U\)-statistic overlap calculation above.

## Relationship to prior work

Čiginas and Pumputis study Gini's mean difference and empirical variance side by side as competing scale statistics. Their paper explicitly writes both as degree-two \(U\)-statistics and develops their separate variance decompositions, asymptotics, Studentization, and finite-population analogues. The inspected full text does not state a cross-covariance or correlation between the two statistics.

That comparison is especially relevant because their superpopulation discussion includes the exponential family as a standard nonnormal scale model, while the present result gives an exact iid finite-sample joint calculation in that model.

Gail and Gastwirth develop exact and asymptotic distribution theory for a scale-free Gini statistic under exponentiality. Their work establishes the importance of Gini-based exponential inference, but the inspected public summary does not provide a joint covariance with sample variance.

Hosking places Gini mean difference within the general theory of \(L\)-moments and contrasts order-statistic scale summaries with conventional moments. This gives a broader statistical reason to quantify how a Gini-based scale estimator and a variance-based estimator co-move.

The present formula is not implied by the separate marginal variance formulas: it requires the mixed one-index projection
\[
\operatorname{Cov}
\left(
\mathbb E[h(X_1,X_2)\mid X_1],
\mathbb E[q(X_1,X_3)\mid X_1]
\right)
=
\frac34.
\]

## Limitations

The exact formulas use exponential sampling. Other distributions generally change both the common-pair and one-index-overlap covariance components.

No joint density, conditional distribution, or independence statement is claimed.

The Gini statistic here is the sample mean absolute pairwise difference, not the mean-normalized Gini coefficient.

General multivariate \(U\)-statistic covariance theory makes the overlap decomposition classical. The substantive distribution-specific content is the exact exponential mixed projection and the resulting closed correlation law. An older source may have recorded the same special-case covariance under different notation, even though the closest full comparison source inspected does not state it.

## References

1. A. Čiginas and D. Pumputis, “Gini's mean difference and variance as measures of finite populations scales,” arXiv:1406.2275, first public version 2014-06-09.
2. M. H. Gail and J. L. Gastwirth, “A Scale-Free Goodness-Of-Fit Test for the Exponential Distribution Based on the Gini Statistic,” *Journal of the Royal Statistical Society, Series B* 40 (1978), 350–357, DOI:10.1111/j.2517-6161.1978.tb01048.x.
3. J. R. M. Hosking, “L-Moments: Analysis and Estimation of Distributions Using Linear Combinations of Order Statistics,” *Journal of the Royal Statistical Society, Series B* 52 (1990), 105–124, DOI:10.1111/j.2517-6161.1990.tb01775.x.
4. W. Hoeffding, “A Class of Statistics with Asymptotically Normal Distribution,” *Annals of Mathematical Statistics* 19 (1948), 293–325.
