# FAdam's adaptive epsilon has a stationary-point singularity and fixed local jump
## Finding

Consider the current paper-form FAdam Algorithm 1 with its displayed defaults
\[
\beta_1=0.9,\qquad
\beta_2=0.999,\qquad
\epsilon=10^{-8},\qquad
\epsilon_2=0.01,
\]
\[
c=1,\qquad
\lambda=0.001,\qquad
\rho=\frac12.
\]
Let the first scheduled learning rate satisfy
\[
\eta_1>0,
\]
and use the source initialization
\[
m_0=0,\qquad f_0=1.
\]

Apply the method to the scalar strongly convex quadratic
\[
F(\theta)=\frac12\theta^2,
\qquad
g_1=\theta_0.
\]

At the first step the source bias-correction coefficient for the diagonal empirical Fisher state is exactly zero. Consequently
\[
f_1=g_1^2=\theta_0^2,
\]
independently of the nominal value of \(\beta_2\) and independently of the initialization \(f_0=1\).

Whenever
\[
0<|\theta_0|<\frac{\epsilon}{\epsilon_2}=10^{-6},
\]
the adaptive stabilizer takes its gradient-dependent branch:
\[
\widehat\epsilon
=
\epsilon_2|\theta_0|.
\]
Since \(\rho=1/2\), the source natural-gradient denominator is
\[
f_1^{1/2}+\widehat\epsilon
=
(1+\epsilon_2)|\theta_0|.
\]
Therefore the un-clipped natural-gradient term is exactly
\[
\overline g_1
=
\frac{\operatorname{sign}(\theta_0)}{1+\epsilon_2}.
\]
Its magnitude is smaller than one, so the default clipping threshold \(c=1\) is inactive.

The source preconditioned weight-decay term has the same first-step value:
\[
\overline g_{w,1}
=
\frac{\operatorname{sign}(\theta_0)}{1+\epsilon_2},
\]
and is also unclipped. Hence
\[
m_1
=
(1-\beta_1)\overline g_1,
\]
and the complete first update is
\[
\boxed{
\theta_1
=
\theta_0
-
D\operatorname{sign}(\theta_0)
}
\]
with
\[
D
=
\eta_1\frac{(1-\beta_1)+\lambda}{1+\epsilon_2}.
\]
For the displayed source defaults,
\[
\boxed{D=\frac{\eta_1}{10}}.
\]

Thus the update does **not** vanish as the gradient tends to zero through nonzero values. It converges to a fixed signed jump.

At the exact minimizer
\[
\theta_0=0,
\]
the first corrected Fisher state is zero and adaptive epsilon is also zero. The printed natural-gradient and weight-decay expressions therefore contain
\[
\frac0{0+0},
\]
so the mathematical update is undefined.

The nearby behavior is stronger than an isolated division-by-zero point. If
\[
0<|\theta_0|<\min\left(10^{-6},\frac D2\right),
\]
then
\[
|\theta_1|
=D-|\theta_0|
>|\theta_0|,
\]
so the strongly convex objective strictly increases in one step. The exact objective-gap amplification is
\[
\boxed{
\frac{F(\theta_1)-F(0)}{F(\theta_0)-F(0)}
=
\left(\frac D{|\theta_0|}-1\right)^2,
}
\]
which diverges as
\[
\theta_0\to0.
\]

For example, if
\[
\eta_1=10^{-3},
\]
then
\[
D=10^{-4}.
\]
Every nonzero initialization in the entire adaptive-epsilon branch
\[
0<|\theta_0|<10^{-6}
\]
then increases the quadratic objective on the first step.

A strictly positive lower floor in the denominator removes the singularity and the fixed jump. In particular, replacing the adaptive stabilizer by any denominator term bounded below by a positive constant makes both the natural-gradient and preconditioned weight-decay contributions tend to zero with \(\theta_0\).

## Assumptions and scope

The claim concerns the equations printed in the current FAdam paper, Algorithm 1.

The test objective is deterministic, scalar, smooth, and strongly convex. This is a mathematical optimizer benchmark, not a claim about the empirical deep-learning experiments in the source.

The source default exponent \(\rho=1/2\), clipping threshold \(c=1\), momentum parameter, adaptive-epsilon constants, and weight-decay coefficient are used exactly. The first scheduled learning rate is only assumed positive.

The analysis is first-step and local around a stationary point. It does not assert that every floating-point implementation evaluates the exact stationary point as a mathematical \(0/0\); an implementation may insert an undocumented floor or special-case zero.

The objective-increase statement uses the open punctured neighborhood where the adaptive branch is active. It is therefore not based only on the singular point itself.

## Proof

The source Fisher bias-correction coefficient at step \(t\) is
\[
\widehat\beta_{2,t}
=
\beta_2\frac{1-\beta_2^{t-1}}{1-\beta_2^t}.
\]
At \(t=1\),
\[
\widehat\beta_{2,1}=0.
\]
Therefore the source Fisher update gives
\[
f_1
=
\widehat\beta_{2,1}f_0
+
(1-\widehat\beta_{2,1})g_1^2
=
g_1^2.
\]
For the quadratic,
\[
g_1=\theta_0,
\]
so
\[
f_1=\theta_0^2.
\]

