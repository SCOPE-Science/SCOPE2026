# Exact sign phase diagram for sample-mean/sample-range covariance in three-point laws

## Finding

Let
\[
n\ge2,
\qquad
a,b,c>0,
\qquad
a+b+c=1.
\]
Let \(X\) have ordered support
\[
x_1<x_2<x_3
\]
with masses
\[
\Pr(X=x_1)=a,\qquad
\Pr(X=x_2)=b,\qquad
\Pr(X=x_3)=c.
\]
For iid copies \(X_1,\ldots,X_n\), write
\[
\bar X_n=\frac1n\sum_{j=1}^nX_j,
\qquad
R_n=X_{(n)}-X_{(1)}.
\]

Positive affine transformations multiply the covariance by a positive square, so its sign depends only on the normalized support
\[
(x_1,x_2,x_3)=(0,t,1),
\qquad
0<t<1.
\]
Define
\[
\phi_n(u)=(1-u)^{n-1}-u^{n-1}.
\]
Then
\[
\boxed{
\begin{aligned}
\operatorname{Cov}(\bar X_n,R_n)
={}&-a(1-a)\phi_n(a)t^2\\
&+ac\!\left[\phi_n(c)-\phi_n(a)\right]t(1-t)\\
&+c(1-c)\phi_n(c)(1-t)^2.
\end{aligned}
}
\tag{1}
\]

This gives a complete sign phase diagram.

If
\[
a\ge\frac12,
\]
then
\[
\boxed{\operatorname{Cov}(\bar X_n,R_n)>0}
\]
for every ordered three-point support.

If
\[
c\ge\frac12,
\]
then
\[
\boxed{\operatorname{Cov}(\bar X_n,R_n)<0}
\]
for every ordered three-point support.

Finally, suppose
\[
a<\frac12,
\qquad
c<\frac12.
\]
Put
\[
\alpha=a(1-a)\phi_n(a)>0,
\qquad
\beta=c(1-c)\phi_n(c)>0,
\]
and
\[
\delta=ac\!\left[\phi_n(c)-\phi_n(a)\right].
\]
Define
\[
r_*=
\frac{\delta+\sqrt{\delta^2+4\alpha\beta}}{2\alpha},
\qquad
t_*=\frac{r_*}{1+r_*}.
\tag{2}
\]
Then \(t_*\in(0,1)\) is the unique support shape for which the two statistics are uncorrelated, and
\[
\boxed{
\begin{cases}
\operatorname{Cov}(\bar X_n,R_n)>0,&0<t<t_*,\\
\operatorname{Cov}(\bar X_n,R_n)=0,&t=t_*,\\
\operatorname{Cov}(\bar X_n,R_n)<0,&t_*<t<1.
\end{cases}
}
\tag{3}
\]

When the endpoint masses agree,
\[
a=c<\frac12,
\]
reflection symmetry gives
\[
t_*=\frac12.
\]
For unequal endpoint masses, the unique zero-covariance support is generally asymmetric.

## Assumptions and scope

The theorem fixes the three ordered atom probabilities and varies only the middle support location up to positive affine equivalence.

The claim is about covariance and uncorrelatedness, not independence. In particular, a zero in (3) does not contradict normal-characterization theorems based on independence of the sample mean and sample range.

The sample size is any fixed integer \(n\ge2\). All moments exist automatically because the population support is finite.

The phase diagram is special to three support points. With four or more atoms, the support geometry has several independent gaps and the covariance becomes a higher-dimensional quadratic form.

## Proof

Write the two support gaps as
\[
d_1=t,\qquad d_2=1-t.
\]
For each observation define the nested indicators
\[
B_{r,1}=\mathbf 1_{\{X_r>x_1\}},
\qquad
B_{r,2}=\mathbf 1_{\{X_r=x_3\}},
\]
and their sample averages
\[
\bar B_k=\frac1n\sum_{r=1}^nB_{r,k}.
\]
Also define
\[
J_1=\mathbf 1_{\{\text{the sample crosses the cut }x_1\mid\{x_2,x_3\}\}},
\]
\[
J_2=\mathbf 1_{\{\text{the sample crosses the cut }\{x_1,x_2\}\mid x_3\}}.
\]
Then
\[
\bar X_n=d_1\bar B_1+d_2\bar B_2,
\qquad
R_n=d_1J_1+d_2J_2.
\tag{4}
\]

By exchangeability,
\[
\operatorname{Cov}(\bar B_k,J_\ell)
=
\operatorname{Cov}(B_{1,k},J_\ell).
\tag{5}
\]
A direct conditioning calculation gives
\[
\operatorname{Cov}(\bar B_1,J_1)
=
-a(1-a)\phi_n(a),
\tag{6}
\]
\[
\operatorname{Cov}(\bar B_2,J_2)
=
c(1-c)\phi_n(c),
\tag{7}
\]
\[
\operatorname{Cov}(\bar B_2,J_1)
=
-ac\phi_n(a),
\tag{8}
\]
and
\[
\operatorname{Cov}(\bar B_1,J_2)
=
ac\phi_n(c).
\tag{9}
\]

