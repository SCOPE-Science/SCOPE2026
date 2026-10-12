# The UTLD Type-II observed information hardcodes three failures and misses a scale factor
## Finding
Consider the unit Topp–Leone distribution under Type-II censoring. Let
\[
1\le r\le n
\]
be the number of observed failures, and let
\[
x_r\in(0,1)
\]
be the largest observed failure time. Write
\[
z=x_r(2-x_r)\in(0,1),
\qquad
q=z^\alpha,
\qquad
L=\log z<0,
\]
with
\[
0<\alpha<1.
\]

The source's own log-likelihood, after collecting all terms that are linear in \(\alpha\), has the form
\[
\ell(\alpha)
=
r\log\alpha
+
(n-r)\log(1-z^\alpha)
+
\alpha C
+
C_0,
\]
where \(C\) and \(C_0\) do not affect the second derivative.

Differentiating gives
\[
\ell'(\alpha)
=
\frac{r}{\alpha}
-
(n-r)\frac{z^\alpha L}{1-z^\alpha}
+
C,
\]
and therefore
\[
\boxed{
\ell''(\alpha)
=
-\frac{r}{\alpha^2}
-
(n-r)
\frac{z^\alpha L^2}{(1-z^\alpha)^2}.
}
\]
Hence the observed information is
\[
\boxed{
J(\alpha)
=
-\ell''(\alpha)
=
\frac{r}{\alpha^2}
+
(n-r)
\frac{z^\alpha L^2}{(1-z^\alpha)^2}.
}
\]
It is strictly positive for every admissible Type-II sample.

Putting the correct Hessian over the denominator used in the source gives the equivalent expression
\[
\boxed{
\ell''(\alpha)
=
\frac{
q\{2r-\alpha^2(n-r)L^2\}
-r(q^2+1)
}{
\alpha^2(q-1)^2
}.
}
\]

The source instead prints
\[
H_{\mathrm{pub}}
=
\frac{
q\{6-\alpha^2(n-3)L^2\}
-3(q^2+1)
}{
(q-1)^2
}.
\]
This has two defects at once: it replaces the general censoring count \(r\) by \(3\), and it omits the overall factor \(1/\alpha^2\).

Indeed,
\[
\boxed{
H_{\mathrm{pub}}
=
\alpha^2\ell''(\alpha)
\quad\text{when }r=3.
}
\]
Thus even on the special slice \(r=3\), literal inversion of the displayed observed information yields a variance larger than the correct inverse observed information by
\[
\boxed{\frac1{\alpha^2}.}
\]

For example, with
\[
(n,r,\alpha,x_r)
=
(10,3,1/2,1/2),
\]
one has
\[
z=\frac34.
\]
The correct curvature is
\[
\ell''(\alpha)
=
-39.95177266710635\ldots,
\]
so
\[
\boxed{
J(\alpha)^{-1}
=
0.02503017846873498\ldots .
}
\]
The source formula gives
\[
H_{\mathrm{pub}}
=
-9.987943166776588\ldots,
\]
hence its literal inverse-information value is
\[
\boxed{
(-H_{\mathrm{pub}})^{-1}
=
0.10012071387493991\ldots ,
}
\]
exactly four times the correct value.

The corrected Hessian also establishes a structural fact omitted from the source:
\[
\boxed{
\ell''(\alpha)<0
\quad\text{for every }0<\alpha<1.
}
\]
Therefore the Type-II log-likelihood is strictly concave in the shape parameter. Any interior score root is the unique interior maximum, and the constrained likelihood has at most one maximizer.

## Assumptions and scope
The result concerns the one-parameter unit Topp–Leone model and the Type-II censoring likelihood printed in the source. The support is
\[
0<x<1,
\]
the parameter domain is
\[
0<\alpha<1,
\]
and the censoring design has \(r\) observed failures from \(n\) units.

The correction is to the displayed second derivative and the inverse observed-information calculation built from it. It does not assert that every numerical confidence interval or Bayesian simulation in the paper was necessarily computed from the printed formula.

The strict-concavity conclusion is about \(\ell(\alpha)\) in the original shape parameter. Reparameterizing by a logit preserves the same likelihood but changes the Hessian through the chain rule.

