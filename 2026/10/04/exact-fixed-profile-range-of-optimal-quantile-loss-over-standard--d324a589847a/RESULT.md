# Exact fixed-profile range of optimal quantile loss over standard deviation

## Finding

Fix a quantile level
\[
0<\tau<1
\]
and positive masses
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
Write
\[
P_j=\sum_{i=1}^j p_i,
\qquad
P_0=0,
\]
and let \(\sigma\) be the standard deviation of \(X\).

Define the optimal quantile loss
\[
D_\tau(X)
=
\min_{z\in\mathbb R}
\left\{
\tau\,\mathbb E(X-z)_+
+(1-\tau)\,\mathbb E(z-X)_+
\right\}.
\]
The minimizers are precisely the \(\tau\)-quantiles.

For each cut \(1\le j<m\), put
\[
a_j
=
\min\left\{(1-\tau)P_j,\,\tau(1-P_j)\right\}
\]
and
\[
L_\tau(\mathbf p)
=
\min_{1\le j<m}
\frac{a_j}{\sqrt{P_j(1-P_j)}}.
\tag{1}
\]

To state the upper endpoint, partition \([0,1]\) into the probability cells
\[
I_i=[P_{i-1},P_i]
\]
and define the quantile score
\[
\psi_\tau(u)
=
\tau-\mathbf 1_{\{u\le\tau\}}.
\]
Let
\[
s_i
=
\frac1{p_i}\int_{I_i}\psi_\tau(u)\,du
\]
and let \(S=s_i\) with probability \(p_i\). Put
\[
C_\tau(\mathbf p)
=
\sqrt{\operatorname{Var}(S)}.
\tag{2}
\]
This constant has the explicit form
\[
C_\tau(\mathbf p)^2
=
\tau(1-\tau)-\Delta_\tau(\mathbf p),
\tag{3}
\]
where \(\Delta_\tau(\mathbf p)=0\) when \(\tau=P_j\) for some \(j\), and otherwise, for the unique index \(k\) satisfying
\[
P_{k-1}<\tau<P_k,
\]
\[
\Delta_\tau(\mathbf p)
=
\frac{(\tau-P_{k-1})(P_k-\tau)}{p_k}.
\tag{4}
\]

The complete attainable set of \(D_\tau(X)/\sigma\) is as follows.

For \(m=2\),
\[
\boxed{
\frac{D_\tau(X)}{\sigma}
=
L_\tau(\mathbf p)
=
C_\tau(\mathbf p)
}
\]
for every strictly increasing two-point support.

For \(m\ge3\), the lower endpoint is always a sharp but unattained infimum. The upper endpoint is attained exactly in the single case
\[
m=3,
\qquad
P_1<\tau<P_2.
\]
In that case
\[
\boxed{
\frac{D_\tau(X)}{\sigma}
\in
\left(L_\tau(\mathbf p),C_\tau(\mathbf p)\right],
}
\tag{5}
\]
and the maximizing support is unique up to positive affine transformation:
\[
x_i=A+B s_i,
\qquad B>0.
\tag{6}
\]

In every other case with \(m\ge3\),
\[
\boxed{
\frac{D_\tau(X)}{\sigma}
\in
\left(L_\tau(\mathbf p),C_\tau(\mathbf p)\right).
}
\tag{7}
\]

The lower endpoint is approached by collapsing all score gaps except one across any cut minimizing (1). The upper endpoint is approached by making the support affine to the cell-average score vector \((s_i)\), with arbitrarily small perturbations when that vector contains ties.

Every interior value is attained.

A concrete median corollary follows by taking \(\tau=1/2\). Since
\[
2D_{1/2}(X)
=
\min_z\mathbb E|X-z|,
\]
for equal masses \(p_i=1/m\) the ratio of minimum mean absolute deviation from a median to standard deviation has lower infimum
\[
\frac1{\sqrt{m-1}}.
\]
Its upper endpoint is
\[
1
\]
when \(m\) is even, and
\[
\sqrt{\frac{m-1}{m}}
\]
when \(m\) is odd. The upper endpoint is attained only for \(m=2\) or \(m=3\); for \(m=3\) the exact interval is
\[
\left(
\frac1{\sqrt2},
\sqrt{\frac23}
\right].
\]

## Assumptions and scope

The probability profile and category order are fixed. Only the distinct numerical support locations vary.

The loss is the ordinary pinball, check, or asymmetric absolute loss whose population minimizers are \(\tau\)-quantiles. The result concerns the minimized population loss, normalized by the parent standard deviation.

The theorem does not address excess risk of an estimated conditional quantile, learning rates, or sampling variation of an empirical quantile estimator.

The support is finite and all atom masses are strictly positive.

## Proof

Let the adjacent support gaps be
\[
d_j=x_{j+1}-x_j>0.
\]
A direct quantile-loss calculation gives
\[
D_\tau(X)
=
\sum_{j=1}^{m-1}a_jd_j,
\tag{8}
\]
with \(a_j\) as in (1). Indeed, if \(P_j<\tau\), the whole gap after \(x_j\) lies below every minimizing quantile location and contributes
\[
(1-\tau)P_jd_j;
\]
if \(P_j>\tau\), it contributes
\[
\tau(1-P_j)d_j.
\]
When \(P_j=\tau\), both expressions agree.

