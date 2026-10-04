# Universal positive covariance of sample richness and unbiased Gini–Simpson diversity

## Finding

Let
\[
X_1,\ldots,X_n,
\qquad n\ge2,
\]
be independent and identically distributed observations from a finite categorical law with positive probabilities
\[
p_1,\ldots,p_m,
\qquad
m\ge2,
\qquad
\sum_{a=1}^m p_a=1.
\]

Let
\[
K_n
=
\#\{X_1,\ldots,X_n\}
\]
be the observed richness, and put
\[
s_2=\sum_{a=1}^m p_a^2.
\]
Define the unbiased Simpson concentration estimator
\[
\widehat D_n
=
\binom n2^{-1}
\sum_{1\le i<j\le n}
\mathbf 1\{X_i=X_j\},
\tag{1}
\]
and the corresponding unbiased Gini--Simpson diversity estimator
\[
\widehat G_n=1-\widehat D_n.
\tag{2}
\]

Set
\[
A_n
=
\sum_{a=1}^m
p_a(1-p_a)^{n-2},
\qquad
B_n
=
\sum_{a=1}^m
p_a^2(1-p_a)^{n-2}.
\tag{3}
\]

Then the covariance is exactly
\[
\boxed{
\operatorname{Cov}(K_n,\widehat G_n)
=
2s_2A_n-(1+s_2)B_n.
}
\tag{4}
\]

It is always strictly positive:
\[
\boxed{
\operatorname{Cov}(K_n,\widehat G_n)>0.
}
\tag{5}
\]

More quantitatively,
\[
\boxed{
\operatorname{Cov}(K_n,\widehat G_n)
\ge
s_2(1-s_2)A_n
>
0.
}
\tag{6}
\]

For \(n=2\), equality holds in (6) for every nondegenerate categorical law. For \(n>2\), equality in (6) holds exactly when
\[
p_1=\cdots=p_m=\frac1m.
\tag{7}
\]

Equivalently,
\[
\operatorname{Cov}(K_n,\widehat D_n)<0:
\]
observed richness and unbiased Simpson concentration always move in opposite covariance directions, for every finite nondegenerate categorical law.

For the uniform law on \(m\) categories,
\[
\boxed{
\operatorname{Cov}(K_n,\widehat G_n)
=
\frac{(m-1)^{n-1}}{m^n}.
}
\tag{8}
\]

## Assumptions and scope

The parent law is categorical with finitely many positive masses and at least two categories.

The statistic \(\widehat D_n\) in (1) is the pair-collision \(U\)-statistic. It is unbiased for the population Simpson concentration
\[
s_2=\Pr(X_1=X_2).
\]
The statistic \(\widehat G_n\) is its complement.

The result concerns covariance sign and an exact finite-sample lower bound. It does not claim stochastic monotonicity, association of the full occupancy vector, or a conditional relationship between richness and diversity.

## Proof

Write
\[
I_a
=
\mathbf 1\{\text{category }a\text{ is observed at least once}\}.
\]
Then
\[
K_n=\sum_{a=1}^m I_a.
\]

By exchangeability of sample pairs,
\[
\operatorname{Cov}(K_n,\widehat D_n)
=
\operatorname{Cov}
\left(
K_n,
\mathbf 1\{X_1=X_2\}
\right).
\tag{9}
\]

Fix a category \(a\), and write
\[
Y=\mathbf 1\{X_1=X_2\}.
\]
Since
\[
\mathbb EY=s_2
\]
and
\[
\mathbb EI_a
=
1-(1-p_a)^n,
\]
it remains to calculate \(\mathbb E(I_aY)\).

If the collision \(X_1=X_2\) occurs in category \(a\), then \(I_a=1\). If the collision occurs in another category, then category \(a\) must appear among the remaining \(n-2\) observations. Therefore
\[
\mathbb E(I_aY)
=
p_a^2
+
(s_2-p_a^2)
\left[
1-(1-p_a)^{n-2}
\right].
\tag{10}
\]
Subtracting the product of the expectations gives
\[
\operatorname{Cov}(I_a,Y)
=
p_a(1-p_a)^{n-2}
\left[
p_a(1+s_2)-2s_2
\right].
\tag{11}
\]
Summing (11) over \(a\) yields
\[
\operatorname{Cov}(K_n,\widehat D_n)
=
(1+s_2)B_n-2s_2A_n.
\tag{12}
\]
Since \(\widehat G_n=1-\widehat D_n\), equation (4) follows.

