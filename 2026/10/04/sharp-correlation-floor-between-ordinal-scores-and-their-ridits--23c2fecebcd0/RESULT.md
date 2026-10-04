# Sharp correlation floor between ordinal scores and their ridits

## Finding

Fix positive category probabilities
\[
p_1,\ldots,p_m,
\qquad
\sum_{i=1}^m p_i=1,
\]
and cumulative probabilities
\[
P_j=\sum_{i=1}^j p_i,
\qquad
P_0=0.
\]
The ridit score of category \(i\) is
\[
q_i=P_{i-1}+\frac{p_i}{2}.
\]
Let
\[
x_1<\cdots<x_m
\]
be any strictly increasing numerical scoring of the same ordered categories.
Define random variables \(X\) and \(Q\) by
\[
\Pr(X=x_i,Q=q_i)=p_i.
\]
Put
\[
S_3=\sum_{i=1}^m p_i^3.
\]

If \(m\ge3\), the exact attainable set is
\[
\boxed{
\operatorname{Corr}(X,Q)
\in
\left(
\lambda(\mathbf p),1
\right],
}
\]
where
\[
\boxed{
\lambda(\mathbf p)
=
\sqrt{
\frac{
3\min_{1\le j<m}P_j(1-P_j)
}{
1-S_3
}
}.
}
\]

The upper endpoint is attained exactly when the numerical scores are a positive affine transform of the ridits:
\[
x_i=a+bq_i,
\qquad
b>0.
\]

The lower endpoint is not attained by a strictly increasing scoring when \(m\ge3\), but it is sharp. It is approached by making one score gap dominate all the others across any cut \(j\) minimizing
\[
P_j(1-P_j).
\]
Equivalently, the scoring approaches a two-level coding separated at that cut.

Every correlation strictly between the lower endpoint and one is attained.

For \(m=2\), every strictly increasing scoring is a positive affine transform of every other one, and
\[
\operatorname{Corr}(X,Q)=1.
\]

For equal masses,
\[
p_i=\frac1m,
\]
the formula simplifies to
\[
\boxed{
\operatorname{Corr}(X,Q)
\in
\left(
\sqrt{\frac3{m+1}},1
\right]
}
\qquad(m\ge3).
\]

## Assumptions and scope

The category order and probabilities are fixed. Only the strictly increasing numerical scores assigned to the categories vary.

The ridits are computed from the same probability profile as the scored variable.

The theorem concerns Pearson correlation between an arbitrary increasing score and its ridit score. It does not optimize a two-sample trend statistic, a contingency-table test statistic, or a correlation between two separately distributed ordinal variables.

The lower endpoint is an infimum over strict scorings. If ties between adjacent scores are allowed, a minimizing two-level scoring attains it.

## Proof

Let
\[
\bar q=\mathbb EQ.
\]
Because \(q_i\) is the midpoint of the probability interval
\[
[P_{i-1},P_i],
\]
we have
\[
\bar q=\frac12.
\]

The ridit variance is
\[
\operatorname{Var}(Q)
=
\frac{1-S_3}{12}.
\tag{1}
\]
To verify this, partition a uniform random variable on \([0,1]\) into the probability cells. Conditional on cell \(i\), its mean is \(q_i\) and its variance is \(p_i^2/12\). The total variance identity gives
\[
\frac1{12}
=
\operatorname{Var}(Q)
+
\sum_i p_i\frac{p_i^2}{12},
\]
which is (1).

For each cut \(j=1,\ldots,m-1\), define the centered upper-block indicator
\[
H_j
=
\mathbf 1_{\{X>x_j\}}
-
(1-P_j).
\]
Its variance is
\[
\operatorname{Var}(H_j)
=
P_j(1-P_j).
\tag{2}
\]

The covariance with the ridit has a simple exact form. Since the ridit scores are cell midpoints,
\[
\sum_{i>j}p_iq_i
=
\int_{P_j}^1u\,du
=
\frac{1-P_j^2}{2}.
\]
Hence
\[
\operatorname{Cov}(H_j,Q)
=
\frac{P_j(1-P_j)}{2}.
\tag{3}
\]
Combining (1)--(3),
\[
\operatorname{Corr}(H_j,Q)
=
\sqrt{
\frac{
3P_j(1-P_j)
}{
1-S_3
}
}.
\tag{4}
\]

Now write the adjacent score gaps as
\[
d_j=x_{j+1}-x_j>0.
\]
After subtracting the mean from \(X\),
\[
X-\mathbb EX
=
\sum_{j=1}^{m-1}d_jH_j.
\tag{5}
\]
Let
\[
\lambda
=
\min_j\operatorname{Corr}(H_j,Q).
\]
Using (3)--(5),
\[
\begin{aligned}
\operatorname{Cov}(X,Q)
&=
\sum_j d_j\operatorname{Cov}(H_j,Q)\\
&\ge
\lambda
\sqrt{\operatorname{Var}(Q)}
\sum_j d_j\sqrt{\operatorname{Var}(H_j)}.
\end{aligned}
\tag{6}
\]
The triangle inequality in the weighted \(L^2\) space gives
\[
\sqrt{\operatorname{Var}(X)}
=
\left\|
\sum_jd_jH_j
\right\|_2
\le
\sum_jd_j\|H_j\|_2.
\tag{7}
\]
Equations (6)--(7) yield
\[
\operatorname{Corr}(X,Q)\ge\lambda.
\tag{8}
\]

