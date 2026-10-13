# Wilcoxon signed-rank and sample mean have an exact Gini covariance

## Finding

Let \(X_1,\ldots,X_n\) be iid from an atomless distribution symmetric about \(0\), and assume
\[
\operatorname{Var}(X_1)=\sigma^2\in(0,\infty).
\]
Let \(R_i\) be the rank of \(|X_i|\) among \(|X_1|,\ldots,|X_n|\), and define the positive Wilcoxon signed-rank statistic
\[
W_n^+=\sum_{i=1}^n R_i\mathbf1\{X_i>0\}.
\]
Put
\[
\mu_1=\mathbb E|X_1|
\]
and let
\[
\Delta=\mathbb E|X_1-X_2|
\]
be the population Gini mean difference.

Then, for every integer \(n\ge1\),
\[
\boxed{
\operatorname{Cov}(\bar X_n,W_n^+)
=
\frac{\mu_1}{2}
+
\frac{n-1}{4}\Delta.
}
\tag{1}
\]

The null variance of the signed-rank statistic is
\[
\boxed{
\operatorname{Var}(W_n^+)
=
\frac{n(n+1)(2n+1)}{24}.
}
\tag{2}
\]

Consequently,
\[
\boxed{
\operatorname{Corr}(\bar X_n,W_n^+)
=
\frac{
\sqrt6\,[2\mu_1+(n-1)\Delta]
}{
2\sigma\sqrt{(n+1)(2n+1)}
}.
}
\tag{3}
\]

In particular,
\[
\boxed{
\operatorname{Corr}(\bar X_n,W_n^+)
\longrightarrow
\frac{\sqrt3\,\Delta}{2\sigma}.
}
\tag{4}
\]

Thus the limiting dependence between the classical sample mean and the distribution-free signed-rank statistic is exactly a standardized Gini mean difference.

For a normal parent \(X_1\sim N(0,\sigma^2)\),
\[
\mu_1=\sigma\sqrt{\frac2\pi},
\qquad
\Delta=\frac{2\sigma}{\sqrt\pi},
\]
and therefore
\[
\boxed{
\operatorname{Corr}(\bar X_n,W_n^+)
=
\sqrt{\frac6\pi}\,
\frac{n-1+\sqrt2}{\sqrt{(n+1)(2n+1)}}
\longrightarrow
\sqrt{\frac3\pi}.
}
\tag{5}
\]
The square of the limiting correlation is
\[
\frac3\pi,
\]
which is the classical normal-theory Pitman asymptotic relative efficiency of the Wilcoxon signed-rank test relative to the one-sample \(t\)-test.

For a centered uniform parent \(X_1\sim\operatorname{Unif}[-a,a]\),
\[
\mu_1=\frac a2,
\qquad
\Delta=\frac{2a}{3},
\qquad
\sigma=\frac a{\sqrt3},
\]
so
\[
\boxed{
\operatorname{Corr}(\bar X_n,W_n^+)
=
\sqrt{\frac{2n+1}{2n+2}}
\longrightarrow1.
}
\tag{6}
\]
Hence the two centered statistics are not merely asymptotically efficient in the same location problem under a uniform law: after standardization they become asymptotically perfectly correlated.

## Assumptions and scope

The parent distribution is atomless and symmetric about \(0\). Atomlessness implies that ties among the absolute observations have probability zero and that pair sums equal zero with probability zero. The result is therefore stated for the usual untied Wilcoxon signed-rank statistic.

A finite, strictly positive second moment is assumed. This guarantees a finite first absolute moment and a finite Gini mean difference.

The theorem is a null-distribution joint-moment statement. It does not give finite-sample power under a location shift, and it does not identify the Pitman efficiency away from the Gaussian model. The equality between the squared limiting correlation and \(3/\pi\) is asserted only for the normal parent.

## Proof

