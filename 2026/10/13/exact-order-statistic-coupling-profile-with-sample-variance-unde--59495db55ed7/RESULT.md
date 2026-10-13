# Exact order-statistic coupling profile with sample variance under a uniform law
## Finding
Let
\[
X_1,\ldots,X_n
\]
be independent and identically distributed on
\[
[0,1],
\qquad
n\ge2,
\]
and let
\[
X_{(1)}\le\cdots\le X_{(n)}
\]
be the order statistics. Write
\[
S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
\]
for the unbiased sample variance.

For every
\[
1\le k\le n,
\]
the exact covariance profile is
\[
\boxed{
\operatorname{Cov}(X_{(k)},S^2)
=
\frac{
k(n+1-k)(2k-n-1)
}{
6n(n-1)(n+1)(n+3)
}.
}
\]

Because
\[
\operatorname{Var}(X_{(k)})
=
\frac{k(n+1-k)}{(n+1)^2(n+2)}
\]
and
\[
\operatorname{Var}(S^2)
=
\frac{2n+3}{360n(n-1)},
\]
the exact correlation is
\[
\boxed{
\operatorname{Corr}(X_{(k)},S^2)
=
\frac{
(2k-n-1)\sqrt{10k(n+1-k)(n+2)}
}{
(n+3)\sqrt{n(n-1)(2n+3)}
}.
}
\]

The sign has a complete finite-sample description:
\[
\operatorname{Cov}(X_{(k)},S^2)<0
\quad\Longleftrightarrow\quad
k<\frac{n+1}{2},
\]
\[
\operatorname{Cov}(X_{(k)},S^2)=0
\quad\Longleftrightarrow\quad
2k=n+1,
\]
and
\[
\operatorname{Cov}(X_{(k)},S^2)>0
\quad\Longleftrightarrow\quad
k>\frac{n+1}{2}.
\]
Thus, for odd \(n\), the sample median is exactly uncorrelated with the sample variance, while lower and upper order statistics have opposite covariance signs of equal magnitude under reflection.

There is also a nontrivial bulk limit. If
\[
\frac{k}{n+1}\longrightarrow u,
\qquad
0<u<1,
\]
then
\[
\boxed{
\operatorname{Corr}(X_{(k)},S^2)
\longrightarrow
\sqrt5\,(2u-1)\sqrt{u(1-u)}.
}
\]
The largest possible limiting magnitude over bulk ranks is
\[
\boxed{
\frac{\sqrt5}{4},
}
\]
attained at
\[
u=\frac12\left(1\pm\frac1{\sqrt2}\right).
\]

## Assumptions and scope
The parent distribution is continuous uniform on a finite interval. The displayed formulas are written for \([0,1]\). For a general interval \([a,b]\), the covariance is multiplied by \((b-a)^3\), while the correlation is unchanged.

The result concerns the unbiased sample variance. It does not claim the same profile for sample standard deviation or for a nonuniform parent law.

The order statistic is paired with the variance calculated from the same sample.

## Proof
Fix
\[
k\in\{1,\ldots,n\}
\]
and condition on
\[
X_{(k)}=x.
\]
Given this event, the \(k-1\) observations below \(x\), ignoring their internal order, are independent uniforms on \([0,x]\), and the \(n-k\) observations above \(x\) are independent uniforms on \([x,1]\). The two groups are conditionally independent.

Put
\[
m=k-1,
\qquad
r=n-k,
\]
and let
\[
T=\sum_{i=1}^n X_i,
\qquad
Q=\sum_{i=1}^n X_i^2.
\]
The conditional first and second raw sums are
\[
\mathbb E[T\mid X_{(k)}=x]
=
\frac r2+\frac{n+1}{2}x,
\]
\[
\operatorname{Var}(T\mid X_{(k)}=x)
=
\frac{mx^2+r(1-x)^2}{12},
\]
and
\[
\mathbb E[Q\mid X_{(k)}=x]
=
\frac{r(1+x)}3+\frac{n+2}{3}x^2.
\]
Since
\[
S^2
=
\frac{Q-T^2/n}{n-1},
\]
we get the exact conditional quadratic
\[
\mathbb E[S^2\mid X_{(k)}=x]
=
\frac{
-3k^2+2knx+2kn+4kx+k+n^2x^2-2n^2x+n^2+nx^2-4nx-n-2x^2
}{
12n(n-1)
}.
\]