For example, to obtain (8), note that
\[
\mathbb E[B_{1,2}J_1]
=
c(1-a^{\,n-1}),
\]
whereas
\[
\mathbb E B_{1,2}=c
\]
and
\[
\mathbb E J_1=1-a^n-(1-a)^n.
\]
Subtracting the product of the means yields
\[
-ac\left[(1-a)^{n-1}-a^{n-1}\right].
\]
The other three identities follow in the same way.

Expanding the covariance of the two expressions in (4) and using (6)--(9) proves (1).

The function \(\phi_n\) is strictly decreasing on \((0,1)\), because
\[
\phi_n'(u)
=
-(n-1)\left[(1-u)^{n-2}+u^{n-2}\right]<0,
\]
and
\[
\phi_n(1/2)=0.
\tag{10}
\]

If \(a\ge1/2\), then \(c<1/2\), so
\[
\phi_n(a)\le0<\phi_n(c).
\]
Every term on the right side of (1) is nonnegative and at least one is strictly positive for \(0<t<1\). Hence the covariance is positive.

If \(c\ge1/2\), the reflected argument gives strict negativity.

Now assume \(a,c<1/2\). With the constants in (2), divide (1) by the positive quantity \((1-t)^2\) and put
\[
r=\frac{t}{1-t}>0.
\]
Then
\[
\frac{\operatorname{Cov}(\bar X_n,R_n)}{(1-t)^2}
=
-\alpha r^2+\delta r+\beta.
\tag{11}
\]
The quadratic in (11) is positive at \(r=0\), tends to negative infinity, and has root product
\[
-\frac{\beta}{\alpha}<0.
\]
It therefore has exactly one positive root, namely \(r_*\) in (2). This proves the sign trichotomy (3).

## Verification

The accompanying checker uses exact rational arithmetic for the covariance formula and sign claims.

For small sample sizes it enumerates every iid sample from random rational three-point populations and checks the direct covariance against (1).

For a much larger collection of rational probability profiles and support locations, it checks the four cut-indicator covariance identities (6)--(9), the majority-endpoint sign rules, and the uniqueness of the positive root in the two-minority-endpoint regime.

It also verifies the reflection identity
\[
C_n(a,b,c;t)=-C_n(c,b,a;1-t),
\]
which is required by replacing \(X\) by \(1-X\).

Finite replay supplements but does not replace the algebraic proof.

## Relationship to prior work

Hwang and Hu established the classical characterization direction: under regularity conditions, independence of the sample mean and a broad class of centered order-statistic functionals characterizes normality, and their class explicitly includes the sample range.

Hu and Lin later revisited and generalized that framework. Their full paper states as Corollary 1 that independence of the sample mean and sample range characterizes the normal distribution, and Section 5 develops additional deterministic inequalities for the sample range. Those results address independence and range normalization rather than the sign of covariance for a fixed discrete population.

The distinction is substantial. Independence forces zero covariance, but zero covariance alone is much weaker. Formula (1) identifies exactly when zero covariance occurs inside every fixed three-point mass profile, including asymmetric non-normal populations.

A recent paper on sample-range inequalities studies deterministic order covariance between two ordered numerical vectors. That is a different covariance from the stochastic covariance between \(\bar X_n\) and \(R_n\) under repeated iid sampling.

Targeted searches for sample-mean/sample-range covariance, uncorrelatedness, three-point populations, and fixed atom probabilities did not locate formula (1), the majority-endpoint sign rule, or the unique zero-support threshold (2).

## Limitations

The complete phase diagram is proved only for three-point populations.

The theorem classifies covariance sign, not the full Pearson correlation magnitude and not independence.

The originality assessment is targeted. Older quality-control or order-statistics literature may contain a special-case covariance computation under different notation.

The archive anchor is indexed with an exact public date that differs from the month printed on the journal issue; the exact indexed date is used in the metadata, while the bibliographic citation retains the journal year.

## References

1. T.-Y. Hwang and C.-Y. Hu, “On Some Characterizations of Population Distributions,” *Taiwanese Journal of Mathematics* 4 (2000), 427–437, DOI 10.11650/twjm/1500407259.
2. C.-Y. Hu and G. D. Lin, “Characterizations of the normal distribution via the independence of the sample mean and the feasible definite statistics with ordered arguments,” *Annals of the Institute of Statistical Mathematics* 74 (2022), 473–488, DOI 10.1007/s10463-021-00805-3.
3. C.-Y. Hu and G. D. Lin, “On the Sample Range Inequalities,” *Sankhya A* (2026), DOI 10.1007/s13171-026-00457-6.
