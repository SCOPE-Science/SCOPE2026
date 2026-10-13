# Exact DZL tail-sums correct its moments and show a light tail
## Finding
Let \(Y\) have the discrete ZLindley (DZL) distribution defined by
\[
\Pr(Y=y)
=
\Lambda_\mu(y)-\Lambda_\mu(y+1),
\qquad
y=0,1,2,\ldots,
\]
where
\[
\Lambda_\mu(k)
=
\left(
1+\frac{\mu k}{2(1+\mu)}
\right)e^{-\mu k},
\qquad
\mu>0.
\]
Telescoping gives the exact lattice survival
\[
\boxed{
\Pr(Y\ge k)=\Lambda_\mu(k),
\qquad k\ge1.
}
\]

Hence every positive integer raw moment has the tail-sum form
\[
\boxed{
\mathbb E[Y^r]
=
\sum_{k=1}^{\infty}
\left\{
k^r-(k-1)^r
\right\}
\Lambda_\mu(k).
}
\]
Writing
\[
\phi=e^{-\mu},
\qquad
a=\frac{\mu}{2(1+\mu)},
\]
the first two raw moments are
\[
\boxed{
\mathbb E[Y]
=
\frac{\phi}{1-\phi}
+
\frac{a\phi}{(1-\phi)^2}
}
\]
and
\[
\boxed{
\mathbb E[Y^2]
=
\frac{\phi(1+\phi)}{(1-\phi)^2}
+
\frac{a\phi(1+3\phi)}{(1-\phi)^3}.
}
\]
Therefore
\[
\boxed{
\operatorname{Var}(Y)
=
\mathbb E[Y^2]-\mathbb E[Y]^2.
}
\]

These formulas do not equal Eqs. (18), (21), and (22) printed in the 2026 source. For example, at
\[
\mu=1,
\]
the exact values are
\[
\mathbb E[Y]
=
0.8121451054212745\ldots
\]
and
\[
\operatorname{Var}(Y)
=
1.3657697942970708\ldots.
\]
The paper's Eq. (18) instead gives
\[
0.4904943422160591\ldots.
\]
The paper's Table 1 reports
\[
0.8121
\quad\text{and}\quad
1.3658
\]
for the mean and variance at \(\mu=1\), so the table is consistent with the corrected formulas, not with the displayed moment formulas.

The same survival representation also fixes the tail classification. The probability generating function is
\[
\boxed{
P(s)
=
1+(s-1)
\left[
\frac{\phi}{1-\phi s}
+
\frac{a\phi}{(1-\phi s)^2}
\right].
}
\]
Its exact radius of convergence is
\[
\boxed{e^\mu.}
\]
Consequently,
\[
\boxed{
\mathbb E[e^{tY}]<\infty
\quad\Longleftrightarrow\quad
t<\mu.
}
\]
Indeed,
\[
\Pr(Y=y)
\sim
a(1-\phi)y\phi^y.
\]
Thus the DZL distribution is exponentially light-tailed for every \(\mu>0\) under the standard moment-generating-function definition of heavy tails.

The paper's description of the DZL as exhibiting “heavy-tailed behavior” is therefore not an asymptotic tail property. High skewness or kurtosis at some parameter values does not change the existence of positive exponential moments.

## Assumptions and scope
The parameter domain is exactly
\[
\mu>0,
\]
and the support is
\[
\{0,1,2,\ldots\}.
\]

The correction concerns the moment formulas and asymptotic tail classification. It does not challenge the normalization of the PMF, the CDF, or the likelihood formula.

The phrase “heavy-tailed” is used in the standard probabilistic sense: a nonnegative law is heavy-tailed if its moment generating function is infinite for every positive argument. Since the DZL MGF is finite on the nonempty interval
\[
0<t<\mu,
\]
the model is light-tailed in that sense.

No claim is made that all numerical values in the source were computed from the wrong displayed formulas. In fact, several Table 1 entries agree with the corrected moments.

## Proof
From
\[
p_y=\Lambda_\mu(y)-\Lambda_\mu(y+1),
\]
one gets, for \(k\ge1\),
\[
\Pr(Y\ge k)
=
\sum_{y=k}^{\infty}p_y
=
\Lambda_\mu(k).
\]

