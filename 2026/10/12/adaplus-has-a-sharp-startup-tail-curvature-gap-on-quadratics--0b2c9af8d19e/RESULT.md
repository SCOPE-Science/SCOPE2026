# AdaPlus has a sharp startup–tail curvature gap on quadratics
## Finding

Consider published AdaPlus Algorithm 1 with zero weight decay on the scalar strongly convex quadratic
\[
f(x)=\frac h2x^2,
\qquad
h>0.
\]
Use
\[
a>0,
\qquad
0\le\beta_1,\beta_2<1,
\qquad
\epsilon>0,
\]
and initialize
\[
m_0=s_0=0.
\]

Define the numerical scale
\[
D
=
\sqrt{\frac{\epsilon}{1-\beta_2}}
+
\epsilon.
\]

The first AdaPlus update is exactly
\[
\boxed{
x_1
=
x_0
\left[
1-
\frac{
a(1+\beta_1)h
}{
\sqrt{
\beta_1^2h^2x_0^2+\epsilon/(1-\beta_2)
}
+\epsilon
}
\right].
}
\]

Consequently, arbitrarily small nonzero source initializations increase the objective exactly when
\[
\boxed{
ah>
\frac{2D}{1+\beta_1}.
}
\]
At equality, every sufficiently small nonzero initialization is still nonexpansive because the square-root denominator is strictly larger than its zero-state limit.

The limiting local linearization tells a sharply different story. Put
\[
\tau=\frac aD.
\]
The asymptotic two-state optimization block for parameter and first moment is
\[
A_h
=
\begin{pmatrix}
1-\tau(1-\beta_1^2)h&-\tau\beta_1^2\\
(1-\beta_1)h&\beta_1
\end{pmatrix}.
\]
The second-moment perturbation contributes the decoupled eigenvalue
\[
\beta_2.
\]

The optimization block is Schur stable if and only if
\[
\boxed{
ah<
\frac{
2(1+\beta_1)D
}{
(1-\beta_1)(1+2\beta_1)
}.
}
\]
At equality, one characteristic root is exactly
\[
-1.
\]

Thus, whenever
\[
\beta_1>0,
\]
there is a nonempty curvature interval in which arbitrarily small source initializations have a first-step objective spike even though the limiting local spectrum is stable.

The exact ratio between the tail-stability curvature ceiling and the startup objective-nonincreasing ceiling is
\[
\boxed{
\frac{(1+\beta_1)^2}
{(1-\beta_1)(1+2\beta_1)}.
}
\]

At the published defaults
\[
a=10^{-3},
\qquad
\beta_1=0.9,
\qquad
\beta_2=0.999,
\qquad
\epsilon=10^{-8},
\]
the startup threshold is
\[
\boxed{
h_{\rm start}
=
3.3287238528\ldots
}
\]
while the limiting local-stability threshold is
\[
\boxed{
h_{\rm tail}
=
42.9167611023\ldots.
}
\]
Their ratio is
\[
12.8928571429\ldots.
\]

For the simple witness
\[
h=10,
\]
which lies strictly between the two thresholds,
\[
\lim_{x_0\to0}
\frac{f(x_1)}{f(x_0)}
=
\boxed{
25.0831545759\ldots.
}
\]

The result identifies a startup–tail mismatch specific to the AdaPlus composition: its accumulated-\(\epsilon\) belief denominator sets a finite local scale, while the first bias-corrected Nesterov numerator is amplified by
\[
1+\beta_1.
\]
The later limiting momentum dynamics have a much wider Schur-stable curvature range.

## Assumptions and scope

The result concerns the mathematical update printed in AdaPlus Algorithm 1.

Weight decay is set to zero in order to isolate the optimizer dynamics.

The objective is deterministic, scalar, smooth, and strongly convex.

The first-step statement concerns objective increase for arbitrarily small nonzero source initializations. It is not a claim that every later iterate increases.

The tail statement concerns the limiting local linearization as the bias-correction factors converge. It does not by itself assert global nonlinear convergence.

The additive
\[
\epsilon
\]
inside the second-moment recurrence is retained exactly as printed in the paper, as is the final
\[
+\epsilon
\]
outside the square root.

## Proof

At the first step,
\[
g_1=h x_0
\]
and
\[
m_1=(1-\beta_1)g_1.
\]
Therefore
\[
g_1-m_1
=
\beta_1g_1.
\]
The second-moment state is
\[
s_1
=
(1-\beta_2)\beta_1^2h^2x_0^2+\epsilon,
\]
so after bias correction
\[
\widehat s_1
=
\beta_1^2h^2x_0^2
+
\frac{\epsilon}{1-\beta_2}.
\]

AdaPlus forms the Nesterov-style numerator
\[
\overline m_1
=
\beta_1m_1+(1-\beta_1)g_1
=
(1-\beta_1^2)g_1.
\]
Its first bias correction gives
\[
\widehat m_1
=
(1+\beta_1)g_1.
\]
Substitution into the parameter update proves the exact first-step formula.

As
\[
x_0\to0,
\]
the first-step multiplier tends to
\[
1-\frac{a(1+\beta_1)h}{D}.
\]
For a quadratic, objective increase is equivalent to the absolute value of this multiplier exceeding one. Since the coefficient is positive, this happens exactly when
\[
\frac{a(1+\beta_1)h}{D}>2.
\]

For the tail linearization, first note that along the zero-parameter reference orbit the additive-\(\epsilon\) recurrence is
\[
s_t
=
\beta_2s_{t-1}+\epsilon.
\]
Hence
\[
s_t
=
\frac{\epsilon(1-\beta_2^t)}{1-\beta_2}
\]
and therefore
\[
\widehat s_t
=
\frac{\epsilon}{1-\beta_2}
\]
exactly on that orbit.

