# Sharp first-step safety frontier for source-form AdaBound
## Finding

AdaBound clips Adam's coordinatewise learning rate between dynamic lower and upper bounds. On the source algorithm, the upper bound itself has an exact curvature-sensitive safety requirement.

Consider
\[
f(x)=\frac h2x^2,
\qquad
h>0,
\]
with source-form AdaBound parameters
\[
\alpha_0>0,
\qquad
0\le\beta_1,\beta_2<1,
\]
and first clipping interval
\[
0\le\ell_1\le u_1<\infty.
\]

The first source update is
\[
g_1=h x_1,
\qquad
m_1=(1-\beta_1)g_1,
\qquad
v_1=(1-\beta_2)g_1^2,
\]
with raw rate
\[
r_1
=
\frac{\alpha_0}
{\sqrt{1-\beta_2}\,h|x_1|}
\]
and clipped rate
\[
\widehat\eta_1
=
\operatorname{Clip}(r_1,\ell_1,u_1).
\]
Therefore
\[
x_2
=
x_1
\left[
1-(1-\beta_1)h\widehat\eta_1
\right],
\]
and
\[
\frac{f(x_2)}{f(x_1)}
=
\left[
1-(1-\beta_1)h\widehat\eta_1
\right]^2.
\]

As the nonzero initialization varies, \(r_1\) ranges over all positive values, so the clipped rate ranges over the entire interval
\[
[\ell_1,u_1].
\]
Thus
\[
f(x_2)\le f(x_1)
\]
for every nonzero initialization if and only if
\[
(1-\beta_1)h u_1\le2.
\]

If
\[
(1-\beta_1)h u_1>2,
\]
then every
\[
0<|x_1|
\le
\frac{\alpha_0}
{\sqrt{1-\beta_2}\,h u_1}
\]
is clipped exactly to \(u_1\), and every point in that neighborhood has the same amplification
\[
\frac{f(x_2)}{f(x_1)}
=
\left[
1-(1-\beta_1)h u_1
\right]^2
>
1.
\]

For the bound schedule recommended in the defining paper,
\[
\eta_u(t)
=
\alpha^\star
\left(
1+\frac{1}{(1-\beta_2)t}
\right),
\]
the first upper bound is
\[
u_1
=
\alpha^\star
\frac{2-\beta_2}{1-\beta_2}.
\]
Hence the exact universal first-step safety condition is
\[
h
\le
\frac{
2(1-\beta_2)
}{
(1-\beta_1)\alpha^\star(2-\beta_2)
}.
\]

At fixed
\[
\beta_1,\alpha^\star,h,
\]
the upper bound satisfies
\[
u_1
\sim
\frac{\alpha^\star}{1-\beta_2}
\]
as \(\beta_2\uparrow1\), and the upper-clipped objective amplification therefore grows quadratically like
\[
\left[
\frac{
(1-\beta_1)h\alpha^\star
}{
1-\beta_2
}
\right]^2.
\]

Using the default values stated in the paper,
\[
\beta_1=0.9,
\qquad
\beta_2=0.999,
\qquad
\alpha^\star=0.1,
\]
gives
\[
u_1=100.1.
\]
Universal first-step safety then requires
\[
h\le0.1998001998.
\]
At
\[
h=1,
\]
the upper-clipped multiplier is
\[
-9.01,
\]
so the objective amplification is
\[
81.1801.
\]

With the paper's initial Adam step
\[
\alpha_0=10^{-3},
\]
the upper-clipped neighborhood at \(h=1\) is
\[
0<|x_1|
\le
3.1591185\times10^{-4}.
\]

Dynamic clipping therefore guarantees a finite rate, but finiteness is not the same as curvature-compatible stability.

## Assumptions and scope

The theorem analyzes Algorithm 2 as written in the defining AdaBound paper. That theoretical source recurrence omits Adam bias correction and denominator epsilon for simplicity.

The objective is deterministic, scalar, unconstrained, and quadratic, so the projection is the identity.

The result concerns first-step objective monotonicity. It does not claim nonconvergence of the full AdaBound trajectory.