Because the parent is symmetric and atomless, the signs of the observations are iid fair signs and are independent of the absolute values. Conditional on the absolute values, the ranks \(R_1,\ldots,R_n\) are a permutation of \(1,\ldots,n\). Therefore
\[
\mathbb E[W_n^+\mid |X_1|,\ldots,|X_n|]
=
\frac12\sum_{r=1}^n r
=
\frac{n(n+1)}4
\]
and
\[
\operatorname{Var}(W_n^+\mid |X_1|,\ldots,|X_n|)
=
\frac14\sum_{r=1}^n r^2
=
\frac{n(n+1)(2n+1)}{24}.
\]
The conditional mean is constant, so (2) follows immediately.

For the covariance, use the exact Walsh-average representation of the signed-rank statistic:
\[
W_n^+
=
\sum_{1\le i\le j\le n}
\mathbf1\{X_i+X_j>0\}.
\tag{7}
\]
A short verification of (7) is as follows. A positive observation contributes its own diagonal pair. For a pair of observations with the same sign, two positive observations contribute one positive Walsh pair and two negative observations contribute none. For an opposite-sign pair, the Walsh average is positive exactly when the positive observation has larger absolute value. This is exactly the contribution counted when the positive observation's absolute rank is expanded into its baseline \(1\) plus the number of smaller absolute observations.

Since \(\mathbb E\bar X_n=0\), expand (7):
\[
\operatorname{Cov}(\bar X_n,W_n^+)
=
\frac1n
\sum_{k=1}^n
\sum_{1\le i\le j\le n}
\mathbb E\!\left[
X_k\mathbf1\{X_i+X_j>0\}
\right].
\tag{8}
\]

For a diagonal Walsh pair \(i=j\), only \(k=i\) contributes, by independence and centering. Symmetry gives
\[
\mathbb E[X_i\mathbf1\{X_i>0\}]
=
\frac12\mathbb E|X_i|
=
\frac{\mu_1}{2}.
\]
There are \(n\) such diagonal contributions, and the prefactor \(1/n\) in (8) leaves
\[
\frac{\mu_1}{2}.
\tag{9}
\]

For an off-diagonal pair \(i<j\), only \(k=i\) and \(k=j\) contribute. Their sum is
\[
\mathbb E\!\left[
(X_i+X_j)\mathbf1\{X_i+X_j>0\}
\right].
\]
The distribution of \(X_i+X_j\) is symmetric, so this equals
\[
\frac12\mathbb E|X_i+X_j|.
\]
Because \(X_j\) and \(-X_j\) have the same distribution,
\[
\mathbb E|X_i+X_j|
=
\mathbb E|X_i-X_j|
=
\Delta.
\]
Thus each off-diagonal pair contributes \(\Delta/2\) before the prefactor \(1/n\). There are \(n(n-1)/2\) such pairs, giving
\[
\frac1n\binom n2\frac{\Delta}{2}
=
\frac{n-1}{4}\Delta.
\tag{10}
\]
Combining (9) and (10) proves (1).

Since
\[
\operatorname{Var}(\bar X_n)=\frac{\sigma^2}{n},
\]
equations (1) and (2) give (3). Dividing numerator and denominator in (3) by \(n\) yields the limit (4).

For a normal parent, the standard absolute-moment formulas give
\[
\mathbb E|X_1|=\sigma\sqrt{\frac2\pi}
\]
and, because \(X_1-X_2\sim N(0,2\sigma^2)\),
\[
\Delta=\frac{2\sigma}{\sqrt\pi}.
\]
Substitution into (3) proves (5).

For \(X_1\sim\operatorname{Unif}[-a,a]\), direct integration gives
\[
\mu_1=\frac a2,
\qquad
\Delta=\frac{2a}{3},
\qquad
\sigma^2=\frac{a^2}{3}.
\]
Substitution into (3) simplifies to (6).

## Verification

The accompanying checker performs three independent finite checks.

First, for every sign pattern through sample size \(12\) on distinct deterministic absolute magnitudes, it compares the rank definition of \(W_n^+\) with the count of positive Walsh averages. This checks the exact combinatorial identity (7).

