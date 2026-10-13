# The WRLE interior mode exists only above an exact Lambert-W threshold
## Finding
Consider the wrapped Lindley–exponential density
\[
g(\theta;\alpha,\beta)
=
C_{\alpha,\beta}
e^{-\alpha\beta\theta}
\left[
1+\beta\theta+
\frac{2\pi\beta e^{-2\pi\alpha\beta}}
{1-e^{-2\pi\alpha\beta}}
\right],
\qquad
0\le\theta<2\pi,
\]
where
\[
\alpha>0,\qquad \beta>0,
\]
and \(C_{\alpha,\beta}>0\) is the normalizing constant.

The source differentiates this density and obtains the stationary point
\[
\theta_0
=
\frac{1-\alpha}{\alpha\beta}
-
\frac{2\pi e^{-2\pi\alpha\beta}}
{1-e^{-2\pi\alpha\beta}},
\]
then states that this value is the mode for arbitrary positive \(\alpha\) and \(\beta\).

The stationary point is not always in the support.

If
\[
\alpha\ge1,
\]
then
\[
\boxed{\theta_0<0}
\]
and
\[
\boxed{
g'(\theta)<0
\quad\text{for every }0\le\theta<2\pi.
}
\]
Thus the density is strictly decreasing on the chosen circular cut and its mode is
\[
\boxed{\theta_{\mathrm{mode}}=0.}
\]

For
\[
0<\alpha<1,
\]
define
\[
x_\alpha
=
-W_{-1}\!\left(
-(1-\alpha)e^{-(1-\alpha)}
\right)
-(1-\alpha),
\]
where \(W_{-1}\) is the lower real branch of the Lambert \(W\) function, and put
\[
\boxed{
\beta_c(\alpha)
=
\frac{x_\alpha}{2\pi\alpha}.
}
\]

Then the exact modality classification is
\[
\boxed{
0<\beta\le\beta_c(\alpha)
\Longrightarrow
\theta_{\mathrm{mode}}=0,
}
\]
with the density strictly decreasing for
\[
0<\beta<\beta_c(\alpha),
\]
and decreasing for every
\[
\theta>0
\]
at equality.

By contrast,
\[
\boxed{
\beta>\beta_c(\alpha)
\Longrightarrow
0<\theta_0<2\pi,
}
\]
and the density is strictly increasing on
\[
[0,\theta_0)
\]
and strictly decreasing on
\[
(\theta_0,2\pi).
\]
Hence \(\theta_0\) is the unique interior mode exactly in this regime.

For example,
\[
\beta_c(1/2)
=
0.3999344750155586\ldots.
\]
At
\[
(\alpha,\beta)=(1/2,1/5),
\]
the source formula gives
\[
\theta_0
=
-2.18524966134038\ldots,
\]
so the density is strictly decreasing and its mode is \(0\).

At
\[
(\alpha,\beta)=(1/2,1/2),
\]
one obtains
\[
\theta_0
=
0.351076603008782\ldots,
\]
which is a genuine interior mode.

The source itself displays curves with
\[
(\alpha,\beta)=(2,1).
\]
For this pair,
\[
\boxed{
\theta_0
=
-0.500021911694667\ldots,
}
\]
so Eq. (3.3) is outside the support even for a parameter choice explicitly plotted in the article.

The family remains unimodal in all regimes; the correction is that its mode undergoes an exact boundary-to-interior phase transition rather than always occurring at the stationary point printed in Eq. (3.3).

## Assumptions and scope
The support is represented by the standard cut
\[
0\le\theta<2\pi.
\]
Because the model is circular, the point \(0\) is the seam of this representation. Calling \(0\) a boundary mode refers to this chosen cut; geometrically it is the circular direction \(0\).

The classification uses the exact WRLE density and derivative printed in the source. It does not alter the model's normalization, characteristic function, trigonometric moments, or estimation method.

The Lambert \(W\) threshold is needed only when
\[
0<\alpha<1.
\]
For
\[
\alpha\ge1,
\]
the density is always strictly decreasing on the cut, independently of \(\beta\).

## Proof
Write
\[
x=2\pi\alpha\beta
\]
and
\[
K=
\frac{2\pi\beta e^{-x}}{1-e^{-x}}.
\]
The source's derivative has a positive prefactor times
\[
B(\theta)
=
1-\alpha(1+\beta\theta+K).
\]
Therefore
\[
B'(\theta)
=
-\alpha\beta<0.
\]
Thus the derivative of \(g\) can change sign at most once.

The unique zero of \(B\) is exactly
\[
\theta_0
=
\frac{1-\alpha}{\alpha\beta}
-
\frac{2\pi}{e^x-1}.
\]

If
\[
\alpha\ge1,
\]
the first term is nonpositive and the second is strictly negative, so
\[
\theta_0<0.
\]
Since \(B\) is strictly decreasing and its zero lies to the left of the support,
\[
B(\theta)<0
\]
throughout the support. Hence \(g\) is strictly decreasing.

Now suppose
\[
0<\alpha<1.
\]
The condition
\[
\theta_0>0
\]
is equivalent to
\[
1-\alpha
>
\frac{x}{e^x-1},
\]
or
\[
q_\alpha(x)
:=
(1-\alpha)(e^x-1)-x
>
0.
\]

