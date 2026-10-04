# Sharp correlation floor for two increasing codings of one ordinal variable

## Finding

Fix positive category probabilities
\[
p_1,\ldots,p_m,
\qquad
\sum_{i=1}^m p_i=1,
\]
and cumulative probabilities
\[
P_j=\sum_{i=1}^j p_i.
\]
Let the same ordered category receive two strictly increasing numerical codings
\[
x_1<\cdots<x_m,
\qquad
y_1<\cdots<y_m.
\]
Define \(X\) and \(Y\) by
\[
\Pr(X=x_i,Y=y_i)=p_i.
\]

If \(m\ge3\), then the complete attainable Pearson-correlation set is
\[
\boxed{
\operatorname{Corr}(X,Y)
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
\frac{p_1p_m}
{(1-p_1)(1-p_m)}
}.
}
\tag{1}
\]

The upper endpoint is attained exactly when the two score vectors differ by a positive affine transformation:
\[
y_i=a+b x_i,
\qquad b>0.
\tag{2}
\]

The lower endpoint is not attained by two strict codings when \(m\ge3\), but it is sharp. It is approached by making the first gap of one coding dominate all its other gaps while making the last gap of the other coding dominate all its other gaps, or by reversing those roles.

Every correlation strictly between the lower endpoint and one is attained.

For \(m=2\), every two strict codings are positively affine and
\[
\operatorname{Corr}(X,Y)=1.
\]

For equal category masses,
\[
p_i=\frac1m,
\]
formula (1) simplifies to
\[
\boxed{
\operatorname{Corr}(X,Y)
\in
\left(
\frac1{m-1},1
\right]
}
\qquad(m\ge3).
\tag{3}
\]

Thus two order-preserving numerical codings of the same ordinal variable cannot become arbitrarily decorrelated once the category-frequency profile is fixed. The exact worst-case agreement depends only on the two endpoint category masses.

## Assumptions and scope

The category order and probability profile are fixed. Both numerical score vectors vary, subject only to strict monotonicity.

The result concerns Pearson correlation between two deterministic recodings of the same ordinal variable. It does not optimize a correlation over couplings of two different marginal distributions.

The endpoint in (1) is an infimum over strict codings. If tied adjacent scores are admitted, the two-level endpoint codings attain it.

No moment assumptions beyond finiteness are needed because the support is finite.

## Proof

For each cut
\[
j=1,\ldots,m-1,
\]
define the centered upper-block indicator
\[
H_j
=
\mathbf 1_{\{i>j\}}-(1-P_j),
\]
viewed as a random variable on category \(i\).

Let the adjacent score gaps be
\[
d_j=x_{j+1}-x_j>0,
\qquad
e_j=y_{j+1}-y_j>0.
\]
After centering,
\[
X-\mathbb EX
=
\sum_{j=1}^{m-1}d_jH_j,
\qquad
Y-\mathbb EY
=
\sum_{j=1}^{m-1}e_jH_j.
\tag{4}
\]

For
\[
j\le k,
\]
the upper block after \(k\) is contained in the upper block after \(j\). Therefore
\[
\operatorname{Cov}(H_j,H_k)
=
P_j(1-P_k),
\tag{5}
\]
while
\[
\operatorname{Var}(H_j)
=
P_j(1-P_j).
\tag{6}
\]
Consequently
\[
\operatorname{Corr}(H_j,H_k)^2
=
\frac{P_j(1-P_k)}
{(1-P_j)P_k}.
\tag{7}
\]

The odds
\[
\frac{P}{1-P}
\]
are strictly increasing in \(P\). Hence among all cut pairs the smallest correlation is obtained by the most separated cuts:
\[
j=1,
\qquad
k=m-1,
\]
or in the reverse order. Using
\[
P_1=p_1,
\qquad
1-P_{m-1}=p_m,
\]
equation (7) gives exactly
\[
\min_{j,k}
\operatorname{Corr}(H_j,H_k)
=
\lambda(\mathbf p).
\tag{8}
\]

Write
\[
v_j=\sqrt{\operatorname{Var}(H_j)}.
\]
From (4) and (8),
\[
\begin{aligned}
\operatorname{Cov}(X,Y)
&=
\sum_{j,k}d_je_k
\operatorname{Cov}(H_j,H_k)\\
&\ge
\lambda(\mathbf p)
\left(\sum_jd_jv_j\right)
\left(\sum_ke_kv_k\right).
\end{aligned}
\tag{9}
\]
On the other hand, the triangle inequality in \(L^2\) gives
\[
\sqrt{\operatorname{Var}(X)}
\le
\sum_jd_jv_j
\tag{10}
\]
and
\[
\sqrt{\operatorname{Var}(Y)}
\le
\sum_ke_kv_k.
\tag{11}
\]
Combining (9)--(11),
\[
\operatorname{Corr}(X,Y)
\ge
\lambda(\mathbf p).
\tag{12}
\]