The source adaptive epsilon is
\[
\widehat\epsilon
=
\min\{\epsilon,\epsilon_2\operatorname{RMS}(g_1)\}.
\]
In one dimension,
\[
\operatorname{RMS}(g_1)=|g_1|=|\theta_0|.
\]
Thus on
\[
0<|\theta_0|<\epsilon/\epsilon_2,
\]
we have
\[
\widehat\epsilon=\epsilon_2|\theta_0|.
\]

With \(\rho=1/2\), Algorithm 1 divides by
\[
f_1^\rho+\widehat\epsilon^{2\rho}
=
|\theta_0|+\epsilon_2|\theta_0|
=
(1+\epsilon_2)|\theta_0|.
\]
Hence
\[
\overline g_1
=
\frac{\theta_0}{(1+\epsilon_2)|\theta_0|}
=
\frac{\operatorname{sign}(\theta_0)}{1+\epsilon_2}.
\]
Because
\[
\frac1{1+\epsilon_2}<1=c,
\]
source RMS clipping does not alter it.

The source weight-decay direction before clipping is
\[
\frac{\theta_0}{f_1^\rho+\widehat\epsilon^{2\rho}},
\]
which is the same signed constant. Its magnitude is also below \(c\), so clipping is again inactive.

Since \(m_0=0\),
\[
m_1
=
(1-\beta_1)\overline g_1.
\]
The source parameter update therefore becomes
\[
\theta_1
=
\theta_0
-
\eta_1\left(m_1+\lambda\overline g_{w,1}\right),
\]
which yields the displayed fixed jump.

For the source constants,
\[
\frac{(1-0.9)+0.001}{1+0.01}
=
\frac{0.101}{1.01}
=
0.1.
\]
Hence \(D=\eta_1/10\).

At \(\theta_0=0\), both the corrected Fisher state and adaptive epsilon equal zero. The two printed preconditioned fractions therefore have zero numerator and zero denominator.

For nonzero \(\theta_0\) with \(|\theta_0|<D\), the update crosses the minimizer and satisfies
\[
|\theta_1|=D-|\theta_0|.
\]
When \(|\theta_0|<D/2\), this is strictly larger than the initial magnitude. Since
\[
F(\theta)=\theta^2/2,
\]
the exact ratio is
\[
\left(D/|\theta_0|-1\right)^2.
\]
The ratio diverges as \(|\theta_0|\downarrow0\).

A positive denominator floor changes the normalized terms from degree-zero functions near zero to terms that vanish with \(\theta_0\), eliminating both the undefined point and the fixed jump.

## Verification

The accompanying `verify.py` reconstructs the first paper-form FAdam step with the displayed defaults.

It checks the exact first-step Fisher correction, the adaptive-epsilon branch, inactivity of clipping, the closed jump \(D=\eta_1/10\), the objective-increase interval, and the unbounded objective-gap amplification along a sequence approaching zero.

It also checks that a positive denominator floor makes the preconditioned terms tend to zero rather than to a nonzero signed constant.

These finite computations are transcription guards only. The punctured-neighborhood formula and singular point are established algebraically above.

## Relationship to prior work

Hwang introduces FAdam and explicitly lists adaptive epsilon among the corrections to Adam. Algorithm 1 sets
\[
\widehat\epsilon
=
\min\{\epsilon,\epsilon_2\operatorname{RMS}(g_t)\}
\]
and Appendix B.3 motivates epsilon as preventing division by zero before clipping. The inspected source does not discuss the zero-gradient case where this adaptive choice itself vanishes, nor the resulting finite local jump.

The same paper states that its convergence analysis follows Défossez, Bottou, Bach, and Usunier. That cited Adam analysis uses a fixed strictly positive numerical stabilizer in the adaptive denominator. Its update is therefore defined at zero gradient and has a different local map. The fixed-positive-stabilizer proof does not by itself cover the zero-floor adaptive-epsilon formula without an extra convention or safeguard.

The FAdam paper initializes the Fisher state at one but also states that its bias correction ignores that initialization. The first-step identity
\[
f_1=g_1^2
\]
is exactly the consequence used here.

Focused searches for FAdam together with zero gradients, adaptive epsilon, division by zero, stationary points, and quadratic local dynamics did not identify an implication-equivalent published analysis.

## Limitations

The result is about the printed mathematical update, not every software implementation that uses the name FAdam.

The singularity occurs at an exact stationary point, but the objective-increase result holds on an open punctured neighborhood and is therefore robust to avoiding exact equality.

A practical implementation can remove the issue by imposing a positive lower floor or by explicitly defining zero-over-zero preconditioned components to be zero. Such a repair changes the local map analyzed here.

The result does not assess FAdam's empirical performance, nor does it disprove every possible convergence theorem for a safeguarded FAdam variant.

## References

1. Dongseong Hwang, “FAdam: Adam is a natural gradient optimizer using diagonal empirical Fisher information,” arXiv:2405.12807, first submitted 2024-05-21; current inspected revision v11.
2. Alexandre Défossez, Léon Bottou, Francis Bach, and Nicolas Usunier, “A Simple Convergence Proof of Adam and Adagrad,” arXiv:2003.02395; Transactions on Machine Learning Research, 2022.
