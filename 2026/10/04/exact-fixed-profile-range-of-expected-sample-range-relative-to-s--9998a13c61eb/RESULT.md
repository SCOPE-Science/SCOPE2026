# Exact fixed-profile range of expected sample range relative to standard deviation

## Finding

Fix integers
\[
N\ge3,
\qquad
m\ge2.
\]
Let a parent distribution have positive masses
\[
p_1,\ldots,p_m,
\qquad
\sum_{i=1}^m p_i=1,
\]
at distinct ordered atoms
\[
x_1<\cdots<x_m.
\]
Put
\[
P_j=\sum_{i=1}^j p_i,
\qquad
P_0=0,
\qquad
\sigma^2=\operatorname{Var}(X).
\]
For an iid sample
\[
X_1,\ldots,X_N,
\]
write
\[
R_N=X_{N:N}-X_{1:N}
\]
for the sample range.

For each support cut define
\[
a_j
=
1-P_j^N-(1-P_j)^N,
\qquad
1\le j<m,
\]
and
\[
\boxed{
L_N(\mathbf p)
=
\min_{1\le j<m}
\frac{a_j}{\sqrt{P_j(1-P_j)}}.
}
\tag{1}
\]

Next define
\[
f_N(u)=u^N+(1-u)^N
\]
and the range-score values
\[
s_i
=
\frac{
f_N(P_i)-f_N(P_{i-1})
}{
p_i
},
\qquad
1\le i\le m.
\tag{2}
\]
These scores have weighted mean zero. Put
\[
\boxed{
U_N(\mathbf p)
=
\sqrt{
\sum_{i=1}^m p_i s_i^2
}.
}
\tag{3}
\]

If \(m=2\), the ratio is independent of the two support locations:
\[
\boxed{
\frac{\mathbb ER_N}{\sigma}
=
L_N(\mathbf p)
=
U_N(\mathbf p).
}
\tag{4}
\]

For every
\[
m\ge3,
\]
the complete attainable set is
\[
\boxed{
\frac{\mathbb ER_N}{\sigma}
\in
\left(
L_N(\mathbf p),
U_N(\mathbf p)
\right].
}
\tag{5}
\]

The upper endpoint is attained exactly by positive affine transforms of the range scores:
\[
\boxed{
x_i=\alpha+\beta s_i,
\qquad
\beta>0.
}
\tag{6}
\]

The lower endpoint is not attained by a strict \(m\)-point support when \(m\ge3\), but it is sharp. It is approached by making one adjacent support gap dominate all others at any cut minimizing the expression in (1).

Every value strictly between the two endpoints is attained.

Thus, once the parent category probabilities and the sample size are known, there is an exact interval of possible expected-range efficiencies relative to the parent standard deviation. The upper-optimal support is explicit and unique up to location and positive scale.

## Assumptions and scope

The sample observations are independent and identically distributed.

The parent probability masses are fixed and positive. Only the distinct ordered support locations vary.

The sample size satisfies \(N\ge3\). The analogous \(N=2\) case reduces to the Gini mean difference and has a separate fixed-profile interpretation.

The theorem concerns the expected sample range normalized by the parent standard deviation. It does not describe the variance or full distribution of the sample range.

## Proof

Let
\[
d_j=x_{j+1}-x_j>0.
\]
A sample spans the \(j\)-th support gap exactly when it contains at least one observation on each side of that cut. Therefore
\[
\Pr\{X_{1:N}\le x_j<X_{N:N}\}
=
1-P_j^N-(1-P_j)^N
=
a_j.
\]
Since the sample range is the sum of precisely the gaps that it spans,
\[
\boxed{
\mathbb ER_N
=
\sum_{j=1}^{m-1}a_jd_j.
}
\tag{7}
\]

For the lower bound, define the centered upper-cut indicators
\[
H_j
=
\mathbf 1_{\{X>x_j\}}-(1-P_j).
\]
Then
\[
X-\mathbb EX
=
\sum_{j=1}^{m-1}d_jH_j
\tag{8}
\]
and
\[
\|H_j\|_2
=
\sqrt{P_j(1-P_j)}.
\tag{9}
\]
By the triangle inequality,
\[
\sigma
\le
\sum_{j=1}^{m-1}
d_j\sqrt{P_j(1-P_j)}.
\tag{10}
\]
Combining (7), (10), and the definition of \(L_N\),
\[
\mathbb ER_N
\ge
L_N(\mathbf p)
\sum_jd_j\sqrt{P_j(1-P_j)}
\ge
L_N(\mathbf p)\sigma.
\tag{11}
\]

If \(m\ge3\), at least two positive coefficients occur in (8), and the corresponding centered nested indicators are not positive scalar multiples. Hence the triangle inequality in (10) is strict. Therefore
\[
\frac{\mathbb ER_N}{\sigma}
>
L_N(\mathbf p).
\tag{12}
\]
If a minimizing cut is fixed and its gap is held at one while every other gap tends to zero through positive values, the centered support converges to a multiple of that cut indicator. Formula (7) then shows that the ratio converges to the value in (1). This proves sharpness of the lower infimum.