## Proof
From the source's Type-II log-likelihood,
\[
\ell(\alpha)
=
r\log(2\alpha)
+
(n-r)\log\!\left[
1-\{x_r(2-x_r)\}^{\alpha}
\right]
+
(\alpha-1)
\sum_{i=1}^{r}
\log\{x_i(2-x_i)\}
+
C_1.
\]
Set
\[
z=x_r(2-x_r),
\qquad
L=\log z.
\]
All sample-sum terms are affine in \(\alpha\), so their second derivative is zero.

The first derivative is
\[
\ell'(\alpha)
=
\frac{r}{\alpha}
+
\sum_{i=1}^{r}\log\{x_i(2-x_i)\}
-
(n-r)
\frac{z^\alpha L}{1-z^\alpha}.
\]
Since
\[
\frac{d}{d\alpha}
\left(
\frac{z^\alpha}{1-z^\alpha}
\right)
=
\frac{z^\alpha L}{(1-z^\alpha)^2},
\]
a second differentiation yields
\[
\ell''(\alpha)
=
-\frac{r}{\alpha^2}
-
(n-r)\frac{z^\alpha L^2}{(1-z^\alpha)^2}.
\]

Both terms are nonpositive, and the first is strictly negative because \(r\ge1\). Thus
\[
\ell''(\alpha)<0.
\]

To compare directly with the source, put
\[
q=z^\alpha.
\]
Multiplying the correct Hessian by
\[
\alpha^2(q-1)^2
\]
gives
\[
-r(q-1)^2-\alpha^2(n-r)qL^2.
\]
Expanding
\[
-r(q-1)^2
=
q(2r)-r(q^2+1)
\]
gives
\[
\ell''(\alpha)
=
\frac{
q\{2r-\alpha^2(n-r)L^2\}
-r(q^2+1)
}{
\alpha^2(q-1)^2
}.
\]
Setting \(r=3\) in the numerator produces exactly the numerator printed in the paper, but the paper lacks the denominator factor \(\alpha^2\). This proves the stated relationship.

## Verification
The accompanying checker differentiates the actual Type-II log-likelihood numerically and compares the result with the corrected closed form for several admissible samples.

It separately evaluates the expression printed in the source and verifies symbolically through direct algebraic evaluation that, when \(r=3\),
\[
H_{\mathrm{pub}}
=
\alpha^2\ell''(\alpha).
\]

At
\[
(n,r,\alpha,x_r)
=
(10,3,1/2,1/2),
\]
the checker reproduces
\[
J(\alpha)^{-1}
=
0.02503017846873498\ldots
\]
and
\[
(-H_{\mathrm{pub}})^{-1}
=
0.10012071387493991\ldots.
\]

It also changes \(r\) while holding \(n,\alpha,x_r\) fixed: the correct Hessian changes with \(r\), whereas the source expression does not. This is a direct reproducibility check of the hardcoded-three defect.

## Relationship to prior work
Al-Moisheer, Sultan, and Mansour derive the Type-II censored log-likelihood and its score for the unit Topp–Leone model. Their printed score retains the general censoring count \(r\). Immediately afterward, however, the displayed second derivative used for the asymptotic variance contains the constants \(3\) and \(n-3\) instead of \(r\) and \(n-r\), and it omits the factor \(1/\alpha^2\).

The corrected Hessian follows directly from the source's preceding likelihood and score and requires no additional modeling assumption. It also yields strict concavity, which strengthens the inferential analysis by ruling out multiple interior likelihood maxima.

Focused searches using the exact DOI, unit Topp–Leone name, Type-II censoring, observed-information, Fisher-information, Hessian, and asymptotic-variance terminology did not locate a published corrigendum or another source already identifying this formula defect.

## Limitations
The finding corrects the analytic observed-information formula. It does not reconstruct the software used to generate every numerical confidence interval, simulation table, or Bayesian chain in the article.

Expected Fisher information, as distinct from the observed information obtained by differentiating the realized log-likelihood, is not derived here.

The paper also contains entropy formulas and other distributional properties that are outside this accepted claim.

## References
1. A. S. Al-Moisheer, K. S. Sultan, and M. M. M. Mansour, “On Unit J-Shaped Distributions: Properties and Estimation with Applications,” Mathematics 14 (2026), 1021. DOI: 10.3390/math14061021.