The function satisfies
\[
q_\alpha(0)=0,
\qquad
q_\alpha'(0)=-\alpha<0,
\]
and
\[
q_\alpha''(x)
=
(1-\alpha)e^x>0.
\]
Hence \(q_\alpha'\) is strictly increasing. The function first decreases below zero, has a unique minimum, and then increases to \(+\infty\). It therefore has exactly one positive zero \(x_\alpha\).

Solving
\[
(1-\alpha)(e^x-1)=x
\]
by setting
\[
c=1-\alpha,
\qquad
z=x+c,
\]
gives
\[
-z e^{-z}
=
-c e^{-c}.
\]
The principal branch \(W_0\) produces the trivial zero \(x=0\). The unique positive zero is obtained from the lower branch:
\[
x_\alpha
=
-W_{-1}(-c e^{-c})-c.
\]

Because
\[
x=2\pi\alpha\beta,
\]
one has
\[
\theta_0>0
\quad\Longleftrightarrow\quad
\beta>\frac{x_\alpha}{2\pi\alpha}.
\]

It remains to check that a positive stationary point cannot lie beyond \(2\pi\). If \(\theta_0>0\), then \(0<\alpha<1\). Moreover,
\[
\frac{x}{1-e^{-x}}>1>1-\alpha,
\]
which is equivalent to
\[
1-\alpha
<
x+\frac{x}{e^x-1}.
\]
After dividing by \(\alpha\beta\), this is exactly
\[
\theta_0<2\pi.
\]

Thus any positive stationary point lies inside the circular cut. Since \(B\) is strictly decreasing, the derivative is positive before that point and negative after it. If the stationary point is nonpositive, the density decreases from the seam. This completes the classification.

## Verification
The accompanying checker implements the published density, derivative-sign factor, stationary point, and the Lambert-\(W\) threshold.

It verifies the normalization numerically for representative parameter pairs and checks that the analytic derivative agrees with numerical differentiation.

For
\[
\alpha=1/2,
\]
it reproduces
\[
\beta_c
=
0.3999344750155586\ldots.
\]
It checks a subcritical pair
\[
\beta=1/5,
\]
for which the derivative is negative across a dense grid of the support, and a supercritical pair
\[
\beta=1/2,
\]
for which the derivative changes sign once at the published \(\theta_0\).

It also verifies the source-displayed pair
\[
(\alpha,\beta)=(2,1),
\]
where \(\theta_0<0\) and the derivative is negative throughout the support.

The grid evaluations are reproducibility checks. The global classification is proved analytically by the strict monotonicity of \(B(\theta)\) and the convexity of \(q_\alpha(x)\).

## Relationship to prior work
Al-Mofleh derives the WRLE density and its first derivative correctly. In the modality section, the article solves \(g'(\theta)=0\) and states that the resulting \(\theta_0\) is the mode for arbitrary positive parameter values. The missing step is support admissibility: the stationary point can be negative.

The source's own plotted parameter sets already include values with \(\alpha>1\), including
\[
(\alpha,\beta)=(2,1).
\]
For all such values the density is strictly decreasing on the chosen cut, so the circular mode is at direction \(0\).

Joshi and Jose study the earlier wrapped Lindley distribution, a different one-parameter circular model. Gemeay and Abd El-Bar study a wrapped new-XLindley model, again with a different density. Neither inspected source provides the WRLE threshold above.

A March 2026 preprint by Ferreira, van Wyk-de Ridder, and van Niekerk characterizes interior and boundary modes for a different wrapped three-parameter Lindley construction. That manuscript was subsequently withdrawn over an identifiability issue. Its mode analysis does not contain the WRLE density or the \((\alpha,\beta)\) threshold derived here.

Focused searches using the exact WRLE DOI, full model name, stationary-point formula, modality aliases, boundary-mode terminology, and Lambert-\(W\) threshold language did not locate a published correction or an equivalent WRLE-specific classification.

## Limitations
The result classifies the location of the density mode. It does not re-estimate the empirical model fits or change the article's trigonometric-moment formulas.

At the threshold
\[
\beta=\beta_c(\alpha),
\]
the derivative is zero at the seam and strictly negative immediately afterward; there is no interior stationary point.

A very recent unindexed correction could exist outside the sources examined.

## References
1. H. Al-Mofleh, “The wrapped Lindley-exponential distribution: properties and application in circular data appearing in geological context,” AIMS Mathematics 11 (2026), 1287–1310. DOI: 10.3934/math.2026055.
2. S. Joshi and K. K. Jose, “Wrapped Lindley distribution,” Communications in Statistics - Theory and Methods 47 (2018), 1013–1021. DOI: 10.1080/03610926.2017.1280168.
3. A. M. Gemeay and A. M. T. Abd El-Bar, “On wrapping a new version of Lindley distribution for circular data analysis,” Environmental and Ecological Statistics 33 (2026), 577–624. DOI: 10.1007/s10651-025-00702-5.
4. J. Ferreira, D. van Wyk-de Ridder, and J. van Niekerk, “A flexible wrapped Lindley-type distribution for angular data modelling,” arXiv:2603.16344 (2026), withdrawn.