Second, it exhausts all \(2^n\) sign patterns through sample size \(14\) and computes the signed-rank null mean and variance by exact rational arithmetic, comparing them with
\[
\frac{n(n+1)}4
\]
and
\[
\frac{n(n+1)(2n+1)}{24}.
\]

Third, for the centered uniform law it checks the covariance by a route that does not use Walsh pairs. Conditional on absolute magnitudes,
\[
\operatorname{Cov}(\bar X_n,W_n^+\mid |X_1|,\ldots,|X_n|)
=
\frac1{2n}\sum_{r=1}^n r\,A_{(r)},
\]
where \(A_i=|X_i|\). For \(A_i\sim\operatorname{Unif}[0,a]\),
\[
\mathbb E A_{(r)}=\frac{ar}{n+1}.
\]
This gives
\[
\operatorname{Cov}(\bar X_n,W_n^+)
=
\frac{a(2n+1)}{12},
\]
which the checker compares by exact arithmetic with (1) using
\[
\mu_1=\frac a2,
\qquad
\Delta=\frac{2a}{3}.
\]

These finite checks supplement, rather than replace, the all-\(n\) proof.

## Relationship to prior work

Wilcoxon introduced the signed-rank statistic in 1945. Modern exact descriptions also identify it with the number of positive Walsh averages, equivalently the number of pairs
\[
\frac{X_i+X_j}{2},
\qquad
i\le j,
\]
above the hypothesized center.

The classical literature compares signed-rank procedures with the one-sample \(t\)-test through power and asymptotic relative efficiency. Hodges and Lehmann studied the Pitman efficiency of nonparametric competitors of the \(t\)-test, and later expositions give
\[
\operatorname{ARE}(W,t)=\frac3\pi
\]
under normal sampling. Klotz studied small-sample power and efficiency of the one-sample Wilcoxon test.

Those comparisons do not determine the same-sample covariance of the two statistics. The identity (1) is instead an exact finite-\(n\) mixed moment under the null. Its limiting form (4) reveals a separate population quantity, the Gini mean difference, as the dependence parameter between the sample mean and signed-rank statistic. Under normality, the square of this limiting correlation happens to equal the classical \(3/\pi\) efficiency.

A modern full treatment of the signed-rank procedure develops its asymptotic power, the normal-theory \(3/\pi\) efficiency, and its Walsh-average estimator. In the inspected signed-rank chapter, no finite formula for
\[
\operatorname{Cov}(\bar X_n,W_n^+)
\]
or its Gini representation is stated.

## Limitations

The theorem assumes an atomless symmetric parent and the untied signed-rank statistic. Ties or point masses require a convention for midranks and alter the exact null variance.

The covariance formula is centered at the true symmetry point. Under a nonzero location shift, neither the fair-sign argument nor the displayed covariance formula applies unchanged.

The normal-theory \(3/\pi\) statement is an asymptotic efficiency comparison. The theorem does not claim that squared correlation equals Pitman efficiency for arbitrary symmetric distributions.

Although targeted searches and the closest signed-rank literature inspected did not reveal the finite covariance identity, the literature on linear rank statistics is extensive. An older source could contain the same mixed moment under a different normalization or in a general joint-limit theorem.

## References

1. F. Wilcoxon, “Individual Comparisons by Ranking Methods,” *Biometrics Bulletin* 1(6), 80–83, first published 1945-12-01, DOI:10.2307/3001968.
2. J. L. Hodges, Jr. and E. L. Lehmann, “The Efficiency of Some Nonparametric Competitors of the \(t\)-Test,” *The Annals of Mathematical Statistics* 27(2), 324–335, 1956, DOI:10.1214/aoms/1177728261.
3. J. Klotz, “Small Sample Power and Efficiency for the One Sample Wilcoxon and Normal Scores Tests,” *The Annals of Mathematical Statistics* 34(2), 624–632, 1963, DOI:10.1214/aoms/1177704175.
4. R. H. Randles, “Wilcoxon Signed Rank Test,” *Wiley StatsRef: Statistics Reference Online*, DOI:10.1002/9781118445112.stat02791.