For the upper bound, use the exact extreme-order probabilities
\[
\Pr\{X_{N:N}=x_i\}
=
P_i^N-P_{i-1}^N
\]
and
\[
\Pr\{X_{1:N}=x_i\}
=
(1-P_{i-1})^N-(1-P_i)^N.
\]
Subtracting the expectations gives
\[
\begin{aligned}
\mathbb ER_N
&=
\sum_{i=1}^m
x_i
\left[
f_N(P_i)-f_N(P_{i-1})
\right]\\
&=
\sum_{i=1}^m p_i x_i s_i.
\end{aligned}
\tag{13}
\]
Because
\[
\sum_i p_is_i
=
f_N(1)-f_N(0)
=
0,
\]
equation (13) is the covariance identity
\[
\boxed{
\mathbb ER_N
=
\operatorname{Cov}(X,S),
}
\tag{14}
\]
where \(S=s_i\) on category \(i\).

Cauchy--Schwarz now gives
\[
\mathbb ER_N
\le
\sigma
\sqrt{\operatorname{Var}(S)}
=
\sigma U_N(\mathbf p).
\tag{15}
\]

It remains to check that the equality support is admissible. For
\[
N\ge3,
\]
the function
\[
f_N(u)=u^N+(1-u)^N
\]
is strictly convex on \([0,1]\), because
\[
f_N''(u)
=
N(N-1)
\left[
u^{N-2}+(1-u)^{N-2}
\right]
>
0.
\]
The values \(s_i\) in (2) are consecutive secant slopes of this strictly convex function across the probability cells
\[
[P_{i-1},P_i].
\]
Hence
\[
s_1<\cdots<s_m.
\tag{16}
\]
Thus the support
\[
x_i=s_i
\]
is strictly ordered and attains equality in (15).

Conversely, equality in Cauchy--Schwarz requires
\[
X-\mathbb EX
=
\beta S
\]
almost surely. Since both supports are strictly increasing,
\[
\beta>0,
\]
which proves the exact upper equality condition (6).

For \(m=2\), there is only one positive support gap, so both lower and upper arguments are equalities and (4) follows.

Finally, after fixing an arbitrary location and scale normalization, the strict support cone is connected and the ratio
\[
\mathbb ER_N/\sigma
\]
is continuous. Its image is therefore an interval. The sharp lower infimum and attained upper endpoint prove (5).

## Verification

The accompanying exact-rational checker verifies the gap formula, the extreme-order probability formula, the score covariance identity, the lower squared inequality, and the upper squared inequality for random rational mass profiles and random strict rational supports.

It separately verifies that the range scores are strictly increasing, that choosing the support affine to those scores gives exact upper equality, and that one-dominant-gap support families approach the predicted lower endpoint.

For small support and sample sizes, it also directly enumerates all iid sample tuples and confirms the expected-range formula.

The finite replay is supplementary. The universal theorem follows from the exact identities, the Hilbert-space triangle inequality, strict convexity of \(f_N\), and Cauchy--Schwarz.

## Relationship to prior work

Classical order-statistic theory has long studied distribution-free bounds for the expected sample range in standard-deviation units. Papadatos reviews the Plackett, Gumbel, and Hartley--David iid bounds and states the classical sharp upper bound when only the common mean and variance are known. His 2014 work then solves a broader dependent-observation range problem under marginal mean--variance information.

Goroncy and Rychlik likewise place sample-range and spacing inequalities inside the projection theory of \(L\)-statistics and review sharp standardized expectation bounds over unrestricted and shape-restricted parent-distribution classes.

Those problems optimize over broad classes of parent distributions. The theorem here imposes different information: the entire vector of atom probabilities is fixed, while the ordered atom locations are free. The additional finite-profile information produces both a positive lower floor and a profile-specific upper endpoint with an explicit unique optimal support.

The upper range score in (2) is the cellwise secant slope of
\[
u\mapsto u^N+(1-u)^N.
\]
This is a discrete fixed-profile analogue of the score/projection functions that appear in classical \(L\)-statistic bounds, but the inspected sources do not state the exact interval (5), the lower cut formula (1), or the cellwise support optimizer (6).

Targeted semantic and exact-formula searches for fixed atom probabilities, prescribed discrete profiles, expected range over parent standard deviation, support geometry, and secant-slope range scores did not locate this statement.

## Limitations

The probability vector is fixed. If profiles themselves vary, the endpoints must be optimized again and classical distribution-free bounds become the relevant comparison.

The theorem assumes iid sampling. The broader dependent-sample range problem has different extremizers.

Only the expected sample range is classified; higher moments and the distribution of the range are not determined.

The originality search was targeted. Projection-theoretic order-statistic literature is extensive, and an equivalent fixed-partition statement may exist under a different formulation.

## References

1. N. Papadatos, “Maximizing the expected range from dependent observations under mean-variance information,” arXiv:1405.6884, first submitted 2014-05-27; later published in *Statistics*, DOI 10.1080/02331888.2015.1074234.
2. A. Goroncy and T. Rychlik, “Evaluations of expectations of order statistics and spacings based on IFR distributions,” *Metrika* 79 (2016), 635–657, DOI 10.1007/s00184-015-0570-8.
3. R. L. Plackett, “Limits of the ratio of mean range to standard deviation,” *Biometrika* 34 (1947), 120–122.
4. H. O. Hartley and H. A. David, “Universal bounds for mean range and extreme observation,” *Annals of Mathematical Statistics* 25 (1954), 85–99.
