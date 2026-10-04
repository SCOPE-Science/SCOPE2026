# Noise amplification imposes an exact deterministic stability tax in Positive-Negative Momentum
## Finding

Positive-Negative Momentum (PNM) deliberately amplifies stochastic gradient noise while normalizing its learning rate by the same noise-amplitude factor. On deterministic positive-definite quadratics, that normalization does not preserve the full gradient-descent stability margin.

The source PNM recurrence is
\[
m_t
=
\beta_1^2m_{t-2}
+
(1-\beta_1^2)g_t
\]
and
\[
\theta_{t+1}
=
\theta_t
-
\eta_0
\left[
(1+\beta_0)m_t-\beta_0m_{t-1}
\right],
\]
where
\[
\eta_0
=
\frac{\eta}
{\sqrt{(1+\beta_0)^2+\beta_0^2}},
\qquad
\beta_0\ge0,
\qquad
0\le\beta_1<1.
\]

Consider the deterministic SPD quadratic
\[
f(\theta)
=
\frac12\theta^\top H\theta,
\qquad
H\succ0,
\]
and set
\[
L=\lambda_{\max}(H).
\]
Write
\[
\beta=\beta_1^2.
\]

For a Hessian eigenmode with curvature
\[
h>0,
\]
define
\[
a_h
=
\eta_0(1-\beta)h.
\]
The exact modal characteristic polynomial is
\[
p_h(r)
=
r^3
+
\left[
-1+a_h(1+\beta_0)
\right]r^2
+
\left[
-\beta-a_h\beta_0
\right]r
+
\beta.
\]

This polynomial is Schur stable exactly when
\[
a_h
<
\frac{2(1-\beta)}
{1+2\beta_0}.
\]
Because
\[
a_h=\eta_0(1-\beta)h,
\]
the momentum factor cancels. The exact modal stability condition is therefore
\[
\boxed{
\eta_0h
<
\frac{2}{1+2\beta_0}
}.
\]
Consequently the full SPD iteration is linearly convergent for every initial state if and only if
\[
\boxed{
\eta_0L
<
\frac{2}{1+2\beta_0}
}.
\]

At equality,
\[
p_L(-1)=0,
\]
so the boundary has the unit-modulus root
\[
r=-1.
\]
Above the boundary,
\[
p_L(-1)>0,
\]
while
\[
p_L(r)\to-\infty
\qquad
\text{as }
r\to-\infty.
\]
Thus a real root lies below
\[
-1,
\]
and the top-curvature mode is linearly unstable.

The result can be expressed directly in the source paper's noise-amplification variable. Let
\[
\Gamma
=
(1+\beta_0)^2+\beta_0^2.
\]
Since
\[
1+2\beta_0
=
\sqrt{2\Gamma-1},
\]
the condition on the unnormalized base learning rate is
\[
\boxed{
\eta L
<
2
\sqrt{
\frac{\Gamma}{2\Gamma-1}
}
}.
\]

The right-hand side is strictly decreasing in
\[
\beta_0\ge0.
\]
It equals
\[
2
\]
at
\[
\beta_0=0,
\]
and tends to
\[
\sqrt2
\]
as
\[
\beta_0\to\infty.
\]

Hence increasing the noise-amplification knob creates an exact deterministic stability tax even after the paper's prescribed normalization by
\[
\sqrt\Gamma.
\]
The tax saturates: the stable base-learning-rate ceiling falls by at most a factor
\[
1/\sqrt2
\]
relative to its value at
\[
\beta_0=0.
\]

The source paper uses
\[
\beta_0=1
\]
as its default, corresponding to
\[
\Gamma=5.
\]
At that setting,
\[
\eta_0L
<
\frac23,
\]
or equivalently
\[
\eta L
<
\frac{2\sqrt5}{3}
=
1.4907119849998598\ldots.
\]

