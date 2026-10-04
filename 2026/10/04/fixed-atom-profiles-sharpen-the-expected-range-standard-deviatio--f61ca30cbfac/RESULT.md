# Fixed atom profiles sharpen the expected-range/standard-deviation bound

## Finding

Fix an integer
\[
n\ge3
\]
and a positive probability profile
\[
p_1,\ldots,p_m,
\qquad
\sum_{i=1}^m p_i=1.
\]
Let \(X\) range over all nondegenerate discrete laws with distinct ordered atoms
\[
x_1<\cdots<x_m,
\qquad
\Pr(X=x_i)=p_i.
\]
For iid copies \(X_1,\ldots,X_n\), define the expected sample range
\[
R_n(X)
=
\mathbb E\!\left[
\max_{1\le j\le n}X_j
-
\min_{1\le j\le n}X_j
\right],
\]
and let
\[
\sigma^2=\operatorname{Var}(X).
\]

Set
\[
P_i=\sum_{j=1}^ip_j,
\qquad
P_0=0,
\]
\[
K_n(u)=u^n+(1-u)^n,
\]
\[
c_i=K_n(P_i)-K_n(P_{i-1}),
\qquad
z_i=\frac{c_i}{p_i}.
\]
Then
\[
\boxed{
R_n(X)^2
\le
C_n(\mathbf p)^2\,\sigma^2,
}
\tag{1}
\]
where the exact fixed-profile constant is
\[
\boxed{
C_n(\mathbf p)^2
=
\sum_{i=1}^m\frac{c_i^2}{p_i}
=
\sum_{i=1}^m p_i z_i^2.
}
\tag{2}
\]

The constant is attained for every positive profile. Equality in (1) holds exactly when
\[
\boxed{
x_i=a+bz_i
\qquad(1\le i\le m)
}
\tag{3}
\]
for some
\[
a\in\mathbb R,
\qquad
b>0.
\]
Thus the probability profile determines a unique maximizing support geometry up to location and positive scale.