Practical implementations that add bias correction, denominator epsilon, or rescale the final learning rate have different quantitative first-step thresholds.

## Proof

The gradient and source moment states are
\[
g_1=h x_1,
\]
\[
m_1=(1-\beta_1)h x_1,
\]
and
\[
v_1=(1-\beta_2)h^2x_1^2.
\]
Thus
\[
\sqrt{v_1}
=
\sqrt{1-\beta_2}\,h|x_1|.
\]

At \(t=1\), the source factor \(1/\sqrt t\) equals one. Therefore
\[
x_2
=
x_1
-
\widehat\eta_1m_1
=
x_1
\left[
1-(1-\beta_1)h\widehat\eta_1
\right].
\]
This proves the exact objective ratio.

The raw rate
\[
\frac{\alpha_0}
{\sqrt{1-\beta_2}\,h|x_1|}
\]
varies continuously from zero to infinity as \(|x_1|\) varies from infinity to zero. After clipping, every value in
\[
[\ell_1,u_1]
\]
is therefore attainable.

For a nonnegative scalar \(z\),
\[
|1-z|\le1
\]
if and only if
\[
0\le z\le2.
\]
Taking
\[
z=(1-\beta_1)h\widehat\eta_1
\]
shows that every first step is objective-nonincreasing exactly when the largest attainable value satisfies
\[
(1-\beta_1)h u_1\le2.
\]

When that inequality fails, all states with raw rate at least \(u_1\) use the upper clip. Solving
\[
\frac{\alpha_0}
{\sqrt{1-\beta_2}\,h|x_1|}
\ge u_1
\]
gives the stated neighborhood, and substitution yields its constant amplification factor.

For the recommended schedule,
\[
u_1
=
\alpha^\star
\left(
1+\frac1{1-\beta_2}
\right)
=
\alpha^\star
\frac{2-\beta_2}{1-\beta_2}.
\]
Substitution proves the curvature frontier. The high-\(\beta_2\) asymptotic follows directly.

## Verification

The accompanying `verify.py` reconstructs the source first update, compares it with the closed-form ratio, verifies both sides of the exact universal safety frontier over randomized parameters, checks the upper-clipping plateau, and reproduces the paper-default numerical values.

The finite calculations are transcription guards. The all-initialization theorem is proved analytically above.

## Relationship to prior work

Luo, Xiong, Liu, and Sun introduced AdaBound to suppress extreme adaptive learning rates by clipping them between dynamic bounds that converge to a common SGD rate. Their defining paper provides the source recurrence used here, recommends the displayed bound schedule, and uses
\[
\beta_1=0.9,
\qquad
\beta_2=0.999
\]
as default AdaBound parameters.

Savarese later showed that the original AdaBound regret proof is incorrect and constructed problems on which convergence can be arbitrarily slow. That work studies global regret and the time variation of the clipping bounds, not first-step curvature safety.

Later task-dependent-bound work has criticized AdaBound's hand-designed task-independent bounds. That qualitative concern is compatible with the present theorem but does not imply its exact necessary-and-sufficient scalar condition or the upper-clipping amplification plateau.

The present result is therefore narrower than global convergence theory but sharper on a distinct question: whether the upper clipping bound is itself dynamically safe at the instant it is applied.

## Limitations

The result is specific to the source theoretical recurrence.

It is a first-step theorem and does not classify later adaptive dynamics.

The scalar quadratic isolates curvature; multidimensional problems add coupling and history effects.

The small-initialization example is used to prove a sharp universal statement and is not asserted to be typical of neural-network training.

## References

1. Liangchen Luo, Yuanhao Xiong, Yan Liu, and Xu Sun, “Adaptive Gradient Methods with Dynamic Bound of Learning Rate,” arXiv:1902.09843v1, 2019.
2. Pedro Savarese, “On the Convergence of AdaBound and its Connection to SGD,” arXiv:1908.04457v2, 2019.
3. “AdaCB: An Adaptive Gradient Method with Convergence Range Bound of Learning Rate,” Applied Sciences 12(18):9389, 2022.