A second notable feature is exact independence from
\[
\beta_1.
\]
Although
\[
\beta_1
\]
changes the roots and therefore the convergence rate inside the stable region, it does not change the location of the Schur boundary.

## Assumptions and scope

The theorem analyzes Algorithm 2 of the defining PNM paper in deterministic mode, so
\[
g_t=H\theta_t.
\]

The result applies to any SPD quadratic because the recurrence commutes with the orthogonal eigenbasis of \(H\) and therefore decomposes into independent scalar curvature modes.

The source restriction
\[
\beta_0\ge0
\]
is retained. The paper notes that a negative value of
\[
\beta_0
\]
can recover conventional momentum as a special case; that extension is outside this statement.

The learning rate is constant. Weight decay, stochastic gradient noise, schedules, and the adaptive AdaPNM variant are excluded.

The theorem is a linear deterministic stability result. It does not assert that the same boundary governs a nonlinear or stochastic training problem.

## Proof

Fix one Hessian eigenmode with curvature
\[
h>0.
\]
The scalar PNM recurrence is
\[
m_t
=
\beta m_{t-2}
+
(1-\beta)h\theta_t
\]
and
\[
\theta_{t+1}
=
\theta_t
-
\eta_0
\left[
(1+\beta_0)m_t-\beta_0m_{t-1}
\right].
\]

Using the state
\[
(\theta_t,m_{t-1},m_{t-2}),
\]
one step is multiplication by
\[
M_h
=
\begin{bmatrix}
1-\eta_0(1+\beta_0)(1-\beta)h
&
\eta_0\beta_0
&
-\eta_0(1+\beta_0)\beta
\\
(1-\beta)h
&
0
&
\beta
\\
0
&
1
&
0
\end{bmatrix}.
\]
Direct determinant expansion gives
\[
\det(rI-M_h)
=
r^3
+
\left[-1+a_h(1+\beta_0)\right]r^2
+
\left[-\beta-a_h\beta_0\right]r
+
\beta.
\]

Write this cubic as
\[
p(r)
=
r^3+Ar^2+Br+C
\]
with
\[
A=-1+a_h(1+\beta_0),
\qquad
B=-\beta-a_h\beta_0,
\qquad
C=\beta.
\]
Because
\[
0\le\beta<1,
\]
the Schur reduction transforms the cubic to the quadratic
\[
q(r)
=
(1-\beta^2)r^2
+
(A-\beta B)r
+
(B-\beta A).
\]
After division by
\[
1-\beta^2,
\]
write
\[
q(r)=r^2+ur+v.
\]
A direct simplification gives
\[
u
=
-1
+
\frac{
a_h[1+\beta_0(1+\beta)]
}{
1-\beta^2
}
\]
and
\[
v
=
-
\frac{
a_h[\beta+\beta_0(1+\beta)]
}{
1-\beta^2
}.
\]

A real monic quadratic
\[
r^2+ur+v
\]
is Schur stable exactly when
\[
|v|<1,
\qquad
1+u+v>0,
\qquad
1-u+v>0.
\]

Here
\[
1+u+v
=
\frac{a_h}{1+\beta}
>
0.
\]
The condition
\[
1-u+v>0
\]
reduces exactly to
\[
a_h
<
\frac{2(1-\beta)}
{1+2\beta_0}.
\]
The remaining condition
\[
|v|<1
\]
gives the weaker upper bound
\[
a_h
<
\frac{1-\beta^2}
{\beta+\beta_0(1+\beta)}
\]
when its denominator is nonzero. Indeed, the ratio of this upper bound to the preceding one is
\[
\frac{
(1+\beta)(1+2\beta_0)
}{
2[\beta+\beta_0(1+\beta)]
}
=
1+
\frac{1-\beta}
{2[\beta+\beta_0(1+\beta)]}
>
1.
\]
Thus the unique active Schur boundary is
\[
a_h
<
\frac{2(1-\beta)}
{1+2\beta_0}.
\]