It remains to prove the sign and the lower bound.

Introduce a size-biased random variable \(P\) by
\[
\Pr(P=p_a)=p_a.
\]
Then
\[
\mathbb EP=s_2,
\qquad
A_n=\mathbb E(1-P)^{n-2},
\qquad
B_n=\mathbb E\left[P(1-P)^{n-2}\right].
\tag{13}
\]

The function
\[
f(x)=(1-x)^{n-2}
\]
is nonincreasing on \([0,1]\). If \(P'\) is an independent copy of \(P\), then
\[
(P-P')
\left(
f(P)-f(P')
\right)
\le0.
\]
Taking expectations gives
\[
B_n
=
\mathbb E[P f(P)]
\le
\mathbb EP\,\mathbb Ef(P)
=
s_2A_n.
\tag{14}
\]

Substituting (14) into (4),
\[
\operatorname{Cov}(K_n,\widehat G_n)
\ge
2s_2A_n-(1+s_2)s_2A_n
=
s_2(1-s_2)A_n.
\]
Because the law has at least two positive masses,
\[
0<s_2<1
\]
and
\[
A_n>0,
\]
which proves strict positivity.

For \(n=2\), the function \(f\) is constant, so equality holds in (14) for every law. For \(n>2\), \(f\) is strictly decreasing. Equality in (14) then holds exactly when \(P\) is constant, which means that all positive masses \(p_a\) are equal. This proves the equality classification in (6).

Under the uniform law,
\[
s_2=\frac1m,
\qquad
A_n=
\left(1-\frac1m\right)^{n-2},
\]
and equality holds in (6), yielding (8).

## Verification

The accompanying checker uses exact rational arithmetic.

It enumerates complete categorical sample spaces for several nonuniform and uniform rational laws through sample size six, computes \(K_n\), \(\widehat D_n\), and \(\widehat G_n\) exactly, and compares the directly enumerated covariance with (4).

It separately tests thousands of rational probability profiles and verifies the inequality
\[
B_n\le s_2A_n,
\]
the quantitative lower bound (6), strict positivity, and the equality conditions.

Finite enumeration is supplementary. The universal proof is the exact one-pair covariance calculation and the antitonic size-biased inequality above.

## Relationship to prior work

Barbour studies the classical occupancy scheme with arbitrary box probabilities and treats the number of occupied boxes and frequency counts as primary summary statistics. That work develops sharp distributional approximations for richness-type statistics, rather than their finite-sample covariance with a collision \(U\)-statistic.

Källberg, Leonenko, and Seleznjev study exact coincidences in discrete samples as generalized \(U\)-statistics for Rényi-type functionals. In the quadratic one-sample case, pair coincidences estimate the same population quantity \(s_2\) appearing here. Their focus is consistency and asymptotic normality of the coincidence estimator, not its exact covariance with observed richness.

The present statement links these two classical summaries directly: sample richness and unbiased Gini--Simpson diversity have a universal positive finite-sample covariance under every nondegenerate categorical law. Targeted searches using occupancy, richness, Simpson concentration, collision counts, and covariance formulations did not locate formula (4), lower bound (6), or its equality classification.

## Limitations

The result is a covariance theorem. It does not imply positive association in the stronger probabilistic sense.

The parent law is assumed to have finite support. The same calculation can be extended under summability to countable support, but that extension is not claimed here.

The lower bound uses only \(s_2\) and \(A_n\); it is exact for uniform laws and for all laws at \(n=2\), but it is generally not the exact covariance for nonuniform laws when \(n>2\).

Older occupancy or ecological-diversity literature may contain an equivalent covariance identity under different notation; this remains the principal originality risk.

## References

1. A. D. Barbour, “Univariate approximations in the infinite occupancy scheme,” arXiv:0902.0879, first submitted 2009-02-05.
2. D. Källberg, N. Leonenko, and O. Seleznjev, “Statistical Inference for Rényi Entropy Functionals,” arXiv:1103.4977, first submitted 2011-03-25.