For \(m\ge3\), all \(d_j\) are positive and at least two distinct centered indicators occur in (5). Distinct \(H_j\) are not positive scalar multiples of one another, so the triangle inequality in (7) is strict. Therefore
\[
\operatorname{Corr}(X,Q)>\lambda.
\]

Sharpness follows by choosing a minimizing cut \(j_*\), setting its gap to one, and making every other adjacent gap tend to zero through positive values. The centered score then converges, after an irrelevant location adjustment, to a multiple of \(H_{j_*}\), so its correlation with \(Q\) tends to the value in (4).

The upper bound
\[
\operatorname{Corr}(X,Q)\le1
\]
is Cauchy--Schwarz. Equality holds exactly when
\[
X-\mathbb EX=b(Q-\mathbb EQ)
\]
almost surely. Because both score vectors are strictly increasing, \(b>0\), giving the stated positive-affine ridit scoring.

Finally, the strict-score cone
\[
\{(x_1,\ldots,x_m):x_1<\cdots<x_m\}
\]
is connected and correlation is continuous on it. Its image is therefore an interval. The sharp lower infimum and attained upper endpoint prove the complete attainable set.

For equal masses,
\[
S_3=\frac1{m^2},
\qquad
\min_jP_j(1-P_j)=\frac{m-1}{m^2},
\]
so
\[
\lambda^2
=
\frac{3}{m+1}.
\]

## Verification

The accompanying exact-rational checker verifies the ridit mean and variance identities, every cut covariance, the sharp lower inequality, and the upper equality case for random rational profiles and random strictly increasing rational scores.

It separately constructs score families with one dominant gap and checks convergence toward the predicted lower endpoint. It also verifies the equal-mass simplification.

The finite replay is supplementary. The universal theorem follows from the step-indicator decomposition, the triangle inequality, and Cauchy--Schwarz.

## Relationship to prior work

Ridit scoring was introduced for ordered categorical data to replace arbitrary category spacing by a probability-based score. Chen and Wang's 2014 article describes ridit scores as uniform-latent conditional-mean scores
\[
q_i=P_{i-1}+\frac{p_i}{2},
\]
and discusses how alternative numerical scoring systems can lead to materially different correlation-based conclusions. It does not give a sharp profile-dependent lower bound on the correlation between an arbitrary increasing score and the ridit score.

Graubard and Korn likewise emphasize that the choice of scores in ordered-category analysis matters and that midrank scores need not be appropriate. Their objective is the power and interpretation of tests in ordered contingency tables, not the geometry of one score vector relative to its ridits.

Kimeldorf, Sampson, and Whitaker study minimum and maximum scores for a two-sample ordinal test statistic. That optimization depends on the observed two-sample problem. The theorem here instead fixes one ordinal marginal distribution and asks a different intrinsic question: how far can any order-preserving numerical coding depart, in Pearson angle, from the probability-determined ridit coding?

A previous fixed-profile Gini inequality identifies ridit spacing as the unique maximizer of a dispersion ratio. It supplies the upper endpoint here but does not imply the new lower endpoint or the complete attainable interval. The new lower bound comes from the extreme rays of the monotone-score cone and from the exact ridit covariance of every cumulative cut.

Targeted searches using ridit correlation floors, arbitrary increasing scores, midrank score robustness, and fixed category probabilities did not locate the displayed lower constant or complete interval.

## Limitations

The theorem fixes the probability profile. If the category probabilities themselves vary, the lower floor can approach zero.

Only order-preserving numerical codings are considered. Allowing arbitrary nonmonotone recodings can produce negative correlations.

The result quantifies linear alignment with ridits, not the power of a particular hypothesis test after recoding.

The originality search was targeted. Older isotonic-cone or score-assignment literature may contain an equivalent angular statement under different terminology.

The full 1992 article on minimum and maximum ordinal scoring was not available through the open full-text routes checked during this review; its abstract-level descriptions and an openly indexed computational follow-up were compared, and this access limitation remains an explicit residual risk.

## References

1. H.-C. Chen and N.-S. Wang, “The Assignment of Scores Procedure for Ordinal Categorical Data,” *The Scientific World Journal* 2014, Article 304213, DOI 10.1155/2014/304213, first published 2014-09-11.
2. B. I. Graubard and E. L. Korn, “Choice of column scores for testing independence in ordered \(2\times K\) contingency tables,” *Biometrics* 43 (1987), 471–476.
3. G. Kimeldorf, A. R. Sampson, and L. R. Whitaker, “Min and Max Scorings for Two-Sample Ordinal Data,” *Journal of the American Statistical Association* 87 (1992), 241–247, DOI 10.1080/01621459.1992.10475198.
4. P. L. Brockett, “A note on the numerical assignment of scores to ranked categorical data,” *Journal of Mathematical Sociology* 8 (1981), 91–101, DOI 10.1080/0022250X.1981.9989917.