Substituting
\[
a_h=\eta_0(1-\beta)h
\]
cancels
\[
1-\beta
\]
and yields
\[
\eta_0h
<
\frac{2}{1+2\beta_0}.
\]

For an SPD matrix, the condition becomes most restrictive at
\[
h=L.
\]
This proves the full-system criterion.

For the base learning rate, use
\[
\eta_0=\eta/\sqrt\Gamma
\]
and
\[
(1+2\beta_0)^2
=
2\Gamma-1.
\]
The equivalent ceiling is
\[
\eta L
<
2\sqrt{\frac{\Gamma}{2\Gamma-1}}.
\]

Finally, let
\[
S(\beta_0)
=
\frac{
2\sqrt{1+2\beta_0+2\beta_0^2}
}{
1+2\beta_0
}.
\]
Differentiating its logarithm gives
\[
\frac{d}{d\beta_0}\log S
=
-\frac{
1
}{
(1+2\beta_0)
(1+2\beta_0+2\beta_0^2)
}
<
0.
\]
This proves strict monotonic decrease from
\[
2
\]
to
\[
\sqrt2.
\]

## Verification

The accompanying `verify.py` reconstructs the source three-state modal matrix directly.

It compares the matrix characteristic polynomial with the displayed closed form, samples both sides of the exact Schur boundary, checks that the boundary root is
\[
-1,
\]
and verifies the equivalent formulas in terms of
\[
\beta_0
\]
and
\[
\Gamma.
\]

The finite calculations are transcription guards. The stability region is proved algebraically through the Schur reduction above.

## Relationship to prior work

Xie, Yuan, Zhu, and Sugiyama introduced Positive-Negative Momentum to amplify stochastic gradient noise through two interleaved momentum streams. Their Algorithm 2 uses
\[
m_t
=
\beta_1^2m_{t-2}
+
(1-\beta_1^2)g_t
\]
and combines the current and previous streams with coefficients
\[
1+\beta_0
\]
and
\[
-\beta_0.
\]
They normalize the learning rate by
\[
\sqrt{(1+\beta_0)^2+\beta_0^2}
\]
and state that this normalization can avoid retuning the learning rate in practice.

The paper proves a stochastic convergence guarantee under smoothness, bounded-gradient, and bounded-variance assumptions. Its sufficient learning-rate condition is not an exact deterministic quadratic stability characterization. The paper also recommends
\[
\beta_0=1
\]
as a default, corresponding to fivefold noise variance relative to its baseline normalization.

The inspected defining paper does not state the cubic characteristic polynomial, the exact Schur boundary, the cancellation of
\[
\beta_1
\]
from that boundary, or the closed-form tradeoff between noise amplification
\[
\Gamma
\]
and the deterministic base-learning-rate ceiling.

Positive-negative momentum was subsequently reused as a component of optimizers such as Ranger21, which reinforces that the noise-control mechanism is not merely a proof device. Focused searches for PNM quadratic stability, spectral-radius conditions, characteristic polynomials, and learning-rate boundaries did not identify an implication-equivalent result.

## Limitations

The theorem concerns deterministic SPD quadratics and constant learning rate.

It classifies linear convergence of the full state, not objective monotonicity at every step.

It does not analyze the negative-\(\beta_0\) parameter choice used to recover conventional momentum.

The source stochastic convergence theorem and the exact deterministic quadratic stability theorem have different assumptions and should not be conflated.

The result does not claim that increasing stochastic gradient noise is undesirable; it isolates the exact deterministic stability cost of the same control parameter.

## References

1. Zeke Xie, Li Yuan, Zhanxing Zhu, and Masashi Sugiyama, “Positive-Negative Momentum: Manipulating Stochastic Gradient Noise to Improve Generalization,” arXiv:2103.17182, 2021.
2. Less Wright and Nestor Demeure, “Ranger21: a synergistic deep learning optimizer,” arXiv:2106.13731, 2021.