For every positive integer \(r\),
\[
Y^r
=
\sum_{k=1}^{Y}
\left\{
k^r-(k-1)^r
\right\}.
\]
All terms are nonnegative, so Tonelli's theorem yields
\[
\mathbb E[Y^r]
=
\sum_{k=1}^{\infty}
\left\{
k^r-(k-1)^r
\right\}
\Pr(Y\ge k),
\]
giving the stated moment identity.

For \(r=1\),
\[
\mathbb E[Y]
=
\sum_{k\ge1}(1+ak)\phi^k.
\]
Using
\[
\sum_{k\ge1}\phi^k
=
\frac{\phi}{1-\phi}
\]
and
\[
\sum_{k\ge1}k\phi^k
=
\frac{\phi}{(1-\phi)^2},
\]
one obtains the mean formula.

For \(r=2\),
\[
\mathbb E[Y^2]
=
\sum_{k\ge1}(2k-1)(1+ak)\phi^k.
\]
Using
\[
\sum_{k\ge1}k^2\phi^k
=
\frac{\phi(1+\phi)}{(1-\phi)^3},
\]
straight simplification gives the displayed second moment.

For the PGF, the discrete tail identity gives
\[
P(s)
=
1+(s-1)
\sum_{k\ge1}\Pr(Y\ge k)s^{k-1}.
\]
Since
\[
\sum_{k\ge1}(1+ak)\phi^k s^{k-1}
=
\frac{\phi}{1-\phi s}
+
\frac{a\phi}{(1-\phi s)^2},
\]
the rational PGF follows.

Finally,
\[
p_y
=
\phi^y
\left[
1+ay-\phi\{1+a(y+1)\}
\right],
\]
so
\[
p_y
\sim
a(1-\phi)y\phi^y.
\]
Therefore
\[
e^{ty}p_y
\sim
a(1-\phi)y e^{-(\mu-t)y}.
\]
The MGF converges for \(t<\mu\), diverges at \(t=\mu\), and its terms do not tend to zero for \(t>\mu\).

## Verification
The included checker independently evaluates the PMF, direct raw-moment sums, the corrected closed forms, the paper's displayed Eqs. (18), (21), and (22), and the MGF boundary.

For
\[
\mu=1,
\]
the direct PMF sum and corrected closed form agree to high precision:
\[
\mathbb E[Y]
=
0.8121451054212745\ldots,
\]
while Eq. (18) gives
\[
0.4904943422160591\ldots.
\]

The checker also reproduces the corrected Table 1 mean and variance values for
\[
\mu=0.5,\ 0.8,\ 1,\ 1.5,\ 2.5.
\]

For the tail, it verifies
\[
\frac{p_y}{a(1-\phi)y\phi^y}\to1
\]
and checks numerical convergence below \(t=\mu\) and divergence at the boundary.

These computations are consistency checks. The formulas and convergence domain are proved analytically above.

## Relationship to prior work
Alotaibi and Elshahhat define the DZL law by survival discretization and give the correct PMF
\[
p_y=\Lambda_\mu(y)-\Lambda_\mu(y+1).
\]
However, the source's moment section shifts the survival argument and changes its linear coefficient. Its Eq. (18) therefore does not equal the mean of the stated PMF. Its Eq. (21), described as the second non-central moment, already subtracts the square of the displayed mean; Eq. (22) then subtracts that square again to define the variance.

The numerical Table 1 is internally more consistent than those equations: for several printed parameter values it matches direct PMF summation and the corrected formulas.

The source also advertises “heavy-tailed behavior” and interprets increasing kurtosis as heavier tails. Yet its own survival function is a linear polynomial times \(e^{-\mu k}\), which gives a nonzero exponential-moment interval. Under the standard probabilistic definition, that is a light tail.

Focused searches using the exact DOI, DZL name, moment equations, mean/variance correction language, and heavy-tail aliases did not locate a published corrigendum or another source already identifying this combined correction.

## Limitations
The finding does not reconstruct every entry of Table 1 or every higher standardized moment.

It does not reassess the likelihood-based or Bayesian parameter estimates, except insofar as interpretations relying on the displayed moment formulas or a heavy-tail label should use the corrected properties.

The order-statistic formulas in the source are not assessed here.

## References
1. R. Alotaibi and A. Elshahhat, “A New Discrete Model of Lindley Families: Theory, Inference, and Real-World Reliability Analysis,” Mathematics 14 (2026), 397. DOI: 10.3390/math14030397.
2. B. Merz, et al., “Understanding Heavy Tails of Flood Peak Distributions,” Water Resources Research 58 (2022). DOI: 10.1029/2021WR030506.