When \(m\ge3\),
\[
\lambda(\mathbf p)<1
\]
because
\[
p_1+p_m<1.
\]
All products \(d_je_k\) in (9) are positive, and the diagonal cut pairs satisfy
\[
\operatorname{Corr}(H_j,H_j)=1>\lambda(\mathbf p).
\]
Thus the covariance inequality in (9) is strict, which makes (12) strict for every pair of strict codings.

To prove sharpness, choose one coding whose first gap is one and whose remaining gaps are a common positive number tending to zero. Choose the other coding with last gap one and all preceding gaps tending to zero. After centering, the two score vectors converge to multiples of
\[
H_1
\qquad\text{and}\qquad
H_{m-1}.
\]
Their correlations therefore converge to the value in (8).

Cauchy--Schwarz gives
\[
\operatorname{Corr}(X,Y)\le1.
\]
Equality occurs exactly when the centered score vectors are scalar multiples. Since both score vectors are strictly increasing, the scalar is positive, proving (2).

Finally, the product of the two strict-score cones is connected and correlation is continuous on it. Its image is therefore an interval. The sharp unattained lower endpoint and attained upper endpoint give the complete range.

For equal masses,
\[
p_1=p_m=\frac1m,
\]
so
\[
\lambda(\mathbf p)
=
\frac1{m-1},
\]
which proves (3).

## Verification

The accompanying exact-rational checker generates random rational probability profiles and two random strictly increasing rational score vectors.

It verifies the cut covariance formula, the exact minimum cut correlation after clearing squares, the strict lower bound for \(m\ge3\), exact correlation one for positive affine recodings, and the two-category degeneracy.

It also constructs one-dominant-gap families and checks convergence to the endpoint formula, and verifies the equal-mass simplification.

The finite replay is supplementary. The universal theorem follows from the cut-indicator decomposition, the exact covariance matrix of those cuts, the \(L^2\) triangle inequality, and Cauchy--Schwarz.

## Relationship to prior work

Karlin's association-array framework studies correlations between monotone transforms and, crucially, decomposes increasing functions into positive combinations of upper-set indicators. That supplies the natural cone representation behind (4). The inspected article uses indicator-function correlations to diagnose positive and negative association for general bivariate laws, but it does not give the fixed-one-variable correlation floor (1), its endpoint-mass formula, or the complete attainable interval.

Cuadras and Cuadras study covariance kernels for functions of bivariate random variables and place the problem in the multivariate-analysis setting. Their covariance-kernel formulation is broader but does not specialize, in the accessible statement, to the sharp angle between two arbitrary increasing recodings of one finite ordinal variable with a prescribed frequency profile.

Barbiero studies attainable Pearson correlations for ordinal variables with fixed marginal distributions by varying dependence through copulas. That is a different optimization: both marginal score distributions are held fixed and the joint coupling changes. Here the joint law is deterministic and comonotone, while the numerical support values of both margins vary.

A fixed-profile ridit result gives a sharper lower bound when one of the two codings is fixed to the probability-determined ridit score. It does not imply the present universal two-coding floor, because both score vectors now vary; conversely, (1) does not recover the stronger ridit-specific constant.

Targeted searches for minimum correlation of increasing recodings, monotone transformations of one discrete variable, association arrays, and fixed category probabilities did not locate formula (1).

## Limitations

The probability profile is fixed. If endpoint category masses are allowed to approach zero, the lower floor can approach zero.

Only order-preserving codings are considered. Nonmonotone recodings can have zero or negative correlation.

The result is one-dimensional and finite-category. More general partially ordered state spaces lead to multiple incomparable extreme rays rather than one chain of cumulative cuts.

The originality search was targeted. Classical association, isotonic-cone, or score-assignment literature may contain an equivalent normalized cone-angle theorem under different notation.

## References

1. S. Karlin, “Association arrays in assessing forms of dependencies between bivariate random variables,” *Proceedings of the National Academy of Sciences of the USA* 80 (1983), 647–651, DOI 10.1073/pnas.80.2.647.
2. C. M. Cuadras and D. Cuadras, “Eigenanalysis on a bivariate covariance kernel,” *Journal of Multivariate Analysis* 99 (2008), 2497–2507, DOI 10.1016/j.jmva.2008.02.039.
3. A. Barbiero, “Inducing a desired value of correlation between two point-scale variables: a two-step procedure using copulas,” *AStA Advances in Statistical Analysis* 106 (2022), 357–381, DOI 10.1007/s10182-021-00405-9.