Perturbations of
\[
(g_t-m_t)^2
\]
are second order at the origin. Thus the second-moment perturbation decouples to first order with eigenvalue
\[
\beta_2.
\]

As
\[
t\to\infty,
\]
the first-moment bias correction tends to one. Writing the old parameter and first moment as
\[
(x,m),
\]
the linear first-moment update is
\[
m^+
=
\beta_1m+(1-\beta_1)hx.
\]
The Nesterov numerator becomes
\[
\overline m^+
=
\beta_1m^++(1-\beta_1)hx
=
\beta_1^2m+(1-\beta_1^2)hx.
\]
Since the denominator tends to
\[
D,
\]
the parameter update is
\[
x^+
=
x-\tau\overline m^+,
\qquad
\tau=\frac aD.
\]
This gives the displayed matrix
\[
A_h.
\]

Its trace and determinant are
\[
T
=
1+\beta_1-\tau(1-\beta_1^2)h
\]
and
\[
\Delta
=
\beta_1
\left[
1-\tau(1-\beta_1)h
\right].
\]
For the characteristic polynomial
\[
r^2-Tr+\Delta,
\]
the three strict Jury inequalities reduce to
\[
1-T+\Delta
=
\tau(1-\beta_1)h>0,
\]
\[
1+T+\Delta
=
2(1+\beta_1)
-
\tau(1-\beta_1)(1+2\beta_1)h>0,
\]
and
\[
1-\Delta
=
(1-\beta_1)
\left(
1+\tau\beta_1h
\right)>0.
\]
Only the middle inequality is restrictive. It gives the exact limiting local-stability threshold. At equality,
\[
1+T+\Delta=0,
\]
which is precisely the condition that
\[
r=-1
\]
is a characteristic root.

Dividing the tail threshold by the startup threshold gives
\[
\frac{(1+\beta_1)^2}
{(1-\beta_1)(1+2\beta_1)}.
\]
For every
\[
\beta_1>0,
\]
this ratio exceeds one.

## Verification

The accompanying `verify.py` reconstructs the printed scalar AdaPlus update and checks the exact first-step formula over multiple parameter choices.

It independently constructs the limiting linearization, verifies the three Jury quantities, confirms that the boundary has eigenvalue
\[
-1,
\]
and checks the published-default thresholds and the
\[
h=10
\]
startup witness.

The numerical checks are transcription guards. The thresholds are proved algebraically above.

## Relationship to prior work

The AdaPlus paper combines three ingredients: decoupled weight decay from AdamW, a Nesterov-style first-moment numerator, and the gradient-prediction-error second moment used by AdaBelief. Its published Algorithm 1 adds
\[
\epsilon
\]
inside the second-moment recurrence and also retains a final numerical
\[
+\epsilon
\]
outside the square root. The paper reports empirical stability but does not give the scalar startup or local Schur thresholds derived here.

The defining AdaBelief paper already uses the prediction-error second moment and an additive numerical floor. Later analysis of AdaBelief's adaptive-step range explicitly studies how the placement of
\[
\epsilon
\]
suppresses the range of adaptive stepsizes. That denominator effect is therefore prior and is not claimed here.

FastAdaBelief gives regret guarantees designed for strongly convex objectives by changing the stepsize schedule. Those online-regret results do not imply the fixed-learning-rate startup transient or the limiting AdaPlus Nesterov spectral boundary.

The new point is the interaction of AdaPlus's two inherited mechanisms. Bias correction makes its first Nesterov numerator
\[
(1+\beta_1)g_1,
\]
while the accumulated belief denominator has the finite zero-gradient scale
\[
D.
\]
In the tail, the two-state Nesterov dynamics instead obey a different exact Jury boundary. The resulting curvature-gap factor is not a generic statement about AdaBelief or Nesterov momentum separately.

Focused searches for AdaPlus together with scalar quadratics, local stability, startup amplification, bias correction, and curvature thresholds did not identify an implication-equivalent published result.

## Limitations

The theorem is for the published scalar deterministic update with constant hyperparameters.

It does not analyze weight decay, stochastic gradients, or multidimensional noncommuting curvature.

The limiting local-stability condition is spectral. It does not claim monotone objectives or global convergence.

Software libraries may implement epsilon placement differently from the printed algorithm; the claim does not transfer automatically to those variants.

## References

1. Lei Guan, “AdaPlus: Integrating Nesterov Momentum and Precise Stepsize Adjustment on AdamW Basis,” arXiv:2309.01966v1, first submitted 2023-09-05; later ICASSP 2024, DOI:10.1109/ICASSP48485.2024.10447337.
2. Juntang Zhuang, Tommy Tang, Yifan Ding, Sekhar Tatikonda, Nicha Dvornek, Xenophon Papademetris, and James S. Duncan, “AdaBelief Optimizer: Adapting Stepsizes by the Belief in Observed Gradients,” arXiv:2010.07468v1, first submitted 2020-10-15.
3. Guoqiang Zhang, Kenta Niwa, and W. Bastiaan Kleijn, “A DNN Optimizer that Improves over AdaBelief by Suppression of the Adaptive Stepsize Range,” arXiv:2203.13273v1, first submitted 2022-03-24.
4. Yangfan Zhou, Kaizhu Huang, Cheng Cheng, Xuguang Wang, Amir Hussain, and Xin Liu, “FastAdaBelief: Improving Convergence Rate for Belief-Based Adaptive Optimizers by Exploiting Strong Convexity,” arXiv:2104.13790v1, first submitted 2021-04-28.