Now
\[
X_{(k)}
\sim
\operatorname{Beta}(k,n+1-k),
\]
so
\[
\mathbb E X_{(k)}
=
\frac{k}{n+1},
\]
\[
\mathbb E X_{(k)}^2
=
\frac{k(k+1)}{(n+1)(n+2)},
\]
and
\[
\mathbb E X_{(k)}^3
=
\frac{k(k+1)(k+2)}{(n+1)(n+2)(n+3)}.
\]
Substitution into
\[
\mathbb E[X_{(k)}S^2]
=
\mathbb E\!\left[
X_{(k)}
\mathbb E(S^2\mid X_{(k)})
\right]
\]
and subtraction of
\[
\mathbb E X_{(k)}\,\mathbb E S^2
=
\frac{k}{n+1}\cdot\frac1{12}
\]
give
\[
\operatorname{Cov}(X_{(k)},S^2)
=
\frac{
k(n+1-k)(2k-n-1)
}{
6n(n-1)(n+1)(n+3)
}.
\]

The variance of a beta order statistic gives the first marginal variance. For the unbiased sample variance under a parent law with variance \(\sigma^2\) and fourth central moment \(\mu_4\),
\[
\operatorname{Var}(S^2)
=
\frac1n
\left(
\mu_4-\frac{n-3}{n-1}\sigma^4
\right).
\]
For the uniform law,
\[
\sigma^2=\frac1{12},
\qquad
\mu_4=\frac1{80},
\]
which simplifies to
\[
\operatorname{Var}(S^2)
=
\frac{2n+3}{360n(n-1)}.
\]
Combining the covariance and the two marginal variances yields the correlation formula.

For the bulk limit, substitute
\[
k=(n+1)u+o(n)
\]
into the exact correlation and cancel the leading powers of \(n\). This gives
\[
\sqrt5\,(2u-1)\sqrt{u(1-u)}.
\]
Writing
\[
z=2u-1
\]
shows that the squared limiting magnitude is
\[
\frac54 z^2(1-z^2),
\]
which is maximized at
\[
z^2=\frac12.
\]
This proves the stated extremal bulk ranks and limiting magnitude.

## Verification
The accompanying `checker.py` performs two exact-rational replays.

First, for every \(2\le n\le12\) and every rank \(k\), it represents the uniform order statistics by Dirichlet spacings and independently expands the cubic moments needed for
\[
\mathbb E[X_{(k)}S^2].
\]
Those direct Dirichlet calculations are compared with the closed covariance formula.

Second, for every \(2\le n\le1000\) and every rank \(k\), it reconstructs the conditional quadratic above from the lower- and upper-uniform groups, combines it with exact beta moments, and checks the covariance, marginal variances, correlation-squared identity, reflection antisymmetry, and median zero.

The bounded calculations supplement the symbolic proof; they are not used to justify the universal quantifiers.

## Relationship to prior work
Bekçi derives recurrence relations for single and product moments of uniform order statistics. That literature supplies the natural exact-moment background for the beta/order-statistic calculations used here. The accessible publication record does not state a covariance between one order statistic and the same-sample variance.

Papadatos gives a broad treatment of expectation bounds for order statistics and \(L\)-statistics under mean-variance information. The complete accessible article reviews classical order-statistic moment and dependence literature and has primary classification \(62G30\). It does not contain the phrase “sample variance,” and its covariance discussion concerns covariance between ordered pairs rather than an order statistic paired with the same-sample variance.

The present result is not a bound on an order statistic. It is an exact same-sample dependence profile across all ranks, including its sign transition and bulk correlation limit.

## Limitations
The simple polynomial profile relies on the uniform conditional splitting property. For a nonuniform parent distribution, conditioning on one order statistic does not leave scaled uniform groups and the formula generally changes.

The 2009 uniform-order-statistic moment article was available through its open publication page and abstract, but the complete article text was not retrievable through the bounded paths used here. Because its stated subject includes product moments, an equivalent identity derivable there remains a residual originality risk.

The covariance formula is elementary once the conditional decomposition is recognized; older order-statistic monographs may contain an equivalent mixed moment under different notation.

## References
1. M. Bekçi, “Recurrence relations for the moments of order statistics from uniform distribution,” *Scientific Research and Essays* 4 (2009), 1302–1305. DOI: 10.5897/SRE.9000790.
2. N. Papadatos, “Maximizing the expected range from dependent observations under mean-variance information,” arXiv:1405.6884, first submitted 27 May 2014.