For each cut define the centered upper-block indicator
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
\tag{9}
\]
and
\[
\|H_j\|_2
=
\sqrt{P_j(1-P_j)}.
\tag{10}
\]
By definition of \(L_\tau\),
\[
a_j\ge L_\tau\|H_j\|_2.
\]
Therefore (8), followed by the triangle inequality in \(L^2\), gives
\[
D_\tau(X)
\ge
L_\tau\sum_jd_j\|H_j\|_2
\ge
L_\tau
\left\|\sum_jd_jH_j\right\|_2
=
L_\tau\sigma.
\tag{11}
\]
For \(m\ge3\), at least two positive coefficients occur in (9), and distinct centered cut indicators are not positive scalar multiples. Hence the triangle inequality is strict and
\[
D_\tau(X)>L_\tau\sigma.
\]
If all gaps except a minimizing \(d_{j_*}\) tend to zero through positive values, the centered support converges to a multiple of \(H_{j_*}\). Thus the lower constant is sharp.

For the upper endpoint, let \(S=s_i\) on atom \(x_i\), with \(s_i\) from (2). Since \(S\) is the probability-cell average of the mean-zero score \(\psi_\tau\),
\[
\mathbb ES=0.
\]
For every cut,
\[
\operatorname{Cov}(H_j,S)
=
\int_{P_j}^1\psi_\tau(u)\,du
=
a_j.
\tag{12}
\]
Equations (8), (9), and (12) imply the exact covariance representation
\[
D_\tau(X)
=
\operatorname{Cov}(X,S).
\tag{13}
\]
Cauchy--Schwarz now gives
\[
D_\tau(X)
\le
\sigma\sqrt{\operatorname{Var}(S)}
=
C_\tau(\mathbf p)\sigma.
\tag{14}
\]

The full score \(\psi_\tau\) has variance
\[
\tau(1-\tau).
\]
All probability cells except possibly the unique cell containing \(\tau\) see a constant score. If \(P_{k-1}<\tau<P_k\), the conditional variance inside that cell, multiplied by its mass, equals
\[
\frac{(\tau-P_{k-1})(P_k-\tau)}{p_k}.
\]
The conditional-variance decomposition therefore proves (3)--(4).

Cauchy--Schwarz is an equality exactly when the centered support vector is proportional to \((s_i)\). The sequence \((s_i)\) is nondecreasing and has at most three distinct levels: one below \(\tau\), at most one intermediate value from the straddling cell, and one above \(\tau\). Hence it is strictly increasing for every two-point profile, and for \(m\ge3\) it is strictly increasing exactly when
\[
m=3,
\qquad
P_1<\tau<P_2.
\]
This proves the upper-endpoint attainment classification. In all other cases, a strictly increasing perturbation of \((s_i)\) shows that \(C_\tau\) remains a sharp supremum.

Finally, the cone of positive gap vectors
\[
(d_1,\ldots,d_{m-1})\in(0,\infty)^{m-1}
\]
is connected, and the normalized loss is continuous there. Its image is therefore an interval, which completes (5)--(7).

## Verification

The accompanying exact-rational checker generates rational probability profiles, rational quantile levels, and strictly increasing rational supports.

It verifies the direct minimization formula (8), the covariance representation (13), the lower and upper inequalities by exact arithmetic, the closed form (3)--(4), exact equality for two-point laws, the three-category upper equality case, and the stated endpoint-approach constructions.

Finite experiments do not establish the universal theorem. They replay the algebra used in the proof and stress-test the endpoint and equality cases.

## Relationship to prior work

Gilat and Hill define the same asymmetric absolute functional
\[
U_\tau(z)
=
\tau\,\mathbb E(X-z)_+
+(1-\tau)\,\mathbb E(z-X)_+
\]
and prove that it is minimized exactly at \(\tau\)-quantiles. Their main sharp theorem bounds the distance between the mean and a quantile in terms of the central absolute first moment. It does not optimize the minimized quantile loss relative to standard deviation over support geometry with a prescribed atom profile.

Xue and Titterington develop the folded-CDF interpretation of mean absolute deviation and its weighted \(p\)-quantile generalization. Their weighted quantity is a constant multiple of the minimized check loss used here, and their paper treats both theoretical and empirical distributional representations. It does not give a fixed-probability support range after normalization by standard deviation, nor the cell-projection upper constant or cut-ray lower constant.

Steinwart and Christmann study pinball-loss calibration and variance bounds for nonparametric conditional-quantile learning. Their variance bounds concern empirical-risk analysis and excess losses rather than the parent standard deviation in the denominator of the present theorem.

Targeted searches using quantile loss, check loss, pinball loss, asymmetric absolute deviation, fixed atom probabilities, and standard deviation did not locate the two-sided fixed-profile attainable interval.

## Limitations

The probability masses are fixed. Allowing arbitrarily fine atomizations changes both endpoints and can recover the unrestricted score variance in the upper bound.

The upper equality classification depends on strict support ordering; if ties are allowed, the cell-average score vector itself attains the upper bound in every profile.

The result concerns a one-dimensional unconditional law. Conditional quantile regression introduces covariates and a different optimization problem.

The originality search was targeted. Older convex-loss or isotonic-cone literature may contain an equivalent fixed-partition projection result under different terminology.

## References

1. D. Gilat and T. P. Hill, “Quantile-locating functions and the distance between the mean and quantiles,” *Statistica Neerlandica* 47(4) (1993), 279–283, DOI 10.1111/j.1467-9574.1993.tb01424.x.
2. J.-H. Xue and D. M. Titterington, “The \(p\)-folded cumulative distribution function and the mean absolute deviation from the \(p\)-quantile,” *Statistics & Probability Letters* 81(8) (2011), 1179–1182, DOI 10.1016/j.spl.2011.03.014.
3. I. Steinwart and A. Christmann, “Estimating conditional quantiles with the help of the pinball loss,” *Bernoulli* 17(1) (2011), 211–225, DOI 10.3150/10-BEJ267.