The unrestricted sharp expected-range/standard-deviation constant is
\[
B_n^2
=
n^2
\left[
\frac{2}{2n-1}
-
\frac{2((n-1)!)^2}{(2n-1)!}
\right].
\tag{4}
\]
Every finite positive atom profile improves it strictly:
\[
\boxed{
C_n(\mathbf p)<B_n.
}
\tag{5}
\]
More precisely,
\[
\boxed{
B_n^2-C_n(\mathbf p)^2
=
\sum_{i=1}^m
\int_{P_{i-1}}^{P_i}
\left(K_n'(u)-z_i\right)^2\,du.
}
\tag{6}
\]
The right side is the exact loss caused by forcing the unrestricted extremal score to be constant on the probability cells of the discrete law.

## Assumptions and scope

The sample size satisfies \(n\ge3\). The atom masses are fixed, positive, and ordered with the support. Only the numerical support locations vary.

The result concerns the expected full sample range. It does not optimize a single order statistic or a trimmed range separately.

The support is finite. Formula (6) compares the fixed finite profile with the unrestricted square-integrable population class; it does not claim that a fixed number of atoms gives one profile-independent best constant.

The case \(n=2\) is excluded from the new claim because it reduces to the classical Gini mean-difference problem and its discrete atom-profile refinement.

## Proof

For the maximum,
\[
\Pr\!\left(\max_{1\le j\le n}X_j=x_i\right)
=
P_i^n-P_{i-1}^n.
\]
For the minimum,
\[
\Pr\!\left(\min_{1\le j\le n}X_j=x_i\right)
=
(1-P_{i-1})^n-(1-P_i)^n.
\]
Subtracting gives
\[
R_n(X)
=
\sum_{i=1}^m c_i x_i.
\tag{7}
\]
Because
\[
\sum_{i=1}^m c_i
=
K_n(1)-K_n(0)
=
0,
\tag{8}
\]
if
\[
\mu=\mathbb EX,
\]
then
\[
R_n(X)
=
\sum_{i=1}^m p_i z_i(x_i-\mu).
\tag{9}
\]
Also
\[
\sum_{i=1}^m p_i z_i=0.
\tag{10}
\]
Cauchy--Schwarz in the weighted space with weights \(p_i\) yields
\[
R_n(X)^2
\le
\left(\sum_i p_i z_i^2\right)
\left(\sum_i p_i(x_i-\mu)^2\right),
\]
which is exactly (1)--(2).

It remains to check that the equality vector is a valid ordered support. Since
\[
c_i
=
\int_{P_{i-1}}^{P_i}K_n'(u)\,du,
\]
we have
\[
z_i
=
\frac1{p_i}
\int_{P_{i-1}}^{P_i}K_n'(u)\,du.
\tag{11}
\]
Moreover,
\[
K_n''(u)
=
n(n-1)
\left[
u^{n-2}+(1-u)^{n-2}
\right]
>
0
\qquad(0\le u\le1).
\tag{12}
\]
Hence \(K_n'\) is strictly increasing. Its averages over consecutive positive-length intervals are therefore strictly increasing:
\[
z_1<z_2<\cdots<z_m.
\tag{13}
\]
Equality in Cauchy--Schwarz occurs exactly when
\[
x_i-\mu=bz_i
\]
for one nonzero constant \(b\). The common ordering in (13) forces \(b>0\), which proves (3) and the uniqueness statement.

For the unrestricted comparison, define
\[
f_n(u)=K_n'(u)
=
n\left[u^{n-1}-(1-u)^{n-1}\right].
\]
A direct beta-integral calculation gives
\[
\int_0^1 f_n(u)^2\,du
=
B_n^2.
\tag{14}
\]
On each cell
\[
I_i=[P_{i-1},P_i],
\]
equation (11) says that \(z_i\) is the mean of \(f_n\) on \(I_i\). Therefore
\[
\int_{I_i}
(f_n-z_i)^2\,du
=
\int_{I_i}f_n(u)^2\,du
-
p_i z_i^2.
\tag{15}
\]
Summing (15) over the partition gives (6).

Finally, \(f_n\) is strictly increasing and every cell has positive length. Thus \(f_n\) is nonconstant on every cell, so every integral in (6) is positive. This proves the strict sharpening (5).

## Verification

The accompanying exact-rational checker constructs thousands of rational probability profiles and rational ordered supports for sample sizes \(n\ge3\).

It verifies the exact maximum-minus-minimum coefficient formula (7), the zero-sum identity (8), strict monotonicity of the cell-average scores \(z_i\), inequality (1), and equality on the support (3).

It also expands \(K_n'\) as a rational polynomial, integrates its square exactly on every probability cell, and verifies the deficit identity (6) together with strict positivity.

The finite replay is supplementary. The universal theorem follows from the order-statistic probability identities, weighted Cauchy--Schwarz, strict convexity of \(K_n\), and the cell-average orthogonal-decomposition identity.

## Relationship to prior work

Plackett's 1947 paper is the classical source for sharp bounds on the ratio of mean sample range to population standard deviation. The available bibliographic record confirms the article, date, and scope. A later order-statistics paper explicitly describes Plackett as having obtained the precise expected-range bound in standard-deviation units. The full Plackett PDF required publisher verification during this review and was therefore not used for a whole-document noncoverage claim.

Kozyra and Rychlik develop sharp bounds for expectations of arbitrary centered \(L\)-statistics in Gini mean-difference units. Their full paper explicitly places Plackett's expected-range/standard-deviation theorem as the first result in the subject, and then solves a different normalization problem based on Gini mean difference. Their theorem optimizes over unrestricted parent distributions rather than over support locations with a prescribed atom-probability profile.

Han, Wang, and Wu define the higher-order Gini deviation as expected sample range divided by the sample order \(n\). Their full arXiv text gives a sharp global comparison with standard deviation and identifies the unrestricted quantile-score extremizer. It does not fix a finite probability partition. The present result is a profile-specific projection theorem: it replaces that unrestricted score by its exact conditional means on the prescribed probability cells, gives a strictly smaller constant, and identifies the unique maximizing support.

Targeted searches using expected range, standard deviation, prescribed probabilities, finite supports, \(L\)-statistics, higher-order Gini deviations, and support geometry did not locate formulas (2), (3), or (6).

## Limitations

The profile is fixed and finite. If the number and masses of atoms may vary, the constants can approach the unrestricted sharp value.

The result treats the full expected range. Other \(L\)-statistics lead to different score functions and may have non-monotone cell averages, so the same equality geometry need not remain an ordered support.

The originality assessment is targeted. Older projection-method literature on order statistics may contain an equivalent fixed-partition specialization under different terminology.

The full 1947 Plackett text was not accessible without a publisher-side human verification step, so the comparison with that paper is limited to its verified bibliographic scope and later primary descriptions.

## References

1. R. L. Plackett, “Limits of the Ratio of Mean Range to Standard Deviation,” *Biometrika* 34 (1947), 120–122, DOI 10.1093/biomet/34.1-2.120.
2. P. M. Kozyra and T. Rychlik, “Sharp bounds on the expectations of L-statistics expressed in the Gini mean difference units,” *Communications in Statistics—Theory and Methods* 46 (2017), 2921–2941, DOI 10.1080/03610926.2015.1053937.
3. X. Han, R. Wang, and Q. Wu, “Higher-order Gini indices: An axiomatic approach,” arXiv:2508.10663, first submitted 2025-08-14.
